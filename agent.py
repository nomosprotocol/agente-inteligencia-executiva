import google.generativeai as genai
import os

class ReportAgent:
    def __init__(self, api_key, model_name="models/gemini-2.5-flash"):
        genai.configure(api_key=api_key)
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
    API_KEY = "AIzaSyB_YoeHfED5tJ88esrMUJfxYQSivHquUFw"
    mock_news = [
        {"title": "IA Generativa revoluciona o mercado de trabalho", "summary": "Novas ferramentas aumentam produtividade em 40%.", "source": "TechCrunch"},
        {"title": "Brasil lidera adoção de energias renováveis", "summary": "Matriz energética brasileira atinge 90% de fontes limpas.", "source": "Exame"}
    ]
    
    try:
        agent = ReportAgent(api_key=API_KEY)
        print("Gerando relatório de teste...")
        report = agent.generate_report(mock_news)
        print("\n--- RELATÓRIO GERADO ---\n")
        print(report)
    except Exception as e:
        print(f"Erro: {e}")
