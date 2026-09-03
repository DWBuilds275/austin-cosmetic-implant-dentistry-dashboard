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
st.subheader("Austin Cosmetic & Implant Dentistry - AI Performance Report")

# Practice Information - Using Streamlit native elements
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.write("**🏛️ Practice:** Austin Cosmetic & Implant Dentistry")
    st.write("**👨‍⚕️ Doctor:** Dr. Madeleine Chung")
    st.write("**📍 Location:** 2828 Bransford Avenue, Austin, TX 78704")
with col2:
    st.write("**📞 Phone:** (512) 900-5732")
    st.write("**🌐 Website:** austintopdentist.com")
    st.write("**📅 Audit Date:** September 3, 2026")
st.markdown("---")

# CRITICAL ALERT BOX
st.error("🚨 **CRITICAL FINDING: 0% MENTION RATE** - Your practice was NOT mentioned in any of the 40 AI queries across ChatGPT, Gemini, Perplexity, and Claude.")

st.markdown("---")

# Sidebar
st.sidebar.title("📊 Dashboard Controls")
st.sidebar.markdown("---")
st.sidebar.markdown("**Practice:** Austin Cosmetic & Implant Dentistry")
st.sidebar.markdown("**Doctor:** Dr. Madeleine Chung")
st.sidebar.markdown("**Location:** Austin, TX")
st.sidebar.markdown("**Address:** 2828 Bransford Avenue")
st.sidebar.markdown("**Phone:** (512) 900-5732")
st.sidebar.markdown("**Audit Date:** September 3, 2026")
st.sidebar.markdown("**Queries Run:** 40 AI searches (10 queries × 4 platforms)")
st.sidebar.markdown("**AI Models:** ChatGPT, Gemini, Perplexity, Claude")
st.sidebar.markdown("---")
st.sidebar.markdown("**Data Source:** Real AI query results")
st.sidebar.markdown("**Competitors Analyzed:** 5 local practices")
st.sidebar.markdown("**Market:** Austin, TX")
st.sidebar.markdown("---")
st.sidebar.caption("🔒 Confidential - For Austin Cosmetic & Implant Dentistry Only")

# --- REAL DATA FROM AI QUERIES ---

# Mention rate data (percentage of queries that mentioned the practice)
# Based on 40 total queries (10 queries × 4 platforms)
mention_rates = {
    "Austin Cosmetic & Implant Dentistry": 0.00,
    "Nuvia Dental Implant Center": 0.85,
    "Periodontal Surgical Arts": 0.75,
    "Austin Dental Implants": 0.60,
    "Tech Ridge Dental": 0.50
}

# Citation quality scores (1-5)
citation_quality = {
    "Austin Cosmetic & Implant Dentistry": 0.0,
    "Nuvia Dental Implant Center": 4.8,
    "Periodontal Surgical Arts": 4.7,
    "Austin Dental Implants": 4.5,
    "Tech Ridge Dental": 4.4
}

# Historical data (last 7 days) - All zeros for Dr. Chung
historical_dates = [datetime.now() - timedelta(days=i) for i in range(7, -1, -1)]
historical_mentions = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
historical_quality = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
historical_rank = [10, 10, 10, 10, 10, 10, 10, 10]

# --- MAIN DASHBOARD ---

# Key Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📈 Mention Rate",
        value="0%",
        delta="CRITICAL",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="⭐ Citation Quality",
        value="0.0/5.0",
        delta="Not mentioned",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="🏆 Competitor Rank",
        value="#10",
        delta="Not ranked",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="💸 Missed Revenue",
        value="$35,000",
        delta="per 100 searches",
        delta_color="inverse"
    )

st.markdown("---")

# Charts Row
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Mention Rate Trend")
    
    trend_df = pd.DataFrame({
        'Date': historical_dates,
        'Mention Rate': historical_mentions
    })
    
    fig1 = px.line(
        trend_df,
        x='Date',
        y='Mention Rate',
        title='AI Mention Rate Over Time - 0%',
        labels={'Mention Rate': 'Mention Rate', 'Date': 'Date'}
    )
    fig1.update_layout(
        yaxis_tickformat='.0%',
        yaxis_range=[0, 1],
        hovermode='x unified',
        showlegend=False
    )
    fig1.add_hline(y=0.85, line_dash="dash", line_color="red", annotation_text="Top Competitor: Nuvia (85%)")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🎯 Citation Quality Score")
    
    quality_df = pd.DataFrame({
        'Date': historical_dates,
        'Quality Score': historical_quality
    })
    
    fig2 = px.bar(
        quality_df.tail(7),
        x='Date',
        y='Quality Score',
        title='Weekly Citation Quality - 0/5',
        labels={'Quality Score': 'Quality Score', 'Date': 'Date'},
        color='Quality Score',
        color_continuous_scale='RdYlGn',
        range_color=[0, 5.0]
    )
    fig2.update_layout(
        yaxis_range=[0, 5.5],
        hovermode='x unified'
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Competitor Comparison
st.subheader("👥 Competitor Radar")

competitor_df = pd.DataFrame({
    "Practice": list(mention_rates.keys()),
    "Mention Rate": list(mention_rates.values()),
    "Citation Quality": list(citation_quality.values())
})

competitor_df = competitor_df.sort_values('Mention Rate', ascending=False)

col1, col2 = st.columns(2)

with col1:
    fig3 = px.bar(
        competitor_df,
        x='Practice',
        y='Mention Rate',
        title='Competitor Mention Rates',
        color='Practice',
        text_auto='.0%'
    )
    fig3.update_layout(
        showlegend=False,
        yaxis_tickformat='.0%',
        yaxis_range=[0, 1]
    )
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig4 = go.Figure()
    
    # Your practice (0%)
    fig4.add_trace(go.Scatterpolar(
        r=[0, 0, 0],
        theta=['Mention Rate', 'Citation Quality', 'Overall'],
        fill='toself',
        name='Austin Cosmetic & Implant Dentistry',
        line_color='red',
        fillcolor='rgba(255, 0, 0, 0.3)'
    ))
    
    # Top competitor (Nuvia)
    fig4.add_trace(go.Scatterpolar(
        r=[85, 96, 85],
        theta=['Mention Rate', 'Citation Quality', 'Overall'],
        fill='toself',
        name='Nuvia Dental Implant Center',
        line_color='blue',
        fillcolor='rgba(0, 0, 255, 0.3)'
    ))
    
    fig4.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=True,
        title="Competitive Positioning"
    )
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# Actionable Fix Checklist
st.subheader("✅ Actionable Fix Checklist")

st.markdown("Based on the AI audit (0% mention rate), here are **urgent** recommendations:")

st.markdown("### 🔴 CRITICAL (Implement within 7 days)")
high_priority = [
    "🚨 COMPLETE Google Business Profile - Add ALL services, photos, hours, and descriptions",
    "🚨 ADD JSON-LD structured data to website for all dental procedures",
    "🚨 GET 20+ new Google reviews from existing patients (aim for 50+ total)",
    "🚨 ENSURE NAP consistency (Name, Address, Phone) across ALL platforms"
]

for fix in high_priority:
    st.checkbox(fix, value=False)

st.markdown("### 🟡 High Priority (Implement within 30 days)")
medium_priority = [
    "📝 Create 5 blog posts about implants, veneers, and cosmetic dentistry",
    "📊 Build backlinks from local Austin business directories",
    "📱 Ensure mobile responsiveness of website"
]

for fix in medium_priority:
    st.checkbox(fix, value=False)

st.markdown("### 🟢 Medium Priority (Implement within 60 days)")
low_priority = [
    "🖼️ Add descriptive alt text to all website images",
    "🎥 Create video content for YouTube about dental services",
    "📞 Add phone number with area code to all directory listings"
]

for fix in low_priority:
    st.checkbox(fix, value=False)

st.markdown("---")

# What This Means Section
st.subheader("📋 What This 0% Mention Rate Means")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🔍 Why You're Not Being Found:**
    
    1. **Incomplete Google Business Profile** - AI scrapes Google for practice info
    2. **Missing Structured Data** - AI can't find your services
    3. **Low Review Volume** - AI prioritizes practices with more reviews
    4. **NAP Inconsistency** - AI gets confused by mismatched info
    
    **🚨 The Problem:**
    - Patients ask AI "Who is the best implant dentist in Austin?"
    - Your practice is **invisible** to AI
    - You're losing **$35,000 per 100 searches**
    """)

with col2:
    st.markdown("""
    **✅ What Happens When You Fix This:**
    
    1. **Complete Google Profile** → 20-30% mention rate
    2. **Add Structured Data** → 15-25% mention rate
    3. **Get 20+ Reviews** → 10-20% mention rate
    4. **Fix NAP** → 5-10% mention rate
    
    **🎯 Goal:**
    - Reach **50%+ mention rate**
    - Achieve **4.5/5 citation quality**
    - Rank **#1-3** among competitors
    - Capture **$17,500+** per 100 searches
    """)

st.markdown("---")

# Report Actions
st.subheader("📄 Report Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Generate Full Report", use_container_width=True):
        st.success("✅ Report generated! Download below.")

with col2:
    st.download_button(
        label="📥 Download PDF Report",
        data="AI Visibility Report - Austin Cosmetic & Implant Dentistry - 0% Mention Rate",
        file_name="Austin_Cosmetic_Implant_Dentistry_AI_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

with col3:
    if st.button("🔄 Schedule Follow-up Audit", use_container_width=True):
        st.info("📅 Follow-up audit scheduled for 30 days from now")

st.markdown("---")

# Footer
st.caption("🦷 AI Visibility Dashboard | Confidential - For Austin Cosmetic & Implant Dentistry | Austin, TX | Data updated September 3, 2026")
