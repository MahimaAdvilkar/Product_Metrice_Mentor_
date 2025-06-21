#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

# ======================== Streamlit App for MetricMentor ========================

st.set_page_config(page_title="MetricMentor", page_icon="📊")

st.title("🧠 MetricMentor – Your Product Strategy Assistant")
st.markdown("""
Welcome to MetricMentor, your interactive product analytics guide. 
Select an action below to explore product challenges, metrics, simulations, and strategy tips!
""")

# ========== Visual Summary ==========
def draw_metric_summary():
    st.subheader("📊 Quick Product Metric Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Retention Rate (Day 30)", value="12%", delta="-33%")

    with col2:
        st.metric(label="CAC (Customer Acquisition Cost)", value="$120", delta="+20%")

    with col3:
        st.metric(label="Feature Adoption Rate", value="8%", delta="-5%")

draw_metric_summary()

# ========== Define Main Navigation ==========
action = st.sidebar.radio("What would you like to do?", [
    "Diagnose Product Problem",
    "Learn About Key Metrics",
    "Product Health Simulator",
    "GPT-Powered Advice (Simulated)"
])

# ========== Diagnose Product Issues ==========
if action == "Diagnose Product Problem":
    st.header("🩺 Product Problem Diagnosis")
    problem = st.selectbox("Select a problem:", [
        "Users not returning",
        "High marketing costs",
        "Low feature engagement",
        "Poor landing page conversion"
    ])

    st.subheader("🧠 Recommendation:")
    if problem == "Users not returning":
        st.write("- Use Retention Rate, DAU/MAU to evaluate churn.")
        st.write("- Improve onboarding and activation points.")
    elif problem == "High marketing costs":
        st.write("- Track CAC & LTV. Reduce paid spend or increase monetization.")
    elif problem == "Low feature engagement":
        st.write("- Analyze Feature Adoption Rate & Time-to-Value (TTV).")
    elif problem == "Poor landing page conversion":
        st.write("- Funnel Conversion Rate, Bounce Rate. Try A/B testing CTAs.")

# ========== Learn Product Metrics ==========
elif action == "Learn About Key Metrics":
    st.header("📚 Learn Key Product Metrics")
    metric = st.selectbox("Choose a metric to learn about:", [
        "Retention Rate",
        "CAC (Customer Acquisition Cost)",
        "LTV (Lifetime Value)",
        "Feature Adoption Rate"
    ])

    st.subheader("🧠 Explanation:")
    if metric == "Retention Rate":
        st.markdown("""
        **Retention** = % of users who return after X days (D1, D7, D30).  
        High retention = strong product-market fit.
        """)
    elif metric == "CAC (Customer Acquisition Cost)":
        st.markdown("""
        **CAC** = Total Marketing Spend ÷ New Customers.  
        Lower CAC = more efficient growth.
        """)
    elif metric == "LTV (Lifetime Value)":
        st.markdown("""
        **LTV** = ARPU × Avg Customer Lifespan.  
        Higher LTV = better monetization and retention.
        """)
    elif metric == "Feature Adoption Rate":
        st.markdown("""
        **Adoption Rate** = Users using feature ÷ Active users.  
        Low adoption = poor discoverability or value.
        """)

# ========== Product Health Simulator ==========
elif action == "Product Health Simulator":
    st.header("📊 Simulate Product Health")
    selected_issues = []

    if st.button("Simulate Retention Drop"):
        selected_issues.append("retention")
        st.subheader("📉 Retention Simulation")
        st.write("Day 1: 45% | Day 7: 28% | Day 30: 12%")
        st.markdown("""
        **🧠 Analysis:**  
        - Steep drop = weak long-term engagement.  
        - Good Day 1? Your onboarding works.  
        
        **💡 Suggestions:**  
        - Add value faster (checklists, reward loops)  
        - Use re-engagement nudges (emails, push notifications)
        """)

    if st.button("Simulate CAC > LTV"):
        selected_issues.append("cac_ltv")
        st.subheader("💰 CAC vs LTV")
        st.write("CAC = $120 | LTV = $90")
        st.markdown("""
        **🧠 Analysis:**  
        - Losing money per user = not scalable.  
        
        **💡 Suggestions:**  
        - Increase LTV (upsell, retain)  
        - Decrease CAC (organic channels, referrals)
        """)

    if st.button("Simulate Low Feature Adoption"):
        selected_issues.append("feature_adoption")
        st.subheader("🧩 Feature Adoption")
        st.write("Feature Adoption Rate = 8%")
        st.markdown("""
        **🧠 Analysis:**  
        - Users don’t discover or use the feature.  
        
        **💡 Suggestions:**  
        - Improve UI placement  
        - Use tooltips, guided tours, modals
        """)

    if st.button("View Product Health Report"):
        score = 100
        if "retention" in selected_issues:
            score -= 25
        if "cac_ltv" in selected_issues:
            score -= 30
        if "feature_adoption" in selected_issues:
            score -= 20

        st.subheader("📋 Product Health Summary")
        st.metric("Health Score", f"{score}/100")

        if score < 90:
            st.markdown("""
            **💡 Recommendations:**  
            - Improve onboarding  
            - Run pricing experiments  
            - Prioritize user-delighting features
            """)
        else:
            st.success("Great! Your metrics are in good shape.")

# ========== Simulated GPT Interaction ==========
elif action == "GPT-Powered Advice (Simulated)":
    st.header("💬 GPT-Powered Product Advisor")
    user_prompt = st.text_input("Describe your product challenge")

    if user_prompt:
        st.write("🧠 GPT Insight:")
        st.write("Try tightening MVP scope, using MoSCoW prioritization, and setting demo deadlines.")

        for i in range(3):
            follow_up = st.text_input(f"Ask follow-up question {i+1} (optional)", key=f"followup_{i}")
            if follow_up:
                st.write("🧠 Simulated Advice:")
                st.write(f"For '{follow_up}': Break work into outcomes, prioritize by user impact.")


# In[ ]:




