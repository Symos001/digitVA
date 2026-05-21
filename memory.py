import sqlite3
import json
from datetime import datetime

class MemoryManager:
    def __init__(self, db_path="digito_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()
    
    def _create_tables(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS user_profile (
                key TEXT PRIMARY KEY,
                value TEXT
            );
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT,
                category TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts USING fts5(
                content, category, content=memories, content_rowid=id
            );
        """)
        self.conn.commit()
    
    # ---------- PERFIL DO USUÁRIO ----------
    def save_profile_field(self, key, value):
        self.conn.execute(
            "INSERT OR REPLACE INTO user_profile (key, value) VALUES (?, ?)",
            (key, str(value))
        )
        self.conn.commit()
    
    def load_full_profile(self):
        cursor = self.conn.execute("SELECT key, value FROM user_profile")
        return {row["key"]: row["value"] for row in cursor.fetchall()}
    
    def update_profile_from_dict(self, updates: dict):
        for k, v in updates.items():
            self.save_profile_field(k, v)
    
    # ---------- HISTÓRICO DE CONVERSAS ----------
    def add_conversation_turn(self, role, content):
        self.conn.execute(
            "INSERT INTO conversations (role, content) VALUES (?, ?)",
            (role, content)
        )
        self.conn.commit()
    
    def get_recent_conversations(self, limit=20):
        cursor = self.conn.execute(
            "SELECT role, content FROM conversations ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        return [{"role": row["role"], "content": row["content"]} for row in cursor.fetchall()][::-1]
    
    def clear_conversations(self):
        self.conn.execute("DELETE FROM conversations")
        self.conn.commit()
    
    # ---------- MEMÓRIAS DE LONGO PRAZO ----------
    def add_memory(self, content, category="general"):
        self.conn.execute(
            "INSERT INTO memories (content, category) VALUES (?, ?)",
            (content, category)
        )
        self.conn.commit()
    
    def search_memories(self, query, limit=3):
        """Busca textual com FTS5"""
        cursor = self.conn.execute("""
            SELECT content, category
            FROM memories_fts
            WHERE memories_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """, (query, limit))
        results = cursor.fetchall()
        if not results:
            # fallback: busca simples por LIKE se FTS não retornar nada
            cursor = self.conn.execute("""
                SELECT content, category FROM memories
                WHERE content LIKE ? OR category LIKE ?
                LIMIT ?
            """, (f"%{query}%", f"%{query}%", limit))
            results = cursor.fetchall()
        return [{"content": row["content"], "category": row["category"]} for row in results]
    
    def get_all_memories_by_category(self, category):
        cursor = self.conn.execute(
            "SELECT content FROM memories WHERE category = ?",
            (category,)
        )
        return [row["content"] for row in cursor.fetchall()]
