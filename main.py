import streamlit as st

# ─────────────────────────────
# CONFIG
# ─────────────────────────────
st.set_page_config(
    page_title="Mujeeb Ahmed Portfolio",
    page_icon="💻",
    layout="wide"
)

# ─────────────────────────────
# CSS (SAFE - NO SIDEBAR BREAK)
# ─────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Outfit', sans-serif;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* App background */
.stApp {
    background: #0b1220;
    color: white;
}

/* Sidebar safe styling */
[data-testid="stSidebar"] {
    background-color: #0f172a;
}

/* Title */
.big-title {
    font-size: 40px;
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
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}

/* Skill bar */
.bar {
    width: 100%;
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
    display:inline-block;
    background: rgba(56,189,248,0.15);
    color:#38bdf8;
    padding:5px 10px;
    border-radius:20px;
    font-size:12px;
    margin:3px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────
with st.sidebar:
    st.title("👨‍💻 Mujeeb Ahmed")
    st.caption("Python Developer | Data Science | Educator")

    page = st.radio(
        "Navigation",
        ["Home", "About Me", "Skills", "Projects", "Contact"]
    )

# ─────────────────────────────
# HOME PAGE
# ─────────────────────────────
if page == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image("profile.jpeg", width=250)
        except:
            st.warning("Please upload profile.jpeg in GitHub repo")

    with col2:
        st.markdown("""
        <div class="big-title">
        Hi, I'm <span class="highlight">Mujeeb Ahmed</span>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        Python Developer, Data Science student, and Educator.
        I build real-world applications using Flask, Streamlit,
        and modern AI tools.
        """)

# ─────────────────────────────
# ABOUT PAGE
# ─────────────────────────────
elif page == "About Me":

    st.title("About Me")

    st.markdown("""
    <div class="card">
    I am Mujeeb Ahmed from Pakistan.
    I am a Python Developer and Data Science student
    at Sukkur IBA University.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    💻 Python Developer  
    🎓 Data Science Student  
    📍 Sukkur, Pakistan  
    👨‍🏫 Programming Instructor  
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────
# SKILLS PAGE
# ─────────────────────────────
elif page == "Skills":

    st.title("Skills")

    skills = {
        "Python": 90,
        "Flask": 85,
        "Streamlit": 92,
        "HTML/CSS": 80,
        "JavaScript": 70
    }

    for skill, percent in skills.items():

        st.write(skill)

        st.markdown(f"""
        <div class="bar">
            <div class="fill" style="width:{percent}%"></div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────
# PROJECTS PAGE
# ─────────────────────────────
elif page == "Projects":

    st.title("Projects")

    projects = [
        {
            "title": "Quiz System",
            "desc": "Flask-based quiz system with admin panel and database."
        },
        {
            "title": "AI Chatbot",
            "desc": "AI chatbot using OpenAI API integration."
        },
        {
            "title": "Data Dashboard",
            "desc": "Interactive Streamlit dashboard for data analysis."
        }
    ]

    for p in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <span class="tag">Python</span>
        <span class="tag">Project</span>
        """, unsafe_allow_html=True)

# ─────────────────────────────
# CONTACT PAGE
# ─────────────────────────────
elif page == "Contact":

    st.title("Contact Me")

    st.markdown("""
    <div class="card">
    📧 Email: ahmedalixy149@gmail.com  
    📱 Phone: +92 318 030 7822  
    📍 Location: Sukkur, Pakistan  
    </div>
    """, unsafe_allow_html=True)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Send Message")
