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
# CSS
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

.stApp {
    background: #0b1220;
    color: white;
}

/* Sidebar always visible */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
    padding-top: 20px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 700;
}

.highlight {
    color: #38bdf8;
}

/* Skills bar */
.bar {
    width: 100%;
    height: 8px;
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
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
# SIDEBAR (REAL FIX)
# ─────────────────────────────
with st.sidebar:

    st.title("👨‍💻 Mujeeb Ahmed")
    st.caption("Python Developer | Data Science | Educator")

    page = st.selectbox(
        "Navigation",
        ["Home", "About Me", "Skills", "Projects", "Contact"]
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
            st.warning("Upload profile.jpeg in folder")

    with col2:
        st.markdown("""
        <div class="title">
        Hi, I'm <span class="highlight">Mujeeb Ahmed</span>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        I am a Python Developer and Data Science student.
        I build real-world applications using Flask, Streamlit, and AI tools.
        """)

# ─────────────────────────────
# ABOUT
# ─────────────────────────────
elif page == "About Me":

    st.title("About Me")

    st.markdown("""
    <div class="card">
    I am Mujeeb Ahmed from Pakistan.
    I specialize in Python development, web apps, and teaching programming.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    🎓 Data Science Student (Sukkur IBA University)<br>
    💻 Python Developer<br>
    📍 Sukkur, Pakistan
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────
# SKILLS
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

    st.title("Projects")

    projects = [
        ("Quiz System", "Flask-based quiz platform with admin panel"),
        ("AI Chatbot", "AI chatbot using OpenAI API"),
        ("Data Dashboard", "Interactive Streamlit dashboard")
    ]

    for title, desc in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────
# CONTACT
# ─────────────────────────────
elif page == "Contact":

    st.title("Contact Me")

    st.markdown("""
    <div class="card">
    📧 Email: ahmedalixy149@gmail.com<br>
    📱 Phone: +92 318 030 7822<br>
    📍 Sukkur, Pakistan
    </div>
    """, unsafe_allow_html=True)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Send")
