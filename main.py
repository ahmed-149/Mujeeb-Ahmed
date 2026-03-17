import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Mujeeb Ahmed", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Page Width Control */
.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
    margin: auto;
}

/* Background */
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
}

/* Section spacing */
.section {
    margin-top: 40px;
}

/* Card Design */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.3);
    transition: 0.3s;
    color: white;
    margin-bottom: 25px;
}

.card:hover {
    transform: translateY(-8px);
}

/* Titles */
.title {
    font-size: 45px;
    font-weight: 700;
}

.subtitle {
    font-size: 18px;
    color: #94a3b8;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #22c55e, #4ade80);
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Home", "About", "Skills", "Projects", "Teaching", "Contact"])

# ---------------- HOME ----------------
if page == "Home":
    st.markdown('<div class="section">', unsafe_allow_html=True)

    col1, col2 = st.columns([1,2], gap="large")

    with col1:
        st.image("profile.jpeg", width=250)

    with col2:
        st.markdown('<p class="title">Mujeeb Ahmed</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Python Developer | Data Science Graduate | Teacher</p>', unsafe_allow_html=True)

        st.write("""
I am a passionate developer and educator specializing in Python and modern web technologies.
I have completed my journey in Data Science and now focus on building high-quality applications
and training students with real-world skills.
""")
        st.success("Turning ideas into real-world applications")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")

    # Cards Section
    st.markdown('<div class="section">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown('<div class="card"><h3>💻 Development</h3><p>Building scalable apps using Flask & Streamlit.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>📊 Data Science</h3><p>Strong analytical and problem-solving skills.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>👨‍🏫 Teaching</h3><p>Practical teaching approach for students.</p></div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
elif page == "About":
    st.markdown('<div class="section card">', unsafe_allow_html=True)

    st.title("About Me")
    st.write("""
I am **Mujeeb Ahmed**, a passionate Python Developer, Data Science graduate, and Programming Instructor with a strong focus on building practical, real-world solutions.

🎓 **Degree:** Data Science from **Sukkur IBA University**  
💼 **Profession:** Programming Teacher & Developer

My journey in technology began with curiosity and quickly turned into a mission to simplify programming for others. I specialize in Python development, data analysis, and web application design. My goal is to combine **practical development skills** with **teaching expertise** to make students industry-ready.

**Key Highlights:**
- ✅ Real-world project experience with Python and web technologies  
- ✅ Strong foundation in Data Science and analytics  
- ✅ Practical, project-based teaching methodology  
- ✅ Expertise in Flask, Streamlit, and SQLite for scalable applications

**Hobbies & Interests:**
- Solving programming challenges and puzzles  
- Exploring AI & Machine Learning trends  
- Mentoring students and sharing knowledge  
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif page == "Skills":
    st.title("Skills")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Programming")
        st.write("Python")
        st.progress(90)
        st.write("C++")
        st.progress(75)
        st.write("JavaScript")
        st.progress(70)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Web & Tools")
        st.write("HTML")
        st.progress(85)
        st.write("CSS")
        st.progress(75)
        st.write("Flask")
        st.progress(85)
        st.write("Streamlit")
        st.progress(90)
        st.write("SQLite")
        st.progress(80)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif page == "Projects":
    st.title("Projects")
    st.markdown('<div class="section">', unsafe_allow_html=True)

    projects = [
        {
            "title": "Quiz System",
            "desc": "A complete quiz platform with an admin panel for managing subjects and questions. Allows students to take quizzes and tracks results in Excel or database.",
            "tech": "Python, Flask, SQLite",
            "features": "Full CRUD, responsive UI, question sequencing, result tracking"
        },
        {
            "title": "AI Chatbot",
            "desc": "An AI-powered chatbot with voice input, chat history, and intelligent responses using OpenAI APIs.",
            "tech": "Python, APIs",
            "features": "Voice input/output, persistent chat history, conversational AI"
        },
        {
            "title": "Portfolio Website",
            "desc": "Modern portfolio UI built using Streamlit, showcasing projects, skills, and teaching experience.",
            "tech": "Python, Streamlit, CSS",
            "features": "Responsive layout, interactive cards, internal CSS styling"
        },
        {
            "title": "Student Mini Projects",
            "desc": "Guided students to create small projects like calculators, web scrapers, and basic games to reinforce learning concepts.",
            "tech": "Python, C++, HTML/CSS, JavaScript",
            "features": "Hands-on learning, practical coding exercises, project mentorship"
        }
    ]

    for p in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
            <p><b>Tech Stack:</b> {p['tech']}</p>
            <p><b>Features:</b> {p['features']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- TEACHING ----------------
elif page == "Teaching":
    st.markdown('<div class="section card">', unsafe_allow_html=True)

    st.title("Teaching Experience")
    st.write("""
I teach programming with a **practical and project-based approach**, ensuring that students not only learn concepts but also know how to apply them in real-world scenarios.

**Subjects I Teach:**
- Python Programming
- C++ Programming
- HTML & CSS
- JavaScript
- Data Science Fundamentals

**My Teaching Approach:**
- 🔹 Hands-on coding exercises  
- 🔹 Project-based learning  
- 🔹 Logical thinking & problem-solving focus  
- 🔹 Mentorship and guidance on real projects

I have successfully trained students who are now confident in developing **applications, websites, and data-driven solutions**. My goal is to help students become **industry-ready** while keeping learning engaging and interactive.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.title("Contact Me")
    st.markdown('<div class="section card">', unsafe_allow_html=True)

    st.write("📧 Email: ahmedalixy149@gmail.com")
    st.write("📱 Phone: +92 3180307822")
    st.write("🔗 LinkedIn: https://www.linkedin.com/in/mujeeb-ullah-a16555321")

    st.markdown("### Send Me a Message")

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            if name.strip() == "" or email.strip() == "" or message.strip() == "":
                st.warning("Please fill in all fields before sending.")
            else:
                try:
                    import smtplib
                    from email.message import EmailMessage
                    import pandas as pd
                    from datetime import datetime
                    import os

                    # --- Email Setup ---
                    msg = EmailMessage()
                    msg['Subject'] = f"Portfolio Contact Form Message from {name}"
                    msg['From'] = "ahmedalixy149@gmail.com"
                    msg['To'] = "ahmedalixy149@gmail.com"
                    msg.set_content(f"Name: {name}\nEmail: {email}\nMessage:\n{message}")

                    # --- Send Email via Gmail SMTP ---
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login("ahmedalixy149@gmail.com", "ftrz lrsx pfvk vrte")  # Your App Password
                        smtp.send_message(msg)

                    # --- Save message locally as backup ---
                    file_path = "contact_messages.csv"
                    new_entry = pd.DataFrame({
                        "Name": [name],
                        "Email": [email],
                        "Message": [message],
                        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                    })
                    if os.path.exists(file_path):
                        df = pd.read_csv(file_path)
                        df = pd.concat([df, new_entry], ignore_index=True)
                    else:
                        df = new_entry
                    df.to_csv(file_path, index=False)

                    st.success("✅ Your message has been sent! I will contact you soon.")

                except Exception as e:
                    st.error(f"❌ Failed to send message. Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)