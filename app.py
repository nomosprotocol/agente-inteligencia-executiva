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
                        
