import streamlit as st
from transcript_utils import fetch_transcript
from summarizer import summarize_text
from qa_engine import create_qa_chain

st.set_page_config(page_title="YouTube Video Q&A Bot", layout="centered")
st.title("📺 YouTube Video Q&A Bot")
st.markdown("Paste a YouTube video link to get a summary and ask questions.")

# Input: YouTube video link
video_url = st.text_input("🔗 Enter YouTube Video URL")

if video_url:
    with st.spinner("Fetching transcript..."):
        transcript = fetch_transcript(video_url)

    if transcript.startswith("Transcript is disabled") or transcript.startswith("No transcript") or transcript.startswith("Error"):
        st.error(transcript)
    else:
        st.success("Transcript fetched successfully ✅")

        with st.expander("📄 Show Transcript"):
            st.write(transcript[:3000] + "..." if len(transcript) > 3000 else transcript)

        with st.spinner("Summarizing video..."):
            summary = summarize_text(transcript)
            st.subheader("🧠 Video Summary")
            st.write(summary)

        st.subheader("❓ Ask a Question")
        user_question = st.text_input("Type your question here")

        if user_question:
            with st.spinner("Thinking..."):
                qa_chain = create_qa_chain(transcript)
                response = qa_chain.run(user_question)
                st.markdown(f"**Answer:** {response}")
