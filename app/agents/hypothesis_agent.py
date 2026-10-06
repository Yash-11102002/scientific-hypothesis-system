from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.models.schemas import ResearchState


client = OpenAI(api_key=OPENAI_API_KEY)


def hypothesis_agent(state: ResearchState) -> ResearchState:

    topic = state["research_topic"]

    findings = state.get("literature_findings", [])
    gaps = state.get("research_gaps", [])

    prompt = f"""
You are a scientific hypothesis generation agent.

Research Topic:
{topic}

Literature Findings:
{findings}

Research Gaps:
{gaps}

Generate 2-3 clear and scientifically testable hypotheses.

Each hypothesis must:

- Be measurable
- Be testable
- Be related to the identified research gaps
- Clearly identify the relationship between variables

Return only the hypotheses as a numbered list.
"""

    response = client.chat.completions.create(
        model="gpt-6-luna",
        messages=[
            {
                "role": "system",
                "content": "You are a scientific research hypothesis generation expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    hypotheses = []

    for line in result.splitlines():

        line = line.strip()

        if line and line[0].isdigit():

            hypothesis = line.split(".", 1)[-1].strip()
            hypotheses.append(hypothesis)

    return {
        **state,
        "hypotheses": hypotheses
    }