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
# GLOBAL CSS
# ─────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Outfit', sans-serif;
}

#MainMenu, footer, header{
    visibility:hidden;
}

.stApp{
    background: #0b1220;
    color: white;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background: #0f172a;
}

/* Title */
.title {
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

/* Cards */
.card{
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}

/* Skill bar */
.bar{
    width: 100%;
    height: 8px;
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    overflow: hidden;
}

.fill{
    height: 100%;
    background: #38bdf8;
}

/* Tag */
.tag{
    display:inline-block;
    background: rgba(56,189,248,0.15);
    color:#38bdf8;
    padding:6px 10px;
    margin:3px;
    border-radius:20px;
    font-size:12px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────
# SIDEBAR (REAL NAVIGATION)
# ─────────────────────────────
with st.sidebar:

    st.title("👨‍💻 Mujeeb Ahmed")
    st.caption("Python Developer | Data Science | Educator")

    menu = st.radio(
        "Navigation",
        ["Home", "About Me", "Skills", "Projects", "Contact"]
    )

# ─────────────────────────────
# HOME PAGE
# ─────────────────────────────
if menu == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image("profile.jpeg", width=250)
        except:
            st.warning("Add profile.jpeg in project folder")

    with col2:

        st.markdown("""
        <div class="title">
        Hi, I'm <span class="highlight">Mujeeb Ahmed</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="subtext">
        I am a Python Developer, Data Science student, and Educator.
        I build modern applications using Python, Flask, Streamlit,
        and AI tools.
        <br><br>
        My goal is to create real-world projects and teach students
        through practical coding experience.
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────
# ABOUT PAGE
# ─────────────────────────────
elif menu == "About Me":

    st.title("About Me")

    st.markdown("""
    <div class="card">
    I am Mujeeb Ahmed from Pakistan, currently studying Data Science at Sukkur IBA University.
    I specialize in Python development, web applications, and teaching programming.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    📍 Location: Sukkur, Sindh, Pakistan  
    🎓 Education: Data Science (Sukkur IBA University)  
    💼 Role: Developer & Programming Instructor  
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────
# SKILLS PAGE
# ─────────────────────────────
elif menu == "Skills":

    st.title("Skills")

    skills = {
        "Python": 90,
        "Flask": 85,
        "Streamlit": 92,
        "HTML & CSS": 80,
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
# PROJECTS PAGE
# ─────────────────────────────
elif menu == "Projects":

    st.title("Projects")

    projects = [
        {
            "title": "Quiz System",
            "desc": "Flask-based quiz system with admin panel, database, and result tracking.",
            "tags": ["Flask", "SQLite", "Python"]
        },
        {
            "title": "AI Chatbot",
            "desc": "AI chatbot with OpenAI API integration and smart responses.",
            "tags": ["AI", "Python", "API"]
        },
        {
            "title": "Data Dashboard",
            "desc": "Interactive dashboard for data visualization using Streamlit.",
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
# CONTACT PAGE
# ─────────────────────────────
elif menu == "Contact":

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
