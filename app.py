import streamlit as st
import pandas as pd
from scraper import NewsScraper
from agent import ReportAgent
import time
import os

st.set_page_config(page_title="Agente de Inteligência Executiva", page_icon="🤖", layout="wide")

st.title("🤖 Agente de Inteligência Executiva")
st.markdown("---")

with st.sidebar:
        st.header("⚙️ Configurações")
        api_key = st.secrets.get("GOOGLE_API_KEY", "")
        if not api_key:
                    api_key = st.text_input("Google API Key", type="password")
else:
        st.success("✅ API Key carregada")

    source_g1 = st.checkbox("G1 (Notícias)", value=True)
    source_rss = st.checkbox("G1 RSS (Tecnologia)", value=True)
    model_option = st.selectbox("Modelo IA", ("models/gemini-2.5-flash", "models/gemini-1.5-flash"))

if 'report' not in st.session_state:
        st.session_state.report = None
    if 'news' not in st.session_state:
            st.session_state.news = []

col1, col2 = st.columns([1, 2])

with col1:
        st.subheader("🔍 Coleta")
        if st.button("🚀 Iniciar Ciclo"):
                    if not api_key:
                                    st.error("Insira a API Key")
        else:
                        with st.spinner("Processando..."):
                                            scraper = NewsScraper()
                                            news = []
                                            if source_g1:
                                                                    news.extend(scraper.scrape_g1())
                                                                if source_rss:
                                                                                        news.extend(scraper.scrape_rss())
                                                                                    st.session_state.news = news
                                            if news:
                                                                    agent = ReportAgent(api_key=api_key, model_name=model_option)
                                                                    st.session_state.report = agent.generate_report(news)
        else:
                        st.error("Nenhuma notícia encontrada.")

        if st.session_state.news:
                    st.write(f"📊 Coletadas: {len(st.session_state.news)}")
                    for item in st.session_state.news[:5]:
                                    st.write(f"- {item['title']}")

            with col2:
                    st.subheader("📑 Relatório")
                    if st.session_state.report:
                                st.markdown(st.session_state.report)
else:
        st.info("Aguardando geração...")
