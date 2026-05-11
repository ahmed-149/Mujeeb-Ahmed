import streamlit as st

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Mujeeb Ahmed Portfolio",
    page_icon="💻",
    layout="wide"
)

# ─────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Outfit', sans-serif;
}

/* Hide Streamlit default menu */
#MainMenu, footer, header{
    visibility:hidden;
}

.stApp{
    background: linear-gradient(135deg,#020617,#0f172a,#111827);
    color:white;
}

.block-container{
    padding-top: 2rem;
    max-width: 1200px;
}

/* Navbar */
.navbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px 0;
    margin-bottom:40px;
}

.logo{
    font-size:28px;
    font-weight:700;
    color:white;
}

.logo span{
    color:#38bdf8;
}

/* Hero Section */
.hero{
    padding:40px 0;
}

.hero-small{
    color:#38bdf8;
    letter-spacing:3px;
    font-size:14px;
    margin-bottom:15px;
}

.hero-title{
    font-size:70px;
    font-weight:700;
    line-height:1;
}

.hero-title span{
    color:#38bdf8;
}

.hero-desc{
    color:#cbd5e1;
    font-size:18px;
    line-height:1.8;
    margin-top:25px;
    max-width:700px;
}

/* Image */
.profile-img{
    border-radius:20px;
    overflow:hidden;
    border:2px solid rgba(255,255,255,0.1);
}

/* Section */
.section-title{
    margin-top:40px;
    margin-bottom:20px;
    font-size:38px;
    font-weight:700;
}

.section-sub{
    color:#94a3b8;
    margin-bottom:40px;
}

/* Cards */
.card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    padding:30px;
    border-radius:20px;
    margin-bottom:20px;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
    border-color:#38bdf8;
}

.card-title{
    font-size:24px;
    font-weight:600;
    margin-bottom:15px;
    color:white;
}

.card-text{
    color:#cbd5e1;
    line-height:1.8;
}

/* Skills */
.skill{
    margin-bottom:25px;
}

.skill-name{
    margin-bottom:8px;
    font-weight:500;
}

.skill-bar{
    width:100%;
    height:8px;
    background:rgba(255,255,255,0.1);
    border-radius:20px;
    overflow:hidden;
}

.skill-fill{
    height:100%;
    background:#38bdf8;
}

/* Tags */
.tag{
    display:inline-block;
    background:rgba(56,189,248,0.15);
    color:#38bdf8;
    padding:6px 14px;
    border-radius:20px;
    margin-right:8px;
    margin-top:10px;
    font-size:12px;
}

/* Contact */
.contact-item{
    margin-bottom:18px;
    font-size:17px;
    color:#cbd5e1;
}

/* Footer */
.footer{
    text-align:center;
    color:#64748b;
    margin-top:60px;
    padding-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# TOP NAVBAR
# ─────────────────────────────────────────
st.markdown("""
<div class="navbar">
    <div class="logo">
        Mujeeb <span>Ahmed</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# TABS
# ─────────────────────────────────────────
tabs = st.tabs([
    "Home",
    "About Me",
    "Skills",
    "Projects",
    "Contact"
])

# ─────────────────────────────────────────
# HOME TAB
# ─────────────────────────────────────────
with tabs[0]:

    col1, col2 = st.columns([1.3, 1])

    with col1:

        st.markdown("""
        <div class="hero">

        <div class="hero-small">
        PYTHON DEVELOPER • DATA SCIENTIST • EDUCATOR
        </div>

        <div class="hero-title">
        Mujeeb <span>Ahmed</span>
        </div>

        <div class="hero-desc">
        I build modern Python applications,
        AI-powered systems, and interactive dashboards.
        I also teach programming through practical
        project-based learning.
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.image(
            "profile.jpeg",
            use_container_width=True
        )

# ─────────────────────────────────────────
# ABOUT TAB
# ─────────────────────────────────────────
with tabs[1]:

    st.markdown("""
    <div class="section-title">
    About Me
    </div>

    <div class="section-sub">
    Developer, educator, and technology enthusiast.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <div class="card-title">
    Who I Am
    </div>

    <div class="card-text">
    I am Mujeeb Ahmed, a Python Developer and
    Data Science student from Pakistan.
    I create web applications, dashboards,
    and intelligent systems using modern technologies.

    I also teach programming and help students
    learn through practical projects instead
    of only theoretical concepts.
    </div>

    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
# SKILLS TAB
# ─────────────────────────────────────────
with tabs[2]:

    st.markdown("""
    <div class="section-title">
    Skills
    </div>

    <div class="section-sub">
    Technologies and tools I work with.
    </div>
    """, unsafe_allow_html=True)

    skills = {
        "Python": 90,
        "Flask": 85,
        "Streamlit": 92,
        "HTML & CSS": 80,
        "JavaScript": 70
    }

    for skill, percent in skills.items():

        st.markdown(f"""
        <div class="skill">

        <div class="skill-name">
        {skill}
        </div>

        <div class="skill-bar">
            <div class="skill-fill" style="width:{percent}%"></div>
        </div>

        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────
# PROJECTS TAB
# ─────────────────────────────────────────
with tabs[3]:

    st.markdown("""
    <div class="section-title">
    Projects
    </div>

    <div class="section-sub">
    Some projects I have developed.
    </div>
    """, unsafe_allow_html=True)

    project1, project2, project3 = st.columns(3)

    with project1:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        Quiz System
        </div>

        <div class="card-text">
        Complete online quiz system with
        admin panel, result tracking,
        and leaderboard functionality.
        </div>

        <span class="tag">Flask</span>
        <span class="tag">SQLite</span>
        <span class="tag">Python</span>

        </div>
        """, unsafe_allow_html=True)

    with project2:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        AI Chatbot
        </div>

        <div class="card-text">
        Intelligent chatbot integrated with
        AI APIs, voice input,
        and modern conversation handling.
        </div>

        <span class="tag">OpenAI</span>
        <span class="tag">Python</span>
        <span class="tag">AI</span>

        </div>
        """, unsafe_allow_html=True)

    with project3:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        Data Dashboard
        </div>

        <div class="card-text">
        Interactive dashboard for visualizing
        CSV datasets with charts,
        filters, and analytics.
        </div>

        <span class="tag">Pandas</span>
        <span class="tag">Plotly</span>
        <span class="tag">Streamlit</span>

        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────
# CONTACT TAB
# ─────────────────────────────────────────
with tabs[4]:

    st.markdown("""
    <div class="section-title">
    Contact Me
    </div>

    <div class="section-sub">
    Let’s build something amazing together.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <div class="contact-item">
    📧 ahmedalixy149@gmail.com
    </div>

    <div class="contact-item">
    📍 Sukkur, Sindh, Pakistan
    </div>

    <div class="contact-item">
    📱 +92 318 030 7822
    </div>

    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.markdown("""
<div class="footer">
Designed & Developed by Mujeeb Ahmed
</div>
""", unsafe_allow_html=True)
