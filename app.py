import streamlit as st
import numpy as np
import requests

# Page setup
st.set_page_config(
    page_title="MathCraft: Quest for the Quarterback Crown", 
    page_icon="🏈",
    layout="wide"
)

# Header
st.markdown("### www.cognitivecloud.ai")
st.markdown("**Developed for Jersey City by Xavier Honablue M.Ed**")
st.markdown("*Target Universities: NJIT & RPI*")
st.markdown("---")

# Title
st.title("🏈 MathCraft: Quest for the Quarterback Crown")
st.markdown("""
**A 4-Week Challenge-Based Math Journey for Jeremiah Erskine**

Welcome, **Future NJIT Engineer**! This MathCraft program transforms 9th grade math review into an epic quest connecting your passions—quarterback mechanics, Sonic speed, Segway adventures, and real estate success with Mom—into mathematical mastery.
""")

# Program Goal
st.markdown("""
### 🎯 Program Goal:
Prepare Jeremiah for a confident and successful 10th grade math experience by reinforcing foundational 9th grade skills through a personalized, interest-based curriculum rooted in Common Core standards.

### 🧰 Academic Tools
- **Ask Dr. X Live Widget** (API-enabled sidebar tutor)
- **Interactive Dashboard**: Sliders, animations, and built-in gamification
- **Algebra Tiles** – Visual algebra modeling
- **TI-84 Plus Emulator** – Practice calculator functions online

### 🎓 College Targeting
- [New Jersey Institute of Technology (NJIT)](https://www.njit.edu/admissions)
- [Rensselaer Polytechnic Institute (RPI)](https://admissions.rpi.edu/undergraduate)

### 🏠 Real-World Math Connection
- Real estate math in collaboration with Mom's business
- [Zillow Jersey City Listings](https://www.zillow.com/jersey-city-nj/)
- Square footage estimators and ROI predictions
""")

# Common Core Standards
st.info("📚 **Common Core Alignment:** This program addresses High School Algebra standards including creating equations (HSA.CED), reasoning with equations (HSA.REI), and building functions (HSF.BF) through real-world applications.")

# Student Info
st.subheader("🎮 Quarterback Profile Setup")
name = st.text_input("Enter your name:", value="Jeremiah Erskine")
position = st.selectbox("Choose your mathematical identity:", [
    "🏈 Quarterback Analyst", "🦔 Speed Calculator", "🛴 Slope Navigator", 
    "🏠 Real Estate Mathematician", "🎯 NJIT Bound Scholar"
])

if name:
    st.success(f"Welcome, {name} the {position}! Ready to dominate 10th grade math!")

# Initialize session state for chat
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

# Sidebar navigation
st.sidebar.title("📚 Navigation")
selected = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home", "📈 Week 1", "📊 Week 2", "🔄 Week 3", "🎓 Week 4", "🤖 Dr. X"]
)

# Initialize progress tracking
if 'total_points' not in st.session_state:
    st.session_state.total_points = 0

if 'achievements' not in st.session_state:
    st.session_state.achievements = []

# Progress display
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 Your Progress")
st.sidebar.metric("Total XP", st.session_state.total_points, "⭐")

if st.session_state.achievements:
    st.sidebar.markdown("### 🏅 Achievements")
    for achievement in st.session_state.achievements:
        st.sidebar.markdown(f"• {achievement}")

# Main content based on selection
if selected == "🏠 Home":
    st.markdown("""
    ## 🚀 Welcome to Your Mathematical Journey!
    
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
        ### Week 1: Linear Functions
        **Segway Hills & Quarterback Math**
        - Slope, rate of change, and real-world applications
        
        ### Week 3: Exponential Functions
        **Growth & Real Estate Investment**
        - Compound interest and performance modeling
        """)
    
    with col2:
        st.markdown("""
        ### Week 2: Quadratic Functions
        **Football Trajectories & Sonic Jumps**
        - Parabolic motion and optimization
        
        ### Week 4: Advanced Topics
        **NJIT & RPI Preparation**
        - Statistics, trigonometry, and college readiness
        """)

elif selected == "📈 Week 1":
    st.title("📈 Week 1: Linear Functions & Real-World Applications")
    
    st.markdown("**📘 IXL Skills Focus:** Solve multi-step linear equations")
    st.markdown("**📚 Common Core:** HSA.CED.A.1, HSA.REI.B.3")
    st.markdown("**🎯 Focus:** Expressions, Equations, and Linear Functions")
    
    # Sonic Speed Calculator
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
        st.markdown(f"""
        **📊 Speed Calculations Explained:**
        
        Your 40-yard dash time: {jeremiah_40_time} seconds
        
        **Step 1:** Convert yards to miles
        - 40 yards ÷ 1,760 yards/mile = {40/1760:.6f} miles
        
        **Step 2:** Convert seconds to hours  
        - {jeremiah_40_time} seconds ÷ 3,600 seconds/hour = {jeremiah_40_time/3600:.6f} hours
        
        **Step 3:** Calculate speed using v = d/t
        - Speed = {40/1760:.6f} miles ÷ {jeremiah_40_time/3600:.6f} hours = {jeremiah_speed_mph:.1f} mph
        """)
    
    # Slope Analysis
    st.markdown("---")
    st.markdown("### 🛴 Segway Slope Analysis")
    
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
    """)

elif selected == "📊 Week 2":
    st.title("📊 Week 2: Quadratic Functions & Parabolic Motion")
    
    st.markdown("**📘 IXL Skills Focus:** Graph parabolas")
    st.markdown("**📚 Common Core:** HSA.REI.B.4")
    st.markdown("**🎯 Focus:** Quadratic Functions and Vertex Form")
    
    # Football Trajectory Calculator
    st.markdown("---")
    st.markdown("### 🎯 Perfect Spiral Trajectory Analysis")
    
    st.markdown("""
    **📚 Mathematical Concept:** Projectile motion follows a **parabolic path** described by quadratic 
    functions. The height of any projectile can be modeled by:
    
    **h(t) = -16t² + v₀t + h₀**
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
        st.markdown(f"""
        **📊 Complete Mathematical Breakdown:**
        
        **Given Parameters:**
        - Initial velocity: {initial_velocity} ft/s at {launch_angle}° angle
        - Release height: {initial_height} feet
        
        **Step 1: Resolve Velocity Components**
        - Horizontal velocity: vₓ = {initial_velocity} × cos({launch_angle}°) = {v_x:.1f} ft/s
        - Vertical velocity: vᵧ = {initial_velocity} × sin({launch_angle}°) = {v_y:.1f} ft/s
        
        **Step 2: Create Height Function**
        - h(t) = {initial_height} + {v_y:.1f}t - 16t²
        
        **Step 3: Find Key Features**
        - **Maximum Height:** {max_height:.1f} feet
        - **Flight Time:** {flight_time:.2f} seconds
        - **Range:** {max_distance:.1f} feet
        """)

elif selected == "🔄 Week 3":
    st.title("📈 Week 3: Exponential and Radical Functions")
    
    st.markdown("**📘 IXL Skills Focus:** Exponential functions")
    st.markdown("**📚 Common Core:** HSF.LE.A.2")
    st.markdown("**🎯 Focus:** Growth, Decay, and Real Estate Investment")
    
    # Exponential Growth
    st.markdown("---")
    st.markdown("### 📈 Exponential Growth Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        growth_type = st.selectbox("Choose growth scenario:", 
                                 ["Athletic Performance", "Real Estate Investment", "Compound Interest"])
        
        if growth_type == "Athletic Performance":
            initial_value = st.slider("Initial throwing distance (yards):", 20, 60, 35)
            growth_rate = st.slider("Weekly improvement rate (%):", 1, 15, 5)
            time_period = st.slider("Training weeks:", 1, 52, 20)
            
        elif growth_type == "Real Estate Investment":
            initial_value = st.slider("Initial property value ($):", 200000, 800000, 400000, 10000)
            growth_rate = st.slider("Annual appreciation rate (%):", 1, 12, 4)
            time_period = st.slider("Investment years:", 1, 30, 10)
            
        else:  # Compound Interest
            initial_value = st.slider("Initial investment ($):", 1000, 50000, 10000, 500)
            growth_rate = st.slider("Annual interest rate (%):", 1, 15, 7)
            time_period = st.slider("Investment years:", 1, 40, 20)
    
    with col2:
        # Calculate exponential growth
        growth_decimal = growth_rate / 100
        final_exponential = initial_value * ((1 + growth_decimal) ** time_period)
        final_linear = initial_value + (initial_value * growth_decimal * time_period)
        difference = final_exponential - final_linear
        
        st.success(f"""
        **📊 Growth Analysis:**
        - **Exponential Final Value:** {final_exponential:,.0f}
        - **Linear Final Value:** {final_linear:,.0f}
        - **Exponential Advantage:** {difference:,.0f} ({((difference/final_linear)*100):.1f}% more!)
        """)

elif selected == "🎓 Week 4":
    st.title("🎓 Week 4: Advanced Topics and College Preparation")
    
    st.markdown("**📘 IXL Skills Focus:** Statistics and Data Analysis")
    st.markdown("**📚 Common Core:** HSS.ID.B.6")
    st.markdown("**🎯 Focus:** Data Analysis, College Readiness, and Future Planning")
    
    # College Readiness
    st.markdown("---")
    st.markdown("### 🎯 NJIT & RPI Readiness Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_gpa = st.slider("Current GPA:", 2.0, 4.0, 3.5, 0.1)
        target_sat = st.slider("Target SAT Score:", 1000, 1600, 1300, 10)
        extracurriculars = st.slider("Extracurricular Activities:", 0, 10, 4)
        
        # NJIT and RPI requirements
        njit_gpa_min = 3.3
        njit_sat_min = 1250
        rpi_gpa_min = 3.7
        rpi_sat_min = 1350
        
        njit_gpa_ready = current_gpa >= njit_gpa_min
        njit_sat_ready = target_sat >= njit_sat_min
        rpi_gpa_ready = current_gpa >= rpi_gpa_min
        rpi_sat_ready = target_sat >= rpi_sat_min
    
    with col2:
        st.markdown("**College Requirements:**")
        st.markdown(f"• NJIT: GPA ≥ {njit_gpa_min}, SAT ≥ {njit_sat_min}")
        st.markdown(f"• RPI: GPA ≥ {rpi_gpa_min}, SAT ≥ {rpi_sat_min}")
        
        st.markdown("**Your Status:**")
        st.markdown(f"• NJIT GPA: {'✅' if njit_gpa_ready else '❌'} ({current_gpa})")
        st.markdown(f"• NJIT SAT: {'✅' if njit_sat_ready else '❌'} ({target_sat})")
        st.markdown(f"• RPI GPA: {'✅' if rpi_gpa_ready else '❌'} ({current_gpa})")
        st.markdown(f"• RPI SAT: {'✅' if rpi_sat_ready else '❌'} ({target_sat})")

elif selected == "🤖 Dr. X":
    st.title("🤖 Ask Dr. X - Your AI Math Tutor")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
        <h3>👓 Dr. X is here to help!</h3>
        <p>Ask me anything about math - whether it's quadratic equations, football trajectories, 
        real estate calculations, or college prep questions!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick help buttons
    st.markdown("### 🎯 Quick Help Topics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏈 Football Math"):
            question = "Help me understand the math behind football trajectories and optimal throwing angles."
            st.session_state.chat_history.append({"role": "user", "content": question})
            response = ask_drx(question)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col2:
        if st.button("🏠 Real Estate"):
            question = "Explain how to calculate real estate ROI and commission structures."
            st.session_state.chat_history.append({"role": "user", "content": question})
            response = ask_drx(question)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col3:
        if st.button("📊 Quadratics"):
            question = "I need help understanding vertex form and completing the square."
            st.session_state.chat_history.append({"role": "user", "content": question})
            response = ask_drx(question)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col4:
        if st.button("🎓 College Prep"):
            question = "What math skills do I need for NJIT and RPI admissions?"
            st.session_state.chat_history.append({"role": "user", "content": question})
            response = ask_drx(question)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Display chat history
    st.markdown("### 💬 Chat with Dr. X")
    
    for message in st.session_state.chat_history:
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
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        if st.button("Send 📤") and user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            with st.spinner("Dr. X is thinking..."):
                response = ask_drx(user_input)
            
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.session_state.total_points += 2
            
            if len([msg for msg in st.session_state.chat_history if msg["role"] == "user"]) >= 10:
                if "💬 Chat Champion" not in st.session_state.achievements:
                    st.session_state.achievements.append("💬 Chat Champion")
            
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Hello Jeremiah! I'm Dr. X, your AI math coach. Ready to tackle some math problems?"}
            ]
            st.rerun()

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
