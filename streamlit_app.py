import streamlit as st

st.set_page_config(
    page_title="Titan OS",
    page_icon="lion",
    layout="wide",
    initial_sidebar_state="collapsed",
)

groq_key = st.secrets.get("GROQ_API_KEY", "")

# Full-page iframe pointing to the static HTML file
st.markdown(
    f"""
    <style>
        #MainMenu {{visibility: hidden;}}
        header {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        .stAppDeployButton {{display: none;}}
        .block-container {{padding: 0 !important; max-width: 100% !important;}}
        .stMainBlockContainer {{padding: 0 !important;}}
    </style>
    <script>
        // Pass API key to the iframe once it loads
        window.addEventListener('message', function(e) {{
            if (e.data === 'titan-ready') {{
                document.getElementById('titan-frame').contentWindow.postMessage(
                    {{type: 'groq-key', key: '{groq_key}'}}, '*'
                );
            }}
        }});
    </script>
    <iframe
        id="titan-frame"
        src="app/static/index.html"
        style="width:100%;height:100vh;border:none;position:fixed;top:0;left:0;z-index:9999;"
    ></iframe>
    """,
    unsafe_allow_html=True,
)
