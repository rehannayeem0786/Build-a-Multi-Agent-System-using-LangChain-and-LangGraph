from dotenv import load_dotenv
import os
from agents import create_research_agent, create_analysis_agent, create_coding_agent

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("Please set OPENROUTER_API_KEY in your .env file")


def run_workflow(query):
    """Run the complete workflow with the given query"""
    print(f"\n{'='*60}")
    print(f"🚀 STARTING MULTI-AGENT WORKFLOW")
    print(f"{'='*60}")
    print(f"\n📋 Query: {query}")
    
    # Step 1: Research
    print(f"\n{'─'*60}")
    print(f"STEP 1/3 🔍 RESEARCH PHASE")
    print(f"{'─'*60}")
    print("⏳ Gathering comprehensive information...")
    research_agent_obj = create_research_agent()
    research_results = research_agent_obj.invoke(query)
    print("✅ Research completed!")
    
    # Step 2: Analysis
    print(f"\n{'─'*60}")
    print(f"STEP 2/3 📊 ANALYSIS PHASE")
    print(f"{'─'*60}")
    print("⏳ Extracting insights and patterns...")
    analysis_agent_obj = create_analysis_agent()
    analysis_results = analysis_agent_obj.invoke(research_results)
    print("✅ Analysis completed!")
    
    # Step 3: Coding
    print(f"\n{'─'*60}")
    print(f"STEP 3/3 💻 CODING PHASE")
    print(f"{'─'*60}")
    print("⏳ Generating implementation code...")
    coding_agent_obj = create_coding_agent()
    coding_results = coding_agent_obj.invoke(analysis_results)
    print("✅ Code generation completed!")
    
    return {
        "research": research_results,
        "analysis": analysis_results,
        "coding": coding_results,
        "complete": True
    }


if __name__ == "__main__":
    import sys

    print(f"\n{'='*60}")
    print("🤖 MULTI-AGENT AI SYSTEM")
    print(f"{'='*60}")
    print("\nAvailable Agents:")
    print("  🔍 Research Agent - Gathers comprehensive information")
    print("  📊 Analysis Agent - Extracts insights and patterns")
    print("  💻 Coding Agent - Generates implementation code")
    print(f"\n{'='*60}")

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"\n📋 Query (from command line): {query}")
    else:
        print("\n💬 Please enter your query for the agents:")
        print("   (Example: 'Explain blockchain technology and its applications')")
        print(f"{'─'*60}")
        query = input("> ").strip()
        
        if not query:
            print("\n⚠️ No query provided. Using default example query.")
            query = "Explain the concept of quantum computing and its applications"

    print(f"\n✅ Query accepted: {query}")
    
    result = run_workflow(query)


    # Final Results Display
    print(f"\n{'='*60}")
    print(f"📊 FINAL RESULTS")
    print(f"{'='*60}")
    
    print(f"\n{'─'*60}")
    print(f"🔍 RESEARCH OUTPUT")
    print(f"{'─'*60}")
    print(result.get('research', 'No research results'))
    
    print(f"\n{'─'*60}")
    print(f"📊 ANALYSIS OUTPUT")
    print(f"{'─'*60}")
    print(result.get('analysis', 'No analysis results'))
    
    print(f"\n{'─'*60}")
    print(f"💻 CODE OUTPUT")
    print(f"{'─'*60}")
    print(result.get('coding', 'No coding results'))
    
    print(f"\n{'='*60}")
    print(f"✅ WORKFLOW COMPLETED SUCCESSFULLY!")
    print(f"{'='*60}")
