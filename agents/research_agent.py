import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class ResearchAgent:
    """Agent specialized in research and information gathering"""
    
    def __init__(self):
        self.client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY
        )
    
    def invoke(self, query):
        """Invoke the research agent with a query"""
        messages = [
            {"role": "user", "content": f"You are a research assistant. Your task is to gather comprehensive information about: {query}\n\nPlease provide detailed, well-researched information with sources and examples. Focus on accuracy and completeness."}
        ]
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    
    @classmethod
    def create_research_agent(cls):
        """Factory method to create a research agent"""
        return cls()


if __name__ == "__main__":
    agent = ResearchAgent.create_research_agent()
    result = agent.invoke("What is LangGraph and how does it work?")
    print("Research Agent Result:")
    print(result)