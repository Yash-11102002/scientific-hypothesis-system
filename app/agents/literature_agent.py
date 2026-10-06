from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.models.schemas import ResearchState


client = OpenAI(api_key=OPENAI_API_KEY)


def literature_agent(state: ResearchState) -> ResearchState:

    topic = state["research_topic"]

    prompt = f"""
You are a scientific literature analysis agent.

Research Topic:
{topic}

Analyze the research topic and provide:

1. Important existing research findings
2. Major limitations in existing research
3. Possible research gaps

Do not generate hypotheses yet.

Return the answer in this format:

FINDINGS:
- finding 1
- finding 2
- finding 3

RESEARCH GAPS:
- gap 1
- gap 2
- gap 3
"""

    response = client.chat.completions.create(
        model="gpt-6-luna",
        messages=[
            {
                "role": "system",
                "content": "You are an academic literature analysis assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    findings = []
    gaps = []

    current_section = None

    for line in result.splitlines():

        line = line.strip()

        if line.upper().startswith("FINDINGS"):
            current_section = "findings"
            continue

        if line.upper().startswith("RESEARCH GAPS"):
            current_section = "gaps"
            continue

        if line.startswith("-"):

            item = line[1:].strip()

            if current_section == "findings":
                findings.append(item)

            elif current_section == "gaps":
                gaps.append(item)

    return {
        **state,
        "literature_findings": findings,
        "research_gaps": gaps
    }