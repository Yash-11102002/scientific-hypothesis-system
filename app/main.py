from fastapi import FastAPI
from pydantic import BaseModel

from app.workflow.graph import build_workflow


app = FastAPI(
    title="Scientific Hypothesis Generation & Experimental Design System"
)

workflow = build_workflow()


class ResearchRequest(BaseModel):

    research_topic: str


@app.get("/")
def home():

    return {
        "message": "Scientific Hypothesis Generation & Experimental Design System"
    }


@app.post("/research")
def generate_research_plan(request: ResearchRequest):

    initial_state = {
        "research_topic": request.research_topic
    }

    result = workflow.invoke(initial_state)

    return {
        "research_topic": result["research_topic"],
        "literature_findings": result.get(
            "literature_findings",
            []
        ),
        "research_gaps": result.get(
            "research_gaps",
            []
        ),
        "hypotheses": result.get(
            "hypotheses",
            []
        ),
        "experiment_design": result.get(
            "experiment_design",
            ""
        )
    }