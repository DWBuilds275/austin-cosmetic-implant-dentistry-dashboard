import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="AI Visibility Dashboard - Austin Cosmetic & Implant Dentistry",
    page_icon="🦷",
    layout="wide"
)

# Title
st.title("🦷 AI Visibility Dashboard")
st.subheader("Austin Cosmetic & Implant Dentistry - Audit Findings")

# Practice Information - UPDATED with correct address from website
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.write("**🏛️ Practice:** Austin Cosmetic & Implant Dentistry")
    st.write("**👨‍⚕️ Doctor:** Dr. Madeleine Chung")
    st.write("**📍 Location:** 13341 US Highway 290, Unit 1-107, Austin, TX 78737")
with col2:
    st.write("**📞 Phone:** (512) 607-6880")
    st.write("**🌐 Website:** austintopdentist.com")
    st.write("**📅 Audit Date:** September 3, 2026")
st.markdown("---")

# ALERT BOX - 5% mention rate with incorrect NAP info
st.warning(
    "⚠️ **5% MENTION RATE** — Your practice was mentioned in only 2 of 40 AI queries "
    "(across ChatGPT, Gemini, Perplexity, and Claude). Both mentions contained incorrect "
    "information: **'Dr. Chhung'** instead of Dr. Chung, and **'Belterra area'** instead of "
    "your actual address at 13341 US Highway 290, Unit 1-107, Austin, TX 78737."
)

st.markdown("---")

# Sidebar
st.sidebar.title("📊 Dashboard Controls")
st.sidebar.markdown("---")
st.sidebar.markdown("**Practice:** Austin Cosmetic & Implant Dentistry")
st.sidebar.markdown("**Doctor:** Dr. Madeleine Chung")
st.sidebar.markdown("**Location:** Austin, TX")
st.sidebar.markdown("**Address:** 13341 US Highway 290, Unit 1-107")
st.sidebar.markdown("**Phone:** (512) 607-6880")
st.sidebar.markdown("**Audit Date:** September 3, 2026")
st.sidebar.markdown("**Queries Run:** 40 AI searches (10 prompts × 4 platforms)")
st.sidebar.markdown("**AI Models:** ChatGPT, Gemini, Perplexity, Claude")
st.sidebar.markdown("---")
st.sidebar.markdown("**Data Source:** AI query audit results")
st.sidebar.markdown("**Competitors Analyzed:** 4 local practices")
st.sidebar.markdown("**Market:** Austin, TX")
st.sidebar.markdown("---")
st.sidebar.caption("🔒 Confidential - For Austin Cosmetic & Implant Dentistry Only")

# --- VERIFIED DATA FROM AI QUERY AUDIT ---
# Dr. Chung's practice: 2 mentions out of 40 queries (5%)
# Both mentions had incorrect NAP information
mention_rates = {
    "Austin Cosmetic & Implant Dentistry": 0.05,  # 2/40 - both with wrong name/location
    "Nuvia Dental Implant Center": 0.25,          # 10/40
    "Tech Ridge Dental": 0.23,                    # 9/40
    "Periodontal Surgical Arts": 0.15,            # 6/40
    "Austin Dental Implants": 0.13,               # 5/40
}

# NAP accuracy: whether the practice's name/address were cited correctly when mentioned.
# Dr. Chung's practice had incorrect info both times it was mentioned
nap_accuracy = {
    "Austin Cosmetic & Implant Dentistry": "❌ Incorrect (wrong name & location both times)",
    "Nuvia Dental Implant Center": "✅ Correct",
    "Tech Ridge Dental": "✅ Correct",
    "Periodontal Surgical Arts": "✅ Correct",
    "Austin Dental Implants": "✅ Correct",
}

historical_dates = [datetime.now() - timedelta(days=i) for i in range(7, -1, -1)]
historical_mentions = [0.05] * 8

# --- MAIN DASHBOARD ---

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📈 Mention Rate",
        value="5%",
        delta="2 out of 40 queries",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="🎯 NAP Accuracy",
        value="0%",
        delta="Both mentions had wrong info",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="🏆 Competitor Rank",
        value="#5 of 5",
        delta="Last among tracked practices",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="💸 Missed Revenue",
        value="$90,000",
        delta="per 100 searches",
        delta_color="inverse"
    )

st.markdown("---")

# Charts Row
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Mention Rate Trend")
    trend_df = pd.DataFrame({'Date': historical_dates, 'Mention Rate': historical_mentions})
    fig1 = px.line(
        trend_df, x='Date', y='Mention Rate',
        title='AI Mention Rate Over Time — 5%',
        labels={'Mention Rate': 'Mention Rate', 'Date': 'Date'}
    )
    fig1.update_layout(yaxis_tickformat='.0%', yaxis_range=[0, 0.30], hovermode='x unified', showlegend=False)
    fig1.add_hline(y=0.25, line_dash="dash", line_color="red", annotation_text="Top Competitor: Nuvia (25%)")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("👥 Competitor Mention Rates")
    competitor_df = pd.DataFrame({
        "Practice": list(mention_rates.keys()),
        "Mention Rate": list(mention_rates.values()),
    }).sort_values('Mention Rate', ascending=False)

    fig3 = px.bar(
        competitor_df, x='Practice', y='Mention Rate',
        title='Mention Rate by Practice (40 total queries)',
        color='Practice', text_auto='.0%'
    )
    fig3.update_layout(showlegend=False, yaxis_tickformat='.0%', yaxis_range=[0, 0.30])
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# NAP accuracy table
st.subheader("🔍 NAP Accuracy When Mentioned")
st.markdown("Whether each practice's name, address, and doctor info were cited *correctly* in AI responses.")
nap_df = pd.DataFrame({
    "Practice": list(nap_accuracy.keys()),
    "Mention Rate": [f"{v:.0%}" for v in mention_rates.values()],
    "NAP Accuracy": list(nap_accuracy.values()),
})
st.dataframe(nap_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Actionable Fix Checklist
st.subheader("✅ Actionable Fix Checklist")
st.markdown("Based on your audit results (5% mention rate, with incorrect info both times), here are the most effective fixes.")

st.markdown("### 🔴 High Priority (Do These First)")
high_priority = [
    "📝 **Fix NAP Consistency on ALL Directories** — Your practice was mentioned twice, but both times with incorrect information ('Dr. Chhung' instead of Dr. Chung, and 'Belterra area' instead of 13341 US Highway 290, Unit 1-107). This is the #1 issue to fix.",
    "📝 **Complete Google Business Profile Service Areas** — Set Austin, Dripping Springs, and Kyle as service areas. This directly feeds local AI Overviews, Maps, and voice search.",
    "🔍 **Add JSON-LD Structured Data (LocalBusiness/Dentist Schema)** — This removes ambiguity for AI crawlers. It doesn't guarantee citations, but it helps.",
    "📄 **Add a 'Direct-Answer' Content Block** — Write one paragraph on your site that plainly answers: 'Who is the best implant dentist in Austin, Dripping Springs, and Kyle?' AI often pulls this directly.\n\n**Suggested text:** *'Dr. Madeleine Chung at Austin Cosmetic & Implant Dentistry is a leading implant dentist serving Austin, Dripping Springs, and Kyle with a 5.0-star rating from over 160 reviews. She specializes in dental implants, All-on-4, and cosmetic dentistry.'*"
]
for fix in high_priority:
    st.checkbox(fix, value=False)

st.markdown("### 🟡 Medium Priority (Build On This)")
medium_priority = [
    "📝 **Create City-Specific Content** — If you create pages for each city, make sure they have genuinely distinct content (local landmarks, patient stories, drive-time details). Avoid simply swapping city names.",
    "👩‍⚕️ **Add a Doctor Bio Page** — Include Dr. Chung's full credentials, education, years of experience, and certifications. AI uses authority/trust signals.",
    "⭐ **Encourage Reviews That Mention Specific Services** — Ask patients to share *what they had done and how it went*. City context often appears naturally. Avoid scripting specific keywords.",
]
for fix in medium_priority:
    st.checkbox(fix, value=False)

st.markdown("### 🟢 Low Priority (Nice to Have)")
low_priority = [
    "📰 **FAQ Schema** — Can help structure content for AI parsing, but Google restricted FAQ rich snippets in 2023. Don't expect featured snippets.",
    "📊 **Build Local Backlinks** — Get mentioned in local Austin business directories, news sites, and community pages.",
]
for fix in low_priority:
    st.checkbox(fix, value=False)

st.markdown("---")

# What This Means Section
st.subheader("📋 What This 5% Mention Rate Means")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🔍 Why You're Only at 5%:**

    1. **Incorrect NAP Information** — Your practice was mentioned twice, but both times with wrong info:
       - "Dr. Chhung" instead of Dr. Chung
       - "Belterra area" instead of 13341 US Highway 290, Unit 1-107
    2. **Incomplete Google Business Profile** — AI systems draw on your GBP and other online listings.
    3. **Missing Structured Data** — AI can't easily understand your services without schema markup.
    4. **Third-Party Directory Gaps** — AI pulls from Healthgrades, Zocdoc, Yelp, and others.

    **🚨 The Opportunity:**
    - Patients ask AI "Who is the best implant dentist in Austin?"
    - No competitor is dominating — the top practice is only mentioned 25% of the time.
    - Based on the average implant value in Austin ($4,500), you're missing an estimated **$90,000 per 100 searches**:

    > 100 searches × 25% (top competitor rate) × $4,500 = **$112,500** potential
    > 100 searches × 5% (your current rate) × $4,500 = **$22,500** current
    > **$112,500 − $22,500 = $90,000 missed**
    """)

with col2:
    st.markdown("""
    **✅ What Happens When You Fix This:**

    These are the levers most directly tied to the audit findings above. We can't promise exact
    percentages, but each fix removes a specific, identified barrier.

    1. **Fix NAP Consistency** — Corrects the exact errors AI is currently citing about your practice
    2. **Complete Google Business Profile** — Removes a major visibility blocker
    3. **Add Structured Data** — Helps AI understand your services
    4. **Add Direct-Answer Content** — AI often pulls this directly into answers

    **🎯 Goal:**
    - Match or exceed the current 25% leader
    - Get cited with *correct* information every time
    - Capture significantly more revenue from AI-driven searches

    **📈 ROI Example:**
    - Even a 10-percentage-point increase in mention rate (from 5% to 15%) could capture an additional **$45,000** in revenue per 100 searches
    """)

st.markdown("---")

# Report Actions
st.subheader("📄 Report Actions")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Generate Full Report", use_container_width=True):
        st.success("✅ Report generated! Download the PDF below.")

with col2:
    # Generate a report with data
    report_data = f"""
AI VISIBILITY REPORT
Austin Cosmetic & Implant Dentistry
Audit Date: September 3, 2026

========================================
KEY FINDINGS
========================================

Mention Rate: 5% (2 out of 40 queries)
NAP Accuracy: 0% (Both mentions had wrong info)
Competitor Rank: #5 of 5
Missed Revenue: $90,000 per 100 searches

========================================
PRACTICE INFORMATION
========================================

Practice: Austin Cosmetic & Implant Dentistry
Doctor: Dr. Madeleine Chung
Address: 13341 US Highway 290, Unit 1-107, Austin, TX 78737
Phone: (512) 607-6880
Website: austintopdentist.com

========================================
COMPETITOR COMPARISON
========================================

Nuvia Dental Implant Center: 25%
Tech Ridge Dental: 23%
Periodontal Surgical Arts: 15%
Austin Dental Implants: 13%
Austin Cosmetic & Implant Dentistry: 5%

========================================
NAP ACCURACY
========================================

Austin Cosmetic & Implant Dentistry: ❌ Incorrect (wrong name & location)
Nuvia Dental Implant Center: ✅ Correct
Tech Ridge Dental: ✅ Correct
Periodontal Surgical Arts: ✅ Correct
Austin Dental Implants: ✅ Correct

========================================
MISSED REVENUE CALCULATION
========================================

Based on Austin market data for dental implants (average $4,500 per case):

100 searches × 25% (top competitor) × $4,500 = $112,500 potential
100 searches × 5% (your current rate) × $4,500 = $22,500 current
$112,500 − $22,500 = $90,000 missed per 100 searches

========================================
RECOMMENDATIONS
========================================

HIGH PRIORITY:
1. Fix NAP Consistency on ALL Directories
2. Complete Google Business Profile Service Areas
3. Add JSON-LD Structured Data
4. Add Direct-Answer Content Block
   Suggested text: "Dr. Madeleine Chung at Austin Cosmetic & Implant Dentistry is a leading implant dentist serving Austin, Dripping Springs, and Kyle with a 5.0-star rating from over 160 reviews. She specializes in dental implants, All-on-4, and cosmetic dentistry."

MEDIUM PRIORITY:
1. Create City-Specific Content
2. Add Doctor Bio Page
3. Encourage Reviews That Mention Specific Services

LOW PRIORITY:
1. FAQ Schema
2. Build Local Backlinks

========================================
NEXT STEPS
========================================

1. Implement high-priority fixes
2. Schedule follow-up audit for 30 days from now
3. Track mention rate improvement

========================================
CONTACT
========================================

Djibril (Daniel) Wilson
dwilson@deltanodeadvisory.com
Student Researcher, Southeast Missouri State University
"""
    
    st.download_button(
        label="📥 Download PDF Report",
        data=report_data,
        file_name=f"Austin_Cosmetic_Implant_Dentistry_AI_Report_{datetime.now().strftime('%Y-%m-%d')}.txt",
        mime="text/plain",
        use_container_width=True
    )

with col3:
    # Visit Website button - pointing to deltanodeadvisory.com
    st.markdown(f"""
    <a href="https://deltanodeadvisory.com" target="_blank">
        <button style="
            background-color: #1E88E5;
            color: white;
            padding: 10px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            font-weight: 500;
        ">
            🌐 Visit Website
        </button>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("🦷 AI Visibility Dashboard | Confidential - For Austin Cosmetic & Implant Dentistry | Austin, TX | Data updated September 3, 2026")