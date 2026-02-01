# Agente de Inteligência Executiva 🤖

Este projeto automatiza o ciclo de vida da informação: desde a coleta de notícias via web scraping até a geração de relatórios executivos estratégicos utilizando IA.

## 🚀 Stack Tecnológica
- **Linguagem:** Python 3.11
- **Web Scraping:** BeautifulSoup4 & Requests
- **Orquestração de IA:** LangChain & Google Generative AI SDK
- **Modelo de IA:** Gemini 1.5 Flash / 2.5 Flash
- **Interface:** Streamlit

## 📂 Estrutura do Projeto
- `app.py`: Interface visual principal e lógica do dashboard.
- `scraper.py`: Módulo responsável pela coleta de dados (G1 e RSS).
- `agent.py`: Módulo de inteligência que processa os dados e gera o relatório.
- `requirements.txt`: Dependências do projeto.

## 🛠️ Como Executar
1. Instale as dependências:
   ```bash
   pip install streamlit langchain-google-genai beautifulsoup4 requests google-generativeai pandas
   ```
2. Execute o aplicativo:
   ```bash
   streamlit run app.py
   ```
3. Insira sua **Google API Key** no menu lateral e clique em "Iniciar Ciclo de Inteligência".

## 📊 Funcionalidades
- **Coleta Multi-fonte:** Busca notícias do G1 e feeds RSS de tecnologia.
- **Processamento em Tempo Real:** Transforma dados brutos em insights estratégicos.
- **Dashboard Interativo:** Visualize as notícias coletadas e o relatório final.
- **Exportação:** Baixe o relatório gerado em formato Markdown.
