
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")



# =========================
# PREMIUM UI STYLING
# =========================

st.markdown("""
<style>

/* Page background */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: white;
}

/* Animated gradient title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #00f5ff, #7c3aed, #00f5ff);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glowMove 6s infinite linear;
    margin-bottom: 30px;
}

@keyframes glowMove {
    0% { background-position: 0% }
    100% { background-position: 300% }
}

/* Glass Card */
.glass-card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(18px);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 30px rgba(0,255,255,0.15);
    transition: 0.4s ease;
    animation: fadeIn 1.2s ease-in-out;
}

.glass-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 50px rgba(0,255,255,0.35);
}

/* Section headers */
.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 15px;
    background: linear-gradient(90deg,#22d3ee,#818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)












st.markdown('<div class="main-title">📊 Stable vs Volatile Market Comparison</div>', unsafe_allow_html=True)




@st.cache_data
def load_data():
    df = yf.download("BTC-USD", period="2y", interval="1d")

    # 🔥 FIX 1: Flatten MultiIndex columns if they exist
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 🔥 FIX 2: Reset index so Date becomes column
    df = df.reset_index()

    return df


df = load_data()
df = df.dropna()

# DEBUG CHECK



# Calculate Returns
df["Returns"] = df["Close"].pct_change()

# Define threshold
vol_threshold = df["Returns"].std()

# Split datasets
stable_df = df[abs(df["Returns"]) <= vol_threshold]
volatile_df = df[abs(df["Returns"]) > vol_threshold]




col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="glass-card">
    <div class="section-title">Total Observations</div>
    <h2>{len(df)}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="glass-card">
    <div class="section-title">Stable Days</div>
    <h2>{len(stable_df)}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="glass-card">
    <div class="section-title">Volatile Days</div>
    <h2>{len(volatile_df)}</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)



























st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🟢 Stable Market Movement</div>', unsafe_allow_html=True)



# Calculate average stable price
stable_mean_price = stable_df["Close"].mean()

# Create straight line dataframe
straight_line_df = stable_df.copy()
straight_line_df["Stable_Line"] = stable_mean_price

fig1 = px.line(
    straight_line_df,
    x="Date",
    y="Stable_Line",
    title=None
)

fig1.update_traces(line=dict(width=4))

fig1.update_layout(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    yaxis_title="Price",
    xaxis_title="Date"
)







fig1.update_layout(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

st.plotly_chart(fig1, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)





st.divider()

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🔴 Volatile Market Movement</div>', unsafe_allow_html=True)

fig2 = px.line(
    volatile_df,
    x="Date",
    y="Close",
    title=None
)

fig2.update_layout(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

st.plotly_chart(fig2, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
