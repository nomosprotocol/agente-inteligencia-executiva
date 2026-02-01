import google.generativeai as genai
import os

class ReportAgent:
        def __init__(self, api_key, model_name="models/gemini-2.5-flash"):
                    # Se a chave não for passada diretamente, tenta buscar do ambiente
                    actual_key = api_key if api_key else os.environ.get("GOOGLE_API_KEY")
                    if not actual_key:
                                    raise ValueError("Google API Key não configurada.")

        genai.configure(api_key=actual_key)
            self.model = genai.GenerativeModel(model_name)

    def generate_report(self, news_data):
                """Gera um relatório executivo a partir dos dados de notícias"""

        news_content = ""
        for idx, item in enumerate(news_data):
                        news_content += f"\n--- Notícia {idx+1} ---\n"
                        news_content += f"Título: {item['title']}\n"
                        news_content += f"Resumo: {item['summary']}\n"
                        news_content += f"Fonte: {item['source']}\n"

        prompt = f"""
                Você é um analista executivo sênior. Sua tarefa é criar um relatório executivo conciso e estratégico baseado nas notícias fornecidas.

                                Notícias:
                                        {news_content}

                                                        O relatório deve conter:
                                                                1. **Resumo Executivo**: Uma visão geral das principais tendências (máximo 3 parágrafos).
                                                                        2. **Principais Destaques**: Lista com os 3-5 pontos mais relevantes e seus impactos.
                                                                                3. **Análise de Tendências**: Como essas notícias se conectam e o que indicam para o futuro próximo.
                                                                                        4. **Recomendações Estratégicas**: Ações sugeridas com base nas informações.

                                                                                                        Use um tom profissional, objetivo e em Português Brasileiro.
                                                                                                                Formate o relatório em Markdown de forma elegante.
                                                                                                                        """

        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
        # Para testes locais, use uma variável de ambiente ou passe a chave aqui
        # NUNCA deixe a chave hardcoded ao subir para o GitHub
        print("Módulo carregado. Use a classe ReportAgent com sua API Key.")
