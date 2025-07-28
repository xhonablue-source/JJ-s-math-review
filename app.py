import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd

# --- Page Setup ---
st.set_page_config(
    page_title="MathCraft: Quest for the Quarterback Crown",
    page_icon="🏈",
    layout="wide"
)

# --- Developer Credit ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("njit_logo.png", width=80)
    except:
        st.markdown("🏫")  # Fallback if logo not found

with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed for Jersey City by Xavier Honablue M.Ed**")
    st.markdown("*Target Universities: NJIT & RPI*")

st.markdown("---")

# --- Title and Intro ---
st.title("🏈 MathCraft: Quest for the Quarterback Crown")
st.markdown("""
**A 4-Week Challenge-Based Math Journey for Jeremiah Erskine**

Welcome, **Future NJIT Engineer**! This MathCraft program transforms 9th grade math review into an epic quest, blending Jeremiah’s passions—quarterback mechanics, Sonic speed, Segway adventures, and real estate success with his mother Rose from South Africa—into mathematical mastery.

---

### 🎯 Program Goal:
Prepare Jeremiah for a confident 10th grade math experience by reinforcing foundational skills through a personalized, interest-based curriculum rooted in Common Core standards, with Rose as his inspiring partner.

### 🧑🏿‍🏫 Who is Dr. X?
Dr. X isn’t a robot 🤓—he’s modeled after Xavier Honablue M.Ed, a real Black educator with glasses, a deep voice, and a heart for student success. He’s your sideline coach for math, cheering Jeremiah and Rose on!
""")

# Common Core Standards Alignment
st.info("📚 **Common Core Alignment:** This program covers High School Algebra standards like creating equations (HSA.CED), reasoning with equations (HSA.REI), and building functions (HSF.BF) through real-world applications.")

# Common Core Standards Dropdown
common_core_standard = st.selectbox("📋 Select specific Common Core Standard focus:", [
    "HSA.CED.A.1 - Create equations and inequalities in one variable",
    "HSA.CED.A.2 - Create equations in two or more variables to represent relationships",
    "HSA.CED.A.3 - Represent constraints by systems of equations and inequalities",
    "HSA.REI.B.3 - Solve linear equations and inequalities in one variable",
    "HSA.REI.B.4 - Solve quadratic equations in one variable",
    "HSA.REI.C.6 - Solve systems of linear equations exactly and approximately",
    "HSA.REI.D.11 - Explain why coordinates of intersection points satisfy both equations",
    "HSA.REI.D.12 - Graph solutions to systems of linear inequalities",
    "HSF.IF.B.4 - Interpret key features of graphs and tables",
    "HSF.IF.C.7 - Graph functions expressed symbolically",
    "HSF.BF.A.1 - Write a function that describes a relationship between quantities",
    "HSF.LE.A.2 - Construct linear and exponential functions"
])

# --- Student Info ---
st.subheader("🎮 Quarterback Profile Setup")
name = st.text_input("Enter your name:", value="Jeremiah Erskine")
position = st.selectbox("Choose your mathematical identity:", [
    "🏈 Quarterback Analyst", "🦔 Speed Calculator", "🛴 Slope Navigator",
    "🏠 Real Estate Mathematician", "🎯 NJIT Bound Scholar"
])

if name:
    st.success(f"Welcome, {name} the {position}! Ready to dominate 10th grade math with Rose by your side!")

# --- Level Selection ---
challenge_level = st.selectbox("Choose your challenge level:", [
    "🟢 Level 1: Sonic Dash Algebra Maze",
    "🔵 Level 2: QB Launch Trajectories",
    "🟡 Level 3: Naruto Systems Faceoff",
    "🔴 Level 4: NJIT College Ready Quest"
])

# Initialize session state for Dr. X chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello Jeremiah and Rose! I'm Dr. X, your AI math coach. Let’s conquer math together, from football fields to real estate deals!"}
    ]

# Dr. X API function
def ask_drx(message):
    try:
        response = requests.post(
            'https://ask-drx-730124987572.us-central1.run.app',
            json={'message': message},
            timeout=30
        )
        if response.status_code == 200:
            return response.json().get('reply', "Sorry, I couldn't process that.")
        else:
            return "I'm having trouble connecting right now. Please try again."
    except Exception as e:
        return "I'm having trouble connecting right now. Please try again."

# --- Week Navigation ---
st.header("📅 4-Week Mathematical Journey")

week_tabs = st.tabs([
    "📈 Week 1: Sonic Speeds & Algebra",
    "📊 Week 2: Football Physics & Quadratics",
    "🔄 Week 3: Naruto Motion & Systems",
    "🎓 Week 4: NJIT Bound - College Prep"
])

# --- WEEK 1 ---
with week_tabs[0]:
    st.subheader("🦔 Week 1: Sonic Speeds & Algebra Foundations")
    st.markdown("**📘 IXL Skills Focus:** [U.2 - Solve multi-step linear equations](https://www.ixl.com/math/algebra-1/solve-multi-step-linear-equations)")
    st.markdown("**📚 Common Core:** HSA.CED.A.1, HSA.REI.B.3")
    st.markdown("**🎯 Focus:** Expressions, Equations, and Linear Functions")

    st.markdown("**🎖 IXL Practice Links:**")
    st.markdown("""
    - [U.2 - Solve multi-step linear equations](https://www.ixl.com/math/algebra-1/solve-multi-step-linear-equations)
    - [U.3 - Solve linear equations: mixed review](https://www.ixl.com/math/algebra-1/solve-linear-equations-mixed-review)
    - [U.4 - Solve equations involving like terms](https://www.ixl.com/math/algebra-1/solve-equations-involving-like-terms)
    - [V.2 - Solve linear equations: word problems](https://www.ixl.com/math/algebra-1/solve-linear-equations-word-problems)
    """)

    # Story: Jeremiah and Rose’s Speed Adventure
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Back in South Africa, Jeremiah and his mom Rose loved watching wildlife dash across the savanna...
    """)

    # Interactive Sonic Speed Challenge
    st.markdown("### 🚀 Sonic vs. Jeremiah Speed Challenge")
    show_speed_chart = st.checkbox("Show Speed Comparison Chart 📊", value=True, key="speed_toggle")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**⚡ Sonic's Canonical Speed:** 767 mph (Speed of Sound)")
        jeremiah_40_time = st.slider("Your 40-yard dash time (seconds):", 4.0, 8.0, 5.5, 0.1)
        jeremiah_speed_mph = (40 * 3600) / (jeremiah_40_time * 5280)
        speed_ratio = 767 / jeremiah_speed_mph
        st.metric("Your Speed", f"{jeremiah_speed_mph:.1f} mph")
        st.metric("Sonic is", f"{speed_ratio:.0f}x faster!")

    with col2:
        if show_speed_chart:
            fig, ax = plt.subplots(figsize=(10, 6))
            speeds = ['Jeremiah', 'Sonic']
            values = [jeremiah_speed_mph, 767]
            colors = ['#ff6b6b', '#4ecdc4']
            ax.bar(speeds, values, color=colors)
            ax.set_ylabel('Speed (mph)')
            ax.set_title('Speed Comparison: Jeremiah vs. Sonic')
            ax.set_ylim(0, 800)
            st.pyplot(fig)

# --- WEEK 2 ---
with week_tabs[1]:
    st.subheader("🏈 Week 2: Football Physics & Quadratics")
    st.markdown("**📘 IXL Skills Focus:** [J.7 - Graph parabolas](https://www.ixl.com/math/algebra-1/graph-a-quadratic-function)")
    st.markdown("**📚 Common Core:** HSA.REI.B.4")
    st.markdown("**🎯 Focus:** Quadratic Functions and Vertex Form")

    st.markdown("**🎖 IXL Practice Links:**")
    st.markdown("""
    - [J.7 - Graph parabolas](https://www.ixl.com/math/algebra-1/graph-a-quadratic-function)
    - [J.8 - Graph a quadratic function](https://www.ixl.com/math/algebra-1/graph-a-quadratic-function-1)
    - [J.9 - Match quadratic functions and graphs](https://www.ixl.com/math/algebra-1/match-quadratic-functions-and-graphs)
    - [K.2 - Solve a quadratic equation using the quadratic formula](https://www.ixl.com/math/algebra-1/solve-a-quadratic-equation-using-the-quadratic-formula)
    """)

    st.markdown("### 🎯 Perfect Spiral Trajectory Analysis")
    # (Football trajectory code remains here...)

# --- WEEK 3 ---
with week_tabs[2]:
    st.subheader("🥷 Week 3: Naruto Motion & Systems of Equations")
    st.markdown("**📘 IXL Skills Focus:** [W.10 - Solve a system of equations by graphing](https://www.ixl.com/math/algebra-1/solve-a-system-of-equations-by-graphing)")
    st.markdown("**📚 Common Core:** HSA.CED.A.3")
    st.markdown("**🎯 Focus:** Simultaneous Equations and Real-Life Situations")

    st.markdown("**🎖 IXL Practice Links:**")
    st.markdown("""
    - [W.10 - Solve a system of equations by graphing](https://www.ixl.com/math/algebra-1/solve-a-system-of-equations-by-graphing)
    - [W.11 - Find the number of solutions to a system](https://www.ixl.com/math/algebra-1/find-the-number-of-solutions-to-a-system)
    - [W.13 - Systems of equations: word problems](https://www.ixl.com/math/algebra-1/systems-of-equations-word-problems)
    """)

    # (Triple challenge & commission systems code remains...)

# --- WEEK 4 ---
with week_tabs[3]:
    st.subheader("🎓 Week 4: NJIT Bound - College Prep & Inequalities")
    st.markdown("**📘 IXL Skills Focus:** [Y.5 - Graph compound inequalities](https://www.ixl.com/math/algebra-1/graph-compound-inequalities)")
    st.markdown("**📚 Common Core:** HSA.REI.D.12, HSA.CED.A.2")
    st.markdown("**🎯 Focus:** Cumulative Assessment and Future Planning")

    st.markdown("**🎖 IXL Practice Links:**")
    st.markdown("""
    - [Y.5 - Graph compound inequalities](https://www.ixl.com/math/algebra-1/graph-compound-inequalities)
    - [Y.7 - Solve compound inequalities](https://www.ixl.com/math/algebra-1/solve-compound-inequalities)
    - [FF.2 - Systems of linear inequalities](https://www.ixl.com/math/algebra-1/systems-of-linear-inequalities)
    """)

    # (College readiness and investment code remains...)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <h4>🎓 Ready to Dominate 10th Grade Math!</h4>
    <p><em>"Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding." - William Paul Thurston</em></p>
    <p><strong>Built for Jere
