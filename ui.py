import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer", 
    layout="centered",
    initial_sidebar_state="collapsed"
    )
st.title("AI YouTube Video Analyzer")

# cache->fast access,temp storage ->most frequent access
@st.cache_resource

def get_agent():
    return build_youtube_agent()

agent = get_agent()

#input box
video_url = st.text_input("Enter YouTube video Link:")

button=st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing video..."):
        response=agent.run(
            f"Analyze this video: {video_url}",
            stream=True,
        )
    
    st.markdown('Analysis Report of Video: ')
    st.markdown(response.content)