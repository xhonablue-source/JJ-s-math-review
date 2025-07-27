import streamlit as st
import requests

# Configure the page
st.set_page_config(page_title="MathCraft: Quest for the Quarterback Crown", page_icon="🏈", layout="wide")

# Header
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(45deg, #1e3c72, #2a5298); color: white; border-radius: 12px;'>
    <h1>🏈 MathCraft: Quest for the Quarterback Crown</h1>
    <p style='font-size:1.2rem;'>A 4-Week Challenge-Based Math Journey for Jeremiah Erskine</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📚 Challenge Levels")
section = st.sidebar.radio("Choose Your Level", [
    "🏋️ Level 1: Sonic Dash Algebra Maze",
    "🎯 Level 2: QB Launch Trajectories",
    "⚡ Level 3: Naruto Systems Faceoff",
    "🎓 Level 4: NJIT College Ready Quest",
    "🤖 Ask Dr. X"
])

# Dr. X API call
def ask_drx(message):
    try:
        res = requests.post('https://ask-drx-730124987572.us-central1.run.app',
                            json={'message': message},
                            timeout=20)
        if res.status_code == 200:
            return res.json().get('reply', "I didn't catch that.")
        return "Dr. X is offline right now."
    except:
        return "Error connecting to Dr. X."

# Level 1
if section == "🏋️ Level 1: Sonic Dash Algebra Maze":
    st.header("🔹 Sonic Dash Algebra Maze")
    st.markdown("""
    **Welcome Speedster!**  
    Sonic needs your help solving linear equations to unlock speed boosts and finish the maze!
    """)
    st.markdown("#### 🎮 Solve to Boost:")
    eq = st.text_input("Solve for x: 3x - 7 = 11")
    if eq.strip() == "6":
        st.success("Speed boost unlocked! Sonic blazes ahead! ⚡")
    elif eq:
        st.error("Try again. Sonic’s waiting...")

# Level 2
elif section == "🎯 Level 2: QB Launch Trajectories":
    st.header("🏈 Quarterback Launch Challenge")
    st.markdown("""
    **Mission:** Launch the football with optimal height and distance using parabolic motion.
    """)
    v0 = st.slider("Initial Velocity (ft/s)", 10, 100, 50)
    h0 = st.slider("Initial Height (ft)", 0, 10, 3)
    t = st.slider("Time (s)", 0, 5, 2)
    height = -16 * (t**2) + v0 * t + h0
    st.metric("📏 Estimated Height of Throw", f"{height:.2f} ft")

# Level 3
elif section == "⚡ Level 3: Naruto Systems Faceoff":
    st.header("⚡ Motion Match-Up: Naruto vs Jeremiah")
    st.markdown("""
    Naruto-style Jeremiah vs Sonic in a race. Use equations to figure out who's faster!
    """)
    st.markdown("#### Sonic: y = 767t\n#### Jeremiah: y = 20t + 100")
    user_guess = st.radio("Who wins after 5 seconds?", ["Sonic", "Jeremiah"])
    if user_guess == "Sonic":
        st.success("Correct! Sonic breaks the sound barrier.")
    elif user_guess:
        st.error("Jeremiah gave a fight — but Sonic wins this time!")

# Level 4
elif section == "🎓 Level 4: NJIT College Ready Quest":
    st.header("🎓 College Ready Quest")
    st.markdown("Use math to unlock NJIT admission requirements!")
    gpa = st.slider("Your GPA", 2.0, 4.0, 3.5)
    sat = st.slider("Your SAT Score", 800, 1600, 1200)
    if gpa >= 3.3 and sat >= 1200:
        st.success("🎓 Admission Badge Unlocked: NJIT Ready!")
    else:
        st.warning("Raise GPA or SAT to unlock admission.")

# Ask Dr. X tab
elif section == "🤖 Ask Dr. X":
    st.subheader("🤖 Ask Dr. X - Your AI Math Coach")
    query = st.text_input("Ask me anything about math:")
    if query:
        with st.spinner("Dr. X is thinking..."):
            reply = ask_drx(query)
        st.success(reply)
