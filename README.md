# 🧠 Projeto: Análise de Resenhas com Inteligência Artificial em Python

Este projeto foi desenvolvido com base e adaptação do curso **“Python: Inteligência Artificial Aplicada”**, oferecido pela **Alura**.  
Seu objetivo é demonstrar, de forma prática, a aplicação de modelos de linguagem para **análise automatizada de sentimentos em resenhas de aplicativos**.

---

## 🚀 Visão Geral

O projeto utiliza **Python** e **integração com modelos de linguagem locais** via **LM Studio** para:  
- Traduzir resenhas de diferentes idiomas para o português;  
- Analisar o **sentimento** (Positivo, Negativo ou Neutro);  
- Estruturar os resultados em **JSON**;  
- Contabilizar e unificar as resenhas traduzidas para análises adicionais.  

O fluxo completo é realizado localmente, utilizando um **modelo de IA hospedado no LM Studio**, eliminando dependências externas da API da OpenAI.

---

## 🧩 Estrutura do Projeto

```
📁 Projeto_IA_Resenhas
│
├── chamada-ao-llm.py        # Teste básico de comunicação com o modelo local via LM Studio
├── contato_llm.py           # Função principal de interação com o modelo (entrada → JSON)
├── desafio.py               # Script principal: leitura, processamento e análise das resenhas
├── resenhas.txt             # Arquivo de entrada contendo resenhas reais
└── README.md                # Documentação do projeto
```

---

## ⚙️ Funcionamento

### 1. Conexão com o Modelo (`chamada-ao-llm.py`)
O script estabelece conexão com o **LM Studio** usando o cliente `openai` configurado para o servidor local:  
```python
client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
```
Ele permite testar rapidamente se o modelo (ex: `google/gemma-3-1b`) está respondendo corretamente.

---

### 2. Processamento de Resenhas (`contato_llm.py`)
Este módulo define a função:
```python
recebe_linha_e_retorna_json(linha)
```
Ela envia uma resenha ao modelo de linguagem, solicitando que o texto seja:  
- Analisado quanto ao sentimento (Positiva, Negativa ou Neutra);  
- Traduzido para português;  
- Retornado em formato JSON padronizado.  

Exemplo de **entrada**:  
```
39485494$Habimana Therese$This app is very important but sometimes it gives lies
```

Exemplo de **saída esperada**:
```json
{
  "usuario": "Habimana Therese",
  "resenha_original": "This app is very important but sometimes it gives lies",
  "resenha_pt": "Este aplicativo é muito importante, mas às vezes dá mentiras",
  "avaliacao": "Negativa"
}
```

---

### 3. Execução e Análise (`desafio.py`)
O script principal:  
- Lê o arquivo `resenhas.txt`;  
- Envia cada linha ao modelo via `recebe_linha_e_retorna_json()`;  
- Armazena as respostas válidas em uma lista de dicionários JSON;  
- Conta as avaliações positivas, negativas e neutras;  
- Une todas as resenhas traduzidas em um único texto.  

Também inclui **tratamento de erros e logs detalhados**, para identificar falhas no parsing de JSON.

---

### 4. Arquivo de Entrada (`resenhas.txt`)
Contém resenhas reais de usuários em diversos idiomas (inglês, francês, espanhol, turco, etc.).  
Cada linha segue o formato:
```
<ID>$<NOME_USUARIO>$<RESENHA>
```

---

## 🧮 Resultado Final

Ao término da execução, o script exibe:  
- Total de resenhas processadas com sucesso;  
- Contadores de avaliações positivas, negativas e neutras;  
- As resenhas traduzidas para português, unificadas com separador `#####`.

---

## 🧠 Conceitos Praticados

Durante o desenvolvimento deste projeto, foram aplicados e aprofundados os seguintes tópicos:  
- Manipulação de **arquivos texto (TXT e CSV)** com `open()` e `encoding='utf-8'`;  
- Uso de **estruturas de repetição** (`for`, `while`) e **condicionais**;  
- Criação e uso de **funções personalizadas** em Python;  
- Manipulação de **listas e dicionários**, e métodos como `.append()`, `.pop()`, `.items()`, `.get()`;  
- Tratamento de exceções com `try`, `except`, `finally`;  
- Integração com **APIs locais de IA** (via LM Studio e modelo **Gemma**);  
- Geração e manipulação de **JSONs bem formatados**;  
- Contagem e agregação de dados para análise quantitativa de sentimentos.

---

## 🧰 Tecnologias Utilizadas

- 🐍 **Python 3.11+**
- 🧠 **LM Studio** (para execução local do modelo)
- 🤖 **Modelo Google Gemma-3-1B**
- 📦 **Biblioteca `openai` (client)**
- 📊 **Pandas / JSON (opcional para análise posterior)**

---

## 💡 Próximos Passos

- Armazenar os resultados em um **DataFrame Pandas** e exportar para `.csv`;  
- Criar um **dashboard interativo** com gráficos de sentimento (Plotly ou Streamlit);  
- Implementar **tratamento automático de idiomas** com detecção e tradução via API.

---

## 👨‍💻 Autor

**Daniel dos Santos**  
Cientista de Dados em formação | Entusiasta de IA e Engenharia de Dados  
📧 [diaSantos.tecno@gmail.com](mailto:diaSantos.tecno@gmail.com)  
📚 Projeto desenvolvido e adaptado a partir do curso **“Python: Inteligência Artificial Aplicada”** – Alura
[README (1).md](https://github.com/user-attachments/files/23279864/README.1.md)
