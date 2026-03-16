import streamlit as st

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

# The React app is hosted on GitHub Pages — loads instantly, no srcdoc issues
st.components.v1.html(
    """
    <iframe
        src="https://kh0ttab.github.io/Titan/"
        style="width:100%;height:100vh;border:none;"
        allow="microphone"
    ></iframe>
    """,
    height=900,
    scrolling=False,
)
