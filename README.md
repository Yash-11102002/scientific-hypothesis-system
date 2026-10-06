# 🔬 Scientific Hypothesis Generation & Experimental Design System

## Overview

The **Scientific Hypothesis Generation & Experimental Design System** is a multi-agent **Agentic AI** application designed to assist researchers in the early stages of scientific research planning.

The system takes a research topic as input and uses three specialized AI agents to:

- Analyze literature-level findings
- Identify research gaps
- Generate testable research hypotheses
- Design suitable experiments
- Suggest datasets
- Suggest research methods
- Define evaluation metrics

The system is designed to simplify the research planning process by dividing the overall task among specialized AI agents.

---

# 🎯 Problem Statement

Scientific research requires significant effort to understand existing literature, identify research gaps, formulate hypotheses, and design suitable experiments.

This project uses **Agentic AI** to divide these tasks among specialized agents and automatically generate a structured research plan from a given research topic.

### Problem Statement

> **Scientific Hypothesis Generation & Experimental Design System**

The system is responsible for:

- Analyzing research-related information
- Identifying research gaps
- Generating scientifically testable hypotheses
- Suggesting suitable datasets
- Suggesting research methods
- Designing experiments
- Defining evaluation metrics

---

# 🤖 Multi-Agent System

The system consists of exactly **three specialized AI agents**.

## 1. Literature Analysis Agent

### Responsibilities

- Analyze the given research topic
- Identify important literature-level findings
- Identify potential research gaps
- Summarize important observations related to the topic

### Output

- Literature Findings
- Research Gaps

---

## 2. Hypothesis Generation Agent

### Responsibilities

- Read literature findings
- Read research gaps
- Generate clear and scientifically testable hypotheses
- Ensure hypotheses are specific and testable

### Output

- 2–3 Research Hypotheses

---

## 3. Experimental Design Agent

### Responsibilities

- Analyze generated hypotheses
- Design an experimental methodology
- Suggest independent variables
- Suggest dependent variables
- Suggest control variables
- Suggest suitable datasets
- Suggest research methods
- Suggest evaluation metrics
- Define experimental procedure

### Output

- Complete Experimental Research Plan

---

# 🏗️ System Architecture

```text
                    USER
                      |
                      v
              RESEARCH TOPIC
                      |
                      v
        +---------------------------+
        |  LITERATURE ANALYSIS      |
        |         AGENT             |
        +---------------------------+
                      |
                      v
          Literature Findings
          + Research Gaps
                      |
                      v
        +---------------------------+
        |  HYPOTHESIS GENERATION    |
        |         AGENT             |
        +---------------------------+
                      |
                      v
              Research
              Hypotheses
                      |
                      v
        +---------------------------+
        |   EXPERIMENTAL DESIGN     |
        |         AGENT             |
        +---------------------------+
                      |
                      v
              FINAL RESEARCH
                  PLAN
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Datasets     Methods    Evaluation
                              Metrics
```

---

# 🔄 Agent Workflow

The agents communicate sequentially through a shared state managed by **LangGraph**.

```text
Research Topic
      |
      v
Literature Analysis Agent
      |
      | Findings + Research Gaps
      v
Hypothesis Generation Agent
      |
      | Research Hypotheses
      v
Experimental Design Agent
      |
      v
Final Research Plan
```

### Workflow Steps

1. User enters a research topic
2. Literature Analysis Agent analyzes the topic
3. Literature findings and research gaps are generated
4. Hypothesis Generation Agent uses these findings and gaps
5. Testable research hypotheses are generated
6. Experimental Design Agent uses the generated hypotheses
7. Experimental methodology is generated
8. Suitable datasets and research methods are suggested
9. Evaluation metrics are defined
10. Final research plan is displayed to the user

---

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
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Yash-11102002/scientific-hypothesis-system.git
cd scientific-hypothesis-system
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate Virtual Environment

### Windows

```cmd
.venv\Scripts\activate
```

After activation:

```text
(.venv) E:\scientific-hypothesis-system>
```

## 4. Install Dependencies

```cmd
pip install -r requirements.txt
```

---

# 🔐 Configure OpenAI API Key

Create a `.env` file in the project root directory.

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Important

Never commit the `.env` file to GitHub.

The `.gitignore` file excludes:

```text
.env
.venv/
__pycache__/
```

A `.env.example` file is included for reference:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

# 🚀 Running the Backend

Open a terminal in the project directory.

Activate the virtual environment:

```cmd
.venv\Scripts\activate
```

Start the FastAPI backend:

```cmd
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

# 📚 FastAPI Swagger Documentation

FastAPI provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

The `/research` endpoint accepts a research topic and executes the complete three-agent workflow.

### Example Request

```json
{
    "research_topic": "Impact of artificial intelligence on student learning"
}
```

---

# 🖥️ Running the Frontend

Open a **second terminal**.

Navigate to the project directory:

```cmd
cd /d E:\scientific-hypothesis-system
```

Activate the virtual environment:

```cmd
.venv\Scripts\activate
```

Run Streamlit:

```cmd
streamlit run frontend\app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

# 🧪 Example Input

Enter the following research topic into the application:

```text
Impact of artificial intelligence on student learning
```

---

# 📊 Example Output

The system generates four major outputs.

## Literature Findings

Example:

```text
- Adaptive learning systems can provide personalized learning support
- Generative AI can provide explanations and feedback
- AI-assisted task completion does not always guarantee long-term retention
- Further investigation is required into long-term learning outcomes
```

## Research Gaps

Example:

```text
- Limited evidence on long-term retention after AI-assisted learning
- Need to compare different forms of AI usage
- Need for studies involving diverse learners and realistic environments
```

## Generated Hypotheses

Example:

```text
H1:
Adaptive AI tutoring with adaptive hints and feedback will produce
higher delayed retention and transfer than answer-generating AI.

H2:
AI-guided adaptive practice will produce greater improvement in
unaided post-test performance than conventional practice.

H3:
The effect of AI-assisted learning will vary according to the
learner's baseline achievement level.
```

## Experimental Design

The Experimental Design Agent generates:

- Experimental methodology
- Independent variables
- Dependent variables
- Control variables
- Suitable datasets
- Research methods
- Evaluation metrics
- Experimental procedure

---

# 🔗 API Workflow

The Streamlit frontend communicates with the FastAPI backend.

```text
Streamlit UI
     |
     | HTTP POST
     v
FastAPI /research
     |
     v
LangGraph Workflow
     |
     +----------------------+
     |                      |
     v                      v
Literature Agent      Hypothesis Agent
     |                      |
     +----------+-----------+
                |
                v
        Experiment Agent
                |
                v
         Final JSON Result
                |
                v
          Streamlit UI
```

---

# 🧠 Shared Agent State

LangGraph maintains a shared state between the agents.

The state can contain:

```text
research_topic
literature_findings
research_gaps
hypotheses
experiment_design
datasets
methods
evaluation_metrics
```

This allows the output of one agent to become the input/context for the next agent.

---

# 🤖 Why Three Agents?

The project uses exactly three agents because each major research-planning task has a clearly defined responsibility.

```text
Literature Analysis Agent
          |
          v
Understand Existing Research
          |
          v
Hypothesis Generation Agent
          |
          v
Generate Testable Hypotheses
          |
          v
Experimental Design Agent
          |
          v
Create Experimental Research Plan
```

This keeps the system:

- Simple
- Modular
- Understandable
- Easy to test
- Easy to extend

---

# 📈 Evaluation

The current implementation focuses on functional evaluation.

The following components were successfully tested:

| Component | Result |
|---|---|
| Literature Analysis Agent | ✅ Successful |
| Hypothesis Generation Agent | ✅ Successful |
| Experimental Design Agent | ✅ Successful |
| LangGraph Workflow | ✅ Successful |
| FastAPI Backend | ✅ Successful |
| Streamlit Frontend | ✅ Successful |
| End-to-End Execution | ✅ Successful |

---

# 🛠️ Troubleshooting

## Streamlit Command Not Recognized

If you see:

```text
'streamlit' is not recognized as an internal or external command
```

activate the virtual environment first:

```cmd
.venv\Scripts\activate
```

Then run:

```cmd
streamlit run frontend\app.py
```

---

## FastAPI Backend Not Running

Make sure the backend is running in another terminal:

```cmd
uvicorn app.main:app --reload
```

Then start Streamlit in the second terminal.

---

## API Key Error

Check that `.env` exists in the project root:

```text
scientific-hypothesis-system/
│
├── .env
├── app/
├── frontend/
└── requirements.txt
```

The `.env` file should contain:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

# 🔮 Future Scope

The current system focuses on the core three-agent workflow.

Future improvements may include:

- Retrieval-Augmented Generation using research papers
- PDF research paper ingestion
- Vector database integration
- Citation-based literature analysis
- Automatic research paper retrieval
- Research report generation
- Advanced evaluation of generated hypotheses
- Automated experiment result analysis
- Integration with scientific research databases

---

# 📚 Current Scope vs Future Scope

| Feature | Status |
|---|---|
| Literature Analysis Agent | ✅ Implemented |
| Hypothesis Generation Agent | ✅ Implemented |
| Experimental Design Agent | ✅ Implemented |
| LangGraph Workflow | ✅ Implemented |
| FastAPI Backend | ✅ Implemented |
| Streamlit Frontend | ✅ Implemented |
| RAG | 🔮 Future Scope |
| PDF Paper Ingestion | 🔮 Future Scope |
| Vector Database | 🔮 Future Scope |
| Citation-based Retrieval | 🔮 Future Scope |

---
