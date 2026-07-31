import streamlit as st 
from streamlit_mic_recorder import speech_to_text
st.title("MY VOICE RECORDER APP ")

user_voice = speech_to_text(
    language="en-US",
    use_container_width=True,
    just_once=True,
    key="STT"
)

if user_voice:
    st.write("You said: ", user_voice)

