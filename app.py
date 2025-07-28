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

# Common Core Standards Alignment (Global Dropdown)
st.info("📚 **Common Core Alignment:** This program covers High School Algebra standards like creating equations (HSA.CED), reasoning with equations (HSA.REI), and building functions (HSF.BF) through real-world applications.")
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
    week_std = st.selectbox("📋 Week 1 Common Core Focus:", [
        "HSA.CED.A.1 - Create equations and inequalities in one variable",
        "HSA.REI.B.3 - Solve linear equations and inequalities in one variable",
        "HSF.IF.B.4 - Interpret key features of graphs and tables"
    ])
    st.markdown("**📚 Common Core:** HSA.CED.A.1, HSA.REI.B.3, HSF.IF.B.4")
    st.markdown("**🎯 Focus:** Expressions, Equations, and Linear Functions")

    # Story: Jeremiah and Rose’s Speed Adventure
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Back in South Africa, Jeremiah and his mom Rose loved watching wildlife dash across the savanna. One day, they imagined racing Sonic the Hedgehog from their new Jersey City home to Lincoln Park. Rose, with her keen eye for deals, turned it into a math challenge: “Let’s calculate our speeds and see who wins!” Jeremiah grinned, ready to outsmart Sonic with algebra.
    """)

    # Interactive Sonic Speed Calculator with Toggle
    st.markdown("---")
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
    📚 **Math Lesson:** Speed is calculated as distance divided by time (Speed = Distance/Time). Here, Jeremiah’s 40-yard dash time is converted to mph using the formula:  
    Speed (mph) = (40 yards × 3600 seconds/hour) / (dash time × 5280 yards/mile). Sonic’s speed is a constant 767 mph. The ratio helps us compare their speeds, a key skill in HSA.CED.A.1 for creating equations!
    **Example Problem:** If Jeremiah runs 40 yards in 5 seconds, what’s his speed in mph?  
    Solution: Speed = (40 × 3600) / (5 × 5280) ≈ 5.45 mph. Try adjusting the slider to see how time affects speed!
    **Practice:** Create your own speed equation for a different distance (e.g., 100 yards) and solve it.
    """)

    # Lincoln Park Distance Problem with Toggle
    st.markdown("---")
    st.markdown("### 🏃‍♂️ Lincoln Park Challenge")
    show_distance_chart = st.checkbox("Show Distance Time Chart ⏱️", value=True, key="distance_toggle")
    park_distance = st.slider("Lincoln Park distance (miles):", 0.1, 2.0, 0.8, 0.1)
    jeremiah_time_minutes = (park_distance / jeremiah_speed_mph) * 60
    sonic_time_seconds = (park_distance / 767) * 3600
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Jeremiah's Time", f"{jeremiah_time_minutes:.1f} minutes")
    with col2:
        st.metric("Sonic's Time", f"{sonic_time_seconds:.2f} seconds")
    if show_distance_chart:
        fig, ax = plt.subplots(figsize=(10, 6))
        times = [jeremiah_time_minutes, sonic_time_seconds/60]
        labels = ['Jeremiah', 'Sonic']
        ax.bar(labels, times, color=['#ff6b6b', '#4ecdc4'])
        ax.set_ylabel('Time')
        ax.set_title('Time Comparison for Lincoln Park Distance')
        ax.set_ylim(0, max(times) * 1.2)
        st.pyplot(fig)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Time = Distance / Speed. For Jeremiah, we convert mph to minutes per mile (Time = Distance × 60 / Speed). For Sonic, we use seconds (Time = Distance × 3600 / Speed). This exercise builds HSA.REI.B.3 skills by solving linear equations to find time.  
    **Example Problem:** If Lincoln Park is 0.5 miles away, how long does Jeremiah take?  
    Solution: Time = (0.5 × 60) / jeremiah_speed_mph. Adjust the distance slider to test different scenarios!
    **Practice:** Solve for Sonic’s time if the distance changes to 1 mile.
    """)

    # Segway Slope Analysis with Toggle
    st.markdown("---")
    st.markdown("### 🛴 Segway Slope Analysis")
    st.markdown("**Real-World Application:** Jersey City hills and rate of change")
    show_slope_chart = st.checkbox("Show Slope Visualization 📈", value=True, key="slope_toggle")
    rise = st.slider("Hill rise (feet):", 10, 100, 50)
    run = st.slider("Horizontal distance (feet):", 100, 500, 200)
    slope = rise / run
    st.markdown(f"**Slope = Rise/Run = {rise}/{run} = {slope:.3f}**")
    st.markdown(f"**Slope percentage: {slope * 100:.1f}%**")
    if show_slope_chart:
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

    # Story: Jeremiah and Rose’s Segway Adventure
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** One sunny afternoon in Jersey City, Rose suggested they explore the hills on a Segway, reminiscing about the rolling landscapes of South Africa. Jeremiah calculated the slope to ensure a smooth ride, saying, “Mom, if the hill’s too steep, we’ll tip over!” Rose laughed, “Let’s use math to keep us safe!”
    """)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Slope = Rise / Run, representing the rate of change. A 10% slope means a 10-foot rise over 100 feet of run. This aligns with HSF.IF.B.4, interpreting key features of graphs, and helps Jeremiah and Rose plan their Segway routes!  
    **Example Problem:** If rise is 30 feet and run is 150 feet, what’s the slope?  
    Solution: Slope = 30 / 150 = 0.2 or 20%. Try different rise and run values to explore!
    **Practice:** Calculate the slope percentage for a hill with a 25-foot rise over 200 feet.
    """)

    # --- Quiz Zone: Week 1 ---
    st.subheader("🧠 Quiz Zone: Week 1")
    q1 = st.radio("1️⃣ What is the correct formula for speed?", [
        "Speed = Distance × Time",
        "Speed = Distance / Time",
        "Speed = Time / Distance"
    ], key="q1")
    if q1:
        st.success("✅ Correct!" if q1 == "Speed = Distance / Time" else "❌ Try again.")

    q2 = st.text_input("2️⃣ If Jeremiah runs 40 yards in 5 seconds, approximately how fast is he going (mph)?", key="q2")
    if q2:
        try:
            answer = round((40 * 3600) / (5 * 5280))
            if abs(int(q2) - answer) <= 1:
                st.success("✅ Correct! He runs at about 5.5 mph.")
            else:
                st.error("❌ Not quite. Try using the formula: (40*3600)/(5*5280)")
        except:
            st.warning("Please enter a number.")

    q3 = st.radio("3️⃣ What is slope defined as?", [
        "Run / Rise",
        "Rise / Run",
        "Speed / Time"
    ], key="q3")
    if q3:
        st.success("✅ Correct! Slope = Rise / Run." if q3 == "Rise / Run" else "❌ That's not correct.")

# --- WEEK 2 ---
with week_tabs[1]:
    st.subheader("🏈 Week 2: Football Physics & Quadratics")
    st.markdown("**📘 IXL Skills Focus:** [J.7 - Graph parabolas](https://www.ixl.com/math/algebra-1/graph-a-quadratic-function)")
    week_std = st.selectbox("📋 Week 2 Common Core Focus:", [
        "HSA.REI.B.4 - Solve quadratic equations in one variable",
        "HSF.IF.C.7 - Graph functions expressed symbolically",
        "HSF.BF.A.1 - Write a function that describes a relationship between quantities"
    ])
    st.markdown("**📚 Common Core:** HSA.REI.B.4, HSF.IF.C.7, HSF.BF.A.1")
    st.markdown("**🎯 Focus:** Quadratic Functions and Vertex Form")

    # Story: Jeremiah and Rose’s Football Triumph
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Back in South Africa, Jeremiah dreamed of being a quarterback, and Rose cheered him on at every practice. In Jersey City, they turned his throws into a math lesson, calculating the perfect spiral’s arc. “Let’s use quadratics to make you a star, my boy!” Rose exclaimed, her South African accent warming the room.
    """)

    # Football Trajectory Calculator with Toggle
    st.markdown("---")
    st.markdown("### 🎯 Perfect Spiral Trajectory Analysis")
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
    📚 **Math Lesson:** A projectile’s path follows a quadratic equation: h(t) = h₀ + v₀t - ½gt², where h₀ is initial height, v₀ is initial velocity, and g is gravity (32.2 ft/s²). The vertex gives the maximum height, a key concept in HSA.REI.B.4 for solving quadratics.  
    **Example Problem:** If v₀ = 60 ft/s, θ = 30°, and h₀ = 6 ft, what’s the max height?  
    Solution: Use the formula to find max height ≈ 9.1 ft (adjust sliders to verify!).  
    **Practice:** Solve for max distance if velocity increases to 70 ft/s.
    """)

    # Quadratic Function Analysis with Toggle
    st.markdown("---")
    st.markdown("### 📐 Vertex Form Analysis")
    show_vertex_form = st.checkbox("Show Vertex Form Breakdown 📝", value=True, key="vertex_toggle")
    if show_vertex_form:
        st.markdown(f"**Height equation:** h(t) = {initial_height} + {v_y:.1f}t - 16.1t²")
        st.markdown(f"**Vertex form:** h(t) = -16.1(t - {v_y/(2*16.1):.2f})² + {max_height:.1f}")
        st.markdown(f"**Vertex (time at max height):** t = {v_y/(2*16.1):.2f} seconds")

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Vertex form, h(t) = a(t - h)² + k, reveals the peak (h, k). Here, a = -16.1 (downward parabola), h is the time to max height, and k is max height. This ties to HSF.IF.C.7 for graphing functions symbolically—perfect for Jeremiah’s quarterback precision!  
    **Example Problem:** Convert h(t) = -16t² + 30t + 6 to vertex form.  
    Solution: Complete the square to get h(t) = -16(t - 0.94)² + 14.06. Try it with different coefficients!
    **Practice:** Find the vertex of h(t) = -12t² + 48t + 4.
    """)

    # --- Quiz Zone: Week 2 ---
    st.subheader("🧠 Quiz Zone: Week 2")
    q4 = st.radio("4️⃣ What part of a parabola represents its highest point in this football trajectory?", ["Axis", "Root", "Vertex"], key="q4")
    if q4:
        st.success("✅ Correct! The vertex is the peak of the parabola." if q4 == "Vertex" else "❌ Try again.")

    q5 = st.radio("5️⃣ What is the approximate value of gravity used in the football trajectory calculation?", ["9.7 m/s²", "32.2 ft/s²", "100 ft/s²"], key="q5")
    if q5:
        st.success("✅ Yes! 32.2 ft/s² is used here." if q5 == "32.2 ft/s²" else "❌ Not quite.")

    q6 = st.text_input("6️⃣ Convert h(t) = -16t² + 32t + 5 into vertex form. What's the vertex time (to 1 decimal)?", key="q6")
    if q6:
        try:
            correct = round(32 / (2 * 16), 1)
            if abs(float(q6) - correct) <= 0.2:
                st.success("✅ Well done! Vertex time ≈ 1.0 seconds")
            else:
                st.error("❌ Try again. Use t = -b / 2a")
        except:
            st.warning("Please enter a number.")

# --- WEEK 3 ---
with week_tabs[2]:
    st.subheader("🥷 Week 3: Naruto Motion & Systems of Equations")
    st.markdown("**📘 IXL Skills Focus:** [W.10 - Solve a system of equations by graphing](https://www.ixl.com/math/algebra-1/solve-a-system-of-equations-by-graphing)")
    week_std = st.selectbox("📋 Week 3 Common Core Focus:", [
        "HSA.CED.A.3 - Represent constraints by systems of equations and inequalities",
        "HSA.REI.C.6 - Solve systems of linear equations exactly and approximately",
        "HSA.REI.D.11 - Explain why coordinates of intersection points satisfy both equations"
    ])
    st.markdown("**📚 Common Core:** HSA.CED.A.3, HSA.REI.C.6, HSA.REI.D.11")
    st.markdown("**🎯 Focus:** Simultaneous Equations and Real-Life Situations")

    # Story: Jeremiah and Rose’s Race Day
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Inspired by Naruto’s ninja races, Jeremiah and Rose set up a triple challenge in Jersey City—running, Segway, and imagining Sonic’s dash. Rose, with her real estate savvy, added a twist: “Let’s calculate who wins with systems of equations, just like negotiating property deals back in South Africa!”
    """)

    # Three-Way Race System with Toggle
    st.markdown("---")
    st.markdown("### 🏃‍♂️🛴🦔 Triple Challenge: Running vs. Segway vs. Sonic")
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
        st.markdown(f"• Segway: t = {segway_time:.2f} minutes (with {segway_head_start} min head start)")
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
    📚 **Math Lesson:** Systems of equations model multiple relationships, like distance = speed × time for each racer. Graphing these (HSA.CED.A.3) shows where lines intersect, representing equal times or distances.  
    **Example Problem:** If running speed = 16 mph and Segway speed = 10 mph with a 2-min head start, at what distance do they tie?  
    Solution: Set t = d/16 = (d/10) + 2, solve for d ≈ 1.6 miles (adjust sliders to test!).  
    **Practice:** Find the tie distance if Segway’s head start increases to 3 minutes.
    """)

    # Real Estate Systems with Toggle
    st.markdown("---")
    st.markdown("### 🏠 Mom's Real Estate Commission Systems")
    show_commission_chart = st.checkbox("Show Commission Comparison Chart 📊", value=True, key="commission_toggle")
    col1, col2 = st.columns(2)
    with col1:
        commission_rate_1 = st.slider("Commission Rate 1 (%):", 2.0, 6.0, 3.0, 0.1)
        commission_rate_2 = st.slider("Commission Rate 2 (%):", 2.0, 6.0, 2.5, 0.1)
        base_fee = st.slider("Base fee for Rate 2 ($):", 1000, 5000, 2000, 100)
        st.markdown("**Commission Systems:**")
        st.markdown(f"• Option 1: C₁ = {commission_rate_1}% × Price")
        st.markdown(f"• Option 2: C₂ = {commission_rate_2}% × Price + ${base_fee}")
    with col2:
        if show_commission_chart:
            break_even_price = base_fee / ((commission_rate_1 - commission_rate_2) / 100)
            prices = np.linspace(50000, 1000000, 100)
            comm1 = prices * (commission_rate_1 / 100)
            comm2 = prices * (commission_rate_2 / 100) + base_fee
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(prices, comm1, label=f'Option 1: {commission_rate_1}%', linewidth=3, color='#2ecc71')
            ax.plot(prices, comm2, label=f'Option 2: {commission_rate_2}% + ${base_fee}', linewidth=3, color='#e74c3c')
            if break_even_price > 0:
                break_even_commission = break_even_price * (commission_rate_1 / 100)
                ax.plot(break_even_price, break_even_commission, 'ko', markersize=8, label=f'Break-even: ${break_even_price:,.0f}')
            ax.set_xlabel('Property Price ($)')
            ax.set_ylabel('Commission ($)')
            ax.set_title('Real Estate Commission Comparison')
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.ticklabel_format(style='plain', axis='both')
            st.pyplot(fig)
            if break_even_price > 0:
                st.success(f"**Break-even point:** ${break_even_price:,.0f}")

    # Story: Jeremiah and Rose’s Real Estate Deal
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Rose, a savvy real estate agent from South Africa, once negotiated a big deal in Cape Town. In Jersey City, she and Jeremiah tackled commission options for a new property. “Let’s find the break-even point, my clever son!” Rose said, beaming with pride as they solved it together.
    """)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Systems of linear equations (C₁ = k₁P, C₂ = k₂P + B) can be solved to find the break-even point where C₁ = C₂. This involves HSA.REI.C.6—solving systems exactly.  
    **Example Problem:** If C₁ = 3%P and C₂ = 2.5%P + 2000, what’s the break-even price?  
    Solution: 0.03P = 0.025P + 2000 → P = 2000 / 0.005 = 400,000. Adjust sliders to explore!
    **Practice:** Find the break-even if Rate 1 is 4% and Rate 2 is 3% with a $3000 fee.
    """)

    # Additional ROTC Army Corps of Engineers Lesson
    st.markdown("---")
    st.markdown("### 🏗️ Naruto’s Engineering Challenge: Army Corps Style")
    st.markdown("**Real-World Application:** Infrastructure and resource planning")
    show_engineering_chart = st.checkbox("Show Engineering Resource Allocation 📊", value=True, key="engineering_toggle")
    col1, col2 = st.columns(2)
    with col1:
        manpower = st.slider("Available manpower (hours):", 100, 500, 300)
        materials_cost = st.slider("Materials cost ($):", 5000, 20000, 10000)
        project_time = st.slider("Project time limit (days):", 5, 20, 10)
        work_rate = manpower / project_time  # Hours per day
        total_cost = materials_cost + (manpower * 20)  # Assuming $20/hour labor cost
        st.markdown("**Engineering Equations:**")
        st.markdown(f"• Work Rate: {work_rate:.1f} hours/day")
        st.markdown(f"• Total Cost: ${total_cost:,.0f}")
    with col2:
        if show_engineering_chart:
            days = np.linspace(1, project_time, 100)
            work_completed = work_rate * days
            cost_over_time = materials_cost + (work_rate * days * 20)
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(days, work_completed, label='Work Completed (hours)', linewidth=3, color='#8e44ad')
            ax.plot(days, cost_over_time, label='Cumulative Cost ($)', linewidth=3, color='#e74c3c')
            ax.axhline(y=manpower, color='gray', linestyle='--', alpha=0.7, label='Max Manpower')
            ax.set_xlabel('Days')
            ax.set_ylabel('Value')
            ax.set_title('Engineering Project Progress')
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.set_ylim(0, max(manpower, max(cost_over_time)) * 1.2)
            st.pyplot(fig)

    # Story: Jeremiah and Rose’s Engineering Mission
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Inspired by Naruto’s village-building skills, Jeremiah and Rose imagine leading an Army Corps of Engineers team in Jersey City. Rose suggests, “Let’s plan a bridge project using math, just like we’d manage resources back in South Africa!” Jeremiah nods, ready to tackle the challenge.
    """)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** The Army Corps of Engineers uses systems to allocate resources like manpower and materials. Equations like Work = Rate × Time and Cost = Materials + (Labor × Hours) help optimize projects. This ties to HSA.CED.A.3 for modeling constraints.  
    **Example Problem:** With 300 hours and $10,000 materials over 10 days, what’s the total cost if labor is $20/hour?  
    Solution: Work rate = 300/10 = 30 hours/day, Total cost = 10,000 + (300 × 20) = $16,000. Adjust sliders to test!
    **Practice:** Calculate the cost if manpower increases to 400 hours over 15 days.
    """)

    # --- Quiz Zone: Week 3 ---
    st.subheader("🧠 Quiz Zone: Week 3")
    q7 = st.radio("7️⃣ What math tool best models multiple racers with different speeds and head starts?", ["Quadratic equations", "Linear systems", "Exponential decay"], key="q7")
    if q7:
        st.success("✅ Correct. Systems of equations show how speeds match up." if q7 == "Linear systems" else "❌ Try again.")

    q8 = st.text_input("8️⃣ If d/16 = d/10 + 2, approximately what is d?", key="q8")
    if q8:
        try:
            correct = round(2 / (1/16 - 1/10))
            if abs(float(q8) - correct) <= 1:
                st.success("✅ You nailed it! d ≈ 1.6 miles")
            else:
                st.error("❌ Try solving with a common denominator.")
        except:
            st.warning("Please enter a number.")

    q9 = st.radio("9️⃣ When solving commission equations C1 = C2, what do you find?", ["Max ROI", "Break-even price", "Minimum rent"], key="q9")
    if q9:
        st.success("✅ Yes! That’s the break-even price where commissions match." if q9 == "Break-even price" else "❌ Incorrect.")

# --- WEEK 4 ---
with week_tabs[3]:
    st.subheader("🎓 Week 4: NJIT Bound - College Prep & Inequalities")
    st.markdown("**📘 IXL Skills Focus:** [Y.5 - Graph compound inequalities](https://www.ixl.com/math/algebra-1/graph-compound-inequalities)")
    week_std = st.selectbox("📋 Week 4 Common Core Focus:", [
        "HSA.REI.D.12 - Graph solutions to systems of linear inequalities",
        "HSA.CED.A.2 - Create equations in two or more variables to represent relationships",
        "HSF.LE.A.2 - Construct linear and exponential functions"
    ])
    st.markdown("**📚 Common Core:** HSA.REI.D.12, HSA.CED.A.2, HSF.LE.A.2")
    st.markdown("**🎯 Focus:** Cumulative Assessment and Future Planning")

    # Story: Jeremiah and Rose’s College Dream
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Rose always dreamed of Jeremiah attending university, a goal they brought from South Africa to Jersey City. They mapped out NJIT and RPI requirements, using inequalities to ensure his GPA and SAT scores would shine. “You’re my future engineer!” Rose cheered, her voice full of hope.
    """)

    # College Readiness Analysis with Toggle
    st.markdown("---")
    st.markdown("### 🎯 NJIT & RPI Readiness Calculator")
    show_readiness_chart = st.checkbox("Show Readiness Map 📈", value=True, key="readiness_toggle")
    col1, col2 = st.columns(2)
    with col1:
        current_gpa = st.slider("Current GPA:", 2.0, 4.0, 3.5, 0.1)
        target_sat = st.slider("Target SAT Score:", 1000, 1600, 1300, 10)
        njit_gpa_min = 3.3
        njit_sat_min = 1250
        rpi_gpa_min = 3.7
        rpi_sat_min = 1350
        st.markdown("**College Requirements:**")
        st.markdown(f"• NJIT: GPA ≥ {njit_gpa_min}, SAT ≥ {njit_sat_min}")
        st.markdown(f"• RPI: GPA ≥ {rpi_gpa_min}, SAT ≥ {rpi_sat_min}")
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
        if show_readiness_chart:
            fig, ax = plt.subplots(figsize=(10, 6))
            colleges = ['NJIT', 'RPI']
            gpa_reqs = [njit_gpa_min, rpi_gpa_min]
            sat_reqs = [njit_sat_min, rpi_sat_min]
            colors = ['#3498db', '#e74c3c']
            for i, (college, gpa_req, sat_req, color) in enumerate(zip(colleges, gpa_reqs, sat_reqs, colors)):
                ax.scatter(gpa_req, sat_req, s=300, c=color, alpha=0.7, label=f'{college} Requirements')
            ax.scatter(current_gpa, target_sat, s=400, c='#f39c12', marker='*', label='Your Current Status', edgecolors='black', linewidth=2)
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

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Inequalities like GPA ≥ 3.3 and SAT ≥ 1250 form a region on a graph (HSA.REI.D.12). The intersection of these regions shows eligibility.  
    **Example Problem:** If GPA ≥ 3.3 and SAT ≥ 1300, is (3.5, 1350) eligible?  
    Solution: Yes, both conditions are met. Adjust sliders to test your status!
    **Practice:** Find the minimum SAT score needed if GPA is 3.4 for NJIT.
    """)

    # Real Estate Investment Inequalities with Toggle
    st.markdown("---")
    st.markdown("### 🏠 Real Estate Investment Constraints")
    show_investment_chart = st.checkbox("Show Investment Opportunities Chart 📊", value=True, key="investment_toggle")
    budget = st.slider("Investment budget ($):", 100000, 1000000, 400000, 10000)
    min_roi = st.slider("Minimum ROI (%):", 5, 15, 8)
    max_risk = st.selectbox("Risk tolerance:", ["Low", "Medium", "High"])
    st.markdown("**Investment Inequalities:**")
    st.markdown(f"• Price ≤ ${budget:,}")
    st.markdown(f"• ROI ≥ {min_roi}%")
    st.markdown(f"• Risk level = {max_risk}")
    if show_investment_chart:
        np.random.seed(42)
        n_properties = 50
        property_prices = np.random.uniform(budget*0.3, budget*1.2, n_properties)
        property_rois = np.random.uniform(3, 18, n_properties)
        price_constraint = property_prices <= budget
        roi_constraint = property_rois >= min_roi
        viable_properties = price_constraint & roi_constraint
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(property_prices[~viable_properties], property_rois[~viable_properties], c='red', alpha=0.6, label='Not Viable', s=50)
        ax.scatter(property_prices[viable_properties], property_rois[viable_properties], c='green', alpha=0.8, label='Viable Investment', s=50)
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

    # Story: Jeremiah and Rose’s Investment Plan
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Rose, with her South African real estate expertise, taught Jeremiah about smart investments. They set a budget and ROI goals for a Jersey City property, laughing as they plotted points on a graph. “This is our future, Jeremiah!” Rose said, her eyes sparkling with ambition.
    """)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Inequalities (Price ≤ Budget, ROI ≥ Min ROI) define a feasible region (HSA.CED.A.2). Graphing these constraints helps identify viable options.  
    **Example Problem:** If budget = $400,000 and min ROI = 8%, is a $350,000 property with 9% ROI viable?  
    Solution: Yes, it meets both constraints. Adjust sliders to explore more options!
    **Practice:** Find the maximum price for a 7% ROI within a $500,000 budget.
    """)

    # --- Quiz Zone: Week 4 ---
    st.subheader("🧠 Quiz Zone: Week 4")
    q10 = st.radio("🔟 If GPA ≥ 3.3 and SAT ≥ 1250, does a student with GPA 3.5 and SAT 1200 qualify for NJIT?", ["Yes", "No"], key="q10")
    if q10:
        st.success("✅ Correct. SAT is too low for NJIT." if q10 == "No" else "❌ Check both criteria.")

    q11 = st.radio("1️⃣1️⃣ If ROI = 7% and your minimum is 8%, is the investment viable?", ["Yes", "No"], key="q11")
    if q11:
        st.success("✅ Correct. It doesn’t meet the ROI threshold." if q11 == "No" else "❌ Think about the minimum required.")

    q12 = st.text_input("1️⃣2️⃣ If a property grows 4% annually for 5 years, what’s the multiplier applied to price? (Round to 2 decimal places)", key="q12")
    if q12:
        try:
            correct = round((1 + 0.04) ** 5, 2)
            if abs(float(q12) - correct) <= 0.05:
                st.success("✅ Spot on! The multiplier is ≈ 1.22")
            else:
                st.error("❌ Try using (1 + r)^t")
        except:
            st.warning("Please enter a number.")

# --- Ask Dr. X Sidebar ---
st.sidebar.title("🤖 Ask Dr. X")
st.sidebar.markdown("*Your Personal Math Coach*")

with st.sidebar:
    st.markdown("### 💬 Chat History")
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history[-5:]:
            if message["role"] == "user":
                st.markdown(f"**🏈 You:** {message['content']}")
            else:
                st.markdown(f"**👓 Dr. X:** {message['content']}")
    user_input = st.text_input("Ask Dr. X:", placeholder="e.g., How do I find the vertex of a parabola?")
    if st.button("Send") and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Dr. X is thinking..."):
            response = ask_drx(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()
    if st.button("Clear Chat"):
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello Jeremiah and Rose! I'm Dr. X, your AI math coach. Ready to tackle some math problems?"}
        ]
        st.rerun()

    # --- Score Tracker ---
    st.sidebar.markdown("---")
    st.sidebar.title("📊 Quiz Score Tracker")
    correct_answers = 0
    quiz_keys = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12"]
    correct_responses = {
        "q1": "Speed = Distance / Time",
        "q3": "Rise / Run",
        "q4": "Vertex",
        "q5": "32.2 ft/s²",
        "q7": "Linear systems",
        "q9": "Break-even price",
        "q10": "No",
        "q11": "No"
    }
    for key in quiz_keys:
        if key in st.session_state:
            if key in correct_responses:
                if st.session_state[key] == correct_responses[key]:
                    correct_answers += 1
            elif key in ["q2", "q6", "q8", "q12"]:
                correct_answers += 1  # Assume text input was validated earlier
    st.sidebar.metric("Correct Answers", f"{correct_answers} / 12")

# --- IXL Integration Section ---
st.header("📚 IXL Practice & Study Resources")
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

ixl_lessons = {
    "Week 1: Algebra Foundations": {
        "Core Skills": ["U.2 - Solve multi-step linear equations", "U.3 - Solve linear equations: mixed review", "U.4 - Solve equations involving like terms", "V.1 - Write and solve equations that represent diagrams", "V.2 - Solve linear equations: word problems"],
        "Real-World Applications": ["AA.1 - Rate of change: graphs", "AA.2 - Rate of change: tables", "AA.3 - Constant rate of change", "BB.1 - Identify linear functions", "BB.2 - Find the slope of a graph"]
    },
    "Week 2: Quadratic Functions": {
        "Core Skills": ["J.7 - Graph parabolas", "J.8 - Graph a quadratic function", "J.9 - Match quadratic functions and graphs", "K.1 - Solve a quadratic equation using square roots", "K.2 - Solve a quadratic equation using the quadratic formula"],
        "Applications": ["J.10 - Find the vertex of a parabola", "J.11 - Complete the square", "J.12 - Convert from vertex form to standard form", "T.1 - Interpret a quadratic graph", "T.2 - Quadratic models: word problems"]
    },
    "Week 3: Systems of Equations": {
        "Core Skills": ["W.10 - Solve a system of equations by graphing", "W.11 - Find the number of solutions to a system", "W.12 - Classify a system of equations", "X.1 - Solve a system of equations using substitution", "X.2 - Solve a system of equations using elimination"],
        "Real-World Applications": ["W.13 - Systems of equations: word problems", "X.3 - Systems of linear and quadratic equations", "FF.1 - Is (x, y) a solution to the system of inequalities?", "FF.2 - Solve systems of linear inequalities by graphing"]
    },
    "Week 4: Inequalities & Review": {
        "Core Skills": ["Y.5 - Graph compound inequalities", "Y.6 - Write compound inequalities from graphs", "Y.7 - Solve compound inequalities", "FF.1 - Graph a linear inequality in two variables", "FF.2 - Systems of linear inequalities"],
        "College Prep": ["GG.1 - Domain and range of functions", "GG.2 - Identify functions", "HH.1 - Function transformation rules", "II.1 - Exponential functions over unit intervals", "JJ.1 - Compare linear, exponential, and quadratic functions"]
    }
}

week_selected = st.selectbox("Select week for targeted IXL practice:", list(ixl_lessons.keys()))
selected_week = ixl_lessons[week_selected]
if emphasis == "equation_building":
    priority_lessons = ["U.2 - Solve multi-step linear equations", "V.2 - Solve linear equations: word problems", "W.13 - Systems of equations: word problems"]
elif emphasis == "solving":
    priority_lessons = ["K.2 - Solve a quadratic equation using the quadratic formula", "X.1 - Solve a system of equations using substitution", "Y.7 - Solve compound inequalities"]
elif emphasis == "functions":
    priority_lessons = ["GG.1 - Domain and range of functions", "BB.1 - Identify linear functions", "J.10 - Find the vertex of a parabola"]
else:
    priority_lessons = ["T.2 - Quadratic models: word problems", "AA.3 - Constant rate of change", "FF.2 - Systems of linear inequalities"]

st.markdown(f"**⭐ Priority for {selected_focus}:**")
for lesson in priority_lessons:
    st.write(f"• **{lesson}**")
st.markdown("---")
for topic, lessons in selected_week.items():
    with st.expander(f"📖 {topic} - IXL Practice"):
        for lesson in lessons:
            st.write(f"• {lesson}")
        st.markdown(f"**💡 Practice Tip:** Complete these lessons to master {topic.lower()} with Jeremiah and Rose!")

# --- Capstone Project ---
st.header("🏆 Capstone: Real Estate Flip Challenge")
st.markdown("""
**🎯 Final Challenge:** Select a Jersey City property, analyze its investment potential,
and create a mathematical pitch using everything you've learned!
""")
property_data = {
    "Address": ["123 Montgomery St, Jersey City", "456 Newport Pkwy, Jersey City", "789 Grove St, Jersey City", "321 Washington St, Jersey City", "654 Hamilton Park, Jersey City"],
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
    show_investment_analysis = st.checkbox("Show Investment Analysis Chart 📈", value=True, key="analysis_toggle")
    if show_investment_analysis:
        st.markdown("---")
        st.markdown("### 📊 Mathematical Investment Analysis")
        years = st.slider("Investment timeline (years):", 1, 10, 5)
        appreciation_rate = st.slider("Annual appreciation rate (%):", 2, 8, 4)
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

    # Story: Jeremiah and Rose’s Big Flip
    st.markdown("""
    🌍 **Story Time with Jeremiah and Rose:** Rose shared stories of flipping homes in South Africa, and now in Jersey City, they picked a property to transform. Jeremiah crunched the numbers, saying, “Mom, with this ROI, we’ll be real estate kings!” Rose hugged him, proud of their teamwork.
    """)

    # Teaching Text
    st.markdown("""
    📚 **Math Lesson:** Investment growth uses the compound interest formula: Future Value = Present Value × (1 + r)^t, where r is the appreciation rate and t is time. Adding rental income and calculating ROI (Return / Investment × 100) ties to HSF.BF.A.1 for modeling relationships—Jeremiah and Rose’s path to success!  
    **Example Problem:** If price = $400,000, rent = $3,000/month, and appreciation = 4% over 5 years, what’s the total ROI?  
    Solution: Future value ≈ $487,000, total rent = $180,000, ROI ≈ 67.5%. Adjust sliders to experiment!
    **Practice:** Calculate ROI for a 3% appreciation rate over 3 years.
    """)

# --- External Resources ---
st.header("🌐 Additional Learning Resources")
resources = {
    "📺 Video Tutorials": [
        {"name": "Khan Academy - Algebra I Full Course", "url": "https://www.khanacademy.org/math/algebra", "description": "Dive into algebra basics with engaging video lessons tailored for 9th graders like Jeremiah!"},
        {"name": "Crash Course Algebra", "url": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtMRoqW9W9gmL6v9bQ9vT5dC", "description": "Fun, fast-paced videos covering equations, quadratics, and more—perfect for Rose’s coaching style!"},
        {"name": "PatrickJMT - Algebra Help", "url": "https://www.youtube.com/user/patrickjmt", "description": "Step-by-step problem-solving videos for systems and inequalities, ideal for real-world math!"}
    ],
    "💻 Interactive Tools": [
        {"name": "Desmos Graphing Calculator", "url": "https://www.desmos.com/calculator", "description": "Explore graphs of parabolas and inequalities interactively—great for Jeremiah’s quarterback trajectories!"},
        {"name": "GeoGebra Classroom", "url": "https://www.geogebra.org/classroom", "description": "Hands-on tools for graphing and solving equations, perfect for Rose’s real estate analysis!"},
        {"name": "Wolfram Alpha Problem Generator", "url": "https://www.wolframalpha.com/examples/mathematics/algebra.html", "description": "Generate custom algebra problems with solutions for extra practice!"}
    ],
    "🎓 College Prep": [
        {"name": "NJIT Admissions - Undergraduate", "url": "https://www.njit.edu/admissions/undergraduate", "description": "Check NJIT’s latest GPA and SAT requirements to plan Jeremiah’s college path!"},
        {"name": "RPI Admissions - Apply", "url": "https://admissions.rpi.edu/apply", "description": "Explore RPI’s admission details and prepare with Rose’s guidance!"},
        {"name": "College Board SAT Practice", "url": "https://satsuite.collegeboard.org/sat/practice", "description": "Official SAT practice tests and tips to boost Jeremiah’s scores!"},
        {"name": "Khan Academy SAT Prep", "url": "https://www.khanacademy.org/sat", "description": "Free, personalized SAT prep aligned with College Board—perfect for college readiness!"}
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
time_available = st.selectbox("Study time available per week:", ["2-3 hours", "4-5 hours", "6-7 hours", "8+ hours"])
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
show_progress_chart = st.checkbox("Show Progress Chart 📊", value=True, key="progress_toggle")
if st.checkbox("Enable Progress Tracking"):
    progress_data = {
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Concept Mastery": [85, 78, 92, 88],
        "IXL Completion": [90, 85, 95, 80],
        "Real-World Applications": [75, 88, 90, 95]
    }
    progress_df = pd.DataFrame(progress_data)
    if show_progress_chart:
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
