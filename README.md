project_name: "Agentic AI E-commerce Customer Service Agent"

description: |
  A multi-agent, retrieval-augmented customer support system for an e-commerce
  environment. Supports order tracking queries, policy/FAQ questions via RAG,
  and provides both a CLI and Web UI interface. Built using Python, FastAPI,
  HTML/JavaScript, and the OpenAI API.

components:
  orchestrator_agent:
    purpose: "Classifies intent, routes queries, and manages sub-agent workflows."
  order_agent:
    purpose: "Handles order lookup and order status queries using structured CSV data."
  faq_agent:
    purpose: "Uses embeddings and cosine similarity to retrieve relevant FAQ information (RAG)."
  conversation_state:
    purpose: "Enables multi-turn workflows such as asking for missing order IDs."
  llm_client:
    purpose: "Handles OpenAI chat completions and embedding generation."
  logger:
    purpose: "Logs each interaction to JSONL for evaluation and debugging."
  web_ui:
    backend: "FastAPI /chat endpoint"
    frontend: "HTML + JavaScript chat interface"

project_structure:
  - agents/orchestrator.py
  - utils/llm_client.py
  - utils/logger.py
  - utils/state.py
  - tools/order_tools.py
  - tools/faq_tools.py
  - data/orders.csv
  - data/faq.json
  - web/main_api.py
  - web/index.html
  - logs/agent_logs.jsonl
  - main.py
  - requirements.txt
  - README.md

installation:
  environment: "PyCharm recommended"
  steps:
    - "Open the project folder in PyCharm."
    - "Create a new virtual environment: File > Settings > Project > Python Interpreter > Add Interpreter > New Virtualenv."
    - "Install dependencies using 'pip install -r requirements.txt'."

dependencies:
  - fastapi
  - uvicorn
  - openai
  - python-dotenv
  - numpy

env_setup:
  file: ".env"
  variables:
    OPENAI_API_KEY: "your_api_key_here"

running:
  cli:
    command: "python main.py"
    notes: "Runs the chatbot in terminal mode."
  web:
    start_api: "uvicorn web.main_api:app --reload"
    open_ui: "Open web/index.html in a browser"

workflow:
  - "User sends message via CLI or Web UI."
  - "Orchestrator classifies intent: ORDER, FAQ, or OTHER."
  - "ConversationState ensures multi-turn logic."
  - "Order Agent or FAQ Agent handles the query."
  - "LLM generates the final response from structured or retrieved data."
  - "Logger writes the full interaction to logs."

troubleshooting:
  web_ui_not_responding: "Ensure FastAPI is running using: uvicorn web.main_api:app --reload"
  modulename_error: "Ensure PyCharm working directory is set to the project root."
  api_key_error: "Check that your .env file contains a valid OPENAI_API_KEY."

requirements:
  python_version: "3.9+"
  tools:
    - "PyCharm IDE"
    - "OpenAI API key"

