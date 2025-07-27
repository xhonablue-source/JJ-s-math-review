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
    except FileNotFoundError:
        st.markdown("🏫")
    except Exception:
        st.markdown("🏫")

with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed for Jersey City by Xavier Honablue M.Ed**")
    st.markdown("*Target Universities: NJIT & RPI*")

st.markdown("---")

# --- Title and Intro ---
st.title("🏈 MathCraft: Quest for the Quarterback Crown")
st.markdown("""
**A 4-Week Challenge-Based Math Journey for Jeremiah Erskine**

Welcome, **Future NJIT Engineer**! This program transforms 9th grade math into an epic quest, blending Jeremiah’s passions—quarterback skills, Sonic speed, Segway adventures, and real estate with his mom Rose from South Africa—into mathematical mastery.

---

### 🎯 Program Goal:
Prepare Jeremiah for 10th grade math with a personalized curriculum aligned with Common Core standards, supported by Rose.

### 🧑🏿‍🏫 Who is Dr. X?
Dr. X, inspired by Xavier Honablue M.Ed, is your AI math coach with a deep voice and a passion for student success!
""")

# Common Core Alignment
st.info("📚 **Common Core Alignment:** HSA.CED.A.1, HSA.REI.B.3, HSA.REI.B.4, HSA.CED.A.3, HSA.REI.D.12")

# --- Student Info ---
st.subheader("🎮 Quarterback Profile Setup")
name = st.text_input("Enter your name:", value="Jeremiah Erskine")
position = st.selectbox("Choose your mathematical identity:", [
    "🏈 Quarterback Analyst", "🦔 Speed Calculator", "🛴 Slope Navigator",
    "🏠 Real Estate Mathematician", "🎯 NJIT Bound Scholar"
])
if name:
    st.success(f"Welcome, {name} the {position}! Let’s conquer math with Rose!")

# --- Level Selection ---
challenge_level = st.selectbox("Choose your challenge level:", [
    "🟢 Level 1: Sonic Dash Algebra Maze",
    "🔵 Level 2: QB Launch Trajectories",
    "🟡 Level 3: Naruto Systems Faceoff",
    "🔴 Level 4: NJIT College Ready Quest"
])

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "Hello Jeremiah and Rose! I'm Dr. X, your math coach. Let’s get started!"}]
if 'jeremiah_speed_mph' not in st.session_state:
    st.session_state.jeremiah_speed_mph = 16.4

# Dr. X API function
def ask_drx(message):
    try:
        response = requests.post(
            'https://ask-drx-730124987572.us-central1.run.app',
            json={'message': message},
            timeout=10
        )
        return response.json().get('reply', "Error processing request.") if response.status_code == 200 else f"API error: {response.status_code}"
    except requests.RequestException:
        return "Connection error. Please try again later."
    except Exception:
        return "Unexpected error. Please try again."

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
    st.subheader("🦔 Week 1: Sonic Speeds & Algebra")
    st.markdown("**🎯 Focus:** Linear Equations and Rates")

    # Sonic vs. Jeremiah Speed
    st.markdown("### 🚀 Sonic vs. Jeremiah Speed Challenge")
    jeremiah_40_time = st.slider("Your 40-yard dash time (seconds):", 4.0, 8.0, 5.5, 0.1)
    if jeremiah_40_time > 0:
        jeremiah_speed_mph = (40 * 3600) / (jeremiah_40_time * 5280)
        st.session_state.jeremiah_speed_mph = jeremiah_speed_mph
        speed_ratio = 767 / jeremiah_speed_mph
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Your Speed", f"{jeremiah_speed_mph:.1f} mph")
        with col2:
            st.metric("Sonic is", f"{speed_ratio:.0f}x faster!")
        if st.checkbox("Show Speed Chart", key="w1_speed"):
            fig, ax = plt.subplots()
            ax.bar(['Jeremiah', 'Sonic'], [jeremiah_speed_mph, 767], color=['#ff6b6b', '#4ecdc4'])
            ax.set_ylabel('Speed (mph)')
            ax.set_title('Speed Comparison')
            st.pyplot(fig)
            plt.close(fig)
    else:
        st.error("Invalid time. Please enter a value greater than 0.")

    # Lincoln Park Challenge
    st.markdown("### 🏃‍♂️ Lincoln Park Challenge")
    park_distance = st.slider("Distance (miles):", 0.1, 2.0, 0.8, 0.1)
    if 'jeremiah_speed_mph' in st.session_state and st.session_state.jeremiah_speed_mph > 0:
        jeremiah_time = (park_distance / st.session_state.jeremiah_speed_mph) * 60
        sonic_time = (park_distance / 767) * 3600
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Your Time", f"{jeremiah_time:.1f} min")
        with col2:
            st.metric("Sonic's Time", f"{sonic_time:.1f} sec")
        if st.checkbox("Show Time Chart", key="w1_time"):
            fig, ax = plt.subplots()
            ax.bar(['Jeremiah', 'Sonic'], [jeremiah_time, sonic_time/60], color=['#ff6b6b', '#4ecdc4'])
            ax.set_ylabel('Time (minutes)')
            ax.set_title('Time Comparison')
            st.pyplot(fig)
            plt.close(fig)
    else:
        st.warning("Calculate your speed first.")

    # Quiz: Week 1
    st.subheader("📝 Week 1 Quiz")
    if 'week1_quiz_scores' not in st.session_state:
        st.session_state.week1_quiz_scores = {}
    questions = [
        {"q": "Jeremiah's speed at 5 sec for 40 yd?", "options": ["14.4", "28.8", "57.6"], "correct": "28.8"},
        {"q": "Sonic's time for 0.8 miles at 767 mph?", "options": ["3.7", "5.6", "7.5"], "correct": "3.7"}
    ]
    score = 0
    for i, q in enumerate(questions, 1):
        if i not in st.session_state.week1_quiz_scores:
            st.session_state.week1_quiz_scores[i] = None
        st.write(f"**Q{i}:** {q['q']}")
        answer = st.radio("", q['options'], key=f"w1_q{i}")
        if st.button(f"Submit Q{i}", key=f"w1_s{i}"):
            st.session_state.week1_quiz_scores[i] = answer == q['correct']
            st.rerun()
        if st.session_state.week1_quiz_scores[i] is not None:
            st.write("✅ Correct!" if st.session_state.week1_quiz_scores[i] else "❌ Incorrect.")
            score += 1 if st.session_state.week1_quiz_scores[i] else 0
    if all(v is not None for v in st.session_state.week1_quiz_scores.values()):
        st.write(f"**Score: {score}/{len(questions)}**")

# --- WEEK 2 ---
with week_tabs[1]:
    st.subheader("🏈 Week 2: Football Physics & Quadratics")
    st.markdown("**🎯 Focus:** Quadratic Functions")

    # Trajectory Calculator
    st.markdown("### 🎯 QB Trajectory Analysis")
    velocity = st.slider("Initial velocity (ft/s):", 30, 80, 60)
    angle = st.slider("Launch angle (degrees):", 15, 60, 30)
    height = st.slider("Release height (ft):", 5, 8, 6)
    angle_rad = np.radians(angle)
    v_y = velocity * np.sin(angle_rad)
    if v_y**2 + 2 * 32.2 * height >= 0:
        flight_time = (v_y + np.sqrt(v_y**2 + 2 * 32.2 * height)) / 32.2
        max_height = height + (v_y**2) / (2 * 32.2)
        distance = (velocity * np.cos(angle_rad)) * flight_time
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Max Height", f"{max_height:.1f} ft")
        with col2: st.metric("Distance", f"{distance:.1f} ft")
        with col3: st.metric("Flight Time", f"{flight_time:.2f} sec")
        if st.checkbox("Show Trajectory Chart", key="w2_traj"):
            t = np.linspace(0, flight_time, 100)
            x = (velocity * np.cos(angle_rad)) * t
            y = height + v_y * t - 16.1 * t**2
            fig, ax = plt.subplots()
            ax.plot(x, y, color='#e74c3c')
            ax.set_xlabel('Distance (ft)')
            ax.set_ylabel('Height (ft)')
            ax.set_title('Trajectory')
            st.pyplot(fig)
            plt.close(fig)
    else:
        st.error("Invalid trajectory parameters.")

    # Quiz: Week 2
    st.subheader("📝 Week 2 Quiz")
    if 'week2_quiz_scores' not in st.session_state:
        st.session_state.week2_quiz_scores = {}
    questions = [
        {"q": "Max height for 60 ft/s at 30° from 6 ft?", "options": ["9.3", "12.5", "15.6"], "correct": "9.3"},
        {"q": "Vertex time for h(t) = -16.1t² + 30t + 6?", "options": ["0.9", "1.2", "1.5"], "correct": "0.9"}
    ]
    score = 0
    for i, q in enumerate(questions, 1):
        if i not in st.session_state.week2_quiz_scores:
            st.session_state.week2_quiz_scores[i] = None
        st.write(f"**Q{i}:** {q['q']}")
        answer = st.radio("", q['options'], key=f"w2_q{i}")
        if st.button(f"Submit Q{i}", key=f"w2_s{i}"):
            st.session_state.week2_quiz_scores[i] = answer == q['correct']
            st.rerun()
        if st.session_state.week2_quiz_scores[i] is not None:
            st.write("✅ Correct!" if st.session_state.week2_quiz_scores[i] else "❌ Incorrect.")
            score += 1 if st.session_state.week2_quiz_scores[i] else 0
    if all(v is not None for v in st.session_state.week2_quiz_scores.values()):
        st.write(f"**Score: {score}/{len(questions)}**")

# --- WEEK 3 ---
with week_tabs[2]:
    st.subheader("🥷 Week 3: Naruto Motion & Systems")
    st.markdown("**🎯 Focus:** Systems of Equations")

    # Triple Challenge
    st.markdown("### 🏃‍♂️🛴🦔 Triple Race")
    running_speed = st.session_state.jeremiah_speed_mph if 'jeremiah_speed_mph' in st.session_state else 16.4
    segway_speed = st.slider("Segway speed (mph):", 8, 12, 10)
    race_distance = st.slider("Race distance (miles):", 0.5, 3.0, 1.0)
    head_start = st.slider("Segway head start (min):", 0, 10, 2)
    running_time = race_distance / running_speed * 60 if running_speed > 0 else 0
    segway_time = (race_distance / segway_speed * 60) - head_start if segway_speed > 0 else 0
    sonic_time = race_distance / 767 * 3600
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Running Time", f"{running_time:.1f} min")
    with col2: st.metric("Segway Time", f"{segway_time:.1f} min")
    with col3: st.metric("Sonic Time", f"{sonic_time:.1f} sec")
    if st.checkbox("Show Race Chart", key="w3_race") and running_speed > 0 and segway_speed > 0:
        t = np.linspace(0, max(running_time, segway_time) * 1.2, 100)
        run_dist = (t / 60) * running_speed
        seg_dist = np.maximum(0, ((t + head_start) / 60) * segway_speed)
        sonic_dist = (t / 60) * 767
        fig, ax = plt.subplots()
        ax.plot(t, run_dist, label='Running', color='#3498db')
        ax.plot(t, seg_dist, label='Segway', color='#e67e22')
        ax.plot(t, sonic_dist, label='Sonic', color='#9b59b6')
        ax.set_xlabel('Time (min)')
        ax.set_ylabel('Distance (miles)')
        ax.set_title('Race Progress')
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    # Quiz: Week 3
    st.subheader("📝 Week 3 Quiz")
    if 'week3_quiz_scores' not in st.session_state:
        st.session_state.week3_quiz_scores = {}
    questions = [
        {"q": "Race distance at 6 min running, 4 min segway with 2 min head?", "options": ["40", "50", "60"], "correct": "40"},
        {"q": "Break-even for 3%P vs 2.5%P + 2000?", "options": ["80000", "100000", "120000"], "correct": "80000"}
    ]
    score = 0
    for i, q in enumerate(questions, 1):
        if i not in st.session_state.week3_quiz_scores:
            st.session_state.week3_quiz_scores[i] = None
        st.write(f"**Q{i}:** {q['q']} (miles or $)")
        answer = st.radio("", q['options'], key=f"w3_q{i}")
        if st.button(f"Submit Q{i}", key=f"w3_s{i}"):
            st.session_state.week3_quiz_scores[i] = answer == q['correct']
            st.rerun()
        if st.session_state.week3_quiz_scores[i] is not None:
            st.write("✅ Correct!" if st.session_state.week3_quiz_scores[i] else "❌ Incorrect.")
            score += 1 if st.session_state.week3_quiz_scores[i] else 0
    if all(v is not None for v in st.session_state.week3_quiz_scores.values()):
        st.write(f"**Score: {score}/{len(questions)}**")

# --- WEEK 4 ---
with week_tabs[3]:
    st.subheader("🎓 Week 4: NJIT Bound - College Prep")
    st.markdown("**🎯 Focus:** Inequalities")

    # Readiness Calculator
    st.markdown("### 🎯 College Readiness")
    gpa = st.slider("Current GPA:", 2.0, 4.0, 3.5, 0.1)
    sat = st.slider("Target SAT:", 1000, 1600, 1300, 10)
    njit_gpa, njit_sat = 3.3, 1250
    rpi_gpa, rpi_sat = 3.7, 1350
    njit_ready = gpa >= njit_gpa and sat >= njit_sat
    rpi_ready = gpa >= rpi_gpa and sat >= rpi_sat
    st.write(f"**NJIT:** {'✅ Eligible' if njit_ready else '❌ Not Eligible'}")
    st.write(f"**RPI:** {'✅ Eligible' if rpi_ready else '❌ Not Eligible'}")
    if st.checkbox("Show Readiness Chart", key="w4_ready"):
        fig, ax = plt.subplots()
        ax.scatter([njit_gpa, rpi_gpa], [njit_sat, rpi_sat], label=['NJIT', 'RPI'], color=['#3498db', '#e74c3c'], s=100)
        ax.scatter(gpa, sat, color='#f39c12', label='You', s=150, marker='*')
        ax.set_xlabel('GPA')
        ax.set_ylabel('SAT Score')
        ax.set_title('College Readiness')
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    # Quiz: Week 4
    st.subheader("📝 Week 4 Quiz")
    if 'week4_quiz_scores' not in st.session_state:
        st.session_state.week4_quiz_scores = {}
    questions = [
        {"q": "Eligible for NJIT with GPA 3.5, SAT 1300?", "options": ["Yes", "No"], "correct": "Yes"},
        {"q": "Viable with $400k budget, 8% ROI, $300k at 10%?", "options": ["Yes", "No"], "correct": "Yes"}
    ]
    score = 0
    for i, q in enumerate(questions, 1):
        if i not in st.session_state.week4_quiz_scores:
            st.session_state.week4_quiz_scores[i] = None
        st.write(f"**Q{i}:** {q['q']}")
        answer = st.radio("", q['options'], key=f"w4_q{i}")
        if st.button(f"Submit Q{i}", key=f"w4_s{i}"):
            st.session_state.week4_quiz_scores[i] = answer == q['correct']
            st.rerun()
        if st.session_state.week4_quiz_scores[i] is not None:
            st.write("✅ Correct!" if st.session_state.week4_quiz_scores[i] else "❌ Incorrect.")
            score += 1 if st.session_state.week4_quiz_scores[i] else 0
    if all(v is not None for v in st.session_state.week4_quiz_scores.values()):
        st.write(f"**Score: {score}/{len(questions)}**")

# --- Ask Dr. X Sidebar ---
st.sidebar.title("🤖 Ask Dr. X")
with st.sidebar:
    for msg in st.session_state.chat_history[-5:]:
        st.write(f"**{'You' if msg['role'] == 'user' else 'Dr. X'}:** {msg['content']}")
    user_input = st.text_input("Ask Dr. X:", placeholder="e.g., How to solve equations?")
    if st.button("Send") and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Thinking..."):
            response = ask_drx(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()
    if st.button("Clear Chat"):
        st.session_state.chat_history = [{"role": "assistant", "content": "Hello! I'm Dr. X, ready to help!"}]
        st.rerun()

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666;">
    <h4>🎓 Ready for 10th Grade Math!</h4>
    <p><strong>By Xavier Honablue M.Ed | CognitiveCloud.ai</strong></p>
</div>
""", unsafe_allow_html=True)
