import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Titan OS",
    page_icon="lion",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome for full-screen app experience
st.markdown(
    """
    <style>
        /* Hide Streamlit header, footer, menu */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stAppDeployButton {display: none;}

        /* Remove default padding so the React app fills the viewport */
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        .stMainBlockContainer {
            padding: 0 !important;
        }

        /* Make the iframe fill the page */
        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inject Groq API key from Streamlit secrets into the HTML
groq_key = st.secrets.get("GROQ_API_KEY", "")

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# Inject the key as a global JS variable before the React app runs
key_script = f'<script>window.GROQ_API_KEY="{groq_key}";</script>'
html_content = html_content.replace('<div id="root"></div>', f'<div id="root"></div>\n  {key_script}')

# Render the full React app inside Streamlit
st.components.v1.html(html_content, height=900, scrolling=True)
