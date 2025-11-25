from groq import Groq
from typing import List, Dict

def create_groq_client(api_key: str) -> Groq:
    """Cria o cliente Groq usando a API key."""
    return Groq(api_key=api_key)

def ask_groq(client: Groq, messages: List[Dict]):
    """Envia mensagens para o modelo da Groq e retorna a resposta."""
    return client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.7,
        max_tokens=2048
    )
