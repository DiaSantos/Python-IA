import json
from contato_llm import recebe_linha_e_retorna_json



#etapa 1
lista_de_resenhas = []

with open("resenhas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha)
        lista_de_resenhas.append(linha.strip())

print(len(lista_de_resenhas))

#etapa 2 e 3
lista_de_resenhas_json = []

for i, resenha in enumerate(lista_de_resenhas, 1):
    try:
        resenha_json = recebe_linha_e_retorna_json(resenha)
        
        # Verifica se a resposta está vazia
        if not resenha_json or resenha_json.strip() == "":
            print(f"Erro: Resposta vazia para resenha {i}: {resenha[:50]}...")
            continue
        
        # Tenta fazer o parse do JSON
        resenha_dict = json.loads(resenha_json)
        lista_de_resenhas_json.append(resenha_dict)
        print(f"✓ Resenha {i} processada com sucesso")
        
    except json.JSONDecodeError as e:
        print(f"Erro ao fazer parse do JSON para resenha {i}: {resenha[:50]}...")
        print(f"Resposta recebida: {resenha_json[:200] if resenha_json else 'vazia'}...")
        print(f"Erro detalhado: {e}")
        continue
    except Exception as e:
        print(f"Erro inesperado ao processar resenha {i}: {e}")
        continue

print(f"\nTotal de resenhas processadas com sucesso: {len(lista_de_resenhas_json)}")
print(lista_de_resenhas_json)

def contador_e_juntador(lista_de_resenhas_json):
    contador_positivo = 0
    contador_negativo = 0
    contador_neutro = 0
    
# Lista para armazenar as resenhas traduzidas em português
    resenhas_pt = []

    for resenha in lista_de_resenhas_json:
        # Conta as avaliações
        if resenha['avaliacao'] == 'Positiva':
            contador_positivo += 1
        elif resenha['avaliacao'] == 'Negativa':
            contador_negativo += 1
        else:
            contador_neutro += 1
        
        # Adiciona a resenha em português à lista
        resenhas_pt.append(resenha['resenha_pt'])
    
    # Junta todas as resenhas traduzidas com o separador "#####"
    textos_unidos = "#####".join(resenhas_pt)
    
    return contador_positivo, contador_negativo, contador_neutro, textos_unidos

cont_positivo, cont_negativo, cont_neutro, textos_unidos = contador_e_juntador(lista_de_resenhas_json)

print(f"\nContadores:")
print(f"  Positivas: {cont_positivo}")
print(f"  Negativas: {cont_negativo}")
print(f"  Neutras: {cont_neutro}")
print(f"\nResenhas em português unidas:\n{textos_unidos}")
