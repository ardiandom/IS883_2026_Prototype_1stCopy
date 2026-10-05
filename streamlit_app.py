import streamlit as st
from google import genai
from google.genai import types

### Load your API Key
try:
    gemini_api_key = st.secrets['MyGeminiKey']
except (KeyError, FileNotFoundError):
    st.error("No Gemini key found. Add `MyGeminiKey` under **Manage app → ⋮ → Settings → Secrets**, then refresh this page.")
    st.stop()

client = genai.Client(api_key=gemini_api_key)

MODEL = "gemini-3.1-flash-lite"

st.title("Mood-Based AI Response")

# Radio button for mood
mood = st.radio(
    "How should the response feel?",
    ["Sad", "Neutral", "Happy"]
)

st.write("Press the button to get a response")

if st.button("Press me!"):
    prompt = f"""
    Write a haiku with a {mood.lower()} mood.
    Make sure the tone of the haiku matches the selected mood.
    """

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    st.write(response.text)
