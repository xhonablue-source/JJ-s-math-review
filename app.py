import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time

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

### 🧰 Academic Tools
- **[Ask Dr. X Live Widget](https://ask-drx-730124987572.us-central1.run.app)** (API-enabled sidebar tutor)
- **[Streamlit Dashboard](https://streamlit.io)**: Interactive apps with sliders, animations, and built-in gamification
- **[Algebra Tiles](https://toytheater.com/algebra-tiles/)** – Visual algebra modeling
- **[Graph Paper PDF](https://www.printablepaper.net/category/graph)** – For hand graphing activities
- **[TI-84 Plus Emulator](https://www.ti84calcwiz.com/emulators/)** – Practice calculator functions online
- **[Math Jeopardy Generator](https://jeopardylabs.com/)** – Create custom review games and track leaderboard

### 🎓 College Targeting
- [New Jersey Institute of Technology (NJIT)](https://www.njit.edu/admissions)
- [Rensselaer Polytechnic Institute (RPI)](https://admissions.rpi.edu/undergraduate)
- Include SAT/GPA criteria comparison in Week 4 activities

### 🏠 Real-World Math Connection
- Real estate math in collaboration with Mom's business
    - [Zillow Jersey City Listings](https://www.zillow.com/jersey-city-nj/)
    - [Realtor Commission Calculator](https://www.calculator.net/real-estate-commission-calculator.html)
    - Square footage estimators and ROI predictions
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

# --- Sidebar navigation ---
st.sidebar.title("📚 Navigation")

# Simple navigation menu
selected = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home", "📈 Week 1", "📊 Week 2", "🔄 Week 3", "🎓 Week 4", "🤖 Dr. X", "📊 Progress"]
)

# Gamified Progress Tracker
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 Your Progress")

# Initialize progress in session state
if 'week_progress' not in st.session_state:
    st.session_state.week_progress = {
        'Week 1': 0,
        'Week 2': 0, 
        'Week 3': 0,
        'Week 4': 0
    }

if 'total_points' not in st.session_state:
    st.session_state.total_points = 0

if 'achievements' not in st.session_state:
    st.session_state.achievements = []

# Progress visualization
total_progress = sum(st.session_state.week_progress.values()) / 4
st.sidebar.metric("Overall Progress", f"{total_progress:.0f}%", f"+{st.session_state.total_points} XP")

# Progress bars for each week
for week, progress in st.session_state.week_progress.items():
    st.sidebar.progress(progress/100, text=f"{week}: {progress}%")

# Achievement system
achievements = {
    "🦔 Speed Demon": "Complete Week 1 Linear Functions",
    "🏈 Trajectory Master": "Complete Week 2 Quadratics", 
    "🔄 Systems Solver": "Complete Week 3 Systems",
    "🎓 College Ready": "Complete Week 4 Advanced Topics",
    "💬 Chat Champion": "Ask Dr. X 10 questions",
    "🎯 Perfect Shot": "Optimize a football trajectory"
}

if st.session_state.achievements:
    st.sidebar.markdown("### 🏅 Achievements Unlocked")
    for achievement in st.session_state.achievements:
        st.sidebar.markdown(f"• {achievement}")

# Week Navigation based on menu selection
if selected == "🏠 Home":
    page_selection = "🏠 Home & Introduction"
elif selected == "📈 Week 1":
    page_selection = "📈 Week 1: Linear Functions"
elif selected == "📊 Week 2":
    page_selection = "📊 Week 2: Quadratics"
elif selected == "🔄 Week 3":
    page_selection = "📈 Week 3: Exponential & Radicals"
elif selected == "🎓 Week 4":
    page_selection = "🎓 Week 4: College Prep"
elif selected == "🤖 Dr. X":
    page_selection = "🤖 Ask Dr. X"
else:
    page_selection = "📊 Progress Dashboard"

# Home page
if page_selection == "🏠 Home & Introduction":
    st.markdown("""
    ## 🚀 Welcome to Your Mathematical Journey!
    
    Welcome to MathCraft, Jeremiah! This program is designed specifically for you as you prepare to dominate 10th grade mathematics. Just like how you've grown from that little 5-year-old running through the park with your arms behind you like Sonic, to a 6'2" quarterback commanding the field with your deep voice, your mathematical skills are about to level up in ways that will surprise you.
    
    This program connects math to everything you're passionate about:
    - 🏈 **Football**: Calculating perfect spiral trajectories and field positioning
    - 🦔 **Sonic**: Speed calculations and optimization problems  
    - 🛴 **Segway Adventures**: Using Jersey City hills for slope and rate problems
    - 🏠 **Real Estate**: Working with your mom on market analysis and investments
    - 🎓 **College Prep**: Building skills for NJIT and RPI applications
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="week-card">
            <h3>Week 1: Linear Functions</h3>
            <p>Segway Hills & Quarterback Math</p>
            <small>Slope, rate of change, and real-world applications</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="week-card">
            <h3>Week 3: Exponential Functions</h3>
            <p>Growth & Real Estate Investment</p>
            <small>Compound interest and performance modeling</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="week-card">
            <h3>Week 2: Quadratic Functions</h3>
            <p>Football Trajectories & Sonic Jumps</p>
            <small>Parabolic motion and optimization</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="week-card">
            <h3>Week 4: Advanced Topics</h3>
            <p>NJIT & RPI Preparation</p>
            <small>Statistics, trigonometry, and college readiness</small>
        </div>
        """, unsafe_allow_html=True)

# Week 1 content
elif page_selection == "📈 Week 1: Linear Functions":
    st.title("📈 Week 1: Linear Functions & Real-World Applications")
    
    day = st.selectbox("Choose a day:", 
                      ["Day 1: Segway Hill Challenge", "Day 2: Speed Calculations", 
                       "Day 3: Systems of Equations", "Day 4: Linear Inequalities", "Day 5: Review Project"])
    
    if day == "Day 1: Segway Hill Challenge":
        st.markdown("**📘 IXL Skills Focus:** [U.2 - Solve multi-step linear equations](https://www.ixl.com/math/algebra-1/solve-multi-step-linear-equations)")
        st.markdown("**📚 Common Core:** HSA.CED.A.1, HSA.REI.B.3")
        st.markdown("**🎯 Focus:** Expressions, Equations, and Linear Functions")
        
        # Mathematical Vocabulary and Concepts
        st.markdown("---")
        st.markdown("### 📚 Essential Vocabulary & Concepts")
        
        with st.expander("📖 Week 1 Mathematical Vocabulary"):
            st.markdown("""
            **📐 Linear Equations:**
            - **Coefficient:** The numerical factor of a variable (in 3x, the coefficient is 3)
            - **Variable:** A symbol (usually x or y) that represents an unknown quantity
            - **Constant:** A fixed numerical value that doesn't change
            - **Like Terms:** Terms that have the same variable raised to the same power
            - **Solution:** The value(s) that make an equation true
            
            **📈 Rate of Change & Slope:**
            - **Rate of Change:** How much one quantity changes relative to another
            - **Slope (m):** The steepness of a line, calculated as rise/run or Δy/Δx
            - **Rise:** The vertical change between two points
            - **Run:** The horizontal change between two points
            - **Slope-Intercept Form:** y = mx + b (where m is slope, b is y-intercept)
            
            **📊 Graphing Terms:**
            - **Coordinate Plane:** The x-y plane with horizontal and vertical axes
            - **Ordered Pair:** A point written as (x, y) coordinates
            - **x-intercept:** Where the line crosses the x-axis (y = 0)
            - **y-intercept:** Where the line crosses the y-axis (x = 0)
            - **Domain:** All possible input values (x-values)
            - **Range:** All possible output values (y-values)
            """)
        
        with st.expander("🧮 Essential Formulas & Properties"):
            st.markdown("""
            **Linear Equation Standard Forms:**
            - **Slope-Intercept Form:** y = mx + b
            - **Point-Slope Form:** y - y₁ = m(x - x₁)
            - **Standard Form:** Ax + By = C
            
            **Rate Calculations:**
            - **Speed = Distance ÷ Time**
            - **Average Rate of Change = (y₂ - y₁) ÷ (x₂ - x₁)**
            - **Slope Formula: m = (y₂ - y₁) ÷ (x₂ - x₁)**
            
            **Properties of Equality:**
            - **Addition Property:** If a = b, then a + c = b + c
            - **Subtraction Property:** If a = b, then a - c = b - c
            - **Multiplication Property:** If a = b, then ac = bc
            - **Division Property:** If a = b and c ≠ 0, then a/c = b/c
            """)
        
        # Interactive Sonic Speed Calculator
        st.markdown("---")
        st.markdown("### 🚀 Sonic vs. Jeremiah Speed Challenge")
        
        st.markdown("""
        **🎯 Learning Objective:** Apply rate calculations and linear relationships to compare speeds
        
        **📚 Mathematical Concept:** When we calculate speed, we're finding a **rate of change** - specifically, 
        how distance changes with respect to time. This creates a **linear relationship** because if you travel 
        at constant speed, doubling the time doubles the distance.
        
        **Formula:** Speed = Distance ÷ Time, or v = d/t
        
        **Real-World Connection:** Understanding rates helps quarterbacks calculate timing for plays, 
        helps real estate agents determine property appreciation rates, and helps engineers design optimal systems.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**⚡ Sonic's Canonical Speed:** 767 mph (Speed of Sound)")
            jeremiah_40_time = st.slider("Your 40-yard dash time (seconds):", 4.0, 8.0, 5.5, 0.1)
            
            # Calculate Jeremiah's speed
            jeremiah_speed_mph = (40 * 3600) / (jeremiah_40_time * 5280)
            speed_ratio = 767 / jeremiah_speed_mph
            
            st.metric("Your Speed", f"{jeremiah_speed_mph:.1f} mph")
            st.metric("Sonic is", f"{speed_ratio:.0f}x faster!")
        
        with col2:
            # Create speed comparison graph with Plotly
            fig = go.Figure()
            
            speeds = ['Jeremiah', 'Sonic']
            values = [jeremiah_speed_mph, 767]
            colors = ['#ff6b6b', '#4ecdc4']
            
            fig.add_trace(go.Bar(
                x=speeds,
                y=values,
                marker_color=colors,
                text=[f'{val:.1f} mph' for val in values],
                textposition='auto',
                hovertemplate='<b>%{x}</b><br>Speed: %{y:.1f} mph<extra></extra>'
            ))
            
            fig.update_layout(
                title='Interactive Speed Comparison: Jeremiah vs. Sonic',
                xaxis_title='Character',
                yaxis_title='Speed (mph)',
                height=400,
                showlegend=False,
                hovermode='x'
            )
            
            # Add animation on load
            fig.update_traces(marker_line_width=2, marker_line_color="darkslategrey")
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Mathematical Analysis of Results
        st.markdown("---")
        st.markdown("### 🧠 Mathematical Analysis")
        
        st.markdown(f"""
        **📊 Speed Calculations Explained:**
        
        Your 40-yard dash time: {jeremiah_40_time} seconds
        
        **Step 1:** Convert yards to miles
        - 40 yards ÷ 1,760 yards/mile = {40/1760:.6f} miles
        
        **Step 2:** Convert seconds to hours  
        - {jeremiah_40_time} seconds ÷ 3,600 seconds/hour = {jeremiah_40_time/3600:.6f} hours
        
        **Step 3:** Calculate speed using v = d/t
        - Speed = {40/1760:.6f} miles ÷ {jeremiah_40_time/3600:.6f} hours = {jeremiah_speed_mph:.1f} mph
        
        **📈 Linear Relationship:** If you maintain this speed, the equation for distance traveled is:
        **d = {jeremiah_speed_mph:.1f}t** (where d is in miles, t is in hours)
        
        **🔍 Rate Analysis:** Your rate of {jeremiah_speed_mph:.1f} mph means you cover {jeremiah_speed_mph:.1f} miles 
        every hour, which is a **constant rate of change** - the hallmark of linear functions.
        """)
        
        # Lincoln Park Distance Problem
        st.markdown("---")
        st.markdown("### 🏃‍♂️ Lincoln Park Challenge")
        
        st.markdown("""
        **🎯 Learning Objective:** Solve real-world problems using linear equations and rate calculations
        
        **📚 Mathematical Concept:** This problem demonstrates **direct variation** - as distance increases, 
        time increases proportionally. The relationship between distance and time at constant speed is linear.
        
        **Key Insight:** When speed is constant, time varies directly with distance: t = d/v
        """)
        
        park_distance = st.slider("Lincoln Park distance (miles):", 0.1, 2.0, 0.8, 0.1)
        
        # Calculate times
        jeremiah_time_minutes = (park_distance / jeremiah_speed_mph) * 60
        sonic_time_seconds = (park_distance / 767) * 3600
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Jeremiah's Time", f"{jeremiah_time_minutes:.1f} minutes")
        with col2:
            st.metric("Sonic's Time", f"{sonic_time_seconds:.2f} seconds")
        
        # Mathematical Explanation
        st.markdown(f"""
        **📐 Mathematical Work:**
        
        **For Jeremiah:**
        - Time = Distance ÷ Speed = {park_distance} miles ÷ {jeremiah_speed_mph:.1f} mph = {jeremiah_time_minutes:.3f} hours
        - Converting to minutes: {jeremiah_time_minutes:.3f} hours × 60 = {jeremiah_time_minutes:.1f} minutes
        
        **For Sonic:**  
        - Time = {park_distance} miles ÷ 767 mph = {(park_distance/767):.6f} hours
        - Converting to seconds: {(park_distance/767):.6f} hours × 3,600 = {sonic_time_seconds:.2f} seconds
        
        **🎯 Key Insight:** Both calculations use the same formula (t = d/v), but different units require 
        different conversion factors. This demonstrates the importance of **dimensional analysis** in mathematics.
        """)
        
        # Segway Slope Analysis
        st.markdown("---")
        st.markdown("### 🛴 Segway Slope Analysis")
        st.markdown("""
        **🎯 Learning Objective:** Understand slope as a rate of change and its real-world applications
        
        **📚 Mathematical Concept:** Slope measures the **steepness** of a line and represents the 
        **rate of change** between two variables. In this case, it's the rate at which elevation 
        changes with respect to horizontal distance.
        
        **Real-World Application:** Slope is crucial in engineering, construction, road design, 
        and understanding how physical forces affect motion on inclined surfaces.
        """)
        st.markdown("**Mathematical Connection:** Jersey City hills and rate of change")
        
        rise = st.slider("Hill rise (feet):", 10, 100, 50)
        run = st.slider("Horizontal distance (feet):", 100, 500, 200)
        slope = rise / run
        
        st.markdown(f"""
        **📊 Slope Calculations:**
        
        **Definition:** Slope = Rise ÷ Run = Vertical Change ÷ Horizontal Change
        
        **Calculation:** Slope = {rise} feet ÷ {run} feet = {slope:.3f}
        
        **Interpretations:**
        - **As a Decimal:** {slope:.3f} means for every 1 foot horizontally, elevation rises {slope:.3f} feet
        - **As a Percentage:** {slope * 100:.1f}% grade (used in road construction)
        - **As a Ratio:** {rise}:{run} (simplified ratio of rise to run)
        - **As an Angle:** {np.degrees(np.arctan(slope)):.1f}° from horizontal
        
        **📐 Mathematical Properties:**
        - **Positive slope:** Line rises from left to right (uphill)
        - **Negative slope:** Line falls from left to right (downhill)  
        - **Zero slope:** Horizontal line (flat ground)
        - **Undefined slope:** Vertical line (cliff face)
        """)
        
        # Engineering Applications
        st.markdown(f"""
        **⚙️ Engineering Applications:**
        - **Road Grade Standards:** Most highways limit grades to 6% ({slope * 100:.1f}% {'exceeds' if slope > 0.06 else 'meets'} this standard)
        - **ADA Compliance:** Wheelchair ramps must have slopes ≤ 1:12 or 8.33% 
        - **Segway Performance:** Steeper slopes require more power and reduce speed/range
        """)
        
        st.markdown(f"**Slope = Rise/Run = {rise}/{run} = {slope:.3f}**")
        st.markdown(f"**Slope percentage: {slope * 100:.1f}%**")
        
        # Create slope visualization with interactive Plotly
        fig = go.Figure()
        x_vals = np.linspace(0, run, 100)
        y_vals = slope * x_vals
        
        # Main slope line
        fig.add_trace(go.Scatter(
            x=x_vals, 
            y=y_vals, 
            mode='lines',
            name=f'Hill Profile (slope = {slope:.3f})',
            line=dict(color='#2ecc71', width=4),
            fill='tonexty',
            fillcolor='rgba(46, 204, 113, 0.3)',
            hovertemplate='Distance: %{x:.0f} ft<br>Height: %{y:.0f} ft<extra></extra>'
        ))
        
        # Add rise and run indicators
        fig.add_trace(go.Scatter(
            x=[0, run, run], 
            y=[0, 0, rise], 
            mode='lines+markers+text',
            name='Rise/Run',
            line=dict(color='red', width=2, dash='dash'),
            marker=dict(size=8, color='red'),
            text=['Start', f'Run: {run} ft', f'Rise: {rise} ft'],
            textposition=['bottom center', 'bottom center', 'middle right'],
            hoverinfo='skip'
        ))
        
        fig.update_layout(
            title=f'Interactive Jersey City Hill Profile<br>Slope = {slope:.3f} ({slope*100:.1f}% grade)',
            xaxis_title='Horizontal Distance (feet)',
            yaxis_title='Vertical Rise (feet)',
            height=500,
            showlegend=True,
            hovermode='x unified'
        )
        
        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Interactive slope calculator
        st.markdown("---")
        st.markdown("### 🎮 Interactive Slope Challenge")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            challenge_rise = st.number_input("Challenge: Enter rise (ft):", min_value=1, max_value=200, value=75)
        with col2:
            challenge_run = st.number_input("Enter run (ft):", min_value=10, max_value=1000, value=300)
        with col3:
            user_guess = st.number_input("Guess the slope:", min_value=0.0, max_value=2.0, value=0.25, step=0.001, format="%.3f")
        
        actual_slope = challenge_rise / challenge_run
        error = abs(user_guess - actual_slope)
        
        if st.button("Check My Answer! 🎯"):
            if error < 0.001:
                st.success(f"🎉 Perfect! Slope = {actual_slope:.3f}")
                st.balloons()
                # Award points
                st.session_state.total_points += 10
                if "🎯 Slope Master" not in st.session_state.achievements:
                    st.session_state.achievements.append("🎯 Slope Master")
            elif error < 0.01:
                st.success(f"👍 Very close! Actual slope = {actual_slope:.3f}, you guessed {user_guess:.3f}")
                st.session_state.total_points += 5
            else:
                st.error(f"❌ Try again! Actual slope = {actual_slope:.3f}")
                st.markdown("💡 **Hint:** Remember, slope = rise ÷ run")

# Week 2 content
elif page_selection == "📊 Week 2: Quadratics":
    st.subheader("🏈 Week 2: Football Physics & Quadratics")
    
    st.markdown("**📘 IXL Skills Focus:** [J.7 - Graph parabolas](https://www.ixl.com/math/algebra-1/graph-a-quadratic-function)")
    st.markdown("**📚 Common Core:** HSA.REI.B.4")
    st.markdown("**🎯 Focus:** Quadratic Functions and Vertex Form")
    
    # Mathematical Vocabulary and Concepts for Week 2
    with st.expander("📖 Week 2 Mathematical Vocabulary"):
        st.markdown("""
        **📊 Quadratic Functions:**
        - **Quadratic Function:** A function of the form f(x) = ax² + bx + c where a ≠ 0
        - **Parabola:** The U-shaped curve that is the graph of a quadratic function
        - **Vertex:** The highest or lowest point on a parabola
        - **Axis of Symmetry:** The vertical line that divides the parabola into two mirror images
        - **Discriminant:** The expression b² - 4ac that determines the nature of solutions
        
        **🎯 Projectile Motion:**
        - **Initial Velocity:** The starting speed and direction of a projectile
        - **Launch Angle:** The angle at which a projectile is released
        - **Maximum Height:** The highest point reached by a projectile
        - **Range:** The horizontal distance traveled by a projectile
        - **Time of Flight:** The total time a projectile remains in the air
        
        **📐 Quadratic Forms:**
        - **Standard Form:** f(x) = ax² + bx + c
        - **Vertex Form:** f(x) = a(x - h)² + k where (h,k) is the vertex
        - **Factored Form:** f(x) = a(x - r₁)(x - r₂) where r₁ and r₂ are roots
        """)
    
    with st.expander("🧮 Quadratic Formulas & Properties"):
        st.markdown("""
        **Essential Quadratic Formulas:**
        - **Quadratic Formula:** x = (-b ± √(b² - 4ac)) / 2a
        - **Vertex x-coordinate:** x = -b / 2a
        - **Axis of Symmetry:** x = -b / 2a
        - **Discriminant:** Δ = b² - 4ac
        
        **Projectile Motion Formulas:**
        - **Height:** h(t) = -16t² + v₀t + h₀ (in feet)
        - **Horizontal Distance:** x(t) = v₀cos(θ)t
        - **Vertical Velocity:** vᵧ(t) = v₀sin(θ) - 32t
        - **Maximum Height:** h_max = h₀ + (v₀sin(θ))² / 64
        
        **Key Properties:**
        - If a > 0, parabola opens upward (has minimum)
        - If a < 0, parabola opens downward (has maximum)  
        - |a| determines how wide or narrow the parabola is
        """)
    
    # Football Trajectory Calculator
    st.markdown("---")
    st.markdown("### 🎯 Perfect Spiral Trajectory Analysis")
    
    st.markdown("""
    **🎯 Learning Objective:** Model projectile motion using quadratic functions and analyze optimization
    
    **📚 Mathematical Concept:** Projectile motion follows a **parabolic path** described by quadratic 
    functions. The height of any projectile (ignoring air resistance) can be modeled by:
    
    **h(t) = -16t² + v₀t + h₀**
    
    Where:
    - h(t) = height at time t (feet)
    - -16 = half the acceleration due to gravity (ft/s²)
    - v₀ = initial vertical velocity (ft/s)
    - h₀ = initial height (feet)
    - t = time (seconds)
    
    **Why Quadratic?** Gravity causes constant acceleration, and when you integrate constant 
    acceleration twice, you get a quadratic (second-degree) function.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        initial_velocity = st.slider("Initial velocity (ft/s):", 30, 80, 60)
        launch_angle = st.slider("Launch angle (degrees):", 15, 60, 30)
        initial_height = st.slider("Release height (feet):", 5, 8, 6)
        
        # Convert angle to radians
        angle_rad = np.radians(launch_angle)
        
        # Calculate velocity components
        v_x = initial_velocity * np.cos(angle_rad)
        v_y = initial_velocity * np.sin(angle_rad)
        
        # Calculate flight time
        flight_time = (v_y + np.sqrt(v_y**2 + 2*32.2*initial_height)) / 32.2
        
        # Calculate maximum height and distance
        max_height = initial_height + (v_y**2) / (2*32.2)
        max_distance = v_x * flight_time
        
        st.metric("Maximum Height", f"{max_height:.1f} feet")
        st.metric("Distance", f"{max_distance:.1f} feet")
        st.metric("Flight Time", f"{flight_time:.2f} seconds")
    
    with col2:
        # Create 3D trajectory plot with Plotly
        t_vals = np.linspace(0, flight_time, 100)
        x_vals = v_x * t_vals
        y_vals = initial_height + v_y * t_vals - 0.5 * 32.2 * t_vals**2
        
        # Only show positive heights
        valid_indices = y_vals >= 0
        x_vals = x_vals[valid_indices]
        y_vals = y_vals[valid_indices]
        t_vals = t_vals[valid_indices]
        
        # Create animated trajectory
        fig = go.Figure()
        
        # Full trajectory path
        fig.add_trace(go.Scatter(
            x=x_vals, 
            y=y_vals,
            mode='lines',
            name='Flight Path',
            line=dict(color='#e74c3c', width=4),
            hovertemplate='Distance: %{x:.1f} ft<br>Height: %{y:.1f} ft<extra></extra>'
        ))
        
        # Mark key points
        # Launch point
        fig.add_trace(go.Scatter(
            x=[0], y=[initial_height],
            mode='markers+text',
            marker=dict(size=12, color='green', symbol='star'),
            text=['Launch'],
            textposition='top center',
            name='Launch Point',
            hovertemplate='Launch Point<br>Height: %{y:.1f} ft<extra></extra>'
        ))
        
        # Peak point
        vertex_x = max_distance / 2
        fig.add_trace(go.Scatter(
            x=[vertex_x], y=[max_height],
            mode='markers+text',
            marker=dict(size=12, color='gold', symbol='diamond'),
            text=['Peak'],
            textposition='top center',
            name='Maximum Height',
            hovertemplate='Peak<br>Distance: %{x:.1f} ft<br>Height: %{y:.1f} ft<extra></extra>'
        ))
        
        # Landing point
        fig.add_trace(go.Scatter(
            x=[max_distance], y=[0],
            mode='markers+text',
            marker=dict(size=12, color='red', symbol='x'),
            text=['Landing'],
            textposition='top center',
            name='Landing Point',
            hovertemplate='Landing Point<br>Distance: %{x:.1f} ft<extra></extra>'
        ))
        
        # Add field markings every 10 yards
        yard_lines = np.arange(0, max_distance + 30, 30)  # Every 10 yards (30 feet)
        for yard in yard_lines:
            fig.add_vline(x=yard, line_dash="dot", line_color="gray", opacity=0.5)
        
        fig.update_layout(
            title=f'🏈 Interactive Football Trajectory Analysis<br>θ={launch_angle}°, v₀={initial_velocity} ft/s',
            xaxis_title='Horizontal Distance (feet)',
            yaxis_title='Height (feet)',
            height=500,
            showlegend=True,
            hovermode='x unified'
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', range=[0, max(y_vals) * 1.1])
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Animated trajectory simulation
    st.markdown("---")
    st.markdown("### 🎬 Trajectory Animation")
    
    if st.button("🚀 Launch Football Animation"):
        animation_placeholder = st.empty()
        progress_bar = st.progress(0)
        
        # Animation parameters
        animation_steps = 50
        
        for step in range(animation_steps + 1):
            progress = step / animation_steps
            current_time = progress * flight_time
            
            # Calculate position at current time
            if current_time <= flight_time:
                current_x = v_x * current_time
                current_y = max(0, initial_height + v_y * current_time - 0.5 * 32.2 * current_time**2)
            else:
                current_x = max_distance
                current_y = 0
            
            # Create animation frame
            anim_fig = go.Figure()
            
            # Full trajectory (faded)
            anim_fig.add_trace(go.Scatter(
                x=x_vals, y=y_vals,
                mode='lines',
                line=dict(color='lightgray', width=2),
                name='Full Path',
                showlegend=False
            ))
            
            # Current position (highlighted)
            anim_fig.add_trace(go.Scatter(
                x=[current_x], y=[current_y],
                mode='markers',
                marker=dict(size=20, color='red', symbol='circle'),
                name='Football',
                showlegend=False
            ))
            
            # Trajectory so far (colored)
            if step > 0:
                t_so_far = np.linspace(0, current_time, step)
                x_so_far = v_x * t_so_far
                y_so_far = np.maximum(0, initial_height + v_y * t_so_far - 0.5 * 32.2 * t_so_far**2)
                
                anim_fig.add_trace(go.Scatter(
                    x=x_so_far, y=y_so_far,
                    mode='lines',
                    line=dict(color='#e74c3c', width=4),
                    name='Flight Path',
                    showlegend=False
                ))
            
            anim_fig.update_layout(
                title=f'🏈 Football in Flight - Time: {current_time:.2f}s<br>Position: ({current_x:.1f}, {current_y:.1f}) ft',
                xaxis_title='Distance (feet)',
                yaxis_title='Height (feet)',
                height=400,
                xaxis=dict(range=[0, max_distance * 1.1]),
                yaxis=dict(range=[0, max_height * 1.2])
            )
            
            animation_placeholder.plotly_chart(anim_fig, use_container_width=True)
            progress_bar.progress(progress)
            time.sleep(0.1)
        
        st.success("🎯 Touchdown! Animation complete!")
        
        # Award achievement points
        st.session_state.total_points += 15
        if "🏈 Trajectory Master" not in st.session_state.achievements:
            st.session_state.achievements.append("🏈 Trajectory Master")
        st.session_state.week_progress['Week 2'] = min(100, st.session_state.week_progress['Week 2'] + 25)

# Week 3 content  
elif page_selection == "📈 Week 3: Exponential & Radicals":
    st.subheader("📈 Week 3: Exponential and Radical Functions")
    
    st.markdown("**📘 IXL Skills Focus:** [M.1 - Exponential functions](https://www.ixl.com/math/algebra-1/exponential-functions)")
    st.markdown("**📚 Common Core:** HSF.LE.A.2")
    st.markdown("**🎯 Focus:** Growth, Decay, and Real Estate Investment")
    
    # Interactive exponential growth visualization
    st.markdown("---")
    st.markdown("### 📈 Interactive Exponential Growth Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        growth_type = st.selectbox("Choose growth scenario:", 
                                 ["Athletic Performance", "Real Estate Investment", "Population Growth", "Compound Interest"])
        
        if growth_type == "Athletic Performance":
            initial_value = st.slider("Initial throwing distance (yards):", 20, 60, 35)
            growth_rate = st.slider("Weekly improvement rate (%):", 1, 15, 5)
            time_period = st.slider("Training weeks:", 1, 52, 20)
            y_label = "Throwing Distance (yards)"
            
        elif growth_type == "Real Estate Investment":
            initial_value = st.slider("Initial property value ($):", 200000, 800000, 400000, 10000)
            growth_rate = st.slider("Annual appreciation rate (%):", 1, 12, 4)
            time_period = st.slider("Investment years:", 1, 30, 10)
            y_label = "Property Value ($)"
            
        elif growth_type == "Population Growth":
            initial_value = st.slider("Initial population:", 1000, 100000, 10000)
            growth_rate = st.slider("Annual growth rate (%):", 0.5, 8.0, 2.5)
            time_period = st.slider("Years:", 1, 50, 25)
            y_label = "Population"
            
        else:  # Compound Interest
            initial_value = st.slider("Initial investment ($):", 1000, 50000, 10000, 500)
            growth_rate = st.slider("Annual interest rate (%):", 1, 15, 7)
            time_period = st.slider("Investment years:", 1, 40, 20)
            y_label = "Account Value ($)"
    
    with col2:
        # Calculate exponential growth
        time_vals = np.linspace(0, time_period, 100)
        growth_decimal = growth_rate / 100
        exponential_values = initial_value * ((1 + growth_decimal) ** time_vals)
        linear_values = initial_value + (initial_value * growth_decimal * time_vals)
        
        # Create interactive comparison plot
        fig = go.Figure()
        
        # Exponential growth
        fig.add_trace(go.Scatter(
            x=time_vals, y=exponential_values,
            mode='lines',
            name=f'Exponential Growth ({growth_rate}%)',
            line=dict(color='#e74c3c', width=4),
            hovertemplate=f'Time: %{{x:.1f}}<br>{y_label}: %{{y:,.0f}}<extra></extra>'
        ))
        
        # Linear growth comparison
        fig.add_trace(go.Scatter(
            x=time_vals, y=linear_values,
            mode='lines',
            name=f'Linear Growth (for comparison)',
            line=dict(color='#3498db', width=3, dash='dash'),
            hovertemplate=f'Time: %{{x:.1f}}<br>{y_label}: %{{y:,.0f}}<extra></extra>'
        ))
        
        # Mark key points
        final_exponential = initial_value * ((1 + growth_decimal) ** time_period)
        final_linear = initial_value + (initial_value * growth_decimal * time_period)
        
        fig.add_trace(go.Scatter(
            x=[time_period], y=[final_exponential],
            mode='markers+text',
            marker=dict(size=12, color='red', symbol='star'),
            text=[f'Final: {final_exponential:,.0f}'],
            textposition='top center',
            name='Exponential End Point',
            showlegend=False
        ))
        
        time_unit = "weeks" if growth_type == "Athletic Performance" else "years"
        fig.update_layout(
            title=f'📊 {growth_type}: Exponential vs Linear Growth',
            xaxis_title=f'Time ({time_unit})',
            yaxis_title=y_label,
            height=500,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Show mathematical analysis
        difference = final_exponential - final_linear
        st.success(f"""
        **📊 Growth Analysis:**
        - **Exponential Final Value:** {final_exponential:,.0f}
        - **Linear Final Value:** {final_linear:,.0f}
        - **Exponential Advantage:** {difference:,.0f} ({((difference/final_linear)*100):.1f}% more!)
        """)

# Week 4 content
elif page_selection == "🎓 Week 4: College Prep":
    st.subheader("🎓 Week 4: Advanced Topics and College Preparation")
    
    st.markdown("**📘 IXL Skills Focus:** [Statistics and Data Analysis](https://www.ixl.com/math/algebra-1/statistics)")
    st.markdown("**📚 Common Core:** HSS.ID.B.6")
    st.markdown("**🎯 Focus:** Data Analysis, College Readiness, and Future Planning")
    
    # Interactive college readiness dashboard
    st.markdown("---")
    st.markdown("### 🎯 Interactive NJIT & RPI Readiness Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_gpa = st.slider("Current GPA:", 2.0, 4.0, 3.5, 0.1)
        target_sat = st.slider("Target SAT Score:", 1000, 1600, 1300, 10)
        extracurriculars = st.slider("Extracurricular Activities:", 0, 10, 4)
        leadership_roles = st.slider("Leadership Positions:", 0, 5, 2)
        
        # NJIT and RPI requirements (approximate)
        njit_gpa_min = 3.3
        njit_sat_min = 1250
        rpi_gpa_min = 3.7
        rpi_sat_min = 1350
    
    with col2:
        # Create interactive college readiness radar chart
        categories = ['GPA', 'SAT Score', 'Extracurriculars', 'Leadership', 'Overall Score']
        
        # Normalize scores to 0-100 scale
        gpa_score = min(100, (current_gpa / 4.0) * 100)
        sat_score = min(100, ((target_sat - 1000) / 600) * 100)
        extra_score = min(100, (extracurriculars / 8) * 100)
        leadership_score = min(100, (leadership_roles / 4) * 100)
        overall_score = (gpa_score + sat_score + extra_score + leadership_score) / 4
        
        current_scores = [gpa_score, sat_score, extra_score, leadership_score, overall_score]
        
        # NJIT requirements normalized
        njit_gpa_score = (njit_gpa_min / 4.0) * 100
        njit_sat_score = ((njit_sat_min - 1000) / 600) * 100
        njit_scores = [njit_gpa_score, njit_sat_score, 60, 50, 60]  # Estimated requirements
        
        # RPI requirements normalized  
        rpi_gpa_score = (rpi_gpa_min / 4.0) * 100
        rpi_sat_score = ((rpi_sat_min - 1000) / 600) * 100
        rpi_scores = [rpi_gpa_score, rpi_sat_score, 75, 65, 75]  # Estimated requirements
        
        fig = go.Figure()
        
        # Current profile
        fig.add_trace(go.Scatterpolar(
            r=current_scores + [current_scores[0]],  # Close the polygon
            theta=categories + [categories[0]],
            fill='toself',
            name='Your Current Profile',
            line_color='#3498db',
            fillcolor='rgba(52, 152, 219, 0.3)'
        ))
        
        # NJIT requirements
        fig.add_trace(go.Scatterpolar(
            r=njit_scores + [njit_scores[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name='NJIT Requirements',
            line_color='#2ecc71',
            fillcolor='rgba(46, 204, 113, 0.2)'
        ))
        
        # RPI requirements
        fig.add_trace(go.Scatterpolar(
            r=rpi_scores + [rpi_scores[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name='RPI Requirements',
            line_color='#e74c3c',
            fillcolor='rgba(231, 76, 60, 0.2)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="🎯 College Readiness Radar",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Ask Dr. X page with enhanced features
elif page_selection == "🤖 Ask Dr. X":
    st.title("🤖 Ask Dr. X - Your AI Math Tutor")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
        <h3>👓 Dr. X is here to help!</h3>
        <p>Ask me anything about math - whether it's quadratic equations, football trajectories, 
        real estate calculations, or college prep questions. I'm specifically tuned to help with 
        your interests in football, Sonic, and real estate!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display chat history with better formatting
    chat_container = st.container()
    with chat_container:
        for i, message in enumerate(st.session_state.chat_history):
            if message["role"] == "user":
                st.markdown(f"""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 10px; margin: 5px 0;">
                    <strong>🏈 You:</strong> {message['content']}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: #f3e5f5; padding: 10px; border-radius: 10px; margin: 5px 0;">
                    <strong>👓 Dr. X:</strong> {message['content']}
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    user_input = st.text_input("Ask Dr. X:", placeholder="e.g., How do I find the vertex of a parabola?")
    
    if st.button("Send 📤") and user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get Dr. X response
        with st.spinner("Dr. X is thinking..."):
            response = ask_drx(user_input)
        
        # Add response
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello Jeremiah! I'm Dr. X, your AI math coach. Ready to tackle some math problems?"}
        ]
        st.rerun()

# Progress Dashboard
elif page_selection == "📊 Progress Dashboard":
    st.title("📊 MathCraft Progress Dashboard")
    
    # Overall progress summary
    col1, col2, col3, col4 = st.columns(4)
    
    total_progress = sum(st.session_state.week_progress.values()) / 4
    
    with col1:
        st.metric("Overall Progress", f"{total_progress:.0f}%", "🎯")
    with col2:
        st.metric("Total XP", st.session_state.total_points, "⭐")
    with col3:
        st.metric("Achievements", len(st.session_state.achievements), "🏅")
    with col4:
        completed_weeks = sum(1 for progress in st.session_state.week_progress.values() if progress >= 100)
        st.metric("Weeks Completed", completed_weeks, "✅")
    
    # Progress visualization
    st.markdown("---")
    st.markdown("### 📈 Weekly Progress Tracking")
    
    # Create interactive progress chart
    weeks = list(st.session_state.week_progress.keys())
    progress_values = list(st.session_state.week_progress.values())
    
    fig = go.Figure()
    
    # Progress bars
    fig.add_trace(go.Bar(
        x=weeks,
        y=progress_values,
        marker_color=['#2ecc71' if p >= 100 else '#3498db' if p >= 50 else '#e74c3c' for p in progress_values],
        text=[f'{p}%' for p in progress_values],
        textposition='auto',
        hovertemplate='Week: %{x}<br>Progress: %{y}%<extra></extra>'
    ))
    
    fig.update_layout(
        title='📊 Weekly Progress Overview',
        xaxis_title='Week',
        yaxis_title='Completion Percentage',
        height=400,
        yaxis=dict(range=[0, 120])
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <h4>🎓 Ready to Dominate 10th Grade Math!</h4>
    <p><em>"Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding." - William Paul Thurston</em></p>
    <p><strong>Built for Jeremiah by Xavier Honablue M.Ed | CognitiveCloud.ai</strong></p>
    <p>🎯 <strong>Target Universities:</strong> NJIT & RPI | 🏈 <strong>Position:</strong> Quarterback | 🏠 <strong>Real Estate Math with Mom</strong></p>
</div>
""", unsafe_allow_html=True)
