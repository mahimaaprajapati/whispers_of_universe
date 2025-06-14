import streamlit as st
from utils.whisper_logic import load_whispers, get_random_whisper, get_whispers_by_tag, get_all_tags
import random

# Load data
whispers = load_whispers()

# Set page config
st.set_page_config(page_title="Whispers of the Universe", layout="centered")

# Background image using CSS
def add_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://raw.githubusercontent.com/mahimaaprajapati/whispers_of_universe/main/assets/background.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_background()

# Title
st.markdown("<h1 style='text-align: center; color: #ffffff;'>🌌 Whispers of the Universe 🌌</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("✨ Explore Whispers")
selected_tag = st.sidebar.selectbox("Select a Tag", ["All"] + get_all_tags(whispers))

# Logic
if selected_tag == "All":
    whisper = get_random_whisper(whispers)
    st.markdown(f"<h3 style='color: #fff;'>🔮 Whisper #{whisper['id']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<blockquote style='color: #dcdcdc; font-size: 20px;'>{whisper['whisper']}</blockquote>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #cccccc;'>🌱 Meaning: {whisper['meaning']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #aaa;'>📚 Source: {whisper['source']} - {whisper['verse']}</p>", unsafe_allow_html=True)
else:
    filtered_whispers = get_whispers_by_tag(whispers, selected_tag)
    st.markdown(f"### Showing whispers tagged with: `{selected_tag}`")
    for whisper in filtered_whispers:
        st.markdown(f"**🔹 Whisper #{whisper['id']}** — *{whisper['source']}* - {whisper['verse']}")
        st.markdown(f"> {whisper['whisper']}")
        st.markdown(f"**Meaning:** {whisper['meaning']}")
        st.markdown("---")

# Optional: Add audio
st.audio("assets/background.mp3", format="audio/mp3", start_time=0)
