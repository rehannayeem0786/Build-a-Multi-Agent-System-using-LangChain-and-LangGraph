from .research_agent import ResearchAgent
from .analysis_agent import AnalysisAgent
from .coding_agent import CodingAgent

# Factory functions
def create_research_agent():
    return ResearchAgent.create_research_agent()

def create_analysis_agent():
    return AnalysisAgent.create_analysis_agent()

def create_coding_agent():
    return CodingAgent.create_coding_agent()

__all__ = [
    'ResearchAgent',
    'AnalysisAgent', 
    'CodingAgent',
    'create_research_agent',
    'create_analysis_agent',
    'create_coding_agent'
]
