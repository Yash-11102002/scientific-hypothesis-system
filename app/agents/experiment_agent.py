from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.models.schemas import ResearchState


client = OpenAI(api_key=OPENAI_API_KEY)


def experiment_agent(state: ResearchState) -> ResearchState:

    topic = state["research_topic"]

    hypotheses = state.get("hypotheses", [])

    prompt = f"""
You are a scientific experimental design agent.

Research Topic:
{topic}

Hypotheses:
{hypotheses}

Design an experiment for testing these hypotheses.

Provide:

1. Experimental methodology
2. Independent variables
3. Dependent variables
4. Control variables
5. Suitable datasets
6. Suitable research methods
7. Evaluation metrics
8. Experimental procedure

Keep the design practical and suitable for an academic research project.

Return a clear structured research experiment plan.
"""

    response = client.chat.completions.create(
        model="gpt-6-luna",
        messages=[
            {
                "role": "system",
                "content": "You are an experimental research design expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
    )

    result = response.choices[0].message.content

    return {
        **state,
        "experiment_design": result
    }