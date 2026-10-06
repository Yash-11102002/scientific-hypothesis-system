from langgraph.graph import StateGraph, END

from app.models.schemas import ResearchState

from app.agents.literature_agent import literature_agent
from app.agents.hypothesis_agent import hypothesis_agent
from app.agents.experiment_agent import experiment_agent


def build_workflow():

    workflow = StateGraph(ResearchState)

    workflow.add_node(
        "literature_agent",
        literature_agent
    )

    workflow.add_node(
        "hypothesis_agent",
        hypothesis_agent
    )

    workflow.add_node(
        "experiment_agent",
        experiment_agent
    )

    workflow.set_entry_point("literature_agent")

    workflow.add_edge(
        "literature_agent",
        "hypothesis_agent"
    )

    workflow.add_edge(
        "hypothesis_agent",
        "experiment_agent"
    )

    workflow.add_edge(
        "experiment_agent",
        END
    )

    return workflow.compile()