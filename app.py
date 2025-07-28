
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

Welcome, **Future NJIT Engineer**! This MathCraft program transforms 9th grade math review into an epic quest, blending Jeremiah’s passions—quarterback for the Lincoln Lions, Sonic speed, Segway adventures, ROTC leadership, and real estate success with his mother Rose from Namibia—into mathematical mastery for 10th grade.

---

### 🎯 Program Goal:
Prepare Jeremiah for 10th grade math (Algebra I and Intro to Algebra II) by reinforcing foundational skills and introducing functions through his ROTC program and the Army Corps of Engineers, with Rose as his inspiring partner.

### 🧑🏿‍🏫 Who is Dr. X?
Dr. X isn’t a robot 🤓—he’s modeled after Xavier Honablue M.Ed, a Black educator with glasses, a deep voice, and a heart for student success. He’s your sideline coach for math, cheering Jeremiah and Rose on!
""")

# Common Core Standards Alignment
st.info("📚 **Common Core Alignment:** Covers High School Algebra standards (HSA.CED, HSA.REI, HSF.BF) and introduces 10th-grade topics like functions (HSF.IF), preparing Jeremiah for NJIT’s mechanical engineering path and Army Corps of Engineers applications.")

# Common Core Standards Dropdown
common_core_standard = st.selectbox("📋 Select specific Common Core Standard focus:", [
    "HSA.CED.A.1 - Create equations and inequalities in one variable",
    "HSA.CED.A.2 - Create equations in two or more variables",
    "HSA.REI.B.3 - Solve linear equations and inequalities",
    "HSA.REI.B.4 - Solve quadratic equations",
    "HSF.IF.B.4 - Interpret key features of graphs and tables",
    "HSF.BF.A.1 - Write functions for relationships",
    "HSF.LE.A.2 - Construct linear and exponential functions"
])

# --- Student Info ---
st.subheader("🎮 Quarterback Profile Setup")
name = st.text_input("Enter your name:", value="Jeremiah Erskine")
position = st.selectbox("Choose your mathematical identity:", [
    "🏈 Lincoln Lions Quarterback", "🦔 Speed Calculator", "🛴 Slope Navigator",
    "🏠 Real Estate Mathematician", "🎖️ ROTC Engineer", "🎯 NJIT Bound Scholar"
])

if name:
    st.success(f"Welcome, {name} the {position}! Ready to dominate 10th grade math with Rose by your side!")

# --- Level Selection ---
challenge_level = st.selectbox("Choose your challenge level:", [
    "🟢 Level 1: Sonic Dash Algebra Maze",
    "🔵 Level 2: QB Launch Trajectories",
    "🟡 Level 3: Naruto Systems Faceoff",
    "🔴 Level 4: NJIT & Army Corps Quest"
])

# Initialize session state for Dr. X chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello Jeremiah and Rose! I'm Dr. X, your AI math coach. Let’s conquer math with the Lincoln Lions spirit and ROTC discipline!"}
    ]

# Dr. X API function
def ask_drx(message):
    try:
        response = requests.post(
            'https://ask-drx-730124987572.us-central1.run.app',
            json={'message': message},
            timeout=30
        )
        return response.json().get('reply', "Sorry, I couldn't process that.") if response.status_code == 200 else "Connection issue. Try again."
    except:
        return "Connection issue. Try again."

# --- Week Navigation ---
st.header("📅 4-Week Mathematical Journey")
week_tabs = st.tabs([
    "📈 Week 1: Sonic Speeds & Linear Functions",
    "📊 Week 2: Football Physics & Quadratics",
    "🔄 Week 3: Naruto Motion & Systems",
    "🎖️ Week 4: ROTC & Army Corps Engineering"
])

# --- WEEK 1 ---
with week_tabs[0]:
    st.subheader("🦔 Week 1: Sonic Speeds & Linear Functions")
    st.markdown("**📘 IXL Skills Focus:** [U.2 - Solve multi-step linear equations](https://www.ixl.com/math/algebra-1/solve-multi-step-linear-equations)")
    st.markdown("**📚 Common Core:** HSA.CED.A.1, HSA.REI.B.3, HSF.IF.B.4")
    st.markdown("**🎯 10th Grade Prep:** Linear functions, domain, and range")

    # Story: Jeremiah and Rose’s Speed Adventure
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** In Namibia, Rose and Jeremiah loved watching cheetahs sprint across the plains. Now in Jersey City, they imagine racing Sonic to Lincoln High School, home of the Lincoln Lions. Rose, with her Namibian wisdom, says, “Let’s use linear functions to calculate our speeds and win!” Jeremiah, the Lions’ quarterback, is ready to apply math to outrun Sonic.
    """)

    # Sonic Speed Calculator
    st.markdown("---")
    st.markdown("### 🚀 Sonic vs. Lincoln Lions QB Speed Challenge")
    show_speed_chart = st.checkbox("Show Speed Comparison Chart 📊", value=True, key="speed_toggle")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**⚡ Sonic's Speed:** 767 mph (Speed of Sound)")
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
            bars = ax.bar(speeds, values, color=colors)
            ax.set_ylabel('Speed (mph)')
            ax.set_title('Speed Comparison: Jeremiah vs. Sonic')
            ax.set_ylim(0, 800)
            for bar, value in zip(bars, values):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 10, f'{value:.1f} mph', ha='center', va='bottom', fontweight='bold')
            st.pyplot(fig)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Speed = Distance/Time, a linear function (HSF.IF.B.4). Jeremiah’s speed is calculated as (40 yards × 3600 seconds/hour) / (time × 5280 yards/mile). The domain (time > 0) and range (speed > 0) introduce 10th-grade function concepts, preparing Jeremiah for ROTC precision.
    """)

# --- WEEK 2 ---
with week_tabs[1]:
    st.subheader("🏈 Week 2: Football Physics & Quadratics")
    st.markdown("**📘 IXL Skills Focus:** [J.7 - Graph parabolas](https://www.ixl.com/math/algebra-1/graph-a-quadratic-function)")
    st.markdown("**📚 Common Core:** HSA.REI.B.4, HSF.IF.C.7")
    st.markdown("**🎯 10th Grade Prep:** Quadratic functions, vertex form, and intercepts")

    # Story: Jeremiah and Rose’s Football Triumph
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** In Namibia, Rose cheered at village soccer games, inspiring Jeremiah’s love for sports. Now, as the Lincoln Lions’ star quarterback, Jeremiah uses quadratic functions to perfect his spiral throws. Rose says, “Let’s calculate the arc to win the game!” The Lions’ championship legacy fuels their drive.
    """)

    # Football Trajectory Calculator
    st.markdown("---")
    st.markdown("### 🎯 Lincoln Lions QB Spiral Analysis")
    show_trajectory_chart = st.checkbox("Show Trajectory Chart 📊", value=True, key="trajectory_toggle")
    col1, col2 = st.columns(2)
    with col1:
        initial_velocity = st.slider("Initial velocity (ft/s):", 30, 80, 60)
        launch_angle = st.slider("Launch angle (degrees):", 15, 60, 30)
        initial_height = st.slider("Release height (feet):", 5, 8, 6)
        angle_rad = np.radians(launch_angle)
        v_x = initial_velocity * np.cos(angle_rad)
        v_y = initial_velocity * np.sin(angle_rad)
        flight_time = (v_y + np.sqrt(v_y**2 + 2*32.2*initial_height)) / 32.2
        max_height = initial_height + (v_y**2) / (2*32.2)
        max_distance = v_x * flight_time
        st.metric("Maximum Height", f"{max_height:.1f} feet")
        st.metric("Distance", f"{max_distance:.1f} feet")
        st.metric("Flight Time", f"{flight_time:.2f} seconds")
    with col2:
        if show_trajectory_chart:
            t_vals = np.linspace(0, flight_time, 100)
            x_vals = v_x * t_vals
            y_vals = initial_height + v_y * t_vals - 0.5 * 32.2 * t_vals**2
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
            vertex_x = max_distance / 2
            ax.plot(vertex_x, max_height, 'ro', markersize=8, label=f'Peak: ({vertex_x:.1f}, {max_height:.1f})')
            ax.legend()
            st.pyplot(fig)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** The football’s path follows h(t) = -16.1t² + v₀t + h₀, a quadratic function (HSF.IF.C.7). The vertex gives the maximum height, and roots show landing points, key for 10th-grade Algebra II. Jeremiah’s throws align with ROTC precision training.
    """)

# --- WEEK 3 ---
with week_tabs[2]:
    st.subheader("🥷 Week 3: Naruto Motion & Systems")
    st.markdown("**📘 IXL Skills Focus:** [W.10 - Solve a system of equations by graphing](https://www.ixl.com/math/algebra-1/solve-a-system-of-equations-by-graphing)")
    st.markdown("**📚 Common Core:** HSA.CED.A.3, HSA.REI.C.6")
    st.markdown("**🎯 10th Grade Prep:** Systems of linear equations and inequalities")

    # Story: Jeremiah and Rose’s Race Day
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Inspired by Naruto’s ninja speed, Rose and Jeremiah, the Lincoln Lions QB, stage a race in Jersey City. Rose, drawing on Namibian storytelling, says, “Let’s use systems of equations to see who wins, just like planning our real estate deals!” The Lions’ winning spirit drives them.
    """)

    # Three-Way Race System
    st.markdown("---")
    st.markdown("### 🏃‍♂️🛴🦔 Triple Challenge: Lions QB vs. Segway vs. Sonic")
    show_race_chart = st.checkbox("Show Race Progress Chart 📈", value=True, key="race_toggle")
    col1, col2 = st.columns(2)
    with col1:
        running_speed = jeremiah_speed_mph if 'jeremiah_speed_mph' in locals() else 16.4
        segway_speed = st.slider("Segway speed (mph):", 8, 12, 10)
        sonic_speed = 767
        race_distance = st.slider("Race distance (miles):", 0.5, 3.0, 1.0)
        segway_head_start = st.slider("Segway head start (minutes):", 0, 10, 2)
        running_time = race_distance / running_speed * 60
        segway_time = race_distance / segway_speed * 60 - segway_head_start
        sonic_time = race_distance / sonic_speed * 60
        st.markdown("**Race Equations:**")
        st.markdown(f"• Running: t = {running_time:.2f} minutes")
        st.markdown(f"• Segway: t = {segway_time:.2f} minutes")
        st.markdown(f"• Sonic: t = {sonic_time:.4f} minutes")
    with col2:
        if show_race_chart:
            times = np.linspace(0, max(running_time, segway_time) * 1.2, 100)
            running_distance = (times / 60) * running_speed
            segway_distance = np.maximum(0, ((times + segway_head_start) / 60) * segway_speed)
            sonic_distance = (times / 60) * sonic_speed
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(times, running_distance, label='Running', linewidth=3, color='#3498db')
            ax.plot(times, segway_distance, label='Segway', linewidth=3, color='#e67e22')
            ax.plot(times, sonic_distance, label='Sonic', linewidth=3, color='#9b59b6')
            ax.axhline(y=race_distance, color='red', linestyle='--', alpha=0.7, label='Finish Line')
            ax.set_xlabel('Time (minutes)')
            ax.set_ylabel('Distance (miles)')
            ax.set_title('Race Progress: Three Systems of Motion')
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.set_ylim(0, race_distance * 1.2)
            st.pyplot(fig)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Systems of equations (Distance = Speed × Time) model multiple racers (HSA.REI.C.6). Graphing finds intersections, a 10th-grade skill for solving systems, useful for ROTC logistics planning.
    """)

# --- WEEK 4 ---
with week_tabs[3]:
    st.subheader("🎖️ Week 4: ROTC & Army Corps Engineering")
    st.markdown("**📘 IXL Skills Focus:** [Y.5 - Graph compound inequalities](https://www.ixl.com/math/algebra-1/graph-compound-inequalities)")
    st.markdown("**📚 Common Core:** HSA.REI.D.12, HSF.BF.A.1")
    st.markdown("**🎯 10th Grade Prep:** Function modeling for engineering applications")

    # Story: Jeremiah and Rose’s Engineering Dream
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** At Lincoln High School, Jeremiah’s ROTC program sparked his interest in the Army Corps of Engineers, inspired by their flood control projects. Rose, from Namibia’s arid landscapes, shared stories of water management, saying, “Use functions to design solutions, my future NJIT engineer!” The Lincoln Lions’ championship spirit drives their vision.
    """)

    # Army Corps Flood Control Challenge
    st.markdown("---")
    st.markdown("### 🌊 Army Corps Flood Wall Design")
    st.markdown("**Context:** Jeremiah, in ROTC, designs a flood wall for Jersey City with the Army Corps of Engineers, using quadratic functions to model water flow.")
    show_flood_chart = st.checkbox("Show Flood Wall Profile 📈", value=True, key="flood_toggle")
    col1, col2 = st.columns(2)
    with col1:
        wall_height = st.slider("Wall height (feet):", 5, 20, 10)
        river_width = st.slider("River width (feet):", 50, 200, 100)
        flow_rate = st.slider("Water flow rate (ft³/s):", 100, 1000, 500)
        # Quadratic function for water pressure: P(x) = a(x - h)² + k
        a = -flow_rate / (2 * river_width**2)  # Scaled for visualization
        h = river_width / 2  # Vertex at river center
        k = wall_height  # Max pressure at center
        st.markdown(f"**Pressure Function:** P(x) = {a:.4f}(x - {h})² + {k}")
        safe_pressure = flow_rate * 0.8
        st.metric("Safe Pressure Limit", f"{safe_pressure:.0f} ft³/s")
    with col2:
        if show_flood_chart:
            x_vals = np.linspace(0, river_width, 100)
            pressure = a * (x_vals - h)**2 + k
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x_vals, pressure, linewidth=3, color='#3498db')
            ax.fill_between(x_vals, pressure, alpha=0.3, color='#3498db')
            ax.axhline(y=safe_pressure, color='red', linestyle='--', alpha=0.7, label='Safe Pressure')
            ax.set_xlabel('River Width (feet)')
            ax.set_ylabel('Pressure (ft³/s)')
            ax.set_title('Flood Wall Pressure Profile')
            ax.legend()
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Quadratic functions model water pressure (HSF.BF.A.1), critical for Army Corps projects. The vertex represents peak pressure, and the safe pressure line ensures structural integrity. This 10th-grade skill prepares Jeremiah for NJIT mechanical engineering and Corps applications.
    """)

    # College Readiness for NJIT and Army Corps
    st.markdown("---")
    st.markdown("### 🎓 NJIT & Army Corps Career Path")
    current_gpa = st.slider("Current GPA:", 2.0, 4.0, 3.5, 0.1)
    target_sat = st.slider("Target SAT Score:", 1000, 1600, 1300, 10)
    njit_gpa_min = 3.3
    njit_sat_min = 1250
    st.markdown(f"**NJIT Mechanical Engineering Requirements:** GPA ≥ {njit_gpa_min}, SAT ≥ {njit_sat_min}")
    st.markdown("**Army Corps Path:** NJIT degree + ROTC leadership")
    st.success(f"**Status:** GPA {'✅' if current_gpa >= njit_gpa_min else '❌'}, SAT {'✅' if target_sat >= njit_sat_min else '❌'}")

# --- Ask Dr. X Sidebar ---
st.sidebar.title("🤖 Ask Dr. X")
with st.sidebar:
    for message in st.session_state.chat_history[-5:]:
        st.markdown(f"**{'🏈 You' if message['role'] == 'user' else '👓 Dr. X'}:** {message['content']}")
    user_input = st.text_input("Ask Dr. X:", placeholder="e.g., How do I model flood control?")
    if st.button("Send") and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Dr. X is thinking..."):
            response = ask_drx(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()
    if st.button("Clear Chat"):
        st.session_state.chat_history = [{"role": "assistant", "content": "Ready to tackle math, Jeremiah?"}]
        st.rerun()

# --- Capstone: Army Corps Project ---
st.header("🏆 Capstone: Jersey City Flood Defense Project")
st.markdown("""
**🎯 Final Challenge:** Design a flood defense system for Jersey City, using functions to model water flow and costs, preparing Jeremiah for the Army Corps after NJIT.
""")
project_data = {
    "Design": ["Basic Wall", "Reinforced Wall", "Smart Barrier"],
    "Cost": [200000, 350000, 500000],
    "Height (ft)": [8, 12, 15],
    "Max Flow (ft³/s)": [400, 600, 800]
}
df = pd.DataFrame(project_data)
df['Cost per Height'] = df['Cost'] / df['Height']
st.dataframe(df, use_container_width=True)
selected_design = st.selectbox("Choose your flood defense design:", df['Design'].tolist())
if selected_design:
    design_data = df[df['Design'] == selected_design].iloc[0]
    st.metric("Cost", f"${design_data['Cost']:,}")
    st.metric("Max Flow", f"{design_data['Max Flow']:.0f} ft³/s")
    show_project_chart = st.checkbox("Show Cost-Flow Analysis 📈", value=True, key="project_toggle")
    if show_project_chart:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df['Max Flow'], df['Cost'], c='#2ecc71', s=80, label='Designs')
        ax.scatter(design_data['Max Flow'], design_data['Cost'], c='#e74c3c', s=120, label='Selected Design')
        ax.set_xlabel('Max Flow (ft³/s)')
        ax.set_ylabel('Cost ($)')
        ax.set_title('Flood Defense Cost vs. Capacity')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.ticklabel_format(style='plain', axis='y')
        st.pyplot(fig)

    # Story: Jeremiah and Rose’s Legacy
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Rose, inspired by Namibia’s water challenges, helps Jeremiah design a flood defense system. “This will protect Jersey City and honor the Lincoln Lions!” Jeremiah says, dreaming of joining the Army Corps post-NJIT.
    """)

# --- Footer ---
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <h4>🎖️ Ready to Engineer the Future!</h4>
    <p><em>"Mathematics is the language of engineering solutions." - Xavier Honablue</em></p>
    <p><strong>Built for Jeremiah by Xavier Honablue M.Ed | CognitiveCloud.ai</strong></p>
    <p>🎯 <strong>Target Path:</strong> NJIT Mechanical Engineering & Army Corps of Engineers</p>
</div>
""", unsafe_allow_html=True)
```
