from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "id": "crypto-trading-agent",
        "title": "Agentic Crypto Trading System",
        "tagline": "Multi-agent AI system for autonomous cryptocurrency trading",
        "description": (
            "A sophisticated multi-agent trading system built with CrewAI and LangGraph. "
            "Features include autonomous market analysis, sentiment analysis, risk management, "
            "backtesting, day trading strategies, and a debate mechanism where agents collaborate "
            "to reach consensus on trading decisions."
        ),
        "tech": ["Python", "CrewAI", "LangGraph", "Terraform", "Docker"],
        "highlights": [
            "Multi-agent debate system for trade consensus",
            "Real-time market data & sentiment analysis",
            "Backtesting engine with historical validation",
            "Day trading with position management",
            "Infrastructure as Code with Terraform",
        ],
        "icon": "📈",
    },
    {
        "id": "farm-ai-assistant",
        "title": "Farm AI Assistant",
        "tagline": "RAG-powered AI assistant for smart farm management",
        "description": (
            "An AI-powered farm management assistant built with FastAPI and OpenAI. "
            "Features a full RAG pipeline that ingests WhatsApp conversation history "
            "to provide context-aware farming advice. Includes document chunking, "
            "vector search with ChromaDB, and context augmentation for accurate, "
            "source-backed responses. Deployed with Docker and Kubernetes on cloud infrastructure."
        ),
        "tech": ["Python", "FastAPI", "OpenAI", "ChromaDB", "RAG", "Docker", "Kubernetes"],
        "highlights": [
            "RAG pipeline with WhatsApp chat ingestion",
            "Vector search using ChromaDB embeddings",
            "Context-augmented LLM responses with source attribution",
            "Farm performance analysis endpoint",
            "Kubernetes deployment with auto-scaling",
            "React Native mobile app integration via CORS",
        ],
        "icon": "🌾",
    },
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)


@app.route("/project/<project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        return "Project not found", 404
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
