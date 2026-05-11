import streamlit as st

# ─────────────────────────────
# PAGE CONFIG
# ─────────────────────────────
st.set_page_config(
    page_title="Mujeeb Ahmed Portfolio",
    page_icon="💻",
    layout="wide"
)

# ─────────────────────────────
# CSS (Modern Clean UI)
# ─────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* App Background */
.stApp {
    background: #0b1220;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0f172a;
}

/* Titles */
.title {
    font-size: 42px;
    font-weight: 700;
}

.highlight {
    color: #38bdf8;
}

.subtext {
    color: #94a3b8;
    font-size: 16px;
    line-height: 1.7;
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 15px;
}

/* Skill bar */
.bar {
    height: 8px;
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    overflow: hidden;
}

.fill {
    height: 100%;
    background: #38bdf8;
}

/* Tag */
.tag {
    display: inline-block;
    padding: 5px 10px;
    margin: 3px;
    background: rgba(56,189,248,0.15);
    color: #38bdf8;
    border-radius: 20px;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────
st.sidebar.title("Mujeeb Ahmed")
st.sidebar.caption("Python Developer | Data Scientist | Educator")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "About", "Skills", "Projects", "Contact"]
)

# ─────────────────────────────
# HOME
# ─────────────────────────────
if page == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image("profile.jpeg", width=250)
        except:
            st.warning("Upload profile.jpeg in project folder")

    with col2:
        st.markdown("""
        <div class="title">
        Hi, I'm <span class="highlight">Mujeeb Ahmed</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="subtext">
        I am a Python Developer and Data Science student
        who builds modern web apps, automation tools,
        and AI-based systems.
        <br><br>
        I also teach programming with a focus on real-world projects.
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────
# ABOUT
# ─────────────────────────────
elif page == "About":

    st.markdown("## About Me")

    st.markdown("""
    <div class="card">
    I am passionate about programming, teaching, and building real-world applications.
    My focus is on Python, Flask, Streamlit, and Data Science.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    🎓 Education: Data Science (Sukkur IBA University)<br>
    💻 Role: Developer & Instructor<br>
    📍 Location: Pakistan<br>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────
# SKILLS
# ─────────────────────────────
elif page == "Skills":

    st.markdown("## Skills")

    skills = {
        "Python": 90,
        "Flask": 85,
        "Streamlit": 92,
        "HTML/CSS": 80,
        "JavaScript": 70
    }

    for skill, value in skills.items():
        st.write(skill)

        st.markdown(f"""
        <div class="bar">
            <div class="fill" style="width:{value}%"></div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────
# PROJECTS
# ─────────────────────────────
elif page == "Projects":

    st.markdown("## Projects")

    projects = [
        {
            "title": "Quiz System",
            "desc": "Flask-based quiz platform with admin panel and database system.",
            "tags": ["Flask", "SQLite", "Python"]
        },
        {
            "title": "AI Chatbot",
            "desc": "AI-powered chatbot with OpenAI API integration.",
            "tags": ["AI", "Python", "API"]
        },
        {
            "title": "Data Dashboard",
            "desc": "Interactive data visualization dashboard using Streamlit.",
            "tags": ["Streamlit", "Pandas", "Plotly"]
        }
    ]

    for p in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

        for t in p["tags"]:
            st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)

# ─────────────────────────────
# CONTACT
# ─────────────────────────────
elif page == "Contact":

    st.markdown("## Contact Me")

    st.markdown("""
    <div class="card">
    📧 Email: ahmedalixy149@gmail.com<br>
    📱 Phone: +92 318 030 7822<br>
    📍 Location: Sukkur, Pakistan
    </div>
    """, unsafe_allow_html=True)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Send Message")
