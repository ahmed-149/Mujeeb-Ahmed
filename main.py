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
#  GLOBAL CSS (Improved & Robust)
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&family=Lato:ital,wght@0,300;0,400;0,700;1,300&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"] { font-family: 'Lato', sans-serif; }

.stApp {
    background-color: #0C0C14 !important;
    color: #DDDDE8 !important;
}

/* Hide Streamlit Header/Footer */
header, footer, [data-testid="stToolbar"] { visibility: hidden !important; height: 0 !important; }

.block-container {
    max-width: 1060px;
    padding: 0 2.5rem 5rem 2.5rem !important;
    margin: auto;
}

/* ════════════════════════════════════════
   SIDEBAR & NAV
════════════════════════════════════════ */
section[data-testid="stSidebar"] {
    background-color: #08080F !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}

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
}
.sb-role {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.58rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #5BA4D4 !important;
    margin-top: 5px;
}

/* Radio Button Styling */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
    background-color: transparent !important;
    padding: 10px 16px !important;
    margin: 4px 12px !important;
    border-radius: 8px !important;
    transition: 0.2s;
    width: 90% !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:hover {
    background-color: rgba(91,164,212,0.08) !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] [data-checked="true"] {
    background-color: rgba(91,164,212,0.15) !important;
    border-left: 3px solid #5BA4D4 !important;
}

/* Hide Radio Circles */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #6A6A88 !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] [data-checked="true"] p {
    color: #5BA4D4 !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label > div:first-child {
    display: none !important;
}

/* ════════════════════════════════════════
   CONTENT CARDS & HEADINGS
════════════════════════════════════════ */
.pg-h1 { font-family: 'Syne', sans-serif; font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 800; color: #DDDDE8; margin: 40px 0 10px; }
.pg-h1 span { color: #5BA4D4; }

.card {
    background: #13131E;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 28px;
    margin-bottom: 18px;
}
.card h3 { font-family: 'Syne', sans-serif; font-size: 1.3rem; color: #DDDDE8; margin-bottom: 10px; }
.card p { color: #8888A4; line-height: 1.7; font-weight: 300; }

.tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    padding: 4px 10px;
    background: rgba(91,164,212,0.1);
    color: #5BA4D4;
    border: 1px solid rgba(91,164,212,0.3);
    border-radius: 4px;
    margin-right: 5px;
}
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

    page = st.radio(
        "Nav",
        options=["Home", "About", "Skills", "Projects", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown('<div style="margin-top:50px; padding:24px; font-family:monospace; font-size:10px; color:#3A3A55;">SUKKUR, PK<br>PYTHON • DATA • WEB</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────
#  PAGES
# ─────────────────────────────────────────

if page == "Home":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
        st.image("profile.jpeg", width=200) if os.path.exists("profile.jpeg") else st.markdown("<div style='width:200px; height:200px; background:#13131E; border:1px solid #5BA4D4; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#5BA4D4; font-size:3rem; font-weight:800;'>MA</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="pg-h1">Mujeeb<br><span>Ahmed</span></div>', unsafe_allow_html=True)
        st.markdown("""
            <p style='color:#8888A4; font-size:1.1rem; max-width:500px;'>
            I build real-world Python applications and train the next generation of developers 
            through hands-on, project-based teaching. Based in Sukkur, Pakistan.
            </p>
        """, unsafe_allow_html=True)

elif page == "About":
    st.markdown('<div class="pg-h1">About <span>Me</span></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div class="card">
            <h3>Developer. Educator. Builder.</h3>
            <p>I am <strong>Mujeebullah S/O Nizamuddin</strong>, a Computer Science professional from Sukkur. 
            I have spent the past years bridging the gap between academic theory and real-world software.</p>
            <br>
            <p>My approach is simple: write code that solves real problems, and teach concepts through things that actually work.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <h3>Quick Facts</h3>
            <p><strong>Location:</strong> Sukkur, PK</p>
            <p><strong>Role:</strong> Instructor</p>
            <p><strong>Focus:</strong> Data Science</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Skills":
    st.markdown('<div class="pg-h1">Skills & <span>Tools</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Programming</h3>
        <span class="tag">Python</span><span class="tag">C++</span><span class="tag">JavaScript</span><span class="tag">SQL</span>
    </div>
    <div class="card">
        <h3>Frameworks & Libraries</h3>
        <span class="tag">Streamlit</span><span class="tag">Flask</span><span class="tag">Pandas</span><span class="tag">Scikit-Learn</span>
    </div>
    """, unsafe_allow_html=True)

elif page == "Projects":
    st.markdown('<div class="pg-h1">Selected <span>Projects</span></div>', unsafe_allow_html=True)
    projects = [
        ("Resume Screening System", "Utilized Python and Scikit-learn to automate classification of professional documents."),
        ("AI Chatbot", "Conversational tool with speech-to-text integration and OpenAI API."),
        ("Data Dashboards", "Interactive analytics dashboards built with Streamlit and Plotly.")
    ]
    for title, desc in projects:
        st.markdown(f"""<div class="card"><h3>{title}</h3><p>{desc}</p></div>""", unsafe_allow_html=True)

elif page == "Contact":
    st.markdown('<div class="pg-h1">Contact <span>Me</span></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Reach Me</h3>
            <p><strong>Email:</strong> ahmedalixy149@gmail.com</p>
            <p><strong>Phone:</strong> +92 318 030 7822</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        msg = st.text_area("Message")
        if st.button("Send Message"):
            st.success("Message details recorded!")
