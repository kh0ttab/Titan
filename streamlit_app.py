import streamlit as st

st.set_page_config(
    page_title="Titan OS",
    page_icon="lion",
    layout="wide",
    initial_sidebar_state="collapsed",
)

groq_key = st.secrets.get("GROQ_API_KEY", "")

# Hide Streamlit UI
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stAppDeployButton {display: none;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .stMainBlockContainer {padding: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Tiny iframe wrapper — loads the full React app from static file
# (avoids the srcdoc size/sandbox issues that caused the black screen)
st.components.v1.html(
    f"""
    <html>
    <body style="margin:0;padding:0;overflow:hidden;background:#060b14;">
    <script>window.GROQ_API_KEY="{groq_key}";</script>
    <iframe
        src="/app/static/index.html"
        style="width:100%;height:100vh;border:none;position:absolute;top:0;left:0;"
        allow="microphone"
    ></iframe>
    </body>
    </html>
    """,
    height=900,
    scrolling=False,
)
