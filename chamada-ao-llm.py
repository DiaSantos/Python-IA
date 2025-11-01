from openai import OpenAI

# Cria o cliente apontando para o servidor local do LM Studio
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",  # 👈 precisa do /v1
    api_key="lm-studio"  # o LM Studio aceita qualquer chave fake
)

# Faz a chamada ao modelo
resposta = client.chat.completions.create(
    model="google/gemma-3-1b",  # nome exato do modelo carregado no LM Studio
    messages=[
        {"role": "system", "content": "Você é um assistente de IA que responde perguntas de forma concisa e objetiva."},
        {"role": "user", "content": "O que é a IA Generativa?"}
    ],
    temperature=0.7
)

# Exibe a resposta do modelo
print(resposta.choices[0].message.content)