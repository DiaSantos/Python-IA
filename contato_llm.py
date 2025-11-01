# contato_com_llm.py
from openai import OpenAI

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {"role": "system", "content": """
            Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
            Eu quero que você analise essa resenha, e me retorne um JSON com as seguintes chaves:

            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha no idioma original que você recebeu
            - 'resenha_pt': a resenha traduzida para o português
            - 'avaliacao': uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)

            Exemplo de entrada:
            '39485494$Habimana Therese$This app is very important but sometimes it gives lies'
            Exemplo de saída:
            {
                "usuario": "Habimana Therese",
                "resenha_original": "This app is very important but sometimes it gives lies",
                "resenha_pt": "Este aplicativo é muito importante, mas às vezes dá mentiras",
                "avaliacao": "Negativa"
            }

            '5466$John Mwangi$This app works perfectly and helps me every day!'
            {
            
                "usuario": "John Mwangi",
                "resenha_original": "This app works perfectly and helps me every day!",
                "resenha_pt": "Este aplicativo funciona perfeitamente e me ajuda todos os dias!",
                "avaliacao": "Positiva"
            }

            '32554454$Aisha Kamau$The app is okay, nothing special but it does its job'
           {
                "usuario": "Aisha Kamau",
                "resenha_original": "The app is okay, nothing special but it does its job",
                "resenha_pt": "O aplicativo é ok, nada de especial, mas faz o seu trabalho",
                "avaliacao": "Neutra"
            }


            Regra importante: você deve retornar apenas o JSON, sem nenhum outro texto antes ou depois.
            """},
            {"role": "user", "content": f"Resenha: {linha}"}
        ],
        temperature=1.0
    )
    resultado = resposta_do_llm.choices[0].message.content

    # Retorna string vazia se o resultado for None
    if not resultado:
        return ""
    
    # Remove possíveis blocos de markdown (```json ... ```)
    resultado = resultado.strip()
    if resultado.startswith("```json"):
        resultado = resultado[7:]  # Remove "```json"
    elif resultado.startswith("```"):
        resultado = resultado[3:]  # Remove "```"
    
    if resultado.endswith("```"):
        resultado = resultado[:-3]  # Remove "```" do final
    
    resultado = resultado.strip()
    
    return resultado

