with col2:
        # Create interactive commission comparison with break-even analysis
        prices = np.linspace(50000, 1000000, 100)
        comm1 = prices * (commission_rate_1 / 100)
        comm2 = prices * (commission_rate_2 / 100) + base_fee
        
        fig = go.Figure()
        
        # Commission option 1
        fig.add_trace(go.Scatter(
            x=prices, y=comm1,
            mode='lines',
            name=f'Option 1: {commission_rate_1}%',
            line=dict(color='#2ecc71', width=4),
            hovertemplate='Price: $%{x:,.0f}<br>Commission: $%{y:,.0f}<extra></extra>'
        ))
        
        # Commission option 2
        fig.add_trace(go.Scatter(
            x=prices, y=comm2,
            mode='lines',
            name=f'Option 2: {commission_rate_2}% + ${base_fee:,}',
            line=dict(color='#e74c3c', width=4),
            hovertemplate='Price: $%{x:,.0f}<br>Commission: $%{y:,.0f}<extra></extra>'
        ))
        
        # Mark break-even point
        if break_even_price > 0 and break_even_price < 1000000:
            break_even_commission = break_even_price * (commission_rate_1 / 100)
            fig.add_trace(go.Scatter(
                x=[break_even_price], y=[break_even_commission],
                mode='markers+text',
                marker=dict(size=15, color='gold', symbol='star'),
                text=[f'Break-Even<br>${break_even_price:,.0f}'],
                textposition='top center',
                name='Break-Even Point',
                hovertemplate=f'Break-Even Point<br>Price: ${break_even_price:,.0f}<br>Commission: ${break_even_commission:,.0f}<extra></extra>'
            ))
            
            # Add vertical line at break-even
            fig.add_vline(
                x=break_even_price,
                line_dash="dot",
                line_color="gold",
                annotation_text=f"Break-Even: ${break_even_price:,.0f}",
                annotation_position="top"
            )
        
            yaxis_title='Commission ($)',
            height=500,
            hovermode='x unified',
            showlegend=True
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        st.plotly_chart(fig, use_container_width=True)
        
        if break_even_price > 0:
            st.success(f"💡 **Break-even Analysis:** At ${break_even_price:,.0f}, both commission structures are equal!")
            
            # Interactive decision helper
            test_price = st.slider("Test a property price:", 100000, 1000000, int(break_even_price), 10000)
            option1_comm = test_price * (commission_rate_1 / 100)
            option2_comm = test_price * (commission_rate_2 / 100) + base_fee
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Option 1 Commission", f"${option1_comm:,.0f}")
            with col_b:
                st.metric("Option 2 Commission", f"${option2_comm:,.0f}")
            with col_c:
                diff = option1_comm - option2_comm
                better_option = "Option 1" if diff > 0 else "Option 2"
                st.metric(f"{better_option} Better By", f"${abs(diff):,.0f}")

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
    
    # College recommendation engine
    st.markdown("---")
    st.markdown("### 🤖 AI College Recommendation Engine")
    
    njit_match = min(100, ((current_gpa >= njit_gpa_min) * 30 + 
                          (target_sat >= njit_sat_min) * 30 + 
                          min(40, extracurriculars * 5)))
    
    rpi_match = min(100, ((current_gpa >= rpi_gpa_min) * 30 + 
                         (target_sat >= rpi_sat_min) * 30 + 
                         min(40, (extracurriculars + leadership_roles) * 4)))
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🟢 NJIT Match", f"{njit_match:.0f}%", 
                 "Strong Fit" if njit_match >= 70 else "Need Improvement")
    
    with col2:
        st.metric("🔴 RPI Match", f"{rpi_match:.0f}%", 
                 "Strong Fit" if rpi_match >= 70 else "Reach School")
    
    with col3:
        backup_schools = 3 if njit_match < 70 else 1
        st.metric("📋 Backup Schools Needed", backup_schools)
    
    # Action plan generator
    if st.button("📋 Generate Personalized Action Plan"):
        st.markdown("### 🎯 Your Personalized College Prep Action Plan")
        
        improvements = []
        if current_gpa < njit_gpa_min:
            improvements.append(f"📚 Raise GPA to {njit_gpa_min:.1f}+ (currently {current_gpa:.1f})")
        if target_sat < njit_sat_min:
            improvements.append(f"📝 Improve SAT to {njit_sat_min}+ (target: {target_sat})")
        if extracurriculars < 4:
            improvements.append(f"🎭 Join {4-extracurriculars} more extracurricular activities")
        if leadership_roles < 2:
            improvements.append(f"👑 Seek {2-leadership_roles} leadership positions")
        
        if improvements:
            st.markdown("**🎯 Priority Improvements:**")
            for improvement in improvements:
                st.markdown(f"• {improvement}")
        else:
            st.success("🎉 You're on track for both NJIT and RPI! Keep up the excellent work!")
        
        # Award progress points
        st.session_state.total_points += 20
        st.session_state.week_progress['Week 4'] = min(100, st.session_state.week_progress['Week 4'] + 50)

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
    
    # Quick help buttons
    st.markdown("### 🎯 Quick Help Topics")
    help_topics = st.columns(4)
    
    with help_topics[0]:
        if st.button("🏈 Football Math"):
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "Help me understand the math behind football trajectories and optimal throwing angles."
            })
            response = ask_drx("Help me understand the math behind football trajectories and optimal throwing angles.")
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    with help_topics[1]:
        if st.button("🏠 Real Estate"):
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "Explain how to calculate real estate ROI and commission structures."
            })
            response = ask_drx("Explain how to calculate real estate ROI and commission structures.")
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    with help_topics[2]:
        if st.button("📊 Quadratics"):
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "I need help understanding vertex form and completing the square."
            })
            response = ask_drx("I need help understanding vertex form and completing the square.")
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    with help_topics[3]:
        if st.button("🎓 College Prep"):
            st.session_state.chat_history.append({
                "role": "user", 
                "content": "What math skills do I need for NJIT and RPI admissions?"
            })
            response = ask_drx("What math skills do I need for NJIT and RPI admissions?")
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    # Enhanced chat interface
    st.markdown("### 💬 Chat with Dr. X")
    
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
    
    # Chat input with suggestions
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input("Ask Dr. X:", 
                                  placeholder="e.g., How do I find the vertex of a parabola?",
                                  key="chat_input")
    
    with col2:
        send_button = st.button("Send 📤", key="send_chat")
    
    if (send_button or user_input) and user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get Dr. X response
        with st.spinner("Dr. X is thinking..."):
            response = ask_drx(user_input)
        
        # Add response
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Award points for asking questions
        st.session_state.total_points += 2
        if len([msg for msg in st.session_state.chat_history if msg["role"] == "user"]) >= 10:
            if "💬 Chat Champion" not in st.session_state.achievements:
                st.session_state.achievements.append("💬 Chat Champion")
        
        st.rerun()
    
    # Chat management buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Hello Jeremiah! I'm Dr. X, your AI math coach. Ready to tackle some math problems?"}
            ]
            st.rerun()
    
    with col2:
        if st.button("💾 Save Chat"):
            chat_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history])
            st.download_button("Download Chat", chat_text, "mathcraft_chat.txt", "text/plain")
    
    with col3:
        st.markdown(f"💬 **Messages:** {len(st.session_state.chat_history)}")

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
    
    # Add target line
    fig.add_hline(y=100, line_dash="dash", line_color="gold", 
                  annotation_text="Target: 100%", annotation_position="right")
    
    fig.update_layout(
        title='📊 Weekly Progress Overview',
        xaxis_title='Week',
        yaxis_title='Completion Percentage',
        height=400,
        yaxis=dict(range=[0, 120])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed skill breakdown
    st.markdown("---")
    st.markdown("### 🎯 Skill Mastery Breakdown")
    
    skills_data = {
        'Skill': ['Linear Equations', 'Slope Analysis', 'Quadratic Functions', 'Projectile Motion', 
                 'Systems of Equations', 'Real Estate Math', 'College Prep', 'Problem Solving'],
        'Mastery Level': [85, 92, 78, 88, 75, 95, 82, 90],
        'Week': ['Week 1', 'Week 1', 'Week 2', 'Week 2', 'Week 3', 'Week 3', 'Week 4', 'Overall']
    }
    
    skills_df = pd.DataFrame(skills_data)
    
    # Interactive skill chart
    fig = px.bar(skills_df, x='Skill', y='Mastery Level', color='Week',
                 title='🎯 Individual Skill Mastery Levels',
                 height=400)
    
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
    
    # Achievement showcase
    st.markdown("---")
    st.markdown("### 🏆 Achievement Gallery")
    
    all_achievements = {
        "🦔 Speed Demon": "Complete Week 1 Linear Functions",
        "🏈 Trajectory Master": "Complete Week 2 Quadratics", 
        "🔄 Systems Solver": "Complete Week 3 Systems",
        "🎓 College Ready": "Complete Week 4 Advanced Topics",
        "💬 Chat Champion": "Ask Dr. X 10 questions",
        "🎯 Perfect Shot": "Optimize a football trajectory",
        "📊 Data Analyst": "Complete statistical analysis",
        "🏠 Real Estate Pro": "Master property calculations"
    }
    
    achievement_cols = st.columns(4)
    
    for i, (achievement, description) in enumerate(all_achievements.items()):
        with achievement_cols[i % 4]:
            if achievement in st.session_state.achievements:
                st.success(f"✅ **{achievement}**\n\n{description}")
            else:
                st.info(f"🔒 **{achievement}**\n\n{description}")
    
    # Study recommendations
    st.markdown("---")
    st.markdown("### 💡 Personalized Study Recommendations")
    
    weakest_week = min(st.session_state.week_progress, key=st.session_state.week_progress.get)
    weakest_score = st.session_state.week_progress[weakest_week]
    
    if weakest_score < 50:
        st.warning(f"📚 **Focus Area:** {weakest_week} needs attention ({weakest_score}% complete)")
        st.markdown("**Recommended Actions:**")
        st.markdown("• Review the interactive lessons")
        st.markdown("• Ask Dr. X for help with specific concepts")
        st.markdown("• Complete the practice problems")
    elif total_progress >= 90:
        st.success("🎉 **Excellent Progress!** You're ready for 10th grade math!")
        st.markdown("**Next Steps:**")
        st.markdown("• Review all completed materials")
        st.markdown("• Challenge yourself with advanced problems")
        st.markdown("• Help other students with their math")
    else:
        st.info(f"👍 **Good Progress!** Keep working on {weakest_week}")

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
            import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
import altair as alt
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
try:
    from streamlit_plotly_events import plotly_events
except ImportError:
    plotly_events = None

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

### 🧑‍🏫 Who is Dr. X?
Dr. X is your AI math tutor 🤓 — Xavier Honablue M.Ed — with a passion for helping students succeed. Think of him as your personal sideline coach for math, always ready to help with any questions.
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

# --- WEEK 2 ---
with week_tabs[1]:
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
    
    # Detailed Mathematical Analysis
    st.markdown("---")
    st.markdown("### 🧠 Quadratic Function Analysis")
    
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
    - This is a quadratic function in **standard form**: h(t) = at² + bt + c
    - Where a = -16, b = {v_y:.1f}, c = {initial_height}
    
    **Step 3: Find Key Features**
    - **Vertex (Maximum Height):** t = -b/2a = -{v_y:.1f}/(2×-16) = {v_y/(2*16.1):.2f} seconds
    - **Maximum Height:** h({v_y/(2*16.1):.2f}) = {max_height:.1f} feet
    - **Flight Time:** Solve h(t) = 0 using quadratic formula = {flight_time:.2f} seconds
    - **Range:** Distance = vₓ × flight time = {v_x:.1f} × {flight_time:.2f} = {max_distance:.1f} feet
    
    **📐 Vertex Form Conversion:**
    - Standard form: h(t) = -16t² + {v_y:.1f}t + {initial_height}
    - Vertex form: h(t) = -16(t - {v_y/(2*16.1):.2f})² + {max_height:.1f}
    - The vertex form clearly shows the maximum occurs at t = {v_y/(2*16.1):.2f} seconds
    """)
    
    # Physics and Engineering Applications
    st.markdown(f"""
    **⚙️ Physics & Engineering Insights:**
    
    **Optimization Analysis:**
    - Current angle ({launch_angle}°) gives range of {max_distance:.1f} feet
    - Theoretical optimal angle for maximum range: 45° (ignoring air resistance)
    - Actual optimal angle for football: 35-40° (accounting for air resistance and spiral)
    
    **Real-World Factors Not in Model:**
    - Air resistance (reduces range by ~10-20%)
    - Spin of the football (affects trajectory)
    - Wind conditions (can significantly alter path)
    - Football shape (not perfectly spherical)
    
    **Quadratic Properties Demonstrated:**
    - **Symmetry:** Time to reach maximum = time to fall from maximum
    - **Concavity:** Opens downward (a = -16 < 0)
    - **Intercepts:** y-intercept at (0, {initial_height}), x-intercepts when h(t) = 0
    """)
    
    # Quadratic Function Analysis
    st.markdown("---")
    st.markdown("### 📐 Vertex Form Analysis")
    st.markdown(f"""
    **🎯 Converting Between Forms:**
    
    **Original Height Equation (Standard Form):**
    h(t) = -16t² + {v_y:.1f}t + {initial_height}
    
    **Completing the Square to Get Vertex Form:**
    
    Step 1: Factor out the coefficient of t²
    h(t) = -16(t² - {v_y/16:.3f}t) + {initial_height}
    
    Step 2: Complete the square inside parentheses
    h(t) = -16(t² - {v_y/16:.3f}t + {(v_y/32)**2:.4f}) + {initial_height} + 16×{(v_y/32)**2:.4f}
    
    Step 3: Factor and simplify
    h(t) = -16(t - {v_y/32:.3f})² + {max_height:.1f}
    
    **Vertex Form:** h(t) = -16(t - {v_y/(2*16.1):.2f})² + {max_height:.1f}
    
    **Key Information from Vertex Form:**
    - **Vertex coordinates:** ({v_y/(2*16.1):.2f}, {max_height:.1f})
    - **Axis of symmetry:** t = {v_y/(2*16.1):.2f} seconds
    - **Maximum value:** {max_height:.1f} feet
    - **Opens:** Downward (because a = -16 < 0)
    
    **🎯 Why Vertex Form is Useful:**
    - Immediately shows the maximum height and when it occurs
    - Makes it easy to identify transformations from the parent function y = x²
    - Useful for optimization problems in physics and engineering
    """)
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
        # Create interactive 3-way race visualization
        times = np.linspace(0, max(running_time, segway_time) * 1.2, 100)
        
        # Distance covered by each mode
        running_distance = (times / 60) * running_speed
        segway_distance = np.maximum(0, ((times + segway_head_start) / 60) * segway_speed)
        sonic_distance = (times / 60) * sonic_speed
        
        fig = go.Figure()
        
        # Add traces for each racer
        fig.add_trace(go.Scatter(
            x=times, y=running_distance,
            mode='lines',
            name='🏃‍♂️ Jeremiah Running',
            line=dict(color='#3498db', width=4),
            hovertemplate='Time: %{x:.1f} min<br>Distance: %{y:.2f} miles<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=times, y=segway_distance,
            mode='lines',
            name='🛴 Jeremiah on Segway',
            line=dict(color='#e67e22', width=4),
            hovertemplate='Time: %{x:.1f} min<br>Distance: %{y:.2f} miles<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=times, y=sonic_distance,
            mode='lines',
            name='🦔 Sonic',
            line=dict(color='#9b59b6', width=4),
            hovertemplate='Time: %{x:.1f} min<br>Distance: %{y:.2f} miles<extra></extra>'
        ))
        
        # Mark finish line
        fig.add_hline(
            y=race_distance, 
            line_dash="dash", 
            line_color="red",
            annotation_text="🏁 Finish Line",
            annotation_position="bottom right"
        )
        
        # Mark intersection points
        for i, time_val in enumerate(times[::10]):  # Check every 10th point
            run_pos = (time_val / 60) * running_speed
            seg_pos = max(0, ((time_val + segway_head_start) / 60) * segway_speed)
            
            if abs(run_pos - seg_pos) < 0.01 and run_pos > 0.1:  # Found intersection
                fig.add_trace(go.Scatter(
                    x=[time_val], y=[run_pos],
                    mode='markers',
                    marker=dict(size=12, color='yellow', symbol='star'),
                    name='Intersection',
                    showlegend=False,
                    hovertemplate=f'Intersection<br>Time: {time_val:.1f} min<br>Distance: {run_pos:.2f} miles<extra></extra>'
                ))
                break
        
        fig.update_layout(
            title='🏃‍♂️🛴🦔 Interactive Three-Way Race: Systems in Motion',
            xaxis_title='Time (minutes)',
            yaxis_title='Distance Covered (miles)',
            height=500,
            hovermode='x unified',
            showlegend=True
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', range=[0, race_distance * 1.2])
        
        st.plotly_chart(fig, use_container_width=True)
    
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
