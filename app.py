from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Meu Caixa", page_icon="🛵", layout="centered")

st.markdown(
    """
    <style>
    header, #MainMenu, footer {visibility: hidden; height: 0;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {height: 100dvh !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "controle-entregas.html").read_text(encoding="utf-8")
components.html(html, height=800, scrolling=True)
