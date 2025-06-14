import streamlit as st
from utils.whisper_logic import load_whispers, get_random_whisper, get_whispers_by_tag, get_all_tags
import streamlit.components.v1 as components
import random
import datetime
import json
from streamlit_lottie import st_lottie

# Load data
whispers = load_whispers()

# Initialize favorites
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# Page config
st.set_page_config(page_title="Whispers of the Universe", layout="centered", initial_sidebar_state="expanded")

# Mode toggle
mode = st.sidebar.radio("🌗 Choose Mode", ["🌙 Dark", "🌞 Light"])
dark_mode = (mode == "🌙 Dark")

# Dynamic theme colors
font_family = "'Marcellus', serif"
bg_color = "#0e0e23" if dark_mode else "#f5f5f5"
text_color = "#ffffff" if dark_mode else "#1a1a1a"
card_bg = "#1a1a40" if dark_mode else "#e0d7ff"
primary_color = "#b388eb"
background_image_url = "https://raw.githubusercontent.com/mahimaaprajapati/whispers_of_universe/main/assets/background.jpg" if dark_mode else "https://raw.githubusercontent.com/mahimaaprajapati/whispers_of_universe/main/assets/light_background.jpg"  # <-- Add your light bg here

# Apply styles
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Marcellus&display=swap');

    html, body, [class*="css"] {{
        font-family: {font_family};
        background-color: {bg_color};
        color: {text_color};
    }}

    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    .stButton > button {{
        background-color: #512da8;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: all 0.3s ease-in-out;
    }}

    .stButton > button:hover {{
        background-color: #673ab7;
        transform: scale(1.05);
    }}
    </style>
""", unsafe_allow_html=True)

# Title & time
st.markdown(f"""
    <h1 style='text-align: center; color: {primary_color};'>🌌 Whispers of the Universe</h1>
    <p style='text-align: center; font-size: 18px; color: {text_color};'>
        {datetime.datetime.now().strftime('%A, %d %B %Y - %I:%M %p')}
    </p>
""", unsafe_allow_html=True)

# Lottie angel animation
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

try:
    lottie_angel = load_lottie_file("assets/angel.json")
    st_lottie(lottie_angel, speed=1, loop=True, quality="high", height=300)
except:
    st.warning("👼 Angel animation not found.")

# Sidebar - tag selector
st.sidebar.title("✨ Explore Whispers")
selected_tag = st.sidebar.selectbox("Select a Tag", ["All"] + get_all_tags(whispers))

# Whisper logic
if selected_tag == "All":
    whisper = get_random_whisper(whispers)
else:
    filtered = get_whispers_by_tag(whispers, selected_tag)
    whisper = random.choice(filtered) if filtered else None

# Whisper display
if whisper:
    st.markdown(f"""
        <div style="background: linear-gradient(145deg, {card_bg}, #2d2d6c);
                    padding: 30px; border-radius: 15px; margin-top: 20px;
                    box-shadow: 0 4px 30px rgba(0,0,0,0.3);">
            <h3 style="text-align: center; color: {primary_color};">🔮 Whisper #{whisper['id']}</h3>
            <p style="font-size: 24px; color: {text_color}; text-align: center; font-style: italic;">
                “{whisper['whisper']}”
            </p>
            <p style="font-size: 18px; color: #9f9fdd; margin-top: 20px;">
                🌱 <strong>Meaning:</strong> {whisper['meaning']}
            </p>
            <p style="font-size: 16px; color: #a0a0a0;">
                📚 <strong>Source:</strong> {whisper['source']} – {whisper['verse']}
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 🎙️ Speak it
    if st.button("🔊 Whisper"):
        components.html(f"""
            <script>
            var msg = new SpeechSynthesisUtterance("{whisper['whisper']}");
            msg.lang = "hi-IN";
            msg.rate = 0.9;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(msg);
            </script>
        """, height=0)

    # ❤️ Save to favorites
    if st.button("❤️ Save to Favorites"):
        if whisper['id'] not in [fav['id'] for fav in st.session_state.favorites]:
            st.session_state.favorites.append(whisper)
            st.success("Added to your favorites!")
else:
    st.warning("No whispers found for this tag.")



# 💖 View favorites
if st.sidebar.button("💖 View Favorites"):
    if st.session_state.favorites:
        st.sidebar.markdown("### Saved Whispers")
        for fav in st.session_state.favorites:
            st.sidebar.markdown(f"""
                <div style="background-color: #291a40; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
                    <p style="font-size: 14px; color: #fff;">“{fav['whisper']}”</p>
                    <p style="font-size: 12px; color: #aaa;">– {fav['source']} {fav['verse']}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.sidebar.warning("No favorites yet. Save one!")

# 🎵 Background music
st.markdown("""
    <audio autoplay loop>
        <source src="https://raw.githubusercontent.com/mahimaaprajapati/whispers_of_universe/main/assets/background.mp3" type="audio/mpeg">
    </audio>
""", unsafe_allow_html=True)
