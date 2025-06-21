#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# =============================================================================
# 🧠 MetricMentor – A Product Strategy Console Assistant
# Final Project for Code in Place 2025
# Developed by: Mahima Advilkar
# =============================================================================
#
# MetricMentor is an interactive, command-line simulator to help product thinkers
# learn, simulate, and reflect on key product health metrics. Built with beginner-
# friendly Python, this tool allows users to diagnose common issues, understand KPIs,
# simulate scenarios, and ask GPT-style follow-up questions (simulated).
#
# Run this script in any Python environment (no libraries needed).
# =============================================================================

# ========== Display Main Menu ==========
def display_main_menu():
    print("\n📊 Welcome to MetricMentor – Your Product Strategy Assistant!\n")
    print("1. Diagnose a Product Problem")
    print("2. Learn About Key Metrics")
    print("3. Product Health Check Simulator")
    print("4. GPT-Powered Product Advice (Simulated)")
    print("5. Exit")

# ========== Diagnose Product Issues ==========
def diagnose_product_problem():
    print("\n🩺 Product Problem Diagnosis")
    print("1. Users not returning")
    print("2. High marketing costs")
    print("3. Low feature engagement")
    print("4. Poor landing page conversion")

    choice = input("Select a problem (1–4): ")
    print("\n🧠 Recommendation:")
    if choice == '1':
        print("- Use Retention Rate, DAU/MAU to evaluate churn.\n- Improve onboarding and activation points.")
    elif choice == '2':
        print("- Track CAC & LTV. Reduce paid spend or increase monetization.")
    elif choice == '3':
        print("- Analyze Feature Adoption Rate & Time-to-Value (TTV).")
    elif choice == '4':
        print("- Funnel Conversion Rate, Bounce Rate. Try A/B testing CTAs.")
    else:
        print("❌ Invalid input.")
    input("\nPress Enter to return to the main menu...")

# ========== Learn Product Metrics ==========
def learn_product_metrics():
    print("\n📚 Learn Key Product Metrics:")
    print("1. Retention Rate")
    print("2. CAC (Customer Acquisition Cost)")
    print("3. LTV (Lifetime Value)")
    print("4. Feature Adoption Rate")
    print("5. Back to Menu")

    choice = input("Choose (1–5): ")
    print("\n🧠 Explanation:")
    if choice == '1':
        print("Retention = % of users who return after X days (D1, D7, D30).\nHigh retention = strong product-market fit.")
    elif choice == '2':
        print("CAC = Total Marketing Spend ÷ New Customers.\nLower CAC = more efficient growth.")
    elif choice == '3':
        print("LTV = ARPU × Avg Customer Lifespan.\nHigher LTV = better monetization and retention.")
    elif choice == '4':
        print("Adoption Rate = Users using feature ÷ Active users.\nLow adoption = poor discoverability or value.")
    elif choice == '5':
        return
    else:
        print("❌ Invalid input.")
    input("\nPress Enter to return to the main menu...")

# ========== Product Health Simulation Modules ==========
def simulate_retention_problem():
    print("\n📉 Retention Simulation:\nDay 1: 45% | Day 7: 28% | Day 30: 12%")
    print("\n🧠 Analysis:\n- Steep drop = weak long-term engagement.\n- Good Day 1? Your onboarding works.")
    print("\n💡 Suggestions:\n• Add value faster (e.g., checklist, reward loops).\n• Use re-engagement nudges like emails.")
    input("\nPress Enter to return...")

def simulate_cac_vs_ltv():
    print("\n💰 CAC = $120 | LTV = $90")
    print("\n🧠 Analysis:\n- You lose money per user.\n- Long-term this is unsustainable.")
    print("\n💡 Suggestions:\n• Increase LTV (upsell, cross-sell, retain).\n• Decrease CAC (organic content, referrals).")
    input("\nPress Enter to return...")

def simulate_feature_adoption_issue():
    print("\n🧩 Feature Adoption Rate: 8%")
    print("\n🧠 Analysis:\n- Users either don’t see or don’t care about the feature.")
    print("\n💡 Suggestions:\n• Use tooltips, modals, or guided tours.\n• Improve feature placement in navigation.")
    input("\nPress Enter to return...")

def display_health_summary(issues_logged):
    print("\n📋 Final Product Health Report:")
    score = 100
    if "retention" in issues_logged: score -= 25
    if "cac_ltv" in issues_logged: score -= 30
    if "feature_adoption" in issues_logged: score -= 20

    print(f"\n✅ Product Health Score: {score}/100")
    print("\n💡 Recommendations:")
    if score < 90:
        print("- Improve onboarding\n- Run pricing tests\n- Highlight value-driven features")
    else:
        print("Great! Your metrics are in good shape.")
    input("\nPress Enter to return...")

def product_health_check():
    issues = []
    while True:
        print("\n📊 Simulate Product Health")
        print("1. Retention Drop")
        print("2. CAC > LTV")
        print("3. Low Feature Adoption")
        print("4. View Final Report")
        print("5. Back to Main Menu")
        choice = input("Select (1–5): ")

        if choice == '1':
            simulate_retention_problem()
            issues.append("retention")
        elif choice == '2':
            simulate_cac_vs_ltv()
            issues.append("cac_ltv")
        elif choice == '3':
            simulate_feature_adoption_issue()
            issues.append("feature_adoption")
        elif choice == '4':
            display_health_summary(issues)
            break
        elif choice == '5':
            break
        else:
            print("❌ Invalid input.")

# ========== Simulated GPT Interaction ==========
def simulate_gpt_advice():
    print("\n💬 GPT-Powered Product Advisor")
    user_prompt = input("Describe your product challenge → ")
    print("\n🧠 Thinking...\n")

    print("🧠 GPT Insight:\n")
    print("Thanks for sharing! Try tightening MVP scope, using MoSCoW prioritization, and setting demo deadlines.")

    for i in range(3):
        follow_up = input("\n💬 Ask a follow-up question (or press Enter to skip): ")
        if follow_up.strip() == "":
            break
        print("\n🧠 Follow-up Insight:")
        print(f"Simulated advice for: '{follow_up}'. Break work into outcomes, prioritize by user impact.")
    input("\nPress Enter to return...")

# ========== Main Program ==========
def run_metric_mentor():
    while True:
        display_main_menu()
        choice = input("Choose (1–5): ")

        if choice == '1':
            diagnose_product_problem()
        elif choice == '2':
            learn_product_metrics()
        elif choice == '3':
            product_health_check()
        elif choice == '4':
            simulate_gpt_advice()
        elif choice == '5':
            print("\n👋 Thank you for using MetricMentor. Goodbye!")
            break
        else:
            print("❌ Invalid input. Please try again.")


# Launch the app
run_metric_mentor()


# In[ ]:




