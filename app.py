import streamlit as st
import pandas as pd
from scraper import NewsScraper
from agent import ReportAgent
import time
import os

# Configuração da página
st.set_page_config(
    page_title="Agente de Inteligência Executiva",
    page_icon="🤖",
    layout="wide"
)

# Título e Sidebar
st.title("🤖 Agente de Inteligência Executiva")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ Configurações")
    
    # Tenta buscar a chave dos Secrets do Streamlit, senão pede input
    default_key = ""
    if "GOOGLE_API_KEY" in st.secrets:
        default_key = st.secrets["GOOGLE_API_KEY"]
    elif "GOOGLE_API_KEY" in os.environ:
        default_key = os.environ["GOOGLE_API_KEY"]
        
    api_key = st.text_input("Google API Key", value=default_key, type="password", help="Sua chave do Google AI Studio")
    
    st.subheader("🌐 Fontes de Dados")
    source_g1 = st.checkbox("G1 (Principais Notícias)", value=True)
    source_rss = st.checkbox("G1 RSS (Tecnologia)", value=True)
    
    st.subheader("🧠 Modelo IA")
    model_option = st.selectbox(
        "Selecione o Modelo",
        ("models/gemini-2.5-flash", "models/gemini-1.5-flash", "models/gemini-2.0-flash")
    )
    
    st.markdown("---")
    st.info("Este site coleta notícias em tempo real e gera relatórios estratégicos usando IA.")

# Inicialização dos componentes
if 'report' not in st.session_state:
    st.session_state.report = None
if 'news' not in st.session_state:
    st.session_state.news = []

# Layout de Colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 Coleta de Informação")
    
    if st.button("🚀 Iniciar Ciclo de Inteligência"):
        if not api_key:
            st.error("⚠️ Por favor, insira sua API Key no menu lateral.")
        else:
            with st.status("📡 Executando fluxo de dados...", expanded=True) as status:
                st.write("🕵️ Iniciando Web Scraping...")
                scraper = NewsScraper()
                all_news = []
                
                if source_g1:
                    st.write("📰 Coletando do G1...")
                    all_news.extend(scraper.scrape_g1())
                
                if source_rss:
                    st.write("🔌 Coletando via RSS...")
                    all_news.extend(scraper.scrape_rss())
                
                st.session_state.news = all_news
                st.write(f"✅ {len(all_news)} notícias encontradas.")
                
                if all_news:
                    st.write("🤖 Processando com Gemini...")
                    try:
                        agent = ReportAgent(api_key=api_key, model_name=model_option)
                        report = agent.generate_report(all_news)
                        st.session_state.report = report
                        status.update(label="✨ Ciclo concluído com sucesso!", state="complete", expanded=False)
                    except Exception as e:
                        st.error(f"Erro na IA: {e}")
                        status.update(label="❌ Falha no processamento.", state="error")
                else:
                    st.error("Nenhuma notícia encontrada.")
                    status.update(label="❌ Falha na coleta.", state="error")

    if st.session_state.news:
        st.write("### 🗞️ Notícias Coletadas")
        df = pd.DataFrame(st.session_state.news)
        st.dataframe(df[['title', 'source']], use_container_width=True)

with col2:
    st.subheader("📄 Relatório Executivo")
    if st.session_state.report:
        st.markdown(st.session_state.report)
        
        # Opção de Download
        st.download_button(
            label="📥 Baixar Relatório (Markdown)",
            data=st.session_state.report,
            file_name="relatorio_executivo.md",
            mime="text/markdown"
        )
    else:
        st.info("💡 O relatório aparecerá aqui após o processamento.")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido com Python, LangChain e Gemini 1.5 Flash.")
