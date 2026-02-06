# 🤖 Multi-Agent AI System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-orange.svg)](https://openrouter.ai/)

A sophisticated multi-agent AI system that orchestrates specialized agents to collaboratively solve complex problems through research, analysis, and code generation.

## ✨ Features

- **🔍 Research Agent** - Gathers comprehensive information on any topic with cited sources
- **📊 Analysis Agent** - Extracts key insights, patterns, and trends from research data
- **💻 Coding Agent** - Generates clean, well-documented Python code based on analysis
- **🔄 Sequential Workflow** - Agents work in pipeline: Research → Analysis → Coding
- **🎨 Rich Console Output** - Beautiful formatted output with progress indicators
- **🔑 OpenRouter Integration** - Access to multiple LLM models through OpenRouter API

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenRouter API key ([Get one free](https://openrouter.ai/))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd multi_agent_system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   # Create .env file
   echo "OPENROUTER_API_KEY=your_api_key_here" > .env
   ```

### Usage

**Run with default query:**
```bash
python main.py
```

**Run with custom query:**
```bash
python main.py "Explain quantum computing and its applications"
```

**Example Output:**
```
🔍 Running Research Agent...
📊 Running Analysis Agent...
💻 Running Coding Agent...

=== Workflow Results ===
Research Results: Comprehensive research with sources...
Analysis Results: Key insights and recommendations...
Coding Results: Generated Python implementation...
```

## 📁 Project Structure

```
multi_agent_system/
├── 📄 main.py                 # Entry point - orchestrates the workflow
├── 📁 agents/                 # Specialized AI agents
│   ├── __init__.py           # Agent exports
│   ├── research_agent.py     # Information gathering agent
│   ├── analysis_agent.py     # Data analysis agent
│   └── coding_agent.py       # Code generation agent
├── 📁 utils/                  # Utility functions
│   └── helpers.py            # Formatting and logging utilities
├── 📁 tests/                  # Unit tests
│   └── test_workflow.py      # Workflow tests
├── 📄 requirements.txt        # Python dependencies
├── 📄 .env                    # Environment variables (not tracked)
└── 📄 README.md               # This file
```

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  User Query │────▶│   Research  │────▶│   Analysis  │────▶│    Coding   │
│             │     │    Agent    │     │    Agent    │     │    Agent    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                           │                   │                   │
                           ▼                   ▼                   ▼
                    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
                    │  Research   │    │  Analysis   │    │    Code     │
                    │   Results   │    │   Results   │    │   Results   │
                    └─────────────┘    └─────────────┘    └─────────────┘
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key | ✅ Yes |

### Agent Settings

Each agent can be configured with different parameters:

- **Research Agent**: `temperature=0.7` - Balanced creativity and accuracy
- **Analysis Agent**: `temperature=0.3` - Focused, analytical responses
- **Coding Agent**: `temperature=0.1` - Precise, deterministic code generation

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

Run a specific test:
```bash
python -m pytest tests/test_workflow.py -v
```

## 📝 Example Use Cases

- **Research & Development** - Gather information on emerging technologies
- **Data Analysis** - Analyze market trends and extract insights
- **Code Generation** - Generate implementations based on analysis
- **Educational Content** - Create comprehensive learning materials
- **Technical Documentation** - Generate code examples and explanations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenRouter](https://openrouter.ai/) - For providing unified API access to multiple LLMs
- [OpenAI](https://openai.com/) - For the underlying language models
- [Rich](https://github.com/Textualize/rich) - For beautiful terminal formatting

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Happy Coding! 🚀**
