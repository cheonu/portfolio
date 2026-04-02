from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "id": "ai-clienteling-platform",
        "title": "AI Agentic Clienteling Platform",
        "tagline": "Multi-agent AI platform automating retail clienteling workflows",
        "company": "Salesfloor",
        "description": (
            "Architected a modular multi-agent AI platform to automate retail clienteling "
            "workflows — generating personalized associate tasks and communications end-to-end, "
            "from customer data qualification through content drafting. Designed a planner-led "
            "agent architecture using A2A (Agent-to-Agent) protocol and MCP (Model Context Protocol), "
            "with a central planner orchestrating specialized downstream agents via standardized "
            "JSON-RPC with discoverable agent cards."
        ),
        "tech": ["Python 3.12", "LangGraph", "LangChain", "MCP", "A2A", "LangSmith", "OpenTelemetry"],
        "highlights": [
            "Planner-led agent architecture with A2A protocol and MCP for standardized agent communication",
            "Deterministic SQL and rules-based logic for filtering; LLMs reserved for reasoning-heavy tasks",
            "Full observability with LangSmith for LLM tracing and OpenTelemetry for distributed telemetry",
            "End-to-end debugging and performance monitoring across agent hops",
            "Reusable architectural pattern with roadmap for production hardening and AI governance",
        ],
        "icon": "🤖",
    },
    {
        "id": "crypto-trading-agent",
        "title": "Agentic Crypto Trading System",
        "tagline": "7 concurrent LLM agents competing in live crypto markets",
        "company": "Personal Project",
        "description": (
            "Architected a multi-agent trading system running 7 concurrent pods on GKE, "
            "each powered by a distinct LLM (GPT-4o, Claude, Gemini, Deepseek, Grok, "
            "+ rule-based baseline) enabling robust ensemble decision-making. Features a "
            "multi-agent debate mechanism where AI agents reach consensus through structured "
            "argumentation before executing trades."
        ),
        "tech": ["Python", "LangGraph", "CrewAI", "GKE", "Helm", "Terraform"],
        "highlights": [
            "7 concurrent agents: GPT-4o, Claude, Gemini, Deepseek, Grok, baseline",
            "Multi-agent debate for trade consensus via structured argumentation",
            "Real-time RSI, EMA, VWAP, regime detection, sentiment analysis",
            "Day trading engine with stop-loss, take-profit, trailing stops, fee-aware filtering",
            "Deployed via Helm to GKE with Terraform IaC and Artifact Registry CI/CD",
        ],
        "icon": "📈",
    },
    {
        "id": "genai-service-desk",
        "title": "GenAI Service Desk Intelligence Platform",
        "tagline": "RAG-powered knowledge base for instant incident resolution",
        "company": "Symcor",
        "description": (
            "Built a GenAI-powered service desk solution that allows support teams to query "
            "the entire knowledge base in natural language — surfacing accurate, context-grounded "
            "answers instantly rather than searching through ticket histories and documentation. "
            "Includes a production RAG pipeline ingesting documents from Google Drive with "
            "automated sync, chunking, and semantic search."
        ),
        "tech": ["Python", "FastAPI", "OpenAI", "RAG", "ChromaDB", "LangChain"],
        "highlights": [
            "RAG pipeline ingesting tickets, runbooks, SOPs, FAQs into ChromaDB vector store",
            "Google Drive document sync with Sentence Transformers embeddings",
            "Semantic search across large enterprise corpora",
            "Reduced MTTR for recurring incidents",
            "Multi-tenant K8s deployment with auto-scaling, persistent vector storage, and TLS",
            "Async FastAPI REST endpoints consumed by React Native mobile app",
        ],
        "icon": "🎯",
    },
    {
        "id": "farm-ai-assistant",
        "title": "Farm AI Assistant",
        "tagline": "RAG-powered mobile assistant for agricultural operations",
        "company": "Personal Project",
        "description": (
            "Built a production RAG pipeline ingesting WhatsApp conversation data for "
            "context-aware agricultural advice with source attribution. Implemented semantic "
            "search using Sentence Transformers embeddings and ChromaDB vector store. Deployed "
            "to Kubernetes with auto-scaling, self-healing, persistent vector storage, and TLS. "
            "Integrated with React Native mobile app via async FastAPI REST endpoints."
        ),
        "tech": ["Python", "FastAPI", "OpenAI", "ChromaDB", "RAG", "Docker", "Kubernetes"],
        "highlights": [
            "RAG pipeline with WhatsApp chat ingestion",
            "Vector search using ChromaDB embeddings",
            "Context-augmented LLM responses with source attribution",
            "Kubernetes deployment with auto-scaling and self-healing",
            "React Native mobile app integration",
        ],
        "icon": "🌾",
    },
]

EXPERIENCE = [
    {
        "role": "AI Engineer / MLOps",
        "company": "Salesfloor",
        "period": "Oct 2024 — Present",
        "bullets": [
            "Designed and built a headless agentic AI application using LLM-driven decision loops, integrating into CRM and workflow systems",
            "Authored full agentic backend — orchestration logic, tool-calling interfaces, prompt chains, async task execution as containerised microservices",
            "Automated database operations (provisioning, backups, failover, schema migrations) reducing manual DBA intervention by over 60%",
            "Owned end-to-end release coordination for iOS/Android apps and built Jenkins CI/CD pipelines with automated testing and artifact promotion",
            "Established MLOps observability with model performance monitoring, drift detection, and alerting across inference services",
        ],
    },
    {
        "role": "AI / MLOps Engineer (Contract)",
        "company": "Symcor Inc.",
        "period": "Dec 2022 — Present",
        "bullets": [
            "Built GenAI-powered service desk intelligence solution with natural language knowledge base queries replacing manual searches",
            "Implemented RAG pipeline ingesting structured and unstructured data into vector store with automated chunking and incremental sync",
            "Designed AI-powered check fraud detection system using Python and Databricks with MLflow tracking",
            "Built feature engineering pipelines in PySpark for real-time fraud scoring at scale",
            "Deployed fraud detection models as inference endpoints on Azure ML with alerting and audit logging",
        ],
    },
    {
        "role": "Senior SRE / DevOps Engineer",
        "company": "Fullscript",
        "period": "Dec 2021 — Oct 2024",
        "bullets": [
            "Migrated .NET microservices to Kubernetes, improving deployment frequency by 40%",
            "Managed EKS/ECS infrastructure serving millions of requests with Terraform and CloudFormation",
            "Architected GitLab CI/CD pipelines supporting 50+ engineers across multiple product teams",
            "Designed Helm charts for K8s workloads including RBAC, secrets management, and ingress controllers",
            "Supported Black Friday traffic spikes through auto-scaling and load testing; integrated Wiz for SOC-2 compliance",
        ],
    },
    {
        "role": "Senior AWS Specialist",
        "company": "TVO",
        "period": "Sep 2020 — Dec 2021",
        "bullets": [
            "Conducted AWS Well-Architected Framework reviews across 5+ products",
            "Designed AWS Landing Zone using Control Tower for hybrid multi-account governance",
            "Containerized React applications and deployed via S3 static hosting with CloudFront CDN",
            "Led Scrum/Kanban ceremonies and mentored junior DevOps engineers",
        ],
    },
    {
        "role": "Software Engineer (Infrastructure & Automation)",
        "company": "Thales Group",
        "period": "Jan 2018 — Sep 2020",
        "bullets": [
            "Developed Python automation frameworks replacing fragile manual runbooks",
            "Built Python data pipeline utilities aggregating CloudWatch metrics into operational dashboards",
            "Authored CloudFormation templates and enforced IAM least-privilege across 20+ AWS accounts, cutting costs by 25%",
        ],
    },
    {
        "role": "Backend Engineer / Cloud Developer",
        "company": "Nexonia",
        "period": "Oct 2016 — Jan 2018",
        "bullets": [
            "Designed Python backend services and REST API integrations for expense management workflows",
            "Developed Lambda functions powering event-driven pipelines with SQS/SNS and DLQ error handling",
            "Configured multi-AZ RDS deployments (Aurora, MySQL) with read replicas achieving 99.9% availability",
        ],
    },
    {
        "role": "Systems & Automation Engineer",
        "company": "National Grid",
        "period": "Jul 2011 — Oct 2016",
        "bullets": [
            "Wrote Python scripts and automation tools managing critical energy infrastructure systems",
            "Developed internal dashboards and alerting systems for real-time infrastructure health metrics",
            "Maintained high-availability on-premises and hybrid systems for fault-tolerant design",
        ],
    },
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS, experience=EXPERIENCE)


@app.route("/project/<project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        return "Project not found", 404
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
