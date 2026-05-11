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
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main, .main > div {
    background-color: #0C0C14 !important;
    color: #DDDDE8 !important;
}

/* ── hide chrome ── */
#MainMenu, [data-testid="stMainMenu"],
[data-testid="stToolbar"], [data-testid="stDecoration"],
footer, header { visibility: hidden !important; height: 0 !important; }

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
    min-width: 220px !important;
    max-width: 220px !important;
}
section[data-testid="stSidebar"] > div {
    background-color: #08080F !important;
    padding: 0 !important;
}
[data-testid="stSidebarContent"] {
    background-color: #08080F !important;
    padding: 0 !important;
}

/* sidebar logo */
.sb-brand {
    padding: 38px 26px 26px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 20px;
}
.sb-name {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    color: #DDDDE8 !important;
    line-height: 1.25;
    margin-bottom: 5px;
}
.sb-role {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.57rem !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    color: #5BA4D4 !important;
}

/* ── RADIO NAV ── */
section[data-testid="stSidebar"] .stRadio {
    padding: 0 10px !important;
}
section[data-testid="stSidebar"] .stRadio > label {
    display: none !important;  /* hide "Navigation" label */
}
section[data-testid="stSidebar"] .stRadio > div {
    display: flex !important;
    flex-direction: column !important;
    gap: 2px !important;
    background: transparent !important;
}

/* each radio option row */
section[data-testid="stSidebar"] .stRadio > div > label {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    padding: 10px 16px !important;
    border-radius: 7px !important;
    cursor: pointer !important;
    transition: background 0.18s ease, color 0.18s ease !important;
    background: transparent !important;
    border: none !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.70rem !important;
    font-weight: 400 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #6A6A88 !important;
}
section[data-testid="stSidebar"] .stRadio > div > label:hover {
    background: rgba(91,164,212,0.07) !important;
    color: #DDDDE8 !important;
}
/* selected radio */
section[data-testid="stSidebar"] .stRadio > div > label[data-baseweb="radio"]:has(input:checked),
section[data-testid="stSidebar"] .stRadio > div > label:has(input:checked) {
    background: rgba(91,164,212,0.13) !important;
    color: #5BA4D4 !important;
    border-left: 2px solid #5BA4D4 !important;
    border-radius: 0 7px 7px 0 !important;
    padding-left: 14px !important;
}
/* hide the actual radio circle */
section[data-testid="stSidebar"] .stRadio > div > label > div:first-child {
    display: none !important;
}
/* the text span */
section[data-testid="stSidebar"] .stRadio > div > label > div:last-child p,
section[data-testid="stSidebar"] .stRadio > div > label > div p {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.70rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: inherit !important;
    margin: 0 !important;
}

/* sidebar footer */
.sb-foot {
    padding: 22px 26px;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin-top: 30px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.56rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #3A3A55;
    line-height: 1.9;
}

/* ════════════════════════════════════════
   PAGE HEADINGS
════════════════════════════════════════ */
.pg-eye {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #5BA4D4;
    margin-top: 46px;
    margin-bottom: 10px;
}
.pg-h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.2rem, 4.5vw, 3.6rem);
    font-weight: 800;
    color: #DDDDE8;
    line-height: 1.05;
    letter-spacing: -0.8px;
}
.pg-h1 span { color: #5BA4D4; }
.pg-rule {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin: 20px 0 38px;
}

/* ════════════════════════════════════════
   CARDS
════════════════════════════════════════ */
.card {
    background: #13131E;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 28px 30px;
    margin-bottom: 16px;
    transition: border-color 0.28s, box-shadow 0.28s, transform 0.28s;
}
.card:hover {
    border-color: rgba(91,164,212,0.30);
    box-shadow: 0 8px 48px rgba(0,0,0,0.6), 0 0 32px rgba(91,164,212,0.09);
    transform: translateY(-3px);
}
.card-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #5BA4D4;
    margin-bottom: 9px;
}
.card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.28rem;
    font-weight: 700;
    color: #DDDDE8;
    margin-bottom: 11px;
}
.card p {
    font-family: 'Lato', sans-serif;
    color: #8888A4;
    font-size: 0.94rem;
    line-height: 1.74;
    font-weight: 300;
}
.card ul { list-style: none; padding: 0; }
.card ul li {
    font-family: 'Lato', sans-serif;
    font-size: 0.92rem;
    font-weight: 300;
    color: #8888A4;
    padding: 8px 0 8px 18px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    position: relative;
    line-height: 1.6;
}
.card ul li:last-child { border-bottom: none; }
.card ul li::before {
    content: '›';
    position: absolute;
    left: 0;
    color: #5BA4D4;
    font-size: 1rem;
    line-height: 1.4;
}

/* ════════════════════════════════════════
   HERO
════════════════════════════════════════ */
.hero-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    color: #5BA4D4;
    margin-bottom: 14px;
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 5.5vw, 4.8rem);
    font-weight: 800;
    color: #DDDDE8;
    letter-spacing: -2px;
    line-height: 0.96;
    margin-bottom: 22px;
}
.hero-name span { color: #5BA4D4; }
.hero-bio {
    font-family: 'Lato', sans-serif;
    font-size: 0.98rem;
    color: #8888A4;
    line-height: 1.78;
    font-weight: 300;
    max-width: 480px;
    margin-bottom: 28px;
}
.hero-avatar {
    width: 185px; height: 185px;
    border-radius: 14px;
    border: 1px solid rgba(91,164,212,0.28);
    background: linear-gradient(135deg,#12122A,#1A1A38);
    box-shadow: 0 0 36px rgba(91,164,212,0.10);
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
}
.hero-avatar img { width:100%; height:100%; object-fit:cover; }
.hero-initials {
    font-family: 'Syne', sans-serif;
    font-size: 3.8rem;
    font-weight: 800;
    color: #5BA4D4;
    letter-spacing: -2px;
}

/* badge row */
.badge-row { display:flex; flex-wrap:wrap; gap:8px; }
.badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #5BA4D4;
    border: 1px solid rgba(91,164,212,0.32);
    background: rgba(91,164,212,0.07);
    padding: 5px 14px;
    border-radius: 4px;
}
.badge.muted {
    color: #6A6A88;
    border-color: rgba(255,255,255,0.08);
    background: transparent;
}

/* ════════════════════════════════════════
   SERVICE CARDS
════════════════════════════════════════ */
.svc-card {
    background: #13131E;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 28px 24px;
    height: 100%;
    transition: border-color 0.28s, transform 0.28s, box-shadow 0.28s;
}
.svc-card:hover {
    border-color: rgba(91,164,212,0.30);
    transform: translateY(-4px);
    box-shadow: 0 10px 50px rgba(0,0,0,0.6), 0 0 32px rgba(91,164,212,0.09);
}
.svc-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 2px;
    color: #5BA4D4;
    margin-bottom: 14px;
}
.svc-bar { width:26px; height:2px; background:#5BA4D4; border-radius:2px; margin-bottom:14px; }
.svc-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.18rem;
    font-weight: 700;
    color: #DDDDE8;
    margin-bottom: 10px;
}
.svc-desc {
    font-family: 'Lato', sans-serif;
    font-size: 0.88rem;
    color: #8888A4;
    line-height: 1.70;
    font-weight: 300;
}

/* ════════════════════════════════════════
   SKILL BARS
════════════════════════════════════════ */
.sk-wrap { margin-bottom: 18px; }
.sk-head { display:flex; justify-content:space-between; margin-bottom:7px; }
.sk-name { font-family:'Lato',sans-serif; font-size:0.88rem; font-weight:400; color:#DDDDE8; }
.sk-pct  { font-family:'JetBrains Mono',monospace; font-size:0.63rem; color:#5BA4D4; }
.sk-track { height:3px; background:rgba(255,255,255,0.06); border-radius:99px; overflow:hidden; }
.sk-fill  { height:3px; border-radius:99px; background:linear-gradient(90deg,#5BA4D4,#8EC8F0); }

/* ════════════════════════════════════════
   TOOL TAGS
════════════════════════════════════════ */
.tag-grid { display:flex; flex-wrap:wrap; gap:8px; margin-top:8px; }
.tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    letter-spacing: 1px;
    color: #7070A0;
    border: 1px solid rgba(255,255,255,0.08);
    padding: 5px 12px;
    border-radius: 4px;
    background: #0E0E1A;
}

/* ════════════════════════════════════════
   PROJECT CARDS
════════════════════════════════════════ */
.proj-card {
    background: #13131E;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 30px 30px 24px;
    margin-bottom: 14px;
    display: grid;
    grid-template-columns: 68px 1fr;
    gap: 22px;
    align-items: start;
    transition: border-color 0.28s, box-shadow 0.28s, transform 0.28s;
}
.proj-card:hover {
    border-color: rgba(91,164,212,0.30);
    box-shadow: 0 8px 48px rgba(0,0,0,0.6), 0 0 32px rgba(91,164,212,0.09);
    transform: translateY(-3px);
}
.proj-idx {
    font-family: 'Syne', sans-serif;
    font-size: 3.4rem;
    font-weight: 800;
    color: #DDDDE8;
    opacity: 0.05;
    line-height: 1;
    user-select: none;
}
.proj-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.32rem;
    font-weight: 700;
    color: #DDDDE8;
    margin-bottom: 9px;
}
.proj-desc {
    font-family: 'Lato', sans-serif;
    font-size: 0.90rem;
    color: #8888A4;
    line-height: 1.70;
    font-weight: 300;
    margin-bottom: 14px;
}
.proj-tags { display:flex; flex-wrap:wrap; gap:6px; }

/* ════════════════════════════════════════
   ABOUT — FACT ROWS
════════════════════════════════════════ */
.fact { display:flex; align-items:center; gap:16px; padding:13px 0; border-bottom:1px solid rgba(255,255,255,0.06); }
.fact:last-child { border-bottom: none; }
.fact-k { font-family:'JetBrains Mono',monospace; font-size:0.58rem; letter-spacing:2px; text-transform:uppercase; color:#5BA4D4; width:68px; flex-shrink:0; }
.fact-v { font-family:'Lato',sans-serif; font-size:0.91rem; color:#8888A4; font-weight:300; }

/* ════════════════════════════════════════
   CONTACT
════════════════════════════════════════ */
.ci-row { display:flex; align-items:center; gap:18px; padding:15px 0; border-bottom:1px solid rgba(255,255,255,0.06); }
.ci-row:last-child { border-bottom:none; }
.ci-k { font-family:'JetBrains Mono',monospace; font-size:0.58rem; letter-spacing:2px; text-transform:uppercase; color:#4A4A72; width:66px; flex-shrink:0; }
.ci-v { font-family:'Lato',sans-serif; font-size:0.91rem; color:#DDDDE8; font-weight:300; }

/* ════════════════════════════════════════
   INPUTS
════════════════════════════════════════ */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #0E0E1A !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 6px !important;
    font-family: 'Lato', sans-serif !important;
    font-size: 0.92rem !important;
    color: #DDDDE8 !important;
    font-weight: 300 !important;
    padding: 11px 15px !important;
    caret-color: #5BA4D4 !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #5BA4D4 !important;
    box-shadow: 0 0 0 3px rgba(91,164,212,0.10) !important;
}
.stTextInput label, .stTextArea label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.60rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #7070A0 !important;
}

/* SEND BUTTON — only in main content */
[data-testid="stMain"] .stButton > button {
    background: #5BA4D4 !important;
    color: #08080F !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.66rem !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    font-weight: 500 !important;
    border: 1px solid #5BA4D4 !important;
    border-radius: 6px !important;
    padding: 11px 28px !important;
    width: 100% !important;
    transition: all 0.22s ease !important;
    box-shadow: none !important;
}
[data-testid="stMain"] .stButton > button:hover {
    background: transparent !important;
    color: #5BA4D4 !important;
}

/* ════════════════════════════════════════
   PULL QUOTES
════════════════════════════════════════ */
.pq {
    border-left: 3px solid #5BA4D4;
    background: rgba(91,164,212,0.07);
    padding: 18px 26px;
    border-radius: 0 8px 8px 0;
    margin: 0 0 16px;
}
.pq p {
    font-family: 'Lato', sans-serif;
    font-style: italic;
    font-size: 1.05rem;
    font-weight: 300;
    color: #DDDDE8;
    line-height: 1.60;
}
.pq-green {
    border-left: 3px solid #5DC89A;
    background: rgba(93,200,154,0.06);
    padding: 18px 26px;
    border-radius: 0 8px 8px 0;
    margin: 0 0 16px;
}
.pq-green p {
    font-family: 'Lato', sans-serif;
    font-style: italic;
    font-size: 1.05rem;
    font-weight: 300;
    color: #DDDDE8;
    line-height: 1.60;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SIDEBAR  —  st.radio (most reliable)
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-name">Mujeeb<br>Ahmed</div>
        <div class="sb-role">Portfolio 2025</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        options=["Home", "About", "Skills", "Projects", "Teaching", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div class="sb-foot">
        Sukkur, Pakistan<br>
        Python · Data · Web
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  HOME
# ─────────────────────────────────────────
if page == "Home":

    col_img, col_txt = st.columns([1, 2.5], gap="large")

    with col_img:
        st.markdown("<div style='height:52px'></div>", unsafe_allow_html=True)
        try:
            st.image("profile.jpeg", width=185)
        except Exception:
            st.markdown("""
            <div class="hero-avatar">
                <span class="hero-initials">MA</span>
            </div>""", unsafe_allow_html=True)

    with col_txt:
        st.markdown("""
        <div style="padding-top:48px">
            <div class="hero-tag">Python Developer &nbsp;&bull;&nbsp; Data Scientist &nbsp;&bull;&nbsp; Educator</div>
            <div class="hero-name">Mujeeb<br><span>Ahmed</span></div>
            <p class="hero-bio">
                I build real-world Python applications and train the next
                generation of developers through hands-on, project-based
                teaching. Based in Sukkur, Pakistan.
            </p>
            <div class="badge-row">
                <span class="badge">Python</span>
                <span class="badge">Flask</span>
                <span class="badge">Streamlit</span>
                <span class="badge muted">Data Science</span>
                <span class="badge muted">Teaching</span>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:48px'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    services = [
        ("01", "Development",        "Production-grade web apps with Flask and Streamlit. Clean architecture, maintainable code, real deployment."),
        ("02", "Data Science",       "From raw CSV to decision-ready dashboards. Pandas, NumPy, Plotly — turning data into clarity."),
        ("03", "Teaching",           "No theory overload. Students build real things from session one. Skills that stick because they were earned."),
    ]
    for col, (num, title, desc) in zip([c1, c2, c3], services):
        with col:
            st.markdown(f"""
            <div class="svc-card">
                <div class="svc-num">{num}</div>
                <div class="svc-bar"></div>
                <div class="svc-title">{title}</div>
                <div class="svc-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  ABOUT
# ─────────────────────────────────────────
elif page == "About":
    st.markdown('<div class="pg-eye">Who I am</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-h1">About <span>Me</span></div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-lbl">Background</div>
            <h3>Developer. Educator. Builder.</h3>
            <p>
                I am <strong style="color:#DDDDE8">Mujeeb Ahmed</strong>, a Python Developer
                and Programming Instructor from Sukkur, Pakistan. I hold a degree in
                <strong style="color:#DDDDE8">Data Science from Sukkur IBA University</strong>
                and have spent the past three years bridging the gap between academic
                theory and real-world software — both in the products I ship and the
                students I train.
            </p><br>
            <p>
                My approach is simple: write code that solves real problems, and teach
                concepts through things that actually work.
            </p>
        </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-lbl">What I do</div>
            <h3>Day to Day</h3>
            <ul>
                <li>Build web applications with Flask and Streamlit</li>
                <li>Analyse datasets and create visual, actionable dashboards</li>
                <li>Design and deliver Python and C++ courses</li>
                <li>Mentor students through real project builds from day one</li>
            </ul>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-lbl">Quick Facts</div>
            <h3>At a Glance</h3>
            <div class="fact"><span class="fact-k">Degree</span><span class="fact-v">B.Sc Data Science</span></div>
            <div class="fact"><span class="fact-k">Uni</span><span class="fact-v">Sukkur IBA University</span></div>
            <div class="fact"><span class="fact-k">Role</span><span class="fact-v">Developer &amp; Instructor</span></div>
            <div class="fact"><span class="fact-k">Based</span><span class="fact-v">Sukkur, Pakistan</span></div>
            <div class="fact"><span class="fact-k">Focus</span><span class="fact-v">Python, Data, Web</span></div>
        </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div class="pq">
            <p>The best way to learn is by building things that actually work.</p>
        </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SKILLS
# ─────────────────────────────────────────
elif page == "Skills":
    st.markdown('<div class="pg-eye">What I know</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-h1">Skills <span>&amp;</span> Tools</div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    def skill_bar(name, pct):
        return f"""<div class="sk-wrap">
            <div class="sk-head"><span class="sk-name">{name}</span><span class="sk-pct">{pct}%</span></div>
            <div class="sk-track"><div class="sk-fill" style="width:{pct}%"></div></div>
        </div>"""

    col1, col2 = st.columns(2, gap="large")

    with col1:
        h = "".join(skill_bar(n, p) for n, p in [("Python", 90), ("C++", 75), ("JavaScript", 70)])
        st.markdown(f'<div class="card"><div class="card-lbl">Languages</div><h3>Programming</h3><div style="margin-top:14px">{h}</div></div>', unsafe_allow_html=True)

    with col2:
        h2 = "".join(skill_bar(n, p) for n, p in [("Streamlit", 90), ("Flask", 85), ("HTML &amp; CSS", 82)])
        st.markdown(f'<div class="card"><div class="card-lbl">Frameworks</div><h3>Web &amp; Frontend</h3><div style="margin-top:14px">{h2}</div></div>', unsafe_allow_html=True)

    tools = ["VS Code", "Git", "Jupyter", "Pandas", "NumPy", "Matplotlib", "Plotly", "MySQL", "Linux", "SQLite"]
    tg = "".join(f'<span class="tag">{t}</span>' for t in tools)
    st.markdown(f'<div class="card"><div class="card-lbl">Ecosystem</div><h3>Tools &amp; Libraries</h3><div class="tag-grid">{tg}</div></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────
#  PROJECTS
# ─────────────────────────────────────────
elif page == "Projects":
    st.markdown('<div class="pg-eye">What I built</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-h1">Selected <span>Projects</span></div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    projects = [
        ("Quiz System",
         "Full-featured quiz platform with an admin panel, result tracking, and a student leaderboard. Built with Flask and SQLite.",
         ["Flask", "SQLite", "HTML / CSS"]),
        ("AI Chatbot",
         "Conversational chatbot with voice input, speech-to-text integration, and context-aware responses via the OpenAI API.",
         ["Python", "OpenAI API", "SpeechRecognition"]),
        ("Portfolio Website",
         "This portfolio — a fully responsive Streamlit application with a forced dark theme and a working contact form.",
         ["Streamlit", "CSS", "Python"]),
        ("Data Dashboard",
         "Interactive analytics dashboard for visualising CSV datasets with dynamic Plotly charts, filters, and export support.",
         ["Pandas", "Plotly", "Streamlit"]),
    ]
    for i, (title, desc, tags) in enumerate(projects):
        tg = "".join(f'<span class="tag">{t}</span>' for t in tags)
        st.markdown(f"""
        <div class="proj-card">
            <div class="proj-idx">0{i+1}</div>
            <div>
                <div class="proj-title">{title}</div>
                <p class="proj-desc">{desc}</p>
                <div class="proj-tags">{tg}</div>
            </div>
        </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  TEACHING
# ─────────────────────────────────────────
elif page == "Teaching":
    st.markdown('<div class="pg-eye">Education &amp; Mentorship</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-h1">Teaching <span>&amp;</span> Learning</div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-lbl">Curriculum</div>
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
            <div class="card-lbl">Pedagogy</div>
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
    <div class="pq-green">
        <p>
            Theory without practice is trivia. Every concept I teach is immediately
            applied — a project, a challenge, a piece of something the student is
            genuinely building. That is how skills stick.
        </p>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-lbl">Philosophy</div>
        <h3>My Belief as an Educator</h3>
        <p>
            I do not teach programming to produce coders who pass exams.
            I teach it to produce people who can look at a problem, break it down,
            and build something that solves it. The language is secondary —
            the thinking is everything.
        </p>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  CONTACT
# ─────────────────────────────────────────
elif page == "Contact":
    st.markdown('<div class="pg-eye">Get in touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-h1">Contact <span>Me</span></div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.4], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-lbl">Direct Contact</div>
            <h3>Reach Me</h3>
            <div class="ci-row"><span class="ci-k">Email</span><span class="ci-v">ahmedalixy149@gmail.com</span></div>
            <div class="ci-row"><span class="ci-k">Phone</span><span class="ci-v">+92 318 030 7822</span></div>
            <div class="ci-row"><span class="ci-k">Location</span><span class="ci-v">Sukkur, Sindh, Pakistan</span></div>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-lbl">Message</div>
            <h3>Send a Message</h3>
        </div>""", unsafe_allow_html=True)

        name  = st.text_input("Your Name",  placeholder="Ali Khan")
        email = st.text_input("Your Email", placeholder="ali@example.com")
        msg   = st.text_area("Message",     placeholder="Hello Mujeeb ...", height=130)

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
                    st.warning("Email credentials not configured. Set EMAIL_USER and EMAIL_PASSWORD in Streamlit secrets or environment variables.")
                else:
                    try:
                        em = EmailMessage()
                        em["Subject"]  = f"Portfolio message from {name}"
                        em["From"]     = EMAIL_USER
                        em["To"]       = EMAIL_USER
                        em["Reply-To"] = email
                        em.set_content(f"Name:    {name}\nEmail:   {email}\n\nMessage:\n{msg}")
                        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                            smtp.login(EMAIL_USER, EMAIL_PASS)
                            smtp.send_message(em)
                        st.success("Message sent. I will get back to you shortly.")
                    except smtplib.SMTPAuthenticationError:
                        st.error("Authentication failed. Use a Gmail App Password at myaccount.google.com > Security > App Passwords.")
                    except Exception as e:
                        st.error(f"Could not send message: {e}")
