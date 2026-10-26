import streamlit as st
import os

# Page Config
st.set_page_config(
    page_title="Arthamrit AI Innovation Lab",
    page_icon="⚡",
    layout="wide"
)

# Custom Styling (Arthamrit Brand Colors)
st.markdown("""
    <style>
    .main-header { font-size: 32px; color: #001D13; font-weight: 700; }
    .sub-header { font-size: 16px; color: #393A3C; }
    .stButton>button { background-color: #056839; color: white; font-weight: 600; border-radius: 6px; padding: 10px 24px; }
    .stButton>button:hover { background-color: #001D13; color: white; }
    </style>
""", unsafe_allow_html=True)

# App Sidebar Navigation
st.sidebar.title("AI Showcase Suite")
app_mode = st.sidebar.selectbox("Select Showcase Module", [
    "📢 Omnichannel AI Content Engine",
    "🏛️ Architecture Zoning Copilot",
    "💼 CA Financial Audit Assistant",
    "👥 HR Resume Screener"
])

# API Key Check
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    openai_api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password")

# ==========================================
# MODULE 1: OMNICHANNEL AI CONTENT ENGINE
# ==========================================
if app_mode == "📢 Omnichannel AI Content Engine":
    st.markdown('<p class="main-header">The Omnichannel AI Content Engine</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Instantly generate multi-platform marketing copy, video scripts, and client broadcast templates.</p>', unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        sector = st.selectbox("Select Target Industry Sector:", [
            "Architecture & Real Estate",
            "Chartered Accountant & Finance",
            "SME Retail & E-Commerce",
            "Corporate HR & IT Services"
        ])
    with col2:
        topic_input = st.text_input("Enter Topic, Keyword, or Project Title:", "Q3 Tax Saving Strategies for SMEs")

    if st.button("Generate Content Suite 🚀"):
        if not openai_api_key:
            st.warning("Please enter your OpenAI API key in the sidebar.")
        else:
            with st.spinner("Generating multi-platform content suite..."):
                try:
                    import openai
                    client = openai.OpenAI(api_key=openai_api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are an expert AI Marketing Director for Arthamrit Technologies Private Limited."},
                            {"role": "user", "content": f"Generate a 45-second Reel script, a LinkedIn thought-leadership post, and a WhatsApp broadcast template for sector: {sector} regarding topic: {topic_input}"}
                        ]
                    )
                    st.success("Content Suite Generated Successfully!")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error connecting to AI service: {e}")

# ==========================================
# MODULE 2: ARCHITECTURE ZONING COPILOT
# ==========================================
elif app_mode == "🏛️ Architecture Zoning Copilot":
    st.markdown('<p class="main-header">Architecture Zoning & Compliance Copilot</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Analyze plot dimensions and municipal bylaws to generate preliminary spatial programs.</p>', unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1: plot_w = st.number_input("Plot Width (meters)", value=20.0)
    with col2: plot_l = st.number_input("Plot Length (meters)", value=30.0)
    with col3: floors = st.number_input("Target Floors", value=4)

    bylaw_desc = st.text_area("Enter Municipal Bylaw Guidelines / Setback Rules:", "Max FAR: 2.5, Front Setback: 3m, Side Setback: 2m")

    if st.button("Run Compliance & Layout Analysis 📐"):
        if not openai_api_key:
            st.warning("Please enter your OpenAI API key in the sidebar.")
        else:
            with st.spinner("Analyzing zoning parameters..."):
                try:
                    import openai
                    client = openai.OpenAI(api_key=openai_api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": f"Analyze plot size {plot_w}x{plot_l}m, {floors} floors with bylaws: {bylaw_desc}. Output zoning compliance and room spatial allocation."}]
                    )
                    st.success("Analysis Complete!")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

# ==========================================
# MODULE 3: CA FINANCIAL AUDIT ASSISTANT
# ==========================================
elif app_mode == "💼 CA Financial Audit Assistant":
    st.markdown('<p class="main-header">CA Financial Statement & Audit Assistant</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Process financial data and generate automated audit workpapers.</p>', unsafe_allow_html=True)
    st.divider()

    fin_text = st.text_area("Paste P&L Summary or Transaction Log:", "Revenue: 50L, Operating Expenses: 32L, Tax Paid: 4.5L, Pending Receivables: 8L")
    if st.button("Generate Audit Workpaper 📊"):
        if not openai_api_key:
            st.warning("Please enter your OpenAI API key in the sidebar.")
        else:
            with st.spinner("Processing financial data..."):
                try:
                    import openai
                    client = openai.OpenAI(api_key=openai_api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": f"Act as an expert CA. Audit this financial summary and generate ledger recommendations and risk anomalies: {fin_text}"}]
                    )
                    st.success("Audit Workpaper Ready!")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")

# ==========================================
# MODULE 4: HR RESUME SCREENER
# ==========================================
elif app_mode == "👥 HR Resume Screener":
    st.markdown('<p class="main-header">Intelligent HR Resume Screener</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Semantic matching of candidate profiles against job requirements.</p>', unsafe_allow_html=True)
    st.divider()

    jd = st.text_area("Job Description:", "Seeking Python / FastAPI backend engineer with 3+ years experience in cloud deployments.")
    resume = st.text_area("Candidate Resume Summary:", "Experienced Full Stack Developer with 4 years building Python APIs, Docker, and SQL databases.")

    if st.button("Evaluate Candidate Match 🎯"):
        if not openai_api_key:
            st.warning("Please enter your OpenAI API key in the sidebar.")
        else:
            with st.spinner("Scoring candidate match..."):
                try:
                    import openai
                    client = openai.OpenAI(api_key=openai_api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": f"Evaluate this resume against the JD. Output a match score percentage, skill gaps, and 3 interview questions. JD: {jd}\n\nResume: {resume}"}]
                    )
                    st.success("Evaluation Complete!")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
