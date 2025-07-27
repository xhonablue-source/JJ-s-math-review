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
    
    # IXL Integration
    st.markdown("**📘 IXL Skills Focus:** [U.2 - Solve multi-step linear equations](https://www.ixl.com/math/algebra-1/solve-multi-step-linear-equations)")
    st.markdown("**📚 Common Core:** HSA.CED.A.1, HSA.REI.B.3")
    st.markdown("**🎯 Focus:** Expressions, Equations, and Linear Functions")
    
    # Interactive Sonic Speed Calculator
    st.markdown("---")
    st.markdown("### 🚀 Sonic vs. Jeremiah Speed Challenge")
    
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
        # Create speed comparison graph
        fig, ax = plt.subplots(figsize=(10, 6))
        speeds = ['Jeremiah', 'Sonic']
        values = [jeremiah_speed_mph, 767]
        colors = ['#ff6b6b', '#4ecdc4']
        
        bars = ax.bar(speeds, values, color=colors)
        ax.set_ylabel('Speed (mph)')
        ax.set_title('Speed Comparison: Jeremiah vs. Sonic')
        ax.set_ylim(0, 800)
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 10,
                   f'{value:.1f} mph', ha='center', va='bottom', fontweight='bold')
        
        st.pyplot(fig)
    
    # Lincoln Park Distance Problem
    st.markdown("---")
    st.markdown("### 🏃‍♂️ Lincoln Park Challenge")
    park_distance = st.slider("Lincoln Park distance (miles):", 0.1, 2.0, 0.8, 0.1)
    
    # Calculate times
    jeremiah_time_minutes = (park_distance / jeremiah_speed_mph) * 60
    sonic_time_seconds = (park_distance / 767) * 3600
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Jeremiah's Time", f"{jeremiah_time_minutes:.1f} minutes")
    with col2:
        st.metric("Sonic's Time", f"{sonic_time_seconds:.2f} seconds")
    
    # Segway Slope Analysis
    st.markdown("---")
    st.markdown("### 🛴 Segway Slope Analysis")
    st.markdown("**Real-World Application:** Jersey City hills and rate of change")
    
    rise = st.slider("Hill rise (feet):", 10, 100, 50)
    run = st.slider("Horizontal distance (feet):", 100, 500, 200)
    slope = rise / run
    
    st.markdown(f"**Slope = Rise/Run = {rise}/{run} = {slope:.3f}**")
    st.markdown(f"**Slope percentage: {slope * 100:.1f}%**")
    
    # Create slope visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    x_vals = np.linspace(0, run, 100)
    y_vals = slope * x_vals
    
    ax.plot(x_vals, y_vals, linewidth=3, color='#2ecc71')
    ax.fill_between(x_vals, y_vals, alpha=0.3, color='#2ecc71')
    ax.set_xlabel('Horizontal Distance (feet)')
    ax.set_ylabel('Vertical Rise (feet)')
    ax.set_title(f'Jersey City Hill Profile (Slope = {slope:.3f})')
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)

# --- WEEK 2 ---
with week_tabs[1]:
    st.subheader("🏈 Week 2: Football Physics & Quadratics")
    
    st.markdown("**📘 IXL Skills Focus:** [J.7 - Graph parabolas](https://www.ixl.com/math/algebra-1/graph-a-quadratic-function)")
    st.markdown("**📚 Common Core:** HSA.REI.B.4")
    st.markdown("**🎯 Focus:** Quadratic Functions and Vertex Form")
    
    # Football Trajectory Calculator
    st.markdown("---")
    st.markdown("### 🎯 Perfect Spiral Trajectory Analysis")
    
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
        # Create trajectory plot
        t_vals = np.linspace(0, flight_time, 100)
        x_vals = v_x * t_vals
        y_vals = initial_height + v_y * t_vals - 0.5 * 32.2 * t_vals**2
        
        # Only show positive heights
        valid_indices = y_vals >= 0
        x_vals = x_vals[valid_indices]
        y_vals = y_vals[valid_indices]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_vals, y_vals, linewidth=3, color='#e74c3c')
        ax.fill_between(x_vals, y_vals, alpha=0.3, color='#e74c3c')
        ax.set_xlabel('Horizontal Distance (feet)')
        ax.set_ylabel('Height (feet)')
        ax.set_title(f'Football Trajectory (θ={launch_angle}°, v₀={initial_velocity} ft/s)')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, max(y_vals) * 1.1)
        
        # Mark maximum height
        vertex_x = max_distance / 2
        ax.plot(vertex_x, max_height, 'ro', markersize=8, label=f'Peak: ({vertex_x:.1f}, {max_height:.1f})')
        ax.legend()
        
        st.pyplot(fig)
    
    # Quadratic Function Analysis
    st.markdown("---")
    st.markdown("### 📐 Vertex Form Analysis")
    st.markdown(f"**Height equation:** h(t) = {initial_height} + {v_y:.1f}t - 16.1t²")
    st.markdown(f"**Vertex form:** h(t) = -16.1(t - {v_y/(2*16.1):.2f})² + {max_height:.1f}")
    st.markdown(f"**Vertex (time at max height):** t = {v_y/(2*16.1):.2f} seconds")

# --- WEEK 3 ---
with week_tabs[2]:
    st.subheader("🥷 Week 3: Naruto Motion & Systems of Equations")
    
    st.markdown("**📘 IXL Skills Focus:** [W.10 - Solve a system of equations by graphing](https://www.ixl.com/math/algebra-1/solve-a-system-of-equations-by-graphing)")
    st.markdown("**📚 Common Core:** HSA.CED.A.3")
    st.markdown("**🎯 Focus:** Simultaneous Equations and Real-Life Situations")
    
    # Three-Way Race System
    st.markdown("---")
    st.markdown("### 🏃‍♂️🛴🦔 Triple Challenge: Running vs. Segway vs. Sonic")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Speed inputs
        running_speed = jeremiah_speed_mph if 'jeremiah_speed_mph' in locals() else 16.4
        segway_speed = st.slider("Segway speed (mph):", 8, 12, 10)
        sonic_speed = 767
        
        # Distance and head start
        race_distance = st.slider("Race distance (miles):", 0.5, 3.0, 1.0)
        segway_head_start = st.slider("Segway head start (minutes):", 0, 10, 2)
        
        # Calculate equations
        # Time for each mode to complete the race
        running_time = race_distance / running_speed * 60  # minutes
        segway_time = race_distance / segway_speed * 60 - segway_head_start
        sonic_time = race_distance / sonic_speed * 60  # minutes
        
        st.markdown("**Race Equations:**")
        st.markdown(f"• Running: t = {running_time:.2f} minutes")
        st.markdown(f"• Segway: t = {segway_time:.2f} minutes (with {segway_head_start} min head start)")
        st.markdown(f"• Sonic: t = {sonic_time:.4f} minutes")
    
    with col2:
        # Create race visualization
        times = np.linspace(0, max(running_time, segway_time) * 1.2, 100)
        
        # Distance covered by each mode
        running_distance = (times / 60) * running_speed
        segway_distance = np.maximum(0, ((times + segway_head_start) / 60) * segway_speed)
        sonic_distance = (times / 60) * sonic_speed
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(times, running_distance, label='Running', linewidth=3, color='#3498db')
        ax.plot(times, segway_distance, label='Segway', linewidth=3, color='#e67e22')
        ax.plot(times, sonic_distance, label='Sonic', linewidth=3, color='#9b59b6')
        
        # Mark finish line
        ax.axhline(y=race_distance, color='red', linestyle='--', alpha=0.7, label='Finish Line')
        
        ax.set_xlabel('Time (minutes)')
        ax.set_ylabel('Distance (miles)')
        ax.set_title('Race Progress: Three Systems of Motion')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, race_distance * 1.2)
        
        st.pyplot(fig)
    
    # Real Estate Systems
    st.markdown("---")
    st.markdown("### 🏠 Mom's Real Estate Commission Systems")
    
    col1, col2 = st.columns(2)
    
    with col1:
        commission_rate_1 = st.slider("Commission Rate 1 (%):", 2.0, 6.0, 3.0, 0.1)
        commission_rate_2 = st.slider("Commission Rate 2 (%):", 2.0, 6.0, 2.5, 0.1)
        base_fee = st.slider("Base fee for Rate 2 ($):", 1000, 5000, 2000, 100)
        
        st.markdown("**Commission Systems:**")
        st.markdown(f"• Option 1: C₁ = {commission_rate_1}% × Price")
        st.markdown(f"• Option 2: C₂ = {commission_rate_2}% × Price + ${base_fee}")
    
    with col2:
        # Find break-even point
        # commission_rate_1 * price = commission_rate_2 * price + base_fee
        # (commission_rate_1 - commission_rate_2) * price = base_fee
        break_even_price = base_fee / ((commission_rate_1 - commission_rate_2) / 100)
        
        # Create commission comparison
        prices = np.linspace(50000, 1000000, 100)
        comm1 = prices * (commission_rate_1 / 100)
        comm2 = prices * (commission_rate_2 / 100) + base_fee
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(prices, comm1, label=f'Option 1: {commission_rate_1}%', linewidth=3, color='#2ecc71')
        ax.plot(prices, comm2, label=f'Option 2: {commission_rate_2}% + ${base_fee}', linewidth=3, color='#e74c3c')
        
        # Mark break-even point
        if break_even_price > 0:
            break_even_commission = break_even_price * (commission_rate_1 / 100)
            ax.plot(break_even_price, break_even_commission, 'ko', markersize=8, 
                   label=f'Break-even: ${break_even_price:,.0f}')
        
        ax.set_xlabel('Property Price ($)')
        ax.set_ylabel('Commission ($)')
        ax.set_title('Real Estate Commission Comparison')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.ticklabel_format(style='plain', axis='both')
        
        st.pyplot(fig)
        
        if break_even_price > 0:
            st.success(f"**Break-even point:** ${break_even_price:,.0f}")

# --- WEEK 4 ---
with week_tabs[3]:
    st.subheader("🎓 Week 4: NJIT Bound - College Prep & Inequalities")
    
    st.markdown("**📘 IXL Skills Focus:** [Y.5 - Graph compound inequalities](https://www.ixl.com/math/algebra-1/graph-compound-inequalities)")
    st.markdown("**📚 Common Core:** HSA.REI.D.12, HSA.CED.A.2")
    st.markdown("**🎯 Focus:** Cumulative Assessment and Future Planning")
    
    # College Readiness Analysis
    st.markdown("---")
    st.markdown("### 🎯 NJIT & RPI Readiness Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_gpa = st.slider("Current GPA:", 2.0, 4.0, 3.5, 0.1)
        target_sat = st.slider("Target SAT Score:", 1000, 1600, 1300, 10)
        
        # NJIT and RPI requirements (approximate)
        njit_gpa_min = 3.3
        njit_sat_min = 1250
        rpi_gpa_min = 3.7
        rpi_sat_min = 1350
        
        st.markdown("**College Requirements:**")
        st.markdown(f"• NJIT: GPA ≥ {njit_gpa_min}, SAT ≥ {njit_sat_min}")
        st.markdown(f"• RPI: GPA ≥ {rpi_gpa_min}, SAT ≥ {rpi_sat_min}")
        
        # Create inequalities
        njit_gpa_ready = current_gpa >= njit_gpa_min
        njit_sat_ready = target_sat >= njit_sat_min
        rpi_gpa_ready = current_gpa >= rpi_gpa_min
        rpi_sat_ready = target_sat >= rpi_sat_min
        
        st.markdown("**Your Status:**")
        st.markdown(f"• NJIT GPA: {'✅' if njit_gpa_ready else '❌'} ({current_gpa} {'≥' if njit_gpa_ready else '<'} {njit_gpa_min})")
        st.markdown(f"• NJIT SAT: {'✅' if njit_sat_ready else '❌'} ({target_sat} {'≥' if njit_sat_ready else '<'} {njit_sat_min})")
        st.markdown(f"• RPI GPA: {'✅' if rpi_gpa_ready else '❌'} ({current_gpa} {'≥' if rpi_gpa_ready else '<'} {rpi_gpa_min})")
        st.markdown(f"• RPI SAT: {'✅' if rpi_sat_ready else '❌'} ({target_sat} {'≥' if rpi_sat_ready else '<'} {rpi_sat_min})")
    
    with col2:
        # Create college readiness visualization
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create scatter plot of college requirements
        colleges = ['NJIT', 'RPI']
        gpa_reqs = [njit_gpa_min, rpi_gpa_min]
        sat_reqs = [njit_sat_min, rpi_sat_min]
        
        # Plot college requirements
        colors = ['#3498db', '#e74c3c']
        for i, (college, gpa_req, sat_req, color) in enumerate(zip(colleges, gpa_reqs, sat_reqs, colors)):
            ax.scatter(gpa_req, sat_req, s=300, c=color, alpha=0.7, label=f'{college} Requirements')
        
        # Plot current status
        ax.scatter(current_gpa, target_sat, s=400, c='#f39c12', marker='*', 
                  label='Your Current Status', edgecolors='black', linewidth=2)
        
        # Add quadrant lines
        ax.axhline(y=njit_sat_min, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=njit_gpa_min, color='gray', linestyle='--', alpha=0.5)
        ax.axhline(y=rpi_sat_min, color='gray', linestyle='--', alpha=0.3)
        ax.axvline(x=rpi_gpa_min, color='gray', linestyle='--', alpha=0.3)
        
        ax.set_xlabel('GPA')
        ax.set_ylabel('SAT Score')
        ax.set_title('College Readiness Map')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xlim(2.8, 4.0)
        ax.set_ylim(1100, 1500)
        
        st.pyplot(fig)
    
    # Real Estate Investment Inequalities
    st.markdown("---")
    st.markdown("### 🏠 Real Estate Investment Constraints")
    
    budget = st.slider("Investment budget ($):", 100000, 1000000, 400000, 10000)
    min_roi = st.slider("Minimum ROI (%):", 5, 15, 8)
    max_risk = st.selectbox("Risk tolerance:", ["Low", "Medium", "High"])
    
    # Create property constraints
    st.markdown("**Investment Inequalities:**")
    st.markdown(f"• Price ≤ ${budget:,}")
    st.markdown(f"• ROI ≥ {min_roi}%")
    st.markdown(f"• Risk level = {max_risk}")
    
    # Simulate property options
    np.random.seed(42)
    n_properties = 50
    property_prices = np.random.uniform(budget*0.3, budget*1.2, n_properties)
    property_rois = np.random.uniform(3, 18, n_properties)
    
    # Apply constraints
    price_constraint = property_prices <= budget
    roi_constraint = property_rois >= min_roi
    viable_properties = price_constraint & roi_constraint
    
    # Visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot all properties
    ax.scatter(property_prices[~viable_properties], property_rois[~viable_properties], 
              c='red', alpha=0.6, label='Not Viable', s=50)
    ax.scatter(property_prices[viable_properties], property_rois[viable_properties], 
              c='green', alpha=0.8, label='Viable Investment', s=50)
    
    # Add constraint lines
    ax.axvline(x=budget, color='blue', linestyle='--', linewidth=2, label=f'Budget Limit: ${budget:,}')
    ax.axhline(y=min_roi, color='orange', linestyle='--', linewidth=2, label=f'Min ROI: {min_roi}%')
    
    ax.set_xlabel('Property Price ($)')
    ax.set_ylabel('Expected ROI (%)')
    ax.set_title('Real Estate Investment Opportunities')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(style='plain', axis='x')
    
    st.pyplot(fig)
    
    viable_count = np.sum(viable_properties)
    st.success(f"**Viable properties:** {viable_count} out of {n_properties} meet your criteria")

# --- Ask Dr. X Sidebar ---
st.sidebar.title("🤖 Ask Dr. X")
st.sidebar.markdown("*Your Personal Math Coach*")

# Display chat history in sidebar
with st.sidebar:
    st.markdown("### 💬 Chat History")
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.chat_history[-5:]:  # Show last 5 messages
            if message["role"] == "user":
                st.markdown(f"**🏈 You:** {message['content']}")
            else:
                st.markdown(f"**👓 Dr. X:** {message['content']}")
    
    # Chat input
    user_input = st.text_input("Ask Dr. X:", placeholder="e.g., How do I find the vertex of a parabola?")
    
    if st.button("Send") and user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get Dr. X response
        with st.spinner("Dr. X is thinking..."):
            response = ask_drx(user_input)
        
        # Add response
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()
    
    if st.button("Clear Chat"):
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello Jeremiah! I'm Dr. X, your AI math coach. Ready to tackle some math problems?"}
        ]
        st.rerun()

# --- IXL Integration Section ---
st.header("📚 IXL Practice & Study Resources")

# Adaptive content based on selected standard
selected_focus = common_core_standard.split(" - ")[0]

if "HSA.CED" in selected_focus:
    st.info("🎯 **Focus: Creating Equations** - Practice building equations from real-world scenarios.")
    emphasis = "equation_building"
elif "HSA.REI" in selected_focus:
    st.info("🎯 **Focus: Solving Equations** - Master solving techniques and graphical methods.")
    emphasis = "solving"
elif "HSF.IF" in selected_focus:
    st.info("🎯 **Focus: Function Interpretation** - Understand domain, range, and key features.")
    emphasis = "functions"
else:
    st.info("🎯 **Focus: Building Functions** - Create and model real-world relationships.")
    emphasis = "modeling"

# IXL lessons organized by week and topic
ixl_lessons = {
    "Week 1: Algebra Foundations": {
        "Core Skills": [
            "U.2 - Solve multi-step linear equations",
            "U.3 - Solve linear equations: mixed review", 
            "U.4 - Solve equations involving like terms",
            "V.1 - Write and solve equations that represent diagrams",
            "V.2 - Solve linear equations: word problems"
        ],
        "Real-World Applications": [
            "AA.1 - Rate of change: graphs",
            "AA.2 - Rate of change: tables", 
            "AA.3 - Constant rate of change",
            "BB.1 - Identify linear functions",
            "BB.2 - Find the slope of a graph"
        ]
    },
    "Week 2: Quadratic Functions": {
        "Core Skills": [
            "J.7 - Graph parabolas",
            "J.8 - Graph a quadratic function", 
            "J.9 - Match quadratic functions and graphs",
            "K.1 - Solve a quadratic equation using square roots",
            "K.2 - Solve a quadratic equation using the quadratic formula"
        ],
        "Applications": [
            "J.10 - Find the vertex of a parabola",
            "J.11 - Complete the square", 
            "J.12 - Convert from vertex form to standard form",
            "T.1 - Interpret a quadratic graph",
            "T.2 - Quadratic models: word problems"
        ]
    },
    "Week 3: Systems of Equations": {
        "Core Skills": [
            "W.10 - Solve a system of equations by graphing",
            "W.11 - Find the number of solutions to a system", 
            "W.12 - Classify a system of equations",
            "X.1 - Solve a system of equations using substitution",
            "X.2 - Solve a system of equations using elimination"
        ],
        "Real-World Applications": [
            "W.13 - Systems of equations: word problems",
            "X.3 - Systems of linear and quadratic equations", 
            "FF.1 - Is (x, y) a solution to the system of inequalities?",
            "FF.2 - Solve systems of linear inequalities by graphing"
        ]
    },
    "Week 4: Inequalities & Review": {
        "Core Skills": [
            "Y.5 - Graph compound inequalities",
            "Y.6 - Write compound inequalities from graphs", 
            "Y.7 - Solve compound inequalities",
            "FF.1 - Graph a linear inequality in two variables",
            "FF.2 - Systems of linear inequalities"
        ],
        "College Prep": [
            "GG.1 - Domain and range of functions",
            "GG.2 - Identify functions", 
            "HH.1 - Function transformation rules",
            "II.1 - Exponential functions over unit intervals",
            "JJ.1 - Compare linear, exponential, and quadratic functions"
        ]
    }
}

# Display IXL lessons based on emphasis
week_selected = st.selectbox("Select week for targeted IXL practice:", list(ixl_lessons.keys()))
selected_week = ixl_lessons[week_selected]

# Priority recommendations based on emphasis
if emphasis == "equation_building":
    priority_lessons = [
        "U.2 - Solve multi-step linear equations", 
        "V.2 - Solve linear equations: word problems", 
        "W.13 - Systems of equations: word problems"
    ]
elif emphasis == "solving":
    priority_lessons = [
        "K.2 - Solve a quadratic equation using the quadratic formula", 
        "X.1 - Solve a system of equations using substitution", 
        "Y.7 - Solve compound inequalities"
    ]
elif emphasis == "functions":
    priority_lessons = [
        "GG.1 - Domain and range of functions", 
        "BB.1 - Identify linear functions", 
        "J.10 - Find the vertex of a parabola"
    ]
else:  # modeling
    priority_lessons = [
        "T.2 - Quadratic models: word problems", 
        "AA.3 - Constant rate of change", 
        "FF.2 - Systems of linear inequalities"
    ]

st.markdown(f"**⭐ Priority for {selected_focus}:**")
for lesson in priority_lessons:
    st.write(f"• **{lesson}**")

st.markdown("---")

# Display selected week's lessons
for topic, lessons in selected_week.items():
    with st.expander(f"📖 {topic} - IXL Practice"):
        for lesson in lessons:
            st.write(f"• {lesson}")
        st.markdown(f"**💡 Practice Tip:** Complete these lessons to master {topic.lower()}!")

# --- Capstone Project ---
st.header("🏆 Capstone: Real Estate Flip Challenge")

st.markdown("""
**🎯 Final Challenge:** Select a Jersey City property, analyze its investment potential, 
and create a mathematical pitch using everything you've learned!
""")

# Property selection simulation
property_data = {
    "Address": [
        "123 Montgomery St, Jersey City",
        "456 Newport Pkwy, Jersey City", 
        "789 Grove St, Jersey City",
        "321 Washington St, Jersey City",
        "654 Hamilton Park, Jersey City"
    ],
    "Price": [385000, 520000, 299000, 675000, 450000],
    "Sqft": [1200, 1800, 950, 2200, 1500],
    "Bedrooms": [2, 3, 1, 4, 3],
    "Estimated_Rent": [2800, 3500, 2200, 4200, 3200]
}

df = pd.DataFrame(property_data)
df['Price_per_Sqft'] = df['Price'] / df['Sqft']
df['Monthly_ROI'] = (df['Estimated_Rent'] / df['Price']) * 100

st.dataframe(df, use_container_width=True)

selected_property = st.selectbox("Choose your investment property:", df['Address'].tolist())

if selected_property:
    prop_data = df[df['Address'] == selected_property].iloc[0]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Purchase Price", f"${prop_data['Price']:,}")
        st.metric("Square Footage", f"{prop_data['Sqft']:,} sq ft")
    
    with col2:
        st.metric("Price per Sq Ft", f"${prop_data['Price_per_Sqft']:.0f}")
        st.metric("Estimated Rent", f"${prop_data['Estimated_Rent']:,}/month")
    
    with col3:
        st.metric("Monthly ROI", f"{prop_data['Monthly_ROI']:.2f}%")
        annual_roi = prop_data['Monthly_ROI'] * 12
        st.metric("Annual ROI", f"{annual_roi:.1f}%")
    
    # Investment analysis
    st.markdown("---")
    st.markdown("### 📊 Mathematical Investment Analysis")
    
    # Linear model for property appreciation
    years = st.slider("Investment timeline (years):", 1, 10, 5)
    appreciation_rate = st.slider("Annual appreciation rate (%):", 2, 8, 4)
    
    # Calculate projections
    future_value = prop_data['Price'] * ((1 + appreciation_rate/100) ** years)
    total_rent = prop_data['Estimated_Rent'] * 12 * years
    total_return = future_value + total_rent - prop_data['Price']
    roi_percentage = (total_return / prop_data['Price']) * 100
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📈 Investment Projections:**")
        st.write(f"• Future property value: ${future_value:,.0f}")
        st.write(f"• Total rental income: ${total_rent:,.0f}")
        st.write(f"• Total return: ${total_return:,.0f}")
        st.write(f"• Total ROI: {roi_percentage:.1f}%")
    
    with col2:
        # Create projection graph
        year_range = np.arange(0, years + 1)
        property_values = prop_data['Price'] * ((1 + appreciation_rate/100) ** year_range)
        rental_income = prop_data['Estimated_Rent'] * 12 * year_range
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(year_range, property_values, label='Property Value', linewidth=3, color='#2ecc71')
        ax.plot(year_range, rental_income, label='Cumulative Rent', linewidth=3, color='#3498db')
        
        ax.set_xlabel('Years')
        ax.set_ylabel('Value ($)')
        ax.set_title(f'Investment Projection: {selected_property}')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.ticklabel_format(style='plain', axis='y')
        
        st.pyplot(fig)

# --- External Resources ---
st.header("🌐 Additional Learning Resources")

resources = {
    "📺 Video Tutorials": [
        {
            "name": "Khan Academy - Algebra Basics",
            "url": "https://www.khanacademy.org/math/algebra-basics",
            "description": "Comprehensive algebra review perfect for 9th grade reinforcement"
        },
        {
            "name": "Professor Leonard - Quadratic Functions",
            "url": "https://www.youtube.com/watch?v=bTHNH04lwas",
            "description": "Clear explanations of parabolas and vertex form"
        },
        {
            "name": "PatrickJMT - Systems of Equations",
            "url": "https://www.youtube.com/watch?v=AqIrdW2-K6k",
            "description": "Multiple methods for solving systems"
        }
    ],
    "💻 Interactive Tools": [
        {
            "name": "Desmos Graphing Calculator",
            "url": "https://www.desmos.com/calculator",
            "description": "Perfect for visualizing functions and trajectories"
        },
        {
            "name": "GeoGebra Algebra",
            "url": "https://www.geogebra.org/algebra",
            "description": "Interactive algebra and graphing tools"
        },
        {
            "name": "Wolfram Alpha",
            "url": "https://www.wolframalpha.com/",
            "description": "Step-by-step equation solving"
        }
    ],
    "🎓 College Prep": [
        {
            "name": "NJIT Admissions Requirements",
            "url": "https://www.njit.edu/admissions/undergraduate",
            "description": "Official admission standards and requirements"
        },
        {
            "name": "RPI Undergraduate Admissions",
            "url": "https://admissions.rpi.edu/undergraduate",
            "description": "Requirements and application information"
        },
        {
            "name": "College Board SAT Prep",
            "url": "https://www.collegeboard.org/sat",
            "description": "Official SAT preparation materials"
        }
    ]
}

resource_tabs = st.tabs(list(resources.keys()))

for i, (category, items) in enumerate(resources.items()):
    with resource_tabs[i]:
        for item in items:
            st.markdown(f"**[{item['name']}]({item['url']})**")
            st.write(f"📝 {item['description']}")
            st.write("---")

# --- Personalized Study Plan ---
st.header("📅 Personalized Study Plan Generator")

current_level = st.selectbox("Rate your current algebra confidence:", [
    "🟢 Strong - Ready for challenge problems",
    "🟡 Good - Need some practice in weak areas", 
    "🟠 Fair - Need systematic review",
    "🔴 Struggling - Need fundamental reinforcement"
])

time_available = st.selectbox("Study time available per week:", [
    "2-3 hours", "4-5 hours", "6-7 hours", "8+ hours"
])

focus_area = st.selectbox("Priority focus area:", [
    "Linear equations and graphing",
    "Quadratic functions and parabolas", 
    "Systems of equations",
    "Real-world problem solving",
    "College prep and review"
])

if st.button("Generate My Personal Study Plan"):
    st.success("🎯 Your Customized MathCraft Study Plan:")
    
    if "Strong" in current_level:
        st.markdown("""
        **🚀 Advanced Track (4 weeks):**
        - Week 1: Challenge problems with real-world applications
        - Week 2: Advanced quadratic modeling and optimization
        - Week 3: Complex systems and matrix methods
        - Week 4: Pre-calculus preparation and competition problems
        """)
    elif "Good" in current_level:
        st.markdown("""
        **📈 Accelerated Track (4 weeks):**
        - Week 1: Review fundamentals, focus on weak areas
        - Week 2: Master quadratic applications and vertex form
        - Week 3: Systems solving and graphical interpretation
        - Week 4: Integration and college-level problems
        """)
    elif "Fair" in current_level:
        st.markdown("""
        **🎯 Standard Track (4-5 weeks):**
        - Week 1-2: Systematic algebra review with practice
        - Week 3: Quadratic functions with multiple approaches
        - Week 4: Systems of equations mastery
        - Week 5: Review and college prep
        """)
    else:
        st.markdown("""
        **🔧 Foundation Track (5-6 weeks):**
        - Week 1-2: Basic equation solving and graphing
        - Week 3: Linear functions and slope concepts
        - Week 4: Introduction to quadratics
        - Week 5: Simple systems of equations
        - Week 6: Review and confidence building
        """)
    
    if time_available == "2-3 hours":
        st.info("💡 **Study Strategy:** Focus on one concept per week with daily 20-30 minute sessions.")
    elif time_available == "4-5 hours":
        st.info("💡 **Study Strategy:** Balance video learning (40%) with hands-on practice (60%).")
    elif time_available == "6-7 hours":
        st.info("💡 **Study Strategy:** Add peer tutoring and teaching to reinforce learning.")
    else:
        st.info("💡 **Study Strategy:** Consider accelerated track and additional challenge problems.")

# --- Progress Tracking ---
st.header("📊 Progress Tracking")

if st.checkbox("Enable Progress Tracking"):
    progress_data = {
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Concept Mastery": [85, 78, 92, 88],
        "IXL Completion": [90, 85, 95, 80],
        "Real-World Applications": [75, 88, 90, 95]
    }
    
    progress_df = pd.DataFrame(progress_data)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(progress_data["Week"]))
    width = 0.25
    
    ax.bar(x - width, progress_data["Concept Mastery"], width, label='Concept Mastery', color='#3498db')
    ax.bar(x, progress_data["IXL Completion"], width, label='IXL Completion', color='#2ecc71')
    ax.bar(x + width, progress_data["Real-World Applications"], width, label='Real-World Apps', color='#e74c3c')
    
    ax.set_xlabel('Program Week')
    ax.set_ylabel('Score (%)')
    ax.set_title('MathCraft Progress Tracking')
    ax.set_xticks(x)
    ax.set_xticklabels(progress_data["Week"])
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 100)
    
    st.pyplot(fig)
    
    overall_avg = np.mean([progress_data["Concept Mastery"], progress_data["IXL Completion"], progress_data["Real-World Applications"]])
    st.metric("Overall Progress", f"{overall_avg:.1f}%")

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <h4>🎓 Ready to Dominate 10th Grade Math!</h4>
    <p><em>"Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding." - William Paul Thurston</em></p>
    <p><strong>Built for Jeremiah by Xavier Honablue M.Ed | CognitiveCloud.ai</strong></p>
    <p>🎯 <strong>Target Universities:</strong> NJIT & RPI | 🏈 <strong>Position:</strong> Quarterback | 🏠 <strong>Real Estate Math with Mom</strong></p>
</div>
""", unsafe_allow_html=True)
