import streamlit as st
import os
import smtplib
from email.message import EmailMessage

# ─────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(page_title="Mujeeb Ahmed — Developer & Educator", layout="wide")

# ─────────────────────────────────────────
#  GLOBAL CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=DM+Mono:wght@300;400;500&family=Outfit:wght@300;400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    scroll-behavior: smooth;
}

/* ── hide streamlit chrome ── */
#MainMenu,
[data-testid="stMainMenu"],
[data-testid="stToolbar"],
footer, header { visibility: hidden; }

.block-container {
    max-width: 1140px;
    padding: 0 2.5rem 5rem;
    margin: auto;
}

/* ── CSS TOKENS ── */
:root {
    --cream:     #F7F3EE;
    --ink:       #111008;
    --ink-mid:   #3D3A32;
    --ink-light: #7A7670;
    --gold:      #C9A84C;
    --gold-dim:  #E8D9B0;
    --rule:      rgba(17,16,8,0.12);
    --card-bg:   rgba(255,255,255,0.72);
    --card-border: rgba(201,168,76,0.22);
    --shadow:    0 2px 20px rgba(17,16,8,0.06);
    --shadow-lg: 0 8px 48px rgba(17,16,8,0.12);
    --mono:      'DM Mono', monospace;
    --serif:     'Cormorant Garamond', Georgia, serif;
    --sans:      'Outfit', sans-serif;
}

/* ── sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--ink) !important;
    border-right: none !important;
    min-width: 220px !important;
    max-width: 220px !important;
}
section[data-testid="stSidebar"] > div {
    padding: 0 !important;
}
[data-testid="stSidebarContent"] {
    padding: 0 !important;
}

/* sidebar inner wrapper */
.sb-wrap {
    padding: 40px 28px 32px;
    display: flex;
    flex-direction: column;
    height: 100%;
    min-height: 100vh;
}
.sb-logo-name {
    font-family: var(--serif);
    font-size: 1.45rem;
    font-weight: 600;
    color: #F7F3EE;
    letter-spacing: 0.3px;
    line-height: 1.2;
    margin-bottom: 4px;
}
.sb-logo-sub {
    font-family: var(--mono);
    font-size: 0.62rem;
    color: var(--gold);
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 44px;
}
.sb-rule {
    border: none;
    border-top: 1px solid rgba(247,243,238,0.12);
    margin-bottom: 32px;
}

/* hide Streamlit radio styles, replaced by custom */
section[data-testid="stSidebar"] .stRadio > div {
    display: flex !important;
    flex-direction: column !important;
    gap: 2px !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-family: var(--mono) !important;
    font-size: 0.72rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: rgba(247,243,238,0.55) !important;
    padding: 10px 14px !important;
    border-radius: 6px !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    border: none !important;
    background: transparent !important;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    color: #F7F3EE !important;
    background: rgba(247,243,238,0.06) !important;
}
section[data-testid="stSidebar"] .stRadio label[data-checked="true"],
section[data-testid="stSidebar"] .stRadio label[aria-checked="true"] {
    color: var(--gold) !important;
    background: rgba(201,168,76,0.1) !important;
}
/* hide radio circles */
section[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] .stRadio span[data-baseweb="radio"] > div:first-child {
    display: none !important;
}

/* ── main area background ── */
.stApp {
    background: var(--cream) !important;
}

/* ── PAGE HEADER RULE ── */
.pg-eyebrow {
    font-family: var(--mono);
    font-size: 0.65rem;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 8px;
    margin-top: 52px;
}
.pg-title {
    font-family: var(--serif);
    font-size: clamp(2.6rem, 5vw, 4.2rem);
    font-weight: 300;
    color: var(--ink);
    letter-spacing: -0.5px;
    line-height: 1.08;
    margin-bottom: 8px;
}
.pg-title strong {
    font-weight: 700;
    font-style: italic;
}
.pg-rule {
    border: none;
    border-top: 1.5px solid var(--ink);
    margin: 20px 0 40px;
}

/* ── CARD ── */
.card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 4px;
    padding: 32px 36px;
    margin-bottom: 20px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(6px);
    transition: box-shadow 0.3s ease, transform 0.3s ease;
}
.card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-3px);
}
.card-label {
    font-family: var(--mono);
    font-size: 0.62rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 12px;
}
.card h3 {
    font-family: var(--serif);
    font-size: 1.45rem;
    font-weight: 600;
    color: var(--ink);
    margin-bottom: 12px;
    line-height: 1.2;
}
.card p, .card li {
    font-family: var(--sans);
    color: var(--ink-mid);
    font-size: 0.95rem;
    line-height: 1.72;
    font-weight: 300;
}
.card ul {
    padding-left: 0;
    list-style: none;
}
.card ul li {
    padding: 7px 0;
    border-bottom: 1px solid rgba(17,16,8,0.06);
    padding-left: 18px;
    position: relative;
}
.card ul li::before {
    content: '—';
    position: absolute;
    left: 0;
    color: var(--gold);
    font-size: 0.8rem;
}
.card ul li:last-child { border-bottom: none; }

/* ── HERO ── */
.hero-wrap {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 52px;
    align-items: center;
    padding: 52px 0 40px;
    border-bottom: 1px solid var(--rule);
    margin-bottom: 48px;
}
.hero-img-ring {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 1px solid var(--gold-dim);
    overflow: hidden;
    flex-shrink: 0;
    position: relative;
}
.hero-img-ring img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
.hero-img-placeholder {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 1px solid var(--gold-dim);
    background: linear-gradient(135deg, #E8D9B0 0%, #C9A84C 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.hero-initials {
    font-family: var(--serif);
    font-size: 3.5rem;
    font-weight: 600;
    color: var(--ink);
    letter-spacing: -1px;
}
.hero-name {
    font-family: var(--serif);
    font-size: clamp(3rem, 6vw, 5.2rem);
    font-weight: 300;
    color: var(--ink);
    letter-spacing: -1.5px;
    line-height: 1;
    margin-bottom: 10px;
}
.hero-name em {
    font-style: italic;
    font-weight: 600;
    color: var(--ink);
}
.hero-role {
    font-family: var(--mono);
    font-size: 0.72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 20px;
}
.hero-bio {
    font-family: var(--sans);
    font-size: 1.02rem;
    color: var(--ink-mid);
    line-height: 1.78;
    font-weight: 300;
    max-width: 520px;
    margin-bottom: 28px;
}
.hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

/* ── TAG / BADGE ── */
.tag {
    font-family: var(--mono);
    font-size: 0.65rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--ink-mid);
    border: 1px solid var(--rule);
    padding: 5px 14px;
    border-radius: 2px;
    background: transparent;
    transition: all 0.2s ease;
}
.tag.accent {
    color: var(--gold);
    border-color: var(--gold-dim);
    background: rgba(201,168,76,0.06);
}

/* ── STAT ROW ── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: var(--rule);
    border: 1px solid var(--rule);
    border-radius: 4px;
    overflow: hidden;
    margin-top: 40px;
    margin-bottom: 48px;
}
.stat-cell {
    background: var(--card-bg);
    padding: 28px 24px;
    text-align: center;
}
.stat-num {
    font-family: var(--serif);
    font-size: 2.8rem;
    font-weight: 700;
    font-style: italic;
    color: var(--ink);
    line-height: 1;
    margin-bottom: 6px;
}
.stat-label {
    font-family: var(--mono);
    font-size: 0.6rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--ink-light);
}

/* ── SERVICE CARDS (home) ── */
.svc-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 4px;
    padding: 32px 28px;
    box-shadow: var(--shadow);
    transition: box-shadow 0.3s ease, transform 0.3s ease;
    height: 100%;
}
.svc-card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-4px);
}
.svc-num {
    font-family: var(--mono);
    font-size: 0.62rem;
    letter-spacing: 2px;
    color: var(--gold);
    margin-bottom: 20px;
}
.svc-title {
    font-family: var(--serif);
    font-size: 1.55rem;
    font-weight: 600;
    color: var(--ink);
    line-height: 1.15;
    margin-bottom: 14px;
}
.svc-desc {
    font-family: var(--sans);
    font-size: 0.92rem;
    color: var(--ink-mid);
    line-height: 1.7;
    font-weight: 300;
}

/* ── SKILL BAR ── */
.skill-wrap { margin-bottom: 18px; }
.skill-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 7px;
}
.skill-name {
    font-family: var(--sans);
    font-size: 0.88rem;
    font-weight: 500;
    color: var(--ink);
}
.skill-pct {
    font-family: var(--mono);
    font-size: 0.68rem;
    color: var(--ink-light);
    letter-spacing: 1px;
}
.skill-track {
    height: 2px;
    background: rgba(17,16,8,0.10);
    border-radius: 99px;
    overflow: hidden;
}
.skill-fill {
    height: 2px;
    border-radius: 99px;
    background: linear-gradient(90deg, var(--gold), #E8C96E);
    transition: width 0.8s cubic-bezier(.4,0,.2,1);
}

/* ── TOOL PILLS ── */
.tool-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 4px;
}

/* ── PROJECT CARD ── */
.proj-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 4px;
    padding: 36px 36px 28px;
    margin-bottom: 18px;
    box-shadow: var(--shadow);
    display: grid;
    grid-template-columns: 80px 1fr;
    gap: 28px;
    align-items: start;
    transition: box-shadow 0.3s ease, transform 0.3s ease;
}
.proj-card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-3px);
}
.proj-index {
    font-family: var(--serif);
    font-size: 4rem;
    font-weight: 700;
    font-style: italic;
    color: var(--ink);
    opacity: 0.08;
    line-height: 1;
    padding-top: 4px;
    user-select: none;
}
.proj-title {
    font-family: var(--serif);
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--ink);
    margin-bottom: 10px;
}
.proj-desc {
    font-family: var(--sans);
    font-size: 0.93rem;
    color: var(--ink-mid);
    line-height: 1.7;
    font-weight: 300;
    margin-bottom: 16px;
}
.proj-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

/* ── CONTACT ── */
.contact-info-item {
    display: flex;
    align-items: center;
    gap: 18px;
    padding: 18px 0;
    border-bottom: 1px solid var(--rule);
}
.contact-info-item:last-child { border-bottom: none; }
.contact-info-key {
    font-family: var(--mono);
    font-size: 0.62rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--ink-light);
    width: 60px;
    flex-shrink: 0;
}
.contact-info-val {
    font-family: var(--sans);
    font-size: 0.95rem;
    color: var(--ink);
    font-weight: 400;
}

/* ── INPUTS ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(255,255,255,0.8) !important;
    border: 1px solid rgba(17,16,8,0.18) !important;
    border-radius: 3px !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.93rem !important;
    color: var(--ink) !important;
    font-weight: 300 !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s ease !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(201,168,76,0.12) !important;
}
.stTextInput label, .stTextArea label {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.64rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: var(--ink-light) !important;
}

/* ── BUTTON ── */
.stButton > button {
    background: var(--ink) !important;
    color: var(--cream) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.68rem !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    font-weight: 400 !important;
    border: 1px solid var(--ink) !important;
    border-radius: 3px !important;
    padding: 12px 32px !important;
    transition: all 0.25s ease !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: transparent !important;
    color: var(--ink) !important;
}

/* ── DIVIDER ── */
.thin-rule {
    border: none;
    border-top: 1px solid var(--rule);
    margin: 36px 0;
}

/* ── QUOTE PULL ── */
.pull-quote {
    border-left: 3px solid var(--gold);
    padding: 16px 0 16px 28px;
    margin: 28px 0;
}
.pull-quote p {
    font-family: var(--serif);
    font-size: 1.3rem;
    font-style: italic;
    font-weight: 400;
    color: var(--ink);
    line-height: 1.55;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SIDEBAR NAV
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-wrap">
        <div class="sb-logo-name">Mujeeb<br>Ahmed</div>
        <div class="sb-logo-sub">Portfolio 2025</div>
        <hr class="sb-rule">
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["Home", "About", "Skills", "Projects", "Teaching", "Contact"],
        label_visibility="collapsed"
    )


# ─────────────────────────────────────────
#  HOME
# ─────────────────────────────────────────
if page == "Home":

    # Hero
    col_img, col_text = st.columns([1, 2.2], gap="large")

    with col_img:
        st.markdown("<div style='height:52px'></div>", unsafe_allow_html=True)
        try:
            st.image("profile.jpeg", width=200)
        except Exception:
            st.markdown("""
            <div class="hero-img-placeholder">
                <span class="hero-initials">MA</span>
            </div>
            """, unsafe_allow_html=True)

    with col_text:
        st.markdown("""
        <div style="padding-top:48px">
            <div class="hero-role">Python Developer &nbsp;&middot;&nbsp; Data Scientist &nbsp;&middot;&nbsp; Educator</div>
            <div class="hero-name">Mujeeb<br><em>Ahmed</em></div>
            <p class="hero-bio">
                I build real-world Python applications and train the next generation
                of developers through hands-on, project-based teaching.
                Based in Sukkur, Pakistan.
            </p>
            <div class="hero-tags">
                <span class="tag accent">Python</span>
                <span class="tag accent">Flask</span>
                <span class="tag accent">Streamlit</span>
                <span class="tag">Data Science</span>
                <span class="tag">Teaching</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Stats
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
            <div class="stat-label">Core Tech Stacks</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Services
    c1, c2, c3 = st.columns(3, gap="medium")
    services = [
        ("01", "Development", "Full-stack Python applications built with Flask and Streamlit — clean architecture, maintainable code."),
        ("02", "Data Science", "From raw CSV to decision-ready insight. Analytical problem-solving with Pandas, NumPy, and Plotly."),
        ("03", "Teaching", "Project-based learning that skips the theory noise and builds real skills from the first session."),
    ]
    for col, (num, title, desc) in zip([c1, c2, c3], services):
        with col:
            st.markdown(f"""
            <div class="svc-card">
                <div class="svc-num">{num}</div>
                <div class="svc-title">{title}</div>
                <div class="svc-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  ABOUT
# ─────────────────────────────────────────
elif page == "About":
    st.markdown('<div class="pg-eyebrow">Who I am</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title"><strong>About</strong> Me</div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Background</div>
            <h3>Developer, Educator, Builder</h3>
            <p>
                I am <strong>Mujeeb Ahmed</strong>, a Python Developer and Programming
                Instructor from Sukkur, Pakistan. I hold a degree in
                <strong>Data Science from Sukkur IBA University</strong> and have spent
                the past three years bridging the gap between academic theory and
                real-world software — both in the products I ship and the students I train.
            </p>
            <br>
            <p>
                My approach is direct: write code that solves real problems, teach
                concepts through things that actually work. No padding, no fluff.
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
                <li>Mentor students through real project builds</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-label">Quick Facts</div>
            <h3>At a Glance</h3>
            <div class="contact-info-item">
                <span class="contact-info-key">Degree</span>
                <span class="contact-info-val">B.Sc Data Science</span>
            </div>
            <div class="contact-info-item">
                <span class="contact-info-key">Uni</span>
                <span class="contact-info-val">Sukkur IBA University</span>
            </div>
            <div class="contact-info-item">
                <span class="contact-info-key">Role</span>
                <span class="contact-info-val">Developer &amp; Instructor</span>
            </div>
            <div class="contact-info-item">
                <span class="contact-info-key">Based</span>
                <span class="contact-info-val">Sukkur, Pakistan</span>
            </div>
            <div class="contact-info-item">
                <span class="contact-info-key">Focus</span>
                <span class="contact-info-val">Python, Data, Web</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pull-quote">
            <p>The best way to learn is by building things that actually work.</p>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SKILLS
# ─────────────────────────────────────────
elif page == "Skills":
    st.markdown('<div class="pg-eyebrow">What I know</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title"><strong>Skills</strong> &amp; Tools</div>', unsafe_allow_html=True)
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
        </div>
        """

    col1, col2 = st.columns(2, gap="large")

    with col1:
        bars = [("Python", 90), ("C++", 75), ("JavaScript", 70)]
        bars_html = "".join(skill_bar(n, p) for n, p in bars)
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Languages</div>
            <h3>Programming</h3>
            <br>{bars_html}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        bars2 = [("Streamlit", 90), ("Flask", 85), ("HTML & CSS", 82)]
        bars2_html = "".join(skill_bar(n, p) for n, p in bars2)
        st.markdown(f"""
        <div class="card">
            <div class="card-label">Frameworks</div>
            <h3>Web &amp; Frontend</h3>
            <br>{bars2_html}
        </div>
        """, unsafe_allow_html=True)

    tools = ["VS Code", "Git", "Jupyter", "Pandas", "NumPy", "Matplotlib", "Plotly", "MySQL", "Linux", "SQLite"]
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tools)
    st.markdown(f"""
    <div class="card">
        <div class="card-label">Ecosystem</div>
        <h3>Tools &amp; Libraries</h3>
        <div class="tool-grid" style="margin-top:16px">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  PROJECTS
# ─────────────────────────────────────────
elif page == "Projects":
    st.markdown('<div class="pg-eyebrow">What I built</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title">Selected <strong>Projects</strong></div>', unsafe_allow_html=True)
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
            "desc": "This portfolio — a modern, fully responsive Streamlit application with adaptive theming and a working contact form.",
            "tags": ["Streamlit", "CSS", "Python"],
        },
        {
            "title": "Data Dashboard",
            "desc": "Interactive analytics dashboard for visualising CSV datasets with dynamic Plotly charts, filters, and export support.",
            "tags": ["Pandas", "Plotly", "Streamlit"],
        },
    ]

    for i, p in enumerate(projects):
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        num = f"0{i+1}" if i < 9 else str(i+1)
        st.markdown(f"""
        <div class="proj-card">
            <div class="proj-index">{num}</div>
            <div>
                <div class="proj-title">{p['title']}</div>
                <p class="proj-desc">{p['desc']}</p>
                <div class="proj-tags">{tags_html}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  TEACHING
# ─────────────────────────────────────────
elif page == "Teaching":
    st.markdown('<div class="pg-eyebrow">Education &amp; Mentorship</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title"><strong>Teaching</strong> &amp; Learning</div>', unsafe_allow_html=True)
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
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-label">Pedagogy</div>
            <h3>How I Teach</h3>
            <ul>
                <li>100% hands-on, project-based learning</li>
                <li>Real assignments from the very first session</li>
                <li>One-on-one code review</li>
                <li>Problem-solving over memorisation</li>
                <li>Industry-relevant tech stack throughout</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pull-quote">
        <p>
            Theory without practice is trivia. Every concept I teach is immediately
            applied — a mini project, a challenge, a piece of something the student
            is genuinely building. That is how skills stick.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-label">Philosophy</div>
        <h3>My Belief as an Educator</h3>
        <p>
            I don't teach programming to produce coders who can pass exams.
            I teach it to produce people who can look at a problem, break it down,
            and build something that solves it. The language is secondary;
            the thinking is everything.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  CONTACT
# ─────────────────────────────────────────
elif page == "Contact":
    st.markdown('<div class="pg-eyebrow">Get in touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-title">Contact <strong>Me</strong></div>', unsafe_allow_html=True)
    st.markdown('<hr class="pg-rule">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.4], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-label">Direct Contact</div>
            <h3>Reach Me</h3>
            <div class="contact-info-item">
                <span class="contact-info-key">Email</span>
                <span class="contact-info-val">ahmedalixy149@gmail.com</span>
            </div>
            <div class="contact-info-item">
                <span class="contact-info-key">Phone</span>
                <span class="contact-info-val">+92 318 030 7822</span>
            </div>
            <div class="contact-info-item">
                <span class="contact-info-key">Location</span>
                <span class="contact-info-val">Sukkur, Sindh, Pakistan</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-label">Message</div>
            <h3>Send a Message</h3>
        </div>
        """, unsafe_allow_html=True)

        name  = st.text_input("Your Name",  placeholder="Ali Khan")
        email = st.text_input("Your Email", placeholder="ali@example.com")
        msg   = st.text_area("Message",     placeholder="Hello Mujeeb, I'd like to ...", height=130)

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
                        "Set EMAIL_USER and EMAIL_PASSWORD in Streamlit secrets or "
                        "as environment variables."
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
