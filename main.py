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
#  SESSION STATE — track active page
# ─────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ─────────────────────────────────────────
#  GLOBAL CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500&family=Lato:wght@300;400;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
}

/* ── FORCE DARK on entire app ── */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stMain"],
.main,
.main > div {
    background-color: #0A0A0F !important;
    color: #E2E2E8 !important;
}

/* ── hide streamlit chrome ── */
#MainMenu,
[data-testid="stMainMenu"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
footer, header { visibility: hidden !important; height: 0 !important; }

.block-container {
    max-width: 1080px;
    padding: 0 2.5rem 5rem 2.5rem !important;
    margin: auto;
}

/* ── CSS TOKENS ── */
:root {
    --bg:         #0A0A0F;
    --bg-raised:  #111118;
    --bg-card:    #16161F;
    --border:     rgba(255,255,255,0.07);
    --border-acc: rgba(99,179,237,0.35);
    --text:       #E2E2E8;
    --text-mid:   #9898A8;
    --text-dim:   #555568;
    --cyan:       #63B3ED;
    --cyan-glow:  rgba(99,179,237,0.18);
    --cyan-dim:   rgba(99,179,237,0.08);
    --green:      #68D391;
    --mono:       'JetBrains Mono', monospace;
    --display:    'Syne', sans-serif;
    --body:       'Lato', sans-serif;
    --shadow:     0 4px 32px rgba(0,0,0,0.5);
    --shadow-lg:  0 12px 60px rgba(0,0,0,0.7);
    --glow:       0 0 40px rgba(99,179,237,0.12);
}

/* ─────────────────────────────────────────
   SIDEBAR
───────────────────────────────────────── */
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"] {
    background-color: #0D0D14 !important;
    border-right: 1px solid rgba(255,255,255,0.07) !important;
    padding: 0 !important;
    min-width: 230px !important;
    max-width: 230px !important;
}

section[data-testid="stSidebar"] * {
    color: #E2E2E8 !important;
}

.sb-logo {
    padding: 36px 28px 28px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    margin-bottom: 24px;
}
.sb-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #E2E2E8 !important;
    letter-spacing: -0.3px;
    line-height: 1.2;
    margin-bottom: 4px;
}
.sb-version {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #63B3ED !important;
}

/* NAV BUTTONS */
section[data-testid="stSidebar"] .stButton > button {
    width: 100% !important;
    text-align: left !important;
    justify-content: flex-start !important;
    background: transparent !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 16px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.70rem !important;
    font-weight: 400 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #9898A8 !important;
    transition: all 0.2s ease !important;
    margin-bottom: 2px !important;
    box-shadow: none !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(99,179,237,0.08) !important;
    color: #E2E2E8 !important;
    border: none !important;
}

/* active nav item */
section[data-testid="stSidebar"] .active-btn .stButton > button {
    background: rgba(99,179,237,0.12) !important;
    color: #63B3ED !important;
    border-left: 2px solid #63B3ED !important;
    border-radius: 0 6px 6px 0 !important;
    padding-left: 14px !important;
}

.sb-footer {
    padding: 20px 28px;
    border-top: 1px solid rgba(255,255,255,0.07);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 1.5px;
    color: #555568 !important;
    text-transform: uppercase;
    line-height: 1.8;
}

/* ─────────────────────────────────────────
   PAGE HEADERS
───────────────────────────────────────── */
.pg-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #63B3ED;
    margin-top: 48px;
    margin-bottom: 10px;
}
.pg-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 5vw, 3.8rem);
    font-weight: 800;
    color: #E2E2E8;
    line-height: 1.05;
    letter-spacing: -1px;
    margin-bottom: 4px;
}
.pg-title span { color: #63B3ED; }
.pg-rule {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin: 22px 0 40px;
}

/* ─────────────────────────────────────────
   CARDS
───────────────────────────────────────── */
.card {
    background: #16161F;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 30px 32px;
    margin-bottom: 18px;
    box-shadow: 0 4px 32px rgba(0,0,0,0.5);
    transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
}
.card:hover {
    border-color: rgba(99,179,237,0.35);
    box-shadow: 0 12px 60px rgba(0,0,0,0.7), 0 0 40px rgba(99,179,237,0.12);
    transform: translateY(-3px);
}
.card-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #63B3ED;
    margin-bottom: 10px;
}
.card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #E2E2E8;
    margin-bottom: 12px;
}
.card p, .card li {
    font-family: 'Lato', sans-serif;
    color: #9898A8;
    font-size: 0.95rem;
    line-height: 1.75;
    font-weight: 300;
}
.card ul {
    list-style: none;
    padding: 0;
}
.card ul li {
    padding: 8px 0 8px 20px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    position: relative;
    color: #9898A8;
    font-size: 0.93rem;
    font-family: 'Lato', sans-serif;
    font-weight: 300;
}
.card ul li::before {
    content: '>';
    position: absolute;
    left: 0;
    color: #63B3ED;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
}
.card ul li:last-child { border-bottom: none; }

/* ─────────────────────────────────────────
   HERO
───────────────────────────────────────── */
.hero-avatar {
    width: 190px;
    height: 190px;
    border-radius: 16px;
    border: 1px solid rgba(99,179,237,0.35);
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    box-shadow: 0 0 40px rgba(99,179,237,0.12);
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}
.hero-initials {
    font-family: 'Syne', sans-serif;
    font-size: 4rem;
    font-weight: 800;
    color: #63B3ED;
    letter-spacing: -2px;
}
.hero-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    color: #63B3ED;
    margin-bottom: 14px;
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6vw, 5rem);
    font-weight: 800;
    color: #E2E2E8;
    letter-spacing: -2px;
    line-height: 0.95;
    margin-bottom: 20px;
}
.hero-name span { color: #63B3ED; }
.hero-bio {
    font-family: 'Lato', sans-serif;
    font-size: 1rem;
    color: #9898A8;
    line-height: 1.78;
    font-weight: 300;
    max-width: 500px;
    margin-bottom: 28px;
}
.badge-row { display: flex; flex-wrap: wrap; gap: 8px; }
.badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #63B3ED;
    border: 1px solid rgba(99,179,237,0.35);
    background: rgba(99,179,237,0.08);
    padding: 5px 14px;
    border-radius: 4px;
}
.badge.plain {
    color: #9898A8;
    border-color: rgba(255,255,255,0.07);
    background: transparent;
}

/* ─────────────────────────────────────────
   STATS
───────────────────────────────────────── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 48px;
}
.stat-cell {
    background: #16161F;
    padding: 28px 20px;
    text-align: center;
    transition: background 0.2s ease;
}
.stat-cell:hover { background: #111118; }
.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    color: #63B3ED;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #555568;
}

/* ─────────────────────────────────────────
   SERVICE CARDS
───────────────────────────────────────── */
.svc-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 48px;
}
.svc-card {
    background: #16161F;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 30px 26px;
    transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
}
.svc-card:hover {
    border-color: rgba(99,179,237,0.35);
    transform: translateY(-4px);
    box-shadow: 0 12px 60px rgba(0,0,0,0.7), 0 0 40px rgba(99,179,237,0.12);
}
.svc-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 2px;
    color: #63B3ED;
    margin-bottom: 16px;
}
.svc-line {
    width: 28px; height: 2px;
    background: #63B3ED;
    margin-bottom: 16px;
    border-radius: 2px;
}
.svc-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #E2E2E8;
    margin-bottom: 10px;
}
.svc-desc {
    font-family: 'Lato', sans-serif;
    font-size: 0.90rem;
    color: #9898A8;
    line-height: 1.72;
    font-weight: 300;
}

/* ─────────────────────────────────────────
   SKILL BARS
───────────────────────────────────────── */
.skill-wrap { margin-bottom: 20px; }
.skill-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 8px;
}
.skill-name {
    font-family: 'Lato', sans-serif;
    font-size: 0.90rem;
    font-weight: 400;
    color: #E2E2E8;
}
.skill-pct {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #63B3ED;
    letter-spacing: 1px;
}
.skill-track {
    height: 4px;
    background: rgba(255,255,255,0.06);
    border-radius: 99px;
    overflow: hidden;
}
.skill-fill {
    height: 4px;
    border-radius: 99px;
    background: linear-gradient(90deg, #63B3ED, #90CDF4);
}

/* ─────────────────────────────────────────
   TOOL TAGS
───────────────────────────────────────── */
.tool-grid { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }
.tool-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 1px;
    color: #9898A8;
    border: 1px solid rgba(255,255,255,0.07);
    padding: 5px 13px;
    border-radius: 4px;
    background: #111118;
    transition: color 0.2s, border-color 0.2s;
}

/* ─────────────────────────────────────────
   PROJECTS
───────────────────────────────────────── */
.proj-card {
    background: #16161F;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 32px 32px 26px;
    margin-bottom: 16px;
    display: grid;
    grid-template-columns: 72px 1fr;
    gap: 24px;
    align-items: start;
    transition: border-color 0.3s, box-shadow 0.3s, transform 0.3s;
}
.proj-card:hover {
    border-color: rgba(99,179,237,0.35);
    box-shadow: 0 12px 60px rgba(0,0,0,0.7), 0 0 40px rgba(99,179,237,0.12);
    transform: translateY(-3px);
}
.proj-index {
    font-family: 'Syne', sans-serif;
    font-size: 3.6rem;
    font-weight: 800;
    color: #E2E2E8;
    opacity: 0.06;
    line-height: 1;
    padding-top: 2px;
    user-select: none;
}
.proj-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #E2E2E8;
    margin-bottom: 10px;
}
.proj-desc {
    font-family: 'Lato', sans-serif;
    font-size: 0.92rem;
    color: #9898A8;
    line-height: 1.72;
    font-weight: 300;
    margin-bottom: 16px;
}
.proj-tags { display: flex; flex-wrap: wrap; gap: 7px; }

/* ─────────────────────────────────────────
   CONTACT
───────────────────────────────────────── */
.info-row {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 16px 0;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}
.info-row:last-child { border-bottom: none; }
.info-key {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #555568;
    width: 70px;
    flex-shrink: 0;
}
.info-val {
    font-family: 'Lato', sans-serif;
    font-size: 0.93rem;
    color: #E2E2E8;
    font-weight: 300;
}

/* ─────────────────────────────────────────
   INPUTS
───────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #111118 !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 6px !important;
    font-family: 'Lato', sans-serif !important;
    font-size: 0.93rem !important;
    color: #E2E2E8 !important;
    font-weight: 300 !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s ease !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #63B3ED !important;
    box-shadow: 0 0 0 3px rgba(99,179,237,0.12) !important;
}
.stTextInput label, .stTextArea label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.62rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #9898A8 !important;
}

/* SEND BUTTON — main content only */
[data-testid="stMain"] .stButton > button {
    background: #63B3ED !important;
    color: #0A0A0F !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    font-weight: 500 !important;
    border: 1px solid #63B3ED !important;
    border-radius: 6px !important;
    padding: 12px 32px !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    box-shadow: none !important;
}
[data-testid="stMain"] .stButton > button:hover {
    background: transparent !important;
    color: #63B3ED !important;
}

/* ─────────────────────────────────────────
   PULL QUOTES
───────────────────────────────────────── */
.pull-quote {
    border-left: 3px solid #63B3ED;
    background: rgba(99,179,237,0.08);
    padding: 20px 28px;
    border-radius: 0 8px 8px 0;
    margin: 0 0 18px;
}
.pull-quote p {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-style: italic;
    font-weight: 500;
    color: #E2E2E8;
    line-height: 1.5;
}
.teach-quote {
    border-left: 3px solid #68D391;
    background: rgba(104,211,145,0.06);
    padding: 20px 28px;
    border-radius: 0 8px 8px 0;
    margin: 0 0 18px;
}
.teach-quote p {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-style: italic;
    font-weight: 500;
    color: #E2E2E8;
    line-height: 1.55;
}

/* ─────────────────────────────────────────
   FACT ROWS (About page)
───────────────────────────────────────── */
.fact-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 0;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}
.fact-row:last-child { border-bottom: none; }
.fact-key {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #63B3ED;
    width: 72px;
    flex-shrink: 0;
}
.fact-val {
    font-family: 'Lato', sans-serif;
    font-size: 0.93rem;
    color: #9898A8;
    font-weight: 300;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SIDEBAR — session_state button nav
# ─────────────────────────────────────────
NAV_ITEMS = ["Home", "About", "Skills", "Projects", "Teaching", "Contact"]
NAV_CODES = ["01", "02", "03", "04", "05", "06"]

with st.sidebar:
    st.markdown("""
    <div class="sb-logo">
        <div class="sb-name">Mujeeb<br>Ahmed</div>
        <div class="sb-version">Portfolio &nbsp;/&nbsp; 2025</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='padding: 0 8px;'>", unsafe_allow_html=True)
    for code, label in zip(NAV_CODES, NAV_ITEMS):
        is_active = st.session_state.page == label
        if is_active:
            st.markdown("<div class='active-btn'>", unsafe_allow_html=True)
        if st.button(f"{code}  {label}", key=f"nav_{label}"):
            st.session_state.page = label
            st.rerun()
        if is_active:
            st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="sb-footer">
        Sukkur, Pakistan<br>
        Python &nbsp;/&nbsp; Data &nbsp;/&nbsp; Web
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  ACTIVE PAGE
# ─────────────────────────────────────────
page = st.session_state.page


# ═════════════════════════════════════════
#  HOME
# ═════════════════════════════════════════
if page == "Home":

    col_img, col_text = st.columns([1, 2.4], gap="large")

    with col_img:
        st.markdown("<div style='height:56px'></div>", unsafe_allow_html=True)
        try:
            st.image("profile.jpeg", width=190)
        except Exception:
            st.markdown("""
            <div class="hero-avatar">
                <span class="hero-initials">MA</span>
            </div>
            """, unsafe_allow_html=True)

    with col_text:
        st.markdown("""
        <div style="padding-top:52px">
            <div class="hero-tag">Python Developer &nbsp;&bull;&nbsp; Data Scientist &nbsp;&bull;&nbsp; Educator</div>
            <div class="hero-name">Mujeeb<br><span>Ahmed</span></div>
            <p class="hero-bio">
                I build real-world Python applications and train the next generation
                of developers through hands-on, project-based teaching.
                Based in Sukkur, Pakistan.
            </p>
            <div class="badge-row">
                <span class="badge">Python</span>
                <span class="badge">Flask</span>
                <span class="badge">Streamlit</span>
                <span class="badge plain">Data Science</span>
                <span class="badge plain">Teaching</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stat-row">
        <div class="stat-cell">
            <div class="stat-num">3+</div>
            <div class="stat-label">Years Coding</div>
        </div>
        <div class="stat-cell">
            <div class="stat-num">10+</div>
            <div class="stat-label">Projects Built</div>
        </div>
        <div class="stat-cell">
            <div class="stat-num">50+</div>
            <div class="stat-label">Students Trained</div>
        </div>
        <div class="stat-cell">
            <div class="stat-num">4</div>
            <div class="stat-label">Core Stacks</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="svc-grid">
        <div class="svc-card">
            <div class="svc-num">01 &mdash; Development</div>
            <div class="svc-line"></div>
            <div class="svc-title">Full-Stack Python</div>
            <div class="svc-desc">Production-grade web apps with Flask and Streamlit. Clean architecture, maintainable code, real deployment.</div>
        </div>
        <div class="svc-card">
            <div class="svc-num">02 &mdash; Data Science</div>
            <div class="svc-line"></div>
            <div class="svc-title">Analytics &amp; Insights</div>
            <div class="svc-desc">From raw CSV to decision-ready dashboards. Pandas, NumPy, Plotly — turning data into clarity.</div>
        </div>
        <div class="svc-card">
            <div class="svc-num">03 &mdash; Teaching</div>
            <div class="svc-line"></div>
            <div class="svc-title">Project-Based Learning</div>
            <div class="svc-desc">No theory overload. Students build real things from session one. Skills that stick because they were earned.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════
#  ABOUT
# ═════════════════════════════════════════
elif page == "About":
    st.markdown('<div class="pg-eyebrow">Who I am</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title">About <span>Me</span></div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Background</div>
            <h3>Developer. Educator. Builder.</h3>
            <p>
                I am <strong style="color:#E2E2E8">Mujeeb Ahmed</strong>, a Python Developer
                and Programming Instructor from Sukkur, Pakistan. I hold a degree in
                <strong style="color:#E2E2E8">Data Science from Sukkur IBA University</strong>
                and have spent the past three years bridging the gap between academic theory
                and real-world software — both in the products I ship and the students I train.
            </p>
            <br>
            <p>
                My approach is simple: write code that solves real problems, and teach
                concepts through things that actually work.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-label">What I do</div>
            <h3>Day to Day</h3>
            <ul>
                <li>Build web applications with Flask and Streamlit</li>
                <li>Analyse datasets and create visual, actionable dashboards</li>
                <li>Design and deliver Python and C++ courses</li>
                <li>Mentor students through real project builds from day one</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-label">Quick Facts</div>
            <h3>At a Glance</h3>
            <div class="fact-row">
                <span class="fact-key">Degree</span>
                <span class="fact-val">B.Sc Data Science</span>
            </div>
            <div class="fact-row">
                <span class="fact-key">Uni</span>
                <span class="fact-val">Sukkur IBA University</span>
            </div>
            <div class="fact-row">
                <span class="fact-key">Role</span>
                <span class="fact-val">Developer &amp; Instructor</span>
            </div>
            <div class="fact-row">
                <span class="fact-key">Based</span>
                <span class="fact-val">Sukkur, Pakistan</span>
            </div>
            <div class="fact-row">
                <span class="fact-key">Focus</span>
                <span class="fact-val">Python, Data, Web</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pull-quote">
            <p>The best way to learn is by building things that actually work.</p>
        </div>
        """, unsafe_allow_html=True)


# ═════════════════════════════════════════
#  SKILLS
# ═════════════════════════════════════════
elif page == "Skills":
    st.markdown('<div class="pg-eyebrow">What I know</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title">Skills <span>&amp;</span> Tools</div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    def skill_bar(name, pct):
        return f"""
        <div class="skill-wrap">
            <div class="skill-head">
                <span class="skill-name">{name}</span>
                <span class="skill-pct">{pct}%</span>
            </div>
            <div class="skill-track">
                <div class="skill-fill" style="width:{pct}%"></div>
            </div>
        </div>"""

    col1, col2 = st.columns(2, gap="large")

    with col1:
        bars = [("Python", 90), ("C++", 75), ("JavaScript", 70)]
        bars_html = "".join(skill_bar(n, p) for n, p in bars)
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Languages</div>
            <h3>Programming</h3>
            <div style="margin-top:16px">{bars_html}</div>
        </div>""", unsafe_allow_html=True)

    with col2:
        bars2 = [("Streamlit", 90), ("Flask", 85), ("HTML &amp; CSS", 82)]
        bars2_html = "".join(skill_bar(n, p) for n, p in bars2)
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Frameworks</div>
            <h3>Web &amp; Frontend</h3>
            <div style="margin-top:16px">{bars2_html}</div>
        </div>""", unsafe_allow_html=True)

    tools = ["VS Code", "Git", "Jupyter", "Pandas", "NumPy", "Matplotlib", "Plotly", "MySQL", "Linux", "SQLite"]
    tags_html = "".join(f'<span class="tool-tag">{t}</span>' for t in tools)
    st.markdown(f"""
    <div class="card">
        <div class="card-label">Ecosystem</div>
        <h3>Tools &amp; Libraries</h3>
        <div class="tool-grid">{tags_html}</div>
    </div>""", unsafe_allow_html=True)


# ═════════════════════════════════════════
#  PROJECTS
# ═════════════════════════════════════════
elif page == "Projects":
    st.markdown('<div class="pg-eyebrow">What I built</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title">Selected <span>Projects</span></div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    projects = [
        {
            "title": "Quiz System",
            "desc": "Full-featured quiz platform with an admin panel, result tracking, and a student leaderboard. Built with Flask and SQLite — production-ready and deployed.",
            "tags": ["Flask", "SQLite", "HTML / CSS"],
        },
        {
            "title": "AI Chatbot",
            "desc": "Conversational chatbot with voice input, speech-to-text integration, and context-aware responses powered by the OpenAI API.",
            "tags": ["Python", "OpenAI API", "SpeechRecognition"],
        },
        {
            "title": "Portfolio Website",
            "desc": "This portfolio — a modern, fully responsive Streamlit application with a dark theme and a working contact form.",
            "tags": ["Streamlit", "CSS", "Python"],
        },
        {
            "title": "Data Dashboard",
            "desc": "Interactive analytics dashboard for visualising CSV datasets with dynamic Plotly charts, filters, and CSV export support.",
            "tags": ["Pandas", "Plotly", "Streamlit"],
        },
    ]

    for i, p in enumerate(projects):
        tags_html = "".join(f'<span class="tool-tag">{t}</span>' for t in p["tags"])
        st.markdown(f"""
        <div class="proj-card">
            <div class="proj-index">0{i+1}</div>
            <div>
                <div class="proj-title">{p['title']}</div>
                <p class="proj-desc">{p['desc']}</p>
                <div class="proj-tags">{tags_html}</div>
            </div>
        </div>""", unsafe_allow_html=True)


# ═════════════════════════════════════════
#  TEACHING
# ═════════════════════════════════════════
elif page == "Teaching":
    st.markdown('<div class="pg-eyebrow">Education &amp; Mentorship</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title">Teaching <span>&amp;</span> Learning</div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Curriculum</div>
            <h3>Subjects I Teach</h3>
            <ul>
                <li>Python — beginner through advanced</li>
                <li>C++ and object-oriented programming</li>
                <li>Web development with HTML, CSS, and Flask</li>
                <li>Data Science fundamentals</li>
                <li>Streamlit application development</li>
            </ul>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-label">Pedagogy</div>
            <h3>How I Teach</h3>
            <ul>
                <li>100% hands-on, project-based learning</li>
                <li>Real assignments from the very first session</li>
                <li>One-on-one code review and feedback</li>
                <li>Problem-solving over memorisation</li>
                <li>Industry-relevant tech stack throughout</li>
            </ul>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="teach-quote">
        <p>
            Theory without practice is trivia. Every concept I teach is immediately
            applied — a mini project, a challenge, a piece of something the student
            is genuinely building. That is how skills stick.
        </p>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-label">Philosophy</div>
        <h3>My Belief as an Educator</h3>
        <p>
            I do not teach programming to produce coders who pass exams.
            I teach it to produce people who can look at a problem, break it down,
            and build something that solves it. The language is secondary —
            the thinking is everything.
        </p>
    </div>""", unsafe_allow_html=True)


# ═════════════════════════════════════════
#  CONTACT
# ═════════════════════════════════════════
elif page == "Contact":
    st.markdown('<div class="pg-eyebrow">Get in touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title">Contact <span>Me</span></div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.4], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Direct Contact</div>
            <h3>Reach Me</h3>
            <div class="info-row">
                <span class="info-key">Email</span>
                <span class="info-val">ahmedalixy149@gmail.com</span>
            </div>
            <div class="info-row">
                <span class="info-key">Phone</span>
                <span class="info-val">+92 318 030 7822</span>
            </div>
            <div class="info-row">
                <span class="info-key">Location</span>
                <span class="info-val">Sukkur, Sindh, Pakistan</span>
            </div>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-label">Message</div>
            <h3>Send a Message</h3>
        </div>""", unsafe_allow_html=True)

        name  = st.text_input("Your Name",  placeholder="Ali Khan")
        email = st.text_input("Your Email", placeholder="ali@example.com")
        msg   = st.text_area("Message",     placeholder="Hello Mujeeb, I would like to ...", height=130)

        if st.button("Send Message"):
            if not name.strip():
                st.error("Please enter your name.")
            elif not email.strip() or "@" not in email:
                st.error("Please enter a valid email address.")
            elif not msg.strip():
                st.error("Please write a message.")
            else:
                try:
                    EMAIL_USER = st.secrets["EMAIL_USER"]
                    EMAIL_PASS = st.secrets["EMAIL_PASSWORD"]
                except Exception:
                    EMAIL_USER = os.environ.get("EMAIL_USER", "")
                    EMAIL_PASS = os.environ.get("EMAIL_PASSWORD", "")

                if not EMAIL_USER or not EMAIL_PASS:
                    st.warning(
                        "Email credentials are not configured. "
                        "Set EMAIL_USER and EMAIL_PASSWORD in Streamlit secrets "
                        "or as environment variables."
                    )
                else:
                    try:
                        em = EmailMessage()
                        em["Subject"]  = f"Portfolio message from {name}"
                        em["From"]     = EMAIL_USER
                        em["To"]       = EMAIL_USER
                        em["Reply-To"] = email
                        em.set_content(
                            f"Name:    {name}\n"
                            f"Email:   {email}\n\n"
                            f"Message:\n{msg}"
                        )
                        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                            smtp.login(EMAIL_USER, EMAIL_PASS)
                            smtp.send_message(em)
                        st.success("Message sent. I will get back to you shortly.")
                    except smtplib.SMTPAuthenticationError:
                        st.error(
                            "Authentication failed. Use a Gmail App Password, "
                            "not your regular Gmail password. "
                            "Generate one at myaccount.google.com > Security > App Passwords."
                        )
                    except Exception as e:
                        st.error(f"Could not send message: {e}")
