import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class AnalysisAgent:
    """Agent specialized in data analysis and insights"""
    
    def __init__(self):
        self.client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY
        )
    
    def invoke(self, research_data):
        """Invoke the analysis agent with research data"""
        messages = [
            {"role": "user", "content": f"You are a data analysis expert. Your task is to analyze the following research data and provide insights:\n\n{research_data}\n\nPlease identify key patterns, trends, and insights. Provide structured analysis with clear conclusions and recommendations."}
        ]
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3
        )
        return response.choices[0].message.content
    
    @classmethod
    def create_analysis_agent(cls):
        """Factory method to create an analysis agent"""
        return cls()


if __name__ == "__main__":
    agent = AnalysisAgent.create_analysis_agent()
    research_data = "LangGraph is a framework for building stateful, multi-actor applications with LLMs. It extends the concepts of LangChain with a more structured approach to agent workflows."
    result = agent.invoke(research_data)
    print("Analysis Agent Result:")
    print(result)
