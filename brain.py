import openai
import json
from tools import available_tools, tool_functions

def ask_digito(user_input, conversation_history, memory_context, model="gpt-4o"):
    """
    Envia a conversa para o LLM e trata chamadas de função.
    Retorna uma string com a resposta final do assistente.
    
    Parâmetros:
    - user_input: mensagem atual do usuário
    - conversation_history: lista de mensagens recentes (formato [{'role':..., 'content':...}])
    - memory_context: string com perfil e memórias relevantes do usuário
    - model: modelo OpenAI a usar
    """
    
    # Monta o prompt do sistema com toda a memória disponível
    system_prompt = f"""Você é o Dígito, um assistente pessoal de programação e companheiro do dia a dia.
Seu objetivo é ajudar a debugar códigos, responder dúvidas, conversar de forma amigável e lembrar de quem é o usuário.

{memory_context}

## Regras de personalidade:
- Seja direto, útil e com um toque de humor (mas sem exageros).
- Quando o usuário mencionar preferências pessoais (nome, estilo de resposta, etc.), atualize o perfil usando a função 'update_profile_field'.
- Se o usuário pedir para lembrar de algo explicitamente, use 'remember_fact'.
- Para tarefas de código, utilize as ferramentas de leitura de arquivos e execução de comandos com segurança.
- Sempre explique o que está fazendo antes de executar comandos potencialmente perigosos.
"""
    
    messages = [
        {"role": "system", "content": system_prompt},
    ]
    
    # Adiciona o histórico recente da conversa
    messages.extend(conversation_history)
    
    # Adiciona a fala atual do usuário (se não estiver vazia)
    if user_input:
        messages.append({"role": "user", "content": user_input})
    
    # Loop principal para tratar function calls
    while True:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            tools=available_tools,
            tool_choice="auto"
        )
        
        message = response.choices[0].message
        
        # Se o modelo quer chamar uma ferramenta
        if message.tool_calls:
            # Adiciona a mensagem do assistente (com tool_calls) ao histórico
            messages.append({
                "role": "assistant",
                "content": message.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    } for tc in message.tool_calls
                ]
            })
            
            # Executa cada tool call e adiciona os resultados
            for tc in message.tool_calls:
                func_name = tc.function.name
                try:
                    args = json.loads(tc.function.arguments)
                except json.JSONDecodeError:
                    args = {}
                
                if func_name in tool_functions:
                    try:
                        result = tool_functions[func_name](**args)
                    except Exception as e:
                        result = f"Erro ao executar {func_name}: {str(e)}"
                else:
                    result = f"Função {func_name} não implementada."
                
                # Adiciona a resposta da ferramenta ao histórico
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "name": func_name,
                    "content": str(result)
                })
            
            # Continua o loop para que o modelo processe o resultado
            continue
        
        # Se não há tool calls, é a resposta final
        final_answer = message.content or ""
        return final_answer
