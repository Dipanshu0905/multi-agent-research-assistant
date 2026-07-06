import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Research Assistant")
st.markdown(
    "Research any topic using **Search Agent**, **Reader Agent**, **Writer**, and **Critic**."
)

topic = st.text_input(
    "Enter a research topic",
    placeholder="Example: Effects of war on stock market"
)

if st.button("🚀 Start Research", type="primary"):

    if topic.strip() == "":
        st.warning("Please enter a research topic.")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    try:

        status.info("🔍 Running Multi-Agent Research...")

        progress.progress(20)

        result = run_research_pipeline(topic)

        progress.progress(100)

        status.success("Research Completed Successfully!")

        st.divider()

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🔍 Search Results",
                "📖 Scraped Content",
                "📝 Report",
                "✅ Critic Review",
            ]
        )

        with tab1:
            st.subheader("Search Results")
            st.write(result["search_results"])

        with tab2:
            st.subheader("Scraped Content")
            st.write(result["scraped_content"])

        with tab3:
            st.subheader("Research Report")
            st.markdown(result["report"])

            st.download_button(
                "⬇ Download Report",
                result["report"],
                file_name="research_report.txt",
            )

        with tab4:
            st.subheader("Critic Feedback")
            st.markdown(result["feedback"])

    except Exception as e:
        st.error(str(e))