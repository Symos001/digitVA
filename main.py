import json
from memory import MemoryManager
from brain import ask_digito  # mantido igual, mas agora recebe memória contextual
import openai

# Inicializa gerenciador de memória
memory = MemoryManager("digito.db")

# Carrega perfil do usuário
user_profile = memory.load_full_profile()

def build_memory_context(user_input):
    """Monta o texto de contexto que será injetado no system prompt"""
    context_parts = []
    
    # 1. Perfil do usuário
    if user_profile:
        context_parts.append(f"Informações do usuário: {json.dumps(user_profile, ensure_ascii=False)}")
    
    # 2. Memórias relevantes com base na entrada do usuário
    relevant = memory.search_memories(user_input, limit=3)
    if relevant:
        memories_text = "\n".join([f"- {m['content']} (categoria: {m['category']})" for m in relevant])
        context_parts.append(f"Lembranças importantes: {memories_text}")
    
    return "\n".join(context_parts)

# Loop de conversa
conversation_history = []  # vamos usar o histórico recente do SQLite também

while True:
    user_input = input("Você: ")
    
    # Salva a fala do usuário no histórico
    memory.add_conversation_turn("user", user_input)
    
    # Monta contexto de memória
    memory_context = build_memory_context(user_input)
    
    # Pega as últimas conversas do SQLite (últimos 10 pares)
    recent_history = memory.get_recent_conversations(20)  # últimas 20 mensagens
    # Obs: ask_digito já recebe o histórico; garantimos que ele inclui as mais recentes
    response = ask_digito(user_input, recent_history, memory_context)
    
    # Se o assistente usou ferramentas, o código de tratamento de function calling continua o mesmo
    # (aqui omitido para brevidade, mas segue o padrão anterior)
    
    # Supondo que response é o texto final da resposta
    final_answer = response.get("content") if isinstance(response, dict) else response
    print("Dígito:", final_answer)
    
    # Salva resposta do assistente
    memory.add_conversation_turn("assistant", final_answer)
    
    # Analisa se o usuário deu uma instrução de "lembrete" e salva como memória de longo prazo
    if "lembre-se" in user_input.lower() or "lembrar" in user_input.lower():
        # Extrai o conteúdo (simplificado; poderia usar LLM para isolar a frase)
        fact = user_input.split("lembre-se", 1)[-1].strip().strip(":,. ")
        if fact:
            memory.add_memory(fact, category="instruction")
            print("Dígito: Entendido, vou me lembrar disso.")
