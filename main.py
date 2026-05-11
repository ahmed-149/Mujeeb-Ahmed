import streamlit as st
import os
import smtplib
from email.message import EmailMessage

# ─────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Mujeeb Ahmed",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
#  GLOBAL CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&family=Lato:ital,wght@0,300;0,400;0,700;1,300&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] { font-family: 'Lato', sans-serif; }

/* ── FORCE DARK ── */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background-color: #0C0C14 !important;
    color: #DDDDE8 !important;
}

/* ── HIDE CHROME ── */
#MainMenu, [data-testid="stMainMenu"], [data-testid="stToolbar"], [data-testid="stDecoration"], footer, header { 
    visibility: hidden !important; height: 0 !important; 
}

.block-container {
    max-width: 1060px;
    padding: 0 2.5rem 5rem 2.5rem !important;
    margin: auto;
}

/* ════════════════════════════════════════
   SIDEBAR 
════════════════════════════════════════ */
section[data-testid="stSidebar"] {
    background-color: #08080F !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
    min-width: 240px !important;
}

/* Sidebar Logo Area */
.sb-brand {
    padding: 40px 24px 20px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 20px;
}
.sb-name {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    color: #DDDDE8 !important;
    line-height: 1.2;
}
.sb-role {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.58rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #5BA4D4 !important;
    margin-top: 5px;
}

/* ── RADIO NAVIGATION FIX ── */
/* Hide the default radio circle and label */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

/* Style the text as a button */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
    background-color: transparent !important;
    border: none !important;
    padding: 12px 18px !important;
    margin: 2px 10px !important;
    border-radius: 8px !important;
    transition: all 0.25s ease !important;
    cursor: pointer !important;
    width: 90% !important;
}

/* Hover State */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:hover {
    background-color: rgba(91,164,212,0.08) !important;
}

/* Active/Selected State */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] [data-checked="true"] {
    background-color: rgba(91,164,212,0.15) !important;
    border-left: 3px solid #5BA4D4 !important;
    border-radius: 0 8px 8px 0 !important;
}

/* Navigation Text Styling */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #6A6A88 !important; /* Default unselected color */
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] [data-checked="true"] p {
    color: #5BA4D4 !important; /* Selected text color */
    font-weight: 600 !important;
}

.sb-foot {
    position: fixed;
    bottom: 20px;
    left: 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.56rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #3A3A55;
}

/* ════════════════════════════════════════
   PAGE CONTENT ELEMENTS
════════════════════════════════════════ */
.pg-h1 { font-family: 'Syne', sans-serif; font-size: 3rem; font-weight: 800; color: #DDDDE8; margin-bottom: 10px; }
.pg-h1 span { color: #5BA4D4; }
.card {
    background: #13131E;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 30px;
    margin-bottom: 20px;
    transition: 0.3s ease;
}
.card:hover { border-color: rgba(91,164,212,0.3); transform: translateY(-3px); }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-name">Mujeeb<br>Ahmed</div>
        <div class="sb-role">Portfolio 2026</div>
    </div>
    """, unsafe_allow_html=True)

    # UPDATED NAVIGATION OPTIONS
    page = st.radio(
        "Nav",
        options=["Home", "About", "Skills", "Projects", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div class="sb-foot">
        SUKKUR, PAKISTAN<br>
        © 2026
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
#  HOME PAGE
# ─────────────────────────────────────────
if page == "Home":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
        try:
            st.image("profile.jpeg", width=200)
        except:
            st.markdown("<div style='width:200px; height:200px; background:#13131E; border:1px solid #5BA4D4; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#5BA4D4; font-size:3rem; font-weight:800;'>MA</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
        st.markdown(f'<div class="pg-h1">Mujeeb<br><span>Ahmed</span></div>', unsafe_allow_html=True)
        st.write("Computer Science professional & Educator specializing in high-performance application development and technical training.")

# ─────────────────────────────────────────
#  ABOUT PAGE
# ─────────────────────────────────────────
elif page == "About":
    st.markdown('<div class="pg-h1">About <span>Me</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Background</h3>
        <p>I am a Computer Science professional based in Sukkur, Pakistan. With a focus on technical instruction and development, 
        I bridge the gap between complex logic and user-friendly interfaces.</p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
#  SKILLS PAGE
# ─────────────────────────────────────────
elif page == "Skills":
    st.markdown('<div class="pg-h1">Technical <span>Skills</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p><strong>Programming & Tools:</strong> Git, VS Code, Linux, SQL, HTML/CSS.</p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
#  PROJECTS PAGE
# ─────────────────────────────────────────
elif page == "Projects":
    st.markdown('<div class="pg-h1">Selected <span>Projects</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Resume Screening System</h3>
        <p>Developed an automated classification system for professional documents using modern NLP techniques.</p>
    </div>
    <div class="card">
        <h3>Interactive Dashboards</h3>
        <p>Built production-ready data visualization platforms for complex datasets.</p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
#  CONTACT PAGE
# ─────────────────────────────────────────
elif page == "Contact":
    st.markdown('<div class="pg-h1">Get In <span>Touch</span></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <p><strong>Email:</strong> ahmedalixy149@gmail.com</p>
            <p><strong>Phone:</strong> +92 318 030 7822</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        if st.button("Send Message"):
            st.success("Message details captured! (Configure secrets to enable sending)")
