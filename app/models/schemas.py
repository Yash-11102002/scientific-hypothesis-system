from typing import List, TypedDict


class ResearchState(TypedDict, total=False):
    research_topic: str

    literature_findings: List[str]
    research_gaps: List[str]

    hypotheses: List[str]

    experiment_design: str
    datasets: List[str]
    methods: List[str]
    evaluation_metrics: List[str]