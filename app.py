import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
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
    # NJIT/Jersey City logo placeholder
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

Welcome, **Future NJIT Engineer**! This MathCraft program transforms 9th grade math review into an epic quest connecting your passions—quarterback mechanics, Sonic speed, Segway adventures, and real estate success with Mom—into mathematical mastery.

---

### 🎯 Program Goal:
Prepare Jeremiah for a confident and successful 10th grade math experience by reinforcing foundational 9th grade skills through a personalized, interest-based curriculum rooted in Common Core standards.

### 🧑🏿‍🏫 Who is Dr. X?
Dr. X is not a robot 🤓. He's modeled after a real Black educator — Xavier Honablue M.Ed — complete with glasses, deep voice, and a passion for helping students succeed. Think of him as your personal sideline coach for math.
""")

# Common Core Standards Alignment
st.info("📚 **Common Core Alignment:** This program addresses High School Algebra standards including creating equations (HSA.CED), reasoning with equations (HSA.REI), and building functions (HSF.BF) through real-world applications.")

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
    st.success(f"Welcome, {name} the {position}! Ready to dominate 10th grade math!")

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
        {"role": "assistant", "content": "Hello Jeremiah! I'm Dr. X, your AI math coach. Whether you need help with quadratic equations for football trajectories, linear functions for real estate analysis, or systems of equations for game strategy, I'm here to help you succeed!"}
    ]

# Dr. X API function
def ask_drx(message):
    try:
        # In a real implementation, this would call an API
        # For now, we'll simulate a response
        if "equation" in message.lower():
            return "To solve this equation, remember to isolate the variable by performing the same operations on both sides."
        elif "function" in message.lower():
            return "Functions describe relationships between inputs and outputs. Think about how your quarterback throw distance relates to the angle and force applied!"
        elif "graph" in message.lower():
            return "When graphing, remember that each point represents a solution to your equation. For football trajectories, this shows the path of the ball!"
        else:
            return "Great question! Let's break this down step by step. What specific part of the problem are you struggling with?"
    except Exception as e:
        return f"I'm having trouble connecting right now. Please try again later. Error: {str(e)}"

# Display chat interface
st.subheader("💬 Ask Dr. X for Math Help")
st.markdown("Need help with a problem? Dr. X is here to guide you!")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**Dr. X:** {message['content']}")

# Chat input
user_input = st.text_input("Type your math question here:", key="user_question")
if st.button("Ask Dr. X"):
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get response from Dr. X
        response = ask_drx(user_input)
        
        # Add Dr. X response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Clear input
        st.experimental_rerun()

# --- Footer ---
st.markdown("---")
st.markdown("© 2023 CognitiveCloud.AI | Personalized Math Education")
