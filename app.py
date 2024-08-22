from src.youtube_transcriber import YoutubeVideoSummarizer
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

st.set_page_config(
    page_title="Youtube Summarizer",
    page_icon="./assets/icon.png"
)

def summary(video_url, api_key):
    youtube_transcriber = YoutubeVideoSummarizer(video_url=video_url, api_key=api_key)
    transcript = youtube_transcriber.extract_transcript()
    summary = youtube_transcriber.generate_summary(transcript)
    return summary


def ui():
    # Sidebar
    with st.sidebar:
        st.header("📝 About")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("The **YouTube Transcript** is a powerful tool designed to help users quickly grasp the key points of a YouTube video without needing to watch the entire content.")
        st.markdown("Sign up and get an API Key: [Google API Key](https://aistudio.google.com/app/apikey)")
        api_key = st.text_input("API Key", type="password", placeholder="Enter Google API key", label_visibility="hidden")

    with st.container():
        with st.container(height=250):
            st.title("Youtube Summarizer")
            
            video_url = st.text_input("YouTube Video URL", placeholder="Enter YouTube video URL", label_visibility="hidden")
            if st.button("Summarize"):
                response = summary(video_url, api_key=api_key)

                st.subheader("Summary")
                with st.container(height=600):
                    st.markdown(response)

if __name__ == "__main__":
    ui()