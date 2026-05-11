import streamlit as st

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Mujeeb Ahmed | Portfolio",
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

/* Hide Streamlit default UI */
#MainMenu, footer, header{
    visibility:hidden;
}

/* Main Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#111827,#020617);
    color: white;
}

/* Main Container */
.block-container{
    padding-top: 2rem;
    max-width: 1200px;
}

/* Hero Section */
.hero{
    padding: 80px 0 40px 0;
}

.small-text{
    color: #38bdf8;
    font-size: 14px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero-title{
    font-size: 72px;
    font-weight: 700;
    line-height: 1;
    color: white;
}

.hero-title span{
    color: #38bdf8;
}

.hero-desc{
    margin-top: 25px;
    color: #cbd5e1;
    font-size: 18px;
    line-height: 1.8;
    max-width: 700px;
}

/* Buttons */
.btns{
    margin-top: 35px;
    display: flex;
    gap: 15px;
}

.btn{
    padding: 12px 28px;
    border-radius: 10px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    transition: 0.3s;
}

.primary-btn{
    background: #38bdf8;
    color: black;
}

.primary-btn:hover{
    background: white;
}

.secondary-btn{
    border: 1px solid #38bdf8;
    color: #38bdf8;
}

.secondary-btn:hover{
    background: #38bdf8;
    color: black;
}

/* Section */
.section-title{
    margin-top: 80px;
    font-size: 40px;
    font-weight: 700;
    color: white;
}

.section-sub{
    color: #94a3b8;
    margin-top: 10px;
    margin-bottom: 40px;
}

/* Cards */
.card{
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    transition: 0.3s;
    height: 100%;
}

.card:hover{
    transform: translateY(-5px);
    border-color: #38bdf8;
}

.card h3{
    color: white;
    margin-bottom: 15px;
    font-size: 24px;
}

.card p{
    color: #cbd5e1;
    line-height: 1.8;
}

/* Skills */
.skill{
    margin-bottom: 25px;
}

.skill-name{
    margin-bottom: 8px;
    font-weight: 500;
}

.skill-bar{
    width: 100%;
    height: 8px;
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    overflow: hidden;
}

.skill-fill{
    height: 100%;
    background: #38bdf8;
}

/* Project Tags */
.tags{
    margin-top: 15px;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.tag{
    background: rgba(56,189,248,0.15);
    color: #38bdf8;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
}

/* Contact Box */
.contact-box{
    background: rgba(255,255,255,0.05);
    padding: 35px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
}

.contact-item{
    margin-bottom: 18px;
    color: #cbd5e1;
    font-size: 17px;
}

/* Footer */
.footer{
    margin-top: 80px;
    text-align: center;
    color: #64748b;
    padding-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# HERO SECTION
# ─────────────────────────────────────────
st.markdown("""
<div class="hero">

<div class="small-text">
PYTHON DEVELOPER • DATA SCIENTIST • EDUCATOR
</div>

<div class="hero-title">
Mujeeb <span>Ahmed</span>
</div>

<div class="hero-desc">
I build modern Python applications, create intelligent systems,
and teach programming through real-world projects.
Focused on clean design, practical coding,
and impactful digital experiences.
</div>

<div class="btns">
    <a href="https://github.com" class="btn primary-btn">View Projects</a>
    <a href="mailto:example@gmail.com" class="btn secondary-btn">Contact Me</a>
</div>

</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# ABOUT
# ─────────────────────────────────────────
st.markdown("""
<div class="section-title">About Me</div>
<div class="section-sub">
Developer, educator, and tech enthusiast from Pakistan.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Who I Am</h3>
        <p>
        I am a Python Developer and Data Science student
        passionate about building modern software solutions.
        My work focuses on web applications, AI tools,
        data visualization, and programming education.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>What I Do</h3>
        <p>
        I develop Flask and Streamlit applications,
        build dashboards, create automation tools,
        and teach students through practical coding projects.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
# SKILLS
# ─────────────────────────────────────────
st.markdown("""
<div class="section-title">Skills</div>
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
        <div class="skill-name">{skill}</div>
        <div class="skill-bar">
            <div class="skill-fill" style="width:{percent}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────
# PROJECTS
# ─────────────────────────────────────────
st.markdown("""
<div class="section-title">Projects</div>
<div class="section-sub">
Some projects I have developed.
</div>
""", unsafe_allow_html=True)

projects = [
    {
        "title": "Quiz Management System",
        "desc": "A complete online quiz system with admin panel, question management, leaderboard, and result tracking.",
        "tags": ["Flask", "SQLite", "Python"]
    },
    {
        "title": "AI Chatbot",
        "desc": "An intelligent chatbot integrated with AI APIs, voice input, and modern conversation handling.",
        "tags": ["OpenAI", "Python", "AI"]
    },
    {
        "title": "Data Dashboard",
        "desc": "Interactive dashboard for visualizing CSV datasets with charts, filters, and analytics.",
        "tags": ["Pandas", "Plotly", "Streamlit"]
    }
]

cols = st.columns(3)

for col, project in zip(cols, projects):
    tags_html = "".join(
        [f"<span class='tag'>{tag}</span>" for tag in project["tags"]]
    )

    with col:
        st.markdown(f"""
        <div class="card">
            <h3>{project['title']}</h3>
            <p>{project['desc']}</p>

            <div class="tags">
                {tags_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────
# CONTACT
# ─────────────────────────────────────────
st.markdown("""
<div class="section-title">Contact</div>
<div class="section-sub">
Let’s build something amazing together.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">

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
