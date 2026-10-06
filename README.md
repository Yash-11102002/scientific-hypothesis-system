# Scientific Hypothesis Generation & Experimental Design System

## Overview

The Scientific Hypothesis Generation & Experimental Design System is a multi-agent Agentic AI application designed to assist researchers in the early stages of scientific research planning.

The system takes a research topic as input and uses three specialized AI agents to:

- Analyze literature-level findings
- Identify research gaps
- Generate testable research hypotheses
- Design suitable experiments
- Suggest datasets
- Suggest research methods
- Define evaluation metrics

## Problem Statement

Scientific research requires significant effort to understand existing literature, identify research gaps, formulate hypotheses, and design suitable experiments.

This project uses Agentic AI to divide these tasks among specialized agents and automatically generate a structured research plan.

## Agents

### 1. Literature Analysis Agent

Responsibilities:

- Analyze the given research topic
- Identify important literature-level findings
- Identify potential research gaps

Output:

- Literature findings
- Research gaps

### 2. Hypothesis Generation Agent

Responsibilities:

- Read literature findings
- Read research gaps
- Generate clear and scientifically testable hypotheses

Output:

- 2–3 research hypotheses

### 3. Experimental Design Agent

Responsibilities:

- Analyze generated hypotheses
- Design an experimental methodology
- Suggest independent and dependent variables
- Suggest datasets
- Suggest research methods
- Suggest evaluation metrics
- Define experimental procedure

Output:

- Complete experimental research plan

## Architecture

```text
User Research Topic
        |
        v
Literature Analysis Agent
        |
        v
Literature Findings + Research Gaps
        |
        v
Hypothesis Generation Agent
        |
        v
Research Hypotheses
        |
        v
Experimental Design Agent
        |
        v
Dataset + Methods + Metrics + Procedure
        |
        v
Final Research Plan



# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenAI API | AI model and reasoning |
| LangGraph | Multi-agent workflow orchestration |
| FastAPI | Backend REST API |
| Streamlit | Frontend user interface |
| Pydantic | Data validation |
| python-dotenv | Environment variable management |
| Requests | Frontend-backend API communication |

---

# 📁 Project Structure

```text
scientific-hypothesis-system/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── literature_agent.py
│   │   ├── hypothesis_agent.py
│   │   └── experiment_agent.py
│   │
│   ├── workflow/
│   │   ├── __init__.py
│   │   └── graph.py
│   │
│   └── models/
│       ├── __init__.py
│       └── schemas.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── papers/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md



⚙️ Installation
1. Clone the Repository
git clone https://github.com/Yash-11102002/scientific-hypothesis-system.git
cd scientific-hypothesis-system

2. Create Virtual Environment
python -m venv .venv

3. Activate Virtual Environment
Windows
.venv\Scripts\activate

After activation:
(.venv) E:\scientific-hypothesis-system>

4. Install Dependencies
pip install -r requirements.txt

🔐 Configure OpenAI API Key
Create a .env file in the project root directory.
OPENAI_API_KEY=your_openai_api_key_here

Important
Never commit the .env file to GitHub.
The .gitignore file excludes:
.env
.venv/
__pycache__/

A .env.example file is included for reference:
OPENAI_API_KEY=your_openai_api_key_here

🚀 Running the Backend
Open a terminal in the project directory.
Activate the virtual environment:
.venv\Scripts\activate

Start the FastAPI backend:
uvicorn app.main:app --reload

Backend URL:
http://127.0.0.1:8000

📚 FastAPI Swagger Documentation
FastAPI provides interactive API documentation at:
http://127.0.0.1:8000/docs

The /research endpoint accepts a research topic and executes the complete three-agent workflow.
Example Request
{
    "research_topic": "Impact of artificial intelligence on student learning"
}

🖥️ Running the Frontend
Open a second terminal.
Navigate to the project directory:
cd /d E:\scientific-hypothesis-system

Activate the virtual environment:
.venv\Scripts\activate

Run Streamlit:
streamlit run frontend\app.py

The application will normally open at:
http://localhost:8501


