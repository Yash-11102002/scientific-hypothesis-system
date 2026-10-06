import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/research"


st.set_page_config(
    page_title="Scientific Hypothesis Generation System",
    page_icon="🔬",
    layout="wide"
)


st.title("🔬 Scientific Hypothesis Generation & Experimental Design System")

st.markdown(
    """
Generate research hypotheses from a research topic and automatically
design an experimental plan with datasets, methods and evaluation metrics.
"""
)

st.divider()


research_topic = st.text_area(
    "Enter Research Topic",
    placeholder="Example: Impact of artificial intelligence on student learning",
    height=100
)


generate_button = st.button(
    "🚀 Generate Research Plan",
    type="primary",
    use_container_width=True
)


if generate_button:

    if not research_topic.strip():

        st.warning("Please enter a research topic.")

    else:

        with st.spinner("Agents are working..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "research_topic": research_topic
                    },
                    timeout=300
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Research plan generated successfully!")

                    # --------------------------------
                    # LITERATURE
                    # --------------------------------

                    st.header("📚 Literature Findings")

                    findings = result.get(
                        "literature_findings",
                        []
                    )

                    for finding in findings:

                        st.markdown(
                            f"- {finding}"
                        )

                    # --------------------------------
                    # RESEARCH GAPS
                    # --------------------------------

                    st.header("🔎 Research Gaps")

                    gaps = result.get(
                        "research_gaps",
                        []
                    )

                    for gap in gaps:

                        st.markdown(
                            f"- {gap}"
                        )

                    # --------------------------------
                    # HYPOTHESES
                    # --------------------------------

                    st.header("💡 Generated Hypotheses")

                    hypotheses = result.get(
                        "hypotheses",
                        []
                    )

                    for index, hypothesis in enumerate(
                        hypotheses,
                        start=1
                    ):

                        st.markdown(
                            f"**H{index}:** {hypothesis}"
                        )

                    # --------------------------------
                    # EXPERIMENT
                    # --------------------------------

                    st.header("🧪 Experimental Design")

                    experiment = result.get(
                        "experiment_design",
                        ""
                    )

                    st.markdown(experiment)

                else:

                    st.error(
                        f"Backend Error: {response.status_code}"
                    )

                    st.code(
                        response.text
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to FastAPI backend. "
                    "Please start the backend first."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request took too long. "
                    "Please try again."
                )

            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )