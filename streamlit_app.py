import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Titan OS",
    page_icon="lion",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stAppDeployButton {display: none;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .stMainBlockContainer {padding: 0 !important;}
        iframe {border: none !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

groq_key = st.secrets.get("GROQ_API_KEY", "")

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# Inject Groq key
html_content = html_content.replace(
    '<div id="root"></div>',
    f'<div id="root"></div>\n<script>window.GROQ_API_KEY="{groq_key}";</script>',
)

st.components.v1.html(html_content, height=900, scrolling=True)
