from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).parent
DASHBOARD_FILE = BASE_DIR / "dashboard.html"

st.set_page_config(
    page_title="Flower Federation Dashboard",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if not DASHBOARD_FILE.exists():
    st.error("File dashboard.html tidak ditemukan. Pastikan file tersebut berada satu folder dengan app.py.")
    st.stop()

html = DASHBOARD_FILE.read_text(encoding="utf-8")

# Menampilkan dashboard HTML asli di dalam aplikasi Streamlit.
# Animasi, tombol Mulai/Reset, log, dan histogram tetap dijalankan oleh JavaScript asli.
components.html(html, height=1250, scrolling=True)
