import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class CodingAgent:
    """Agent specialized in code generation and programming tasks"""
    
    def __init__(self):
        self.client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY
        )
    
    def invoke(self, analysis_data):
        """Invoke the coding agent with analysis data"""
        messages = [
            {"role": "user", "content": f"You are a senior software engineer. Your task is to generate code based on the following analysis:\n\n{analysis_data}\n\nPlease write clean, well-documented Python code that implements the analysis findings. Include error handling and follow best practices."}
        ]
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.1
        )
        return response.choices[0].message.content
    
    @classmethod
    def create_coding_agent(cls):
        """Factory method to create a coding agent"""
        return cls()


if __name__ == "__main__":
    agent = CodingAgent.create_coding_agent()
    analysis_data = "The analysis shows that LangGraph can be used to build a multi-agent system. The system should have three agents: research, analysis, and coding."
    result = agent.invoke(analysis_data)
    print("Coding Agent Result:")
    print(result)