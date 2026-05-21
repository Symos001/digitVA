from memory import MemoryManager
from tools import set_memory_manager
from brain import ask_digito
import json

# Inicializa memória
memory = MemoryManager("digito.db")
set_memory_manager(memory)  # injeta a instância nas tools

# Carrega perfil
user_profile = memory.load_full_profile()

def build_memory_context(user_input):
    parts = []
    if user_profile:
        parts.append(f"👤 Perfil do usuário: {json.dumps(user_profile, ensure_ascii=False)}")
    memories = memory.search_memories(user_input, limit=3)
    if memories:
        mem_text = "\n".join([f"- [{m['category']}] {m['content']}" for m in memories])
        parts.append(f"🧠 Memórias relevantes: {mem_text}")
    return "\n".join(parts)

while True:
    user_input = input("Você: ")
    if user_input.lower() in ("sair", "exit", "quit"):
        break
    
    # Salva no histórico
    memory.add_conversation_turn("user", user_input)
    
    # Monta contexto de memória
    context = build_memory_context(user_input)
    
    # Pega histórico recente do SQLite
    history = memory.get_recent_conversations(20)
    
    # Chama o cérebro
    response = ask_digito(user_input, history, context)
    
    print("Dígito:", response)
    
    # Salva resposta
    memory.add_conversation_turn("assistant", response)
    
    # Atualiza o perfil local se necessário (já foi salvo no banco pela ferramenta)
    user_profile = memory.load_full_profile()
