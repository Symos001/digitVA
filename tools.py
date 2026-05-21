import os
import subprocess
import json
from typing import Optional

# ------------------------------------------------------------
# GERENCIADOR DE MEMÓRIA (será injetado pelo main)
# ------------------------------------------------------------
memory_manager = None

def set_memory_manager(mem):
    """Permite que o módulo principal injete a instância do MemoryManager."""
    global memory_manager
    memory_manager = mem

# ------------------------------------------------------------
# FERRAMENTAS DE SISTEMA / DEBUG
# ------------------------------------------------------------

def read_file(path: str, start_line: int = 1, end_line: Optional[int] = None) -> str:
    """Lê o conteúdo de um arquivo. Opcionalmente, pode limitar as linhas."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        total = len(lines)
        if start_line < 1:
            start_line = 1
        if end_line is None or end_line > total:
            end_line = total
        snippet = ''.join(lines[start_line-1:end_line])
        return f"📄 {path} (linhas {start_line}-{end_line}):\n{snippet}"
    except FileNotFoundError:
        return f"❌ Arquivo não encontrado: {path}"
    except Exception as e:
        return f"❌ Erro ao ler arquivo: {str(e)}"

def run_command(command: str, timeout: int = 10) -> str:
    """
    Executa um comando shell.
    ⚠️ ATENÇÃO: use com responsabilidade. Em um ambiente real, isole com Docker ou sandbox.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=os.getcwd()  # executa no diretório atual
        )
        stdout = result.stdout.strip() or "(sem saída)"
        stderr = result.stderr.strip() or "(sem erros)"
        return f"🔧 Comando: {command}\n📤 STDOUT:\n{stdout}\n⚠️ STDERR:\n{stderr}"
    except subprocess.TimeoutExpired:
        return f"⏰ O comando excedeu o tempo limite de {timeout}s."

def list_project_files(directory: str = ".") -> str:
    """Lista arquivos do projeto, ignorando pastas comuns de dependências."""
    important_exts = ('.py', '.js', '.ts', '.html', '.css', '.json', '.md', '.env', '.txt', '.yaml', '.yml')
    files = []
    for root, dirs, filenames in os.walk(directory):
        # Ignorar pastas que poluem a listagem
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '__pycache__', 'venv', '.venv')]
        for f in filenames:
            if f.endswith(important_exts):
                files.append(os.path.join(root, f))
    if not files:
        return "Nenhum arquivo de código encontrado."
    return "📂 Arquivos do projeto:\n" + "\n".join(files[:50])  # limite para não estourar tokens

# ------------------------------------------------------------
# FERRAMENTAS DE MEMÓRIA (integradas ao SQLite)
# ------------------------------------------------------------

def update_profile_field(field: str, value: str) -> str:
    """Atualiza um campo do perfil do usuário no banco de memória."""
    if memory_manager is None:
        return "Erro: gerenciador de memória não inicializado."
    try:
        memory_manager.save_profile_field(field, value)
        return f"✅ Perfil atualizado: {field} = {value}"
    except Exception as e:
        return f"❌ Falha ao atualizar perfil: {str(e)}"

def remember_fact(content: str, category: str = "general") -> str:
    """Guarda uma memória de longo prazo (fato, lembrete, aprendizado)."""
    if memory_manager is None:
        return "Erro: gerenciador de memória não inicializado."
    try:
        memory_manager.add_memory(content, category)
        return f"🧠 Lembrei: [{category}] {content}"
    except Exception as e:
        return f"❌ Falha ao salvar memória: {str(e)}"

def search_my_memories(query: str) -> str:
    """Busca nas memórias pessoais salvas (usando busca textual)."""
    if memory_manager is None:
        return "Erro: gerenciador de memória não inicializado."
    results = memory_manager.search_memories(query, limit=3)
    if not results:
        return "Nenhuma memória encontrada."
    return "📌 Memórias encontradas:\n" + "\n".join(
        f"- [{r['category']}] {r['content']}" for r in results
    )

# ------------------------------------------------------------
# DEFINIÇÕES PARA FUNCTION CALLING (OpenAI)
# ------------------------------------------------------------
available_tools = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Lê o conteúdo de um arquivo do sistema de arquivos.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Caminho do arquivo"},
                    "start_line": {"type": "integer", "description": "Linha inicial (padrão 1)"},
                    "end_line": {"type": "integer", "description": "Linha final (opcional)"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Executa um comando no terminal e retorna a saída.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "Comando a executar"},
                    "timeout": {"type": "integer", "description": "Timeout em segundos (padrão 10)"}
                },
                "required": ["command"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_project_files",
            "description": "Lista arquivos do projeto atual (filtra pastas como .git, node_modules).",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {"type": "string", "description": "Diretório a listar (padrão '.' )"}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_profile_field",
            "description": "Atualiza uma informação de perfil do usuário (ex: nome, preferência de resposta, linguagem favorita).",
            "parameters": {
                "type": "object",
                "properties": {
                    "field": {"type": "string", "description": "Campo a atualizar (ex: 'name', 'response_style')"},
                    "value": {"type": "string", "description": "Novo valor"}
                },
                "required": ["field", "value"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "remember_fact",
            "description": "Salva um fato ou instrução importante na memória de longo prazo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "content": {"type": "string", "description": "Fato ou instrução a lembrar"},
                    "category": {"type": "string", "description": "Categoria (ex: 'preference', 'bug', 'instruction')"}
                },
                "required": ["content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_my_memories",
            "description": "Busca nas memórias pessoais do usuário (lembretes, bugs passados, preferências).",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Termo de busca"}
                },
                "required": ["query"]
            }
        }
    }
]

# Mapeamento nome da função -> função Python
tool_functions = {
    "read_file": read_file,
    "run_command": run_command,
    "list_project_files": list_project_files,
    "update_profile_field": update_profile_field,
    "remember_fact": remember_fact,
    "search_my_memories": search_my_memories
}
