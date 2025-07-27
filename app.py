import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="MathCraft: 4-Week Math Mastery for Jeremiah",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .week-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .activity-box {
        background: #e8f4fd;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #007bff;
    }
    .personal-connection {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #ffc107;
    }
    .standards-box {
        background: #d1ecf1;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #17a2b8;
    }
    .drx-chat {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #dee2e6;
        max-height: 300px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello Jeremiah! I'm Dr. X, your AI math tutor. Whether you need help with quadratic equations, want to calculate football trajectories, or understand real estate mathematics, just ask!"}
    ]

# Header
st.markdown("""
<div class="main-header">
    <h1>🏈 MathCraft 📊</h1>
    <h3>4-Week 9th Grade Math Mastery Program</h3>
    <p>Designed for Jeremiah Erskine - Jersey City</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home & Introduction", "📈 Week 1: Linear Functions", "📊 Week 2: Quadratics", 
     "📈 Week 3: Exponential & Radicals", "🎓 Week 4: College Prep", "🤖 Ask Dr. X"]
)

# Function to call Dr. X API
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
            return "Sorry, I'm having trouble connecting right now. Please try again."
    except Exception as e:
        return "Sorry, I'm having trouble connecting right now. Please try again."

# Home page
if page == "🏠 Home & Introduction":
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
elif page == "📈 Week 1: Linear Functions":
    st.title("📈 Week 1: Linear Functions & Real-World Applications")
    
    day = st.selectbox("Choose a day:", 
                      ["Day 1: Segway Hill Challenge", "Day 2: Speed Calculations", 
                       "Day 3: Systems of Equations", "Day 4: Linear Inequalities", "Day 5: Review Project"])
    
    if day == "Day 1: Segway Hill Challenge":
        st.markdown("""
        <div class="personal-connection">
            <strong>🛴 Personal Connection:</strong> Remember navigating those Jersey City hills on your Segway? Every hill has a slope, and understanding slope is crucial for both football field positioning and real estate property analysis.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="standards-box">
            <strong>📚 Common Core Standards:</strong>
            <ul>
                <li>A-CED.2: Create equations in two or more variables to represent relationships</li>
                <li>F-IF.6: Calculate and interpret the average rate of change</li>
                <li>A-REI.10: Represent and solve systems of equations graphically</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🎯 Activity 1: "Segway Speed Analysis"</h4>
            <p>Your Segway can reach 10 mph. If you travel up a hill that rises 50 feet over a horizontal distance of 200 feet:</p>
            <ul>
                <li>Calculate the slope of the hill</li>
                <li>Determine how your speed changes with incline</li>
                <li>Graph the relationship between incline and speed</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏈 Activity 2: "Quarterback Throwing Mechanics"</h4>
            <p>Analyze the trajectory of your football throws:</p>
            <ul>
                <li>Chart the path of a 30-yard pass</li>
                <li>Calculate the rate of change in height over distance</li>
                <li>Compare different throwing angles and their slopes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏠 Activity 3: "Real Estate Property Analysis"</h4>
            <p>Help your mom analyze property values:</p>
            <ul>
                <li>Graph Jersey City home prices over the last 5 years</li>
                <li>Calculate the average rate of change in property values</li>
                <li>Predict future trends using linear models</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif day == "Day 2: Speed Calculations":
        st.markdown("""
        <div class="personal-connection">
            <strong>💨 Personal Connection:</strong> Sonic's speed has always fascinated you. Let's explore how linear equations help us understand motion, from Sonic's fictional speed to your real quarterback arm strength.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🦔 Activity 1: "Sonic Speed Calculations"</h4>
            <p>If Sonic runs at his canonical speed of 767 mph (speed of sound):</p>
            <ul>
                <li>Write an equation for distance traveled over time</li>
                <li>Compare this to your running speed during football practice</li>
                <li>Create a linear model showing the difference</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏈 Activity 2: "Football Field Positioning"</h4>
            <p>As quarterback, you need to understand field positioning:</p>
            <ul>
                <li>Model the relationship between down and distance</li>
                <li>Create equations for optimal passing zones</li>
                <li>Calculate completion percentages based on distance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>💰 Activity 3: "Real Estate Commission Calculations"</h4>
            <p>Help calculate your mom's real estate commissions:</p>
            <ul>
                <li>Write linear equations for commission based on sale price</li>
                <li>Model how commission changes with property value</li>
                <li>Create break-even analysis for different price points</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Week 2 content
elif page == "📊 Week 2: Quadratics":
    st.title("📊 Week 2: Quadratic Functions & Parabolic Motion")
    
    day = st.selectbox("Choose a day:", 
                      ["Day 6: Trajectory Mathematics", "Day 7: Vertex Form", 
                       "Day 8: Solving Quadratics", "Day 9: Applications", "Day 10: Assessment"])
    
    if day == "Day 6: Trajectory Mathematics":
        st.markdown("""
        <div class="personal-connection">
            <strong>🏈 Personal Connection:</strong> Every football you throw follows a parabolic path. Understanding quadratics isn't just academic - it's the mathematics behind every perfect spiral you've ever thrown.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🎯 Activity 1: "The Perfect Spiral Analysis"</h4>
            <p>Model your football throws using quadratic functions:</p>
            <ul>
                <li>Height = -16t² + v₀t + h₀</li>
                <li>Calculate maximum height and distance</li>
                <li>Optimize throwing angle for different situations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🦔 Activity 2: "Sonic's Jump Mechanics"</h4>
            <p>Analyze Sonic's jumping ability using parabolic motion:</p>
            <ul>
                <li>Model his jump trajectory</li>
                <li>Calculate hang time and maximum height</li>
                <li>Compare to real-world athletic performance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif day == "Day 7: Vertex Form":
        st.markdown("""
        <div class="personal-connection">
            <strong>🎯 Personal Connection:</strong> Finding the vertex of a parabola is like finding the optimal point in any situation - the highest point of your pass, the best price point for a property, or the perfect speed for your Segway on different terrains.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏈 Activity 1: "Quarterback Efficiency Optimization"</h4>
            <p>Find the optimal throwing distance for maximum completion percentage:</p>
            <ul>
                <li>Model completion rate as a quadratic function of distance</li>
                <li>Find the vertex to determine optimal range</li>
                <li>Apply this to game strategy</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏠 Activity 2: "Real Estate Pricing Strategy"</h4>
            <p>Help your mom find optimal listing prices:</p>
            <ul>
                <li>Model days on market vs listing price</li>
                <li>Find the price point that minimizes time to sale</li>
                <li>Balance quick sale vs maximum profit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Week 3 content
elif page == "📈 Week 3: Exponential & Radicals":
    st.title("📈 Week 3: Exponential and Radical Functions")
    
    day = st.selectbox("Choose a day:", 
                      ["Day 11: Growth Functions", "Day 12: Logarithms", 
                       "Day 13: Radical Functions", "Day 14: Rational Functions", "Day 15: Integration"])
    
    if day == "Day 11: Growth Functions":
        st.markdown("""
        <div class="personal-connection">
            <strong>📏 Personal Connection:</strong> Your growth from a 5-year-old Sonic fan to a 6'2" quarterback represents exponential change. Understanding exponential functions helps us model growth in height, skills, and investments.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏈 Activity 1: "Athletic Performance Growth"</h4>
            <p>Model your development as a quarterback:</p>
            <ul>
                <li>Track improvement in throwing distance over time</li>
                <li>Model skill development using exponential functions</li>
                <li>Predict future performance based on current growth rate</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏠 Activity 2: "Real Estate Investment Compound Growth"</h4>
            <p>Help your mom understand compound appreciation:</p>
            <ul>
                <li>Model property value growth over time</li>
                <li>Compare simple vs compound appreciation</li>
                <li>Calculate long-term investment returns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif day == "Day 12: Logarithms":
        st.markdown("""
        <div class="personal-connection">
            <strong>🗣️ Personal Connection:</strong> Just as your deep voice represents a dramatic change from your younger self, logarithms help us understand dramatic changes in scale - from measuring earthquake intensity to calculating how long investments take to grow.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🔊 Activity 1: "Sound and Speed Analysis"</h4>
            <p>Explore the relationship between your voice and sound physics:</p>
            <ul>
                <li>Use logarithms to measure decibel levels</li>
                <li>Model sound intensity vs distance</li>
                <li>Connect to Sonic's sound barrier breaking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>💰 Activity 2: "Investment Time Calculations"</h4>
            <p>Calculate how long investments take to reach goals:</p>
            <ul>
                <li>Use logarithms to solve compound interest problems</li>
                <li>Determine time needed to save for college</li>
                <li>Analyze different investment strategies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Week 4 content
elif page == "🎓 Week 4: College Prep":
    st.title("🎓 Week 4: Advanced Topics and College Preparation")
    
    day = st.selectbox("Choose a day:", 
                      ["Day 16: Statistics", "Day 17: Trigonometry", 
                       "Day 18: Sequences", "Day 19: College Applications", "Day 20: Final Assessment"])
    
    if day == "Day 16: Statistics":
        st.markdown("""
        <div class="personal-connection">
            <strong>📊 Personal Connection:</strong> Modern quarterbacks use extensive statistics to improve performance. Real estate agents analyze market data to advise clients. Understanding statistics gives you the tools to make smart decisions in both fields.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏈 Activity 1: "Quarterback Performance Analytics"</h4>
            <p>Analyze your football statistics:</p>
            <ul>
                <li>Calculate correlations between practice time and performance</li>
                <li>Create scatter plots showing improvement trends</li>
                <li>Use regression to predict future performance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏠 Activity 2: "Jersey City Real Estate Market Analysis"</h4>
            <p>Help your mom analyze local market trends:</p>
            <ul>
                <li>Collect and analyze recent sales data</li>
                <li>Identify correlations between property features and prices</li>
                <li>Create predictive models for property values</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif day == "Day 17: Trigonometry":
        st.markdown("""
        <div class="personal-connection">
            <strong>📐 Personal Connection:</strong> Understanding angles is crucial for quarterbacks - launch angles, throwing mechanics, and field positioning all involve trigonometric relationships.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏈 Activity 1: "Optimal Throwing Angles"</h4>
            <p>Calculate the best angles for different passes:</p>
            <ul>
                <li>Use trigonometry to find launch angles for maximum distance</li>
                <li>Analyze how angle affects trajectory and hang time</li>
                <li>Model optimal angles for different field positions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="activity-box">
            <h4>🏠 Activity 2: "Property Surveying Mathematics"</h4>
            <p>Apply trigonometry to real estate:</p>
            <ul>
                <li>Calculate property boundaries using angles and distances</li>
                <li>Determine building heights using shadow measurements</li>
                <li>Analyze sight lines and view corridors</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif day == "Day 20: Final Assessment":
        st.markdown("""
        <div class="activity-box">
            <h4>🎯 Final Project: "The Complete Mathematical Profile"</h4>
            <p>Create a presentation demonstrating mastery of all 9th grade Common Core mathematics standards through projects connected to your interests:</p>
            <ul>
                <li><strong>Athletic Mathematics:</strong> Trajectory analysis, statistical modeling, training sequences</li>
                <li><strong>Real Estate Mathematics:</strong> Market analysis, investment calculations, geometric applications</li>
                <li><strong>College Preparation:</strong> Financial planning, academic progression modeling</li>
                <li><strong>Personal Growth Analysis:</strong> Mathematical model of your development from age 5 to present</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Ask Dr. X page
elif page == "🤖 Ask Dr. X":
    st.title("🤖 Ask Dr. X - Your AI Math Tutor")
    
    st.markdown("""
    <div class="personal-connection">
        <strong>👓 Dr. X is here to help!</strong> Ask me anything about math - whether it's quadratic equations, football trajectories, real estate calculations, or college prep questions. I'm specifically tuned to help with your interests in football, Sonic, and real estate!
    </div>
    """, unsafe_allow_html=True)
    
    # Display chat history
    st.markdown('<div class="drx-chat">', unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"**🏈 You:** {message['content']}")
        else:
            st.markdown(f"**👓 Dr. X:** {message['content']}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Chat input
    user_input = st.text_input("Ask Dr. X a question:", placeholder="e.g., How do I calculate the trajectory of a football pass?")
    
    if st.button("Send") and user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get response from Dr. X
        with st.spinner("Dr. X is thinking..."):
            response = ask_drx(user_input)
        
        # Add response to history
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Rerun to update display
        st.rerun()
    
    if st.button("Clear Chat"):
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Hello Jeremiah! I'm Dr. X, your AI math tutor. Whether you need help with quadratic equations, want to calculate football trajectories, or understand real estate mathematics, just ask!"}
        ]
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <p><em>"Speed is life. Mathematical understanding is the fuel that powers that speed."</em></p>
    <p>- Adapted for the modern student-athlete</p>
</div>
""", unsafe_allow_html=True)
