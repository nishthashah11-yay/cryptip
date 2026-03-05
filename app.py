
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import streamlit.components.v1 as components


import streamlit as st
import yfinance as yf
import pandas as pd









import streamlit as st
import time

if "page" not in st.session_state:
    st.session_state.page = "splash"




# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Crypto Volatility Visualizer",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>

/* ---------------- BACKGROUND ---------------- */

.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    overflow: hidden;
}

/* Floating glowing blobs */
.blob {
    position: absolute;
    border-radius: 50%;
    filter: blur(120px);
    opacity: 0.6;
    animation: float 12s infinite ease-in-out alternate;
}

.blob1 {
    width: 400px;
    height: 400px;
    background: #00f5ff;
    top: -100px;
    left: -100px;
}

.blob2 {
    width: 350px;
    height: 350px;
    background: #ff00cc;
    bottom: -120px;
    right: -120px;
}

@keyframes float {
    from { transform: translateY(0px); }
    to { transform: translateY(40px); }
}

/* ---------------- GLASS CARD ---------------- */

.glass-card {
    backdrop-filter: blur(25px);
    background: rgba(255,255,255,0.05);
    border-radius: 25px;
    padding: 60px;
    border: 1px solid rgba(255,255,255,0.15);
    animation: fadeSlide 1.2s ease;
    box-shadow: 0 0 40px rgba(0,255,255,0.2);
}

@keyframes fadeSlide {
    from {opacity:0; transform: translateY(40px);}
    to {opacity:1; transform: translateY(0);}
}

/* ---------------- HEADING ANIMATION ---------------- */

.gradient-text {
    background: linear-gradient(90deg, #00f5ff, #ff00cc, #00ffcc);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 6s infinite linear;
    font-size: 60px;
    font-weight: 800;
    text-align:center;
}

@keyframes gradientMove {
    0% {background-position: 0%;}
    100% {background-position: 300%;}
}

/* ---------------- BUTTON ---------------- */

.glow-btn button {
    background: linear-gradient(45deg, #00f5ff, #ff00cc);
    border: none;
    padding: 12px 30px;
    border-radius: 15px;
    font-weight: 600;
    color: white;
    transition: 0.3s ease;
}

.glow-btn button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 25px #00f5ff;
}

/* Remove Streamlit default padding */
.block-container {
    padding-top: 3rem;
}

</style>

<div class="blob blob1"></div>
<div class="blob blob2"></div>

""", unsafe_allow_html=True)



st.markdown("""
<style>

/* Glass Panel */
.glass-panel {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 0 30px rgba(0,255,255,0.15);
    animation: fadeSlide 0.8s ease-in-out;
}

/* Fade Animation */
@keyframes fadeSlide {
    from {opacity:0; transform: translateY(20px);}
    to {opacity:1; transform: translateY(0);}
}

/* Neon Button */
.neon-btn button {
    background: linear-gradient(45deg, #00f5ff, #ff00cc);
    border: none;
    border-radius: 12px;
    padding: 10px 25px;
    color: white;
    font-weight: 600;
    transition: 0.3s ease;
}

.neon-btn button:hover {
    transform: scale(1.07);
    box-shadow: 0 0 25px #00f5ff;
}

/* Input Styling */
input, textarea {
    border-radius: 10px !important;
}



[data-baseweb="tab"] {
    font-weight: 600;
    transition: 0.3s;
}
[data-baseweb="tab"]:hover {
    color: #00f5ff;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)






st.markdown("""
<style>

/* Glass Tab Container */
.glass-container {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);
    padding: 30px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 0 35px rgba(0,255,255,0.15);
    animation: fadeIn 0.8s ease-in-out;
    transition: 0.4s ease;
}

.glass-container:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 60px rgba(0,255,255,0.35);
}

/* Animated Tab Header */
.glow-header {
    font-size: 28px;
    font-weight: 700;
    background: linear-gradient(90deg, #00f5ff, #7c3aed, #00f5ff);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glowMove 5s infinite linear;
    margin-bottom: 20px;
}

@keyframes glowMove {
    0% { background-position: 0% }
    100% { background-position: 300% }
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)






st.markdown("""
<style>

/* Glowing Animated Dashboard Title */
.glow-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #00f5ff, #7c3aed, #00f5ff);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 6s linear infinite, pulseGlow 2.5s ease-in-out infinite;
    margin-bottom: 10px;
}

/* Subtext */
.glow-subtext {
    text-align: center;
    font-size: 18px;
    opacity: 0.85;
}

/* Moving gradient */
@keyframes gradientMove {
    0% { background-position: 0% }
    100% { background-position: 300% }
}

/* Soft glow pulse */
@keyframes pulseGlow {
    0% { text-shadow: 0 0 10px rgba(0,245,255,0.3); }
    50% { text-shadow: 0 0 30px rgba(0,245,255,0.8); }
    100% { text-shadow: 0 0 10px rgba(0,245,255,0.3); }
}

</style>
""", unsafe_allow_html=True)






# ==================================================
# SPLASH SCREEN
# ==================================================

if st.session_state.page == "splash":

    splash_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        margin:0;
        overflow:hidden;
        background: radial-gradient(circle at center, #0f2027, #203a43, #2c5364);
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        font-family: 'Segoe UI', sans-serif;
        color:white;
    }
    .container {
        text-align:center;
    }
    .title {
        font-size:3.5rem;
        font-weight:700;
        background: linear-gradient(90deg, #00f5ff, #00ff88);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        animation: glow 2s infinite alternate;
    }
    @keyframes glow {
        from { text-shadow:0 0 10px #00f5ff; }
        to { text-shadow:0 0 30px #00ff88; }
    }
    .wave {
        width:300px;
        height:3px;
        background: linear-gradient(90deg, transparent, #00ff88, transparent);
        margin:20px auto;
        animation: expand 2.5s forwards;
    }
    @keyframes expand {
        from { width:0; }
        to { width:300px; }
    }
    .subtitle {
        opacity:0;
        animation: fadeIn 3s forwards;
        animation-delay:1.5s;
    }
    @keyframes fadeIn {
        to { opacity:1; }
    }
    </style>
    </head>
    <body>
    <div class="container">
        <div class="title">📊 Crypto Volatility Visualizer</div>
        <div class="wave"></div>
        <div class="subtitle">
            Mathematics for AI-II • Market Swing Simulation
        </div>
    </div>
    </body>
    </html>
    """
    
    if "splash_shown" not in st.session_state:
        components.html(splash_html, height=800)
        time.sleep(3)
        st.session_state.splash_shown = True
        

    st.session_state.page = "landing"
    st.rerun()





# ==================================================
# LANDING PAGE
# ==================================================

if st.session_state.page == "landing":




    landing_html = """
    <div class="landing-container">
    
        <!-- PARTICLES BACKGROUND -->
        <div class="particles"></div>
    
        <!-- CURTAINS -->
        <div class="curtain-left"></div>
        <div class="curtain-right"></div>
    
        <!-- MAIN CONTENT -->
        <div class="content">
            <div class="glass-card">
                <div class="gradient-text">
                    VolatiX AI
                </div>
                <p style="text-align:center; font-size:18px; opacity:0.8; margin-top:20px;">
                    AI-Powered Crypto Volatility Intelligence Platform
                </p>
            </div>
        </div>
    
    </div>
    
    <style>
    /* PARTICLES */
    .particles {
        position: absolute;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(0,245,255,0.12) 1px, transparent 1px);
        background-size: 70px 70px;
        animation: moveParticles 60s linear infinite;
        z-index: 1;
    }
    
    @keyframes moveParticles {
        from { background-position: 0 0; }
        to { background-position: 800px 800px; }
    }
    
    /* CURTAINS */
    .curtain-left, .curtain-right {
        position: absolute;
        top: 0;
        width: 50%;
        height: 100%;
        background: linear-gradient(to bottom, #3a0000, #120000);
        z-index: 3;
    }
    
    .curtain-left {
        left: 0;
        border-right: 4px solid #D4AF37;
        animation: openLeft 3s forwards ease-in-out;
    }
    
    .curtain-right {
        right: 0;
        border-left: 4px solid #D4AF37;
        animation: openRight 3s forwards ease-in-out;
    }
    
    @keyframes openLeft {
        to { transform: translateX(-100%); }
    }
    
    @keyframes openRight {
        to { transform: translateX(100%); }
    }
    
    /* CONTENT FADE-IN */
    .content {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 2;
        width: 85%;
        max-width: 600px;
        opacity: 0;
        animation: fadeIn 2s forwards;
        animation-delay: 3s; /* starts after curtains open */
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translate(-50%, -40%); }
        to { opacity: 1; transform: translate(-50%, -50%); }
    }
    
    /* OPTIONAL: glass-card styling if not already applied */
    .glass-card {
        backdrop-filter: blur(5px);
        background: rgba(255,255,255,0.05);
        border-radius: 25px;
        padding: 60px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 0 40px rgba(0,255,255,0.2);
    }


    .gradient-text {
        background: linear-gradient(90deg, #00f5ff, #ff00cc, #00ffcc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 60px;
        font-weight: 800;
        text-align:center;
    
        /* GLOW EFFECT */
        text-shadow:
            0 0 2px #00f5ff,
            0 0 1px #00f5ff,
            0 0 2px #ff00cc,
            0 0 3px #ff00cc,
            0 0 4px #00ffcc;
        animation: glowText 2s ease-in-out infinite alternate;
    }
    
    @keyframes glowText {
        0% {
            text-shadow:
                0 0 2px #00f5ff,
                0 0 1px #00f5ff,
                0 0 2px #ff00cc,
                0 0 3px #ff00cc,
                0 0 4px #00ffcc;
        }
        100% {
            text-shadow:
                0 0 5px #00f5ff,
                0 0 5px #00f5ff,
                0 0 4px #ff00cc,
                0 0 5px #ff00cc,
                0 0 6px #00ffcc;
        }
    }
    </style>
    """
    
    import streamlit.components.v1 as components
    components.html(landing_html, height=600)






    

   

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="glow-btn">', unsafe_allow_html=True)
        if st.button("🚀 Get Started"):
            st.session_state.page = "signup"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.stop()






# ==================================================
# SIGNUP PAGE
# ==================================================

if st.session_state.page == "signup":

    st.markdown("""
    <div class="glass-card">
        <div class="gradient-text" style="font-size:45px;">
            Create Your Account
        </div>
        <p style="text-align:center; font-size:16px; opacity:0.8; margin-top:10px;">
            Enter the VolatiX Intelligence Dashboard
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ✅ DEFINE COLUMNS FIRST
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        st.markdown('<div class="glow-btn">', unsafe_allow_html=True)
        if st.button("✨ Enter Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.stop()





particles_html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
}
#particles-js {
    position: fixed;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    z-index: -1;
    top: 0;
    left: 0;
}
</style>
</head>
<body>
<div id="particles-js"></div>

<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
particlesJS("particles-js", {
  "particles": {
    "number": {"value": 100},
    "color": {"value": "#00f5ff"},
    "shape": {"type": "circle"},
    "opacity": {"value": 0.6},
    "size": {"value": 3},
    "line_linked": {
      "enable": true,
      "distance": 150,
      "color": "#00f5ff",
      "opacity": 0.4,
      "width": 1
    },
    "move": {
      "enable": true,
      "speed": 2
    }
  }
});
</script>
</body>
</html>
"""

components.html(particles_html, height=0)




















st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)



import numpy as np

def gbm_simulation(S0, mu, sigma, T=1, steps=252):
    dt = T / steps
    prices = [S0]

    for _ in range(steps):
        shock = np.random.normal(0, 1)
        St = prices[-1] * np.exp((mu - 0.5 * sigma**2)*dt + sigma*np.sqrt(dt)*shock)
        prices.append(St)

    return prices








# ==================================================
# CINEMATIC SPLASH SCREEN (Neon Financial Theme)
# ==================================================

splash_html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin:0;
    overflow:hidden;
    background: radial-gradient(circle at center, #0f2027, #203a43, #2c5364);
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    font-family: 'Segoe UI', sans-serif;
    color:white;
}
.container {
    text-align:center;
}
.title {
    font-size:3.5rem;
    font-weight:700;
    background: linear-gradient(90deg, #00f5ff, #00ff88);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { text-shadow:0 0 10px #00f5ff; }
    to { text-shadow:0 0 30px #00ff88; }
}
.wave {
    width:300px;
    height:3px;
    background: linear-gradient(90deg, transparent, #00ff88, transparent);
    margin:20px auto;
    animation: expand 2.5s forwards;
}
@keyframes expand {
    from { width:0; }
    to { width:300px; }
}
.subtitle {
    opacity:0;
    animation: fadeIn 3s forwards;
    animation-delay:1.5s;
}
@keyframes fadeIn {
    to { opacity:1; }
}
</style>
</head>
<body>
<div class="container">
    <div class="title">📊 Crypto Volatility Visualizer</div>
    <div class="wave"></div>
    <div class="subtitle">
        Mathematics for AI-II • Market Swing Simulation
    </div>
</div>
</body>
</html>
"""

if "splash_shown" not in st.session_state:
    components.html(splash_html, height=800)
    time.sleep(3)
    st.session_state.splash_shown = True
    st.rerun()


st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0f0f, #1a1a2e);
    box-shadow: 0 0 20px #00f2ff;
}
</style>
""", unsafe_allow_html=True)



# ==================================================
# GLASSMORPHISM THEME
# ==================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
}
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
h1, h2, h3 {
    color:white;
}
</style>
""", unsafe_allow_html=True)




st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(45deg, #00f2ff, #ff00ff);
    color: white;
    border-radius: 10px;
    box-shadow: 0 0 15px #00f2ff;
    transition: 0.3s;
}
div.stButton > button:hover {
    box-shadow: 0 0 25px #ff00ff;
    transform: scale(1.05);
}








</style>
""", unsafe_allow_html=True)





st.markdown("""
<style>

/* Metric Card Container */
.metric-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 0 15px rgba(0,255,255,0.3);
    transition: all 0.4s ease-in-out;
    text-align: center;
    animation: fadeUp 1s ease forwards;
}

/* Hover Neon Effect */
.metric-card:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 0 25px #00f5ff, 0 0 40px #ff00ff;
}

/* Value Styling */
.metric-value {
    font-size: 28px;
    font-weight: 700;
    margin-top: 10px;
}

/* Label Styling */
.metric-label {
    font-size: 14px;
    opacity: 0.8;
}

/* Fade animation */
@keyframes fadeUp {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Risk Colors */
.low-risk { color: #00ff88; }
.medium-risk { color: #ffaa00; }
.high-risk { color: #ff3b3b; }

</style>
""", unsafe_allow_html=True)




# ==================================================
# HEADER
# ==================================================
if st.session_state.page == "dashboard":
    st.markdown("""
    <div class="glass">
        <div class="glow-title">🚀 Crypto Volatility Dashboard</div>
        <div class="glow-subtext">
            Mathematical Simulation + Real Bitcoin Data Analysis
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    
    
    # ==================================================
    # LOAD DATASET
    # ==================================================
    # ==================================================
    # LOAD DATASET (CORRECT VERSION)
    # ==================================================
    
    @st.cache_data
    def load_data(period_choice):
    
        period_map = {
            "Full Sample": "10y",
            "10 Years": "10y",
            "5 Years": "5y",
            "2 Years": "2y",
            "1 Year": "1y",
            "6 Months": "6mo"
        }
    
        selected_period = period_map[period_choice]
    
        df = yf.download("BTC-USD", period=selected_period, interval="1d")
    
        # Flatten MultiIndex if needed
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
    
        df = df.reset_index()
    
        return df
    
    
    
    
    
    
    
    
    # ==================================================
    # SIDEBAR CONTROLS (Stage 6)
    # ==================================================
    
    # ==================================================
    # ELEGANT SIDEBAR — GLASS STYLE LIKE YOUR IMAGE
    # ==================================================
    
    st.markdown("""
    <style>
    .sidebar-glass {
        background: rgba(255,255,255,0.10);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        color: #00f5ff;
        margin-bottom: 10px;
    }
    .sidebar-label {
        font-size: 14px;
        color: #d8e6f3;
        margin-top: 15px;
        font-weight: 600;
    }
    .sidebar-desc {
        font-size: 12px;
        opacity: 0.7;
        color: #c9d2df;
        margin-bottom: 5px;
    }
    
    
    
    /* Toggle container */
    [data-testid="stToggle"] {
        margin-top: 10px;
    }
    
    /* Toggle track (background) */
    [data-testid="stToggle"] div[role="switch"] {
        background-color: #bfc4cc !important;
        border-radius: 20px !important;
        width: 42px !important;
        height: 22px !important;
        transition: 0.3s ease-in-out !important;
    }
    
    /* Toggle ON state */
    [data-testid="stToggle"] div[aria-checked="true"] {
        background-color: #00ff88 !important;
    }
    
    /* Toggle circle */
    [data-testid="stToggle"] div[role="switch"]::before {
        background-color: white !important;
        width: 18px !important;
        height: 18px !important;
        border-radius: 50% !important;
        top: 2px !important;
        left: 2px !important;
        transition: 0.3s ease-in-out !important;
    }
    
    /* Move circle when ON */
    [data-testid="stToggle"] div[aria-checked="true"]::before {
        transform: translateX(20px) !important;
    }
    
    
    
    </style>
    """, unsafe_allow_html=True)
    
    
    
    
    
    
    
    with st.sidebar:
        st.markdown('<div class="sidebar-glass">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">⚙ Simulation Controls</div>', unsafe_allow_html=True)
    
    
        st.markdown('<div class="sidebar-label">Upload Bitcoin CSV</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Upload Kaggle Bitcoin dataset.</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type=["csv"])
        
    
    
        # Pattern
        st.markdown('<div class="sidebar-label">Select Price Pattern</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Choose how price movement is simulated.</div>', unsafe_allow_html=True)
        pattern = st.selectbox("", ["Sine Wave (Cyclical)", "Cosine Wave (Shifted Cycle)", "Random Noise (Chaotic)", "Hybrid Model (Sine + Drift + Noise)"])
    
        # Amplitude
        st.markdown('<div class="sidebar-label">Amplitude (Volatility Size)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Higher value = higher swings in price.</div>', unsafe_allow_html=True)
        amplitude = st.slider("", 1, 50, 15)
    
        # Frequency
        st.markdown('<div class="sidebar-label">Frequency (Swing Speed)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Low = slow waves • High = rapid movement.</div>', unsafe_allow_html=True)
        frequency = st.slider("", 1, 10, 3)
    
        # Drift
        st.markdown('<div class="sidebar-label">Drift (Long-term Trend)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Positive = bullish • Negative = bearish.</div>', unsafe_allow_html=True)
    
    
        drift = st.slider("", -2.0, 2.0, 0.1)
    
        # Noise
        st.markdown('<div class="sidebar-label">Noise Intensity</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Adds unpredictability like real crypto markets.</div>', unsafe_allow_html=True)
        noise = st.slider("", 0, 30, 5)




         # =========================
        # TIME PERIOD SELECTION
        # =========================
        
        st.markdown('<div class="sidebar-label">Select Time Period</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Choose historical data range.</div>', unsafe_allow_html=True)
        
        time_period = st.selectbox(
            "",
            [
                "Full Sample",
                "10 Years",
                "5 Years",
                "2 Years",
                "1 Year",
                "6 Months"
            ]
        )
    
        # Comparison Mode Toggle
        st.markdown('<div class="sidebar-label">Enable Comparison Mode</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-desc">Compare stable vs volatile simulation.</div>', unsafe_allow_html=True)




       



        
        compare_mode = st.toggle("")
    
        if compare_mode:
            st.switch_page("pages/1_📊_Stable_Volatile_Comparison.py")
            st.stop()
            
    
    
        market_mode = st.sidebar.radio("Market Mode", ["Bull", "Bear"])
    
    
    
        # Main Button
        simulate_btn = st.button("Simulate", use_container_width=True)
    
        st.markdown('</div>', unsafe_allow_html=True)
    
    
    
    if uploaded_file is not None:
        st.write("Using Uploaded CSV")
    
        df = pd.read_csv(uploaded_file)
    
        # Convert Timestamp → Date
        if "Timestamp" in df.columns:
            df["Date"] = pd.to_datetime(df["Timestamp"], unit="s")
    
        df = df.dropna()
    
        df["MA50"] = df["Close"].rolling(50).mean()
        df["MA200"] = df["Close"].rolling(200).mean()
    
    
        delta = df["Close"].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        
        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()
        
        rs = avg_gain / avg_loss
        df["RSI"] = 100 - (100 / (1 + rs))
    
    
    
        
        df = df.sort_values("Date")
        df = df.tail(500)
    
    else:
        st.write("Using btc optimized parquet data ")
        df = load_data(time_period)
        df = df.dropna()
        df = df.tail(500)
    
    
    
    
    
    # ==================================================
    # ADDITIONAL METRIC CALCULATIONS
    # ==================================================
    
    df["Returns"] = df["Close"].pct_change()
    
    volatility_index = df["Close"].std()
    price_range = df["High"].max() - df["Low"].min()
    average_price = df["Close"].mean()
    peak_price = df["High"].max()
    average_drift = df["Close"].diff().mean()


    if not df.empty and "Close" in df.columns:
        market_trend = "📈 Upward" if df["Close"].iloc[-1] > df["Close"].iloc[0] else "📉 Downward"
    else:
        market_trend = "⚠️ No Data"
    
    
    
    
    
    
    # ==================================================
    # STABLE vs VOLATILE CLASSIFICATION
    # ==================================================
    
    df["Returns"] = df["Close"].pct_change()
    
    vol_threshold = df["Returns"].std()
    
    df["Market_Type"] = df["Returns"].apply(
        lambda x: "Volatile" if abs(x) > vol_threshold else "Stable"
    )



    # ==================================================
    # AVERAGE DRIFT CALCULATION
    # ==================================================
    
    average_drift = df["Close"].diff().mean()
    


    
    
    
    
    # ===== METRIC CARDS SECTION =====
    
    latest_price = df["Close"].iloc[-1]
    prev_price = df["Close"].iloc[-2]
    price_change = ((latest_price - prev_price) / prev_price) * 100
    avg_volume = df["Volume"].mean()
    volatility = df["Close"].pct_change().std() * 100
    
    # Risk Classification
    if volatility < 2:
        risk_level = "Low Risk"
        risk_class = "low-risk"
    elif volatility < 5:
        risk_level = "Medium Risk"
        risk_class = "medium-risk"
    else:
        risk_level = "High Risk"
        risk_class = "high-risk"
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💰 Current Price</div>
            <div class="metric-value">${latest_price:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        arrow = "▲" if price_change >= 0 else "▼"
        color = "#00ff88" if price_change >= 0 else "#ff3b3b"
    
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📈 Daily Change</div>
            <div class="metric-value" style="color:{color}">
                {arrow} {price_change:.2f}%
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📊 Avg Volume</div>
            <div class="metric-value">{avg_volume:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📉 Volatility</div>
            <div class="metric-value {risk_class}">
                {volatility:.2f}% ({risk_level})
            </div>
        </div>
        """, unsafe_allow_html=True)
    # ==================================================
    # ADDITIONAL METRIC CARDS
    # ==================================================
    
    # ==================================================
    # ADDITIONAL CUSTOM METRIC CARDS
    # ==================================================
    
    col5, col6, col7, col8 = st.columns(4)
    
    # Volatility Index
    with col5:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📊 Volatility Index</div>
            <div class="metric-value">
                ${volatility_index:,.0f}
            </div>
            <div class="metric-sub">Std Dev σ</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Price Range
    with col6:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📏 Price Range</div>
            <div class="metric-value">
                ${price_range:,.0f}
            </div>
            <div class="metric-sub">High − Low</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Average Price
    with col7:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📈 Average Price</div>
            <div class="metric-value">
                ${average_price:,.0f}
            </div>
            <div class="metric-sub">Mean</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Peak Price
    with col8:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">🚀 Peak Price</div>
            <div class="metric-value">
                ${peak_price:,.0f}
            </div>
            <div class="metric-sub">Max</div>
        </div>
        """, unsafe_allow_html=True)

    # ==================================================
    # AVERAGE DRIFT CARD (NEW ROW)
    # ==================================================
    
    col9 = st.columns(1)[0]
    
    with col9:
        drift_arrow = "▲" if average_drift >= 0 else "▼"
        drift_color = "#00ff88" if average_drift >= 0 else "#ff3b3b"
    
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📊 Average Drift</div>
            <div class="metric-value" style="color:{drift_color}">
                {drift_arrow} {average_drift:+.2f}
            </div>
            <div class="metric-sub">Mean Daily Change</div>
        </div>
        """, unsafe_allow_html=True)     




    
    
    
    # ==================================================
    # TAB STRUCTURE
    # ==================================================
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📈 Simulation",
    "💰 Close Price",
    "📊 Volume",
    "📉 Volatility",
    "📉 High vs Low",    
    "💬 Feedback",
    "⚙ Settings"
     ])
    # ==================================================
    # TAB 1 — REAL DATA VISUALIZATION
    # ==================================================
    
    with tab2:
    
        st.subheader("Bitcoin Close Price Over Time")
    
        fig = px.line(
            df,
            x="Date",
            y="Close",
            title="Bitcoin Close Price"
        )
    
        fig.update_layout(template="plotly_dark")
    
        st.plotly_chart(fig, use_container_width=True)
    
        




        
        st.markdown("""
        <div class="glass-container">
        <div class="glow-header">📌 Market Insight</div>
        
        The closing price trend reflects overall market direction.
        Sustained upward movement signals bullish momentum,
        while downward trends indicate bearish pressure.
        
        Trend structure analysis helps detect accumulation,
        distribution, and possible reversal zones. 
        
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
    
        st.subheader("Trading Volume Analysis")
    
        fig3 = px.bar(
            df,
            x="Date",
            y="Volume",
            title="Bitcoin Trading Volume"
        )
    
        fig3.update_layout(template="plotly_dark")
    
        st.plotly_chart(fig3, use_container_width=True)
    
        





        
        st.markdown("""
        <div class="glass-container">
        <div class="glow-header">📌 Market Insight</div>
        
        Volume measures market participation.
        
        • Rising price + rising volume = strong trend confirmation  
        • Rising price + falling volume = weak breakout  
        • Falling price + high volume = panic selling  
        
        Volume often precedes major price movements.
        
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
    
        df["Volatility"] = df["Close"].pct_change().rolling(10).std()
    
        st.subheader("Rolling Volatility (10 Period)")
    
        fig4 = px.line(
            df,
            x="Date",
            y="Volatility",
            title="Rolling Volatility Index"
        )
    
        fig4.update_layout(template="plotly_dark")
    
        st.plotly_chart(fig4, use_container_width=True)
    
       




        
        st.markdown("""
        <div class="glass-container">
        <div class="glow-header">📌 Market Insight</div>
        
        Rolling volatility measures short-term risk intensity.
        
        High volatility indicates unstable markets and higher risk.
        Low volatility periods often precede explosive price moves
        (volatility compression phenomenon).
        
        Volatility is central to option pricing models
        and quantitative risk management.
        
        </div>
        """, unsafe_allow_html=True)
    
    
    
    
    
    
    
    
    
    
    
    
    # ==================================================
    # TAB 2 — MATHEMATICAL SIMULATION
    # ==================================================
    
    with tab1:
    
        st.subheader("📉 Geometric Brownian Motion Simulation")
    
        # 1️⃣ Add Market Mode toggle FIRST
        market_mode = st.radio("Market Mode", ["Bull", "Bear"], horizontal=True)
    
        # 2️⃣ Set drift based on mode
        if market_mode == "Bull":
            mu = 0.25
        else:
            mu = -0.15
    
    
    
        # 3️⃣ Volatility slider
        sigma = st.slider("Volatility", 0.2, 2.0, 0.8)
        steps = st.slider("Time Steps", 100, 500, 252)
    
        # 4️⃣ Get latest price
        S0 = df["Close"].iloc[-1]
    
        # 5️⃣ Run simulation AFTER mu is defined
        simulated_price = gbm_simulation(S0, mu, sigma, steps=steps)
    
        
    
        
        
        
    
    
    
    
    
        # Generate simulation
        simulated_price = gbm_simulation(S0, mu, sigma, steps=steps)
        
    
        # Create figure
        fig = go.Figure()
        
    
        fig.add_trace(
            go.Scatter(
                y=simulated_price,
                mode="lines",
                name="Simulated Path"
            )
        )
        
    
        fig.update_layout(
            template="plotly_dark",
            title="Geometric Brownian Motion Simulation",
            xaxis_title="Time Steps",
            yaxis_title="Price"
        )
        
    
        st.plotly_chart(fig, use_container_width=True)
        

        
        st.markdown("""
        <div class="glass-container">
        <div class="glow-header">📌 Market Insight</div>
        
        This simulation is based on Geometric Brownian Motion (GBM), 
        a stochastic differential equation widely used in quantitative finance.
        
        Mathematical Form:
        
        dS = μS dt + σS dW
        
        Where:
        • μ (mu) represents drift (expected return)
        • σ (sigma) represents volatility
        • dW is a Wiener process (random shock)
        
        Key Observations:
        
        • Increasing volatility (σ) widens possible price paths.
        • Positive drift creates long-term upward bias.
        • Negative drift simulates bearish conditions.
        • Random shocks introduce unpredictability similar to real crypto markets.
        
        This model forms the foundation of modern financial engineering 
        and derivative pricing systems.
        
        </div>
        """, unsafe_allow_html=True)

    






    with tab6:

        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
        st.subheader("💬 User Feedback")
    
        feedback_text = st.text_area("Share your experience", height=150)
    
        rating = st.slider("Rate the platform", 1, 5, 4)
    
        st.markdown('<div class="neon-btn">', unsafe_allow_html=True)
        if st.button("🚀 Submit Feedback"):
            st.success("Thank you! Your feedback has been recorded.")
        st.markdown('</div>', unsafe_allow_html=True)
    
        st.markdown('</div>', unsafe_allow_html=True)      



    with tab7:

        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
        st.subheader("⚙ Account Settings")
    
        st.write("Manage your session and preferences.")
    
        st.divider()
    
        notifications = st.toggle("Enable Notifications")
    
        st.divider()
    
        st.markdown('<div class="neon-btn">', unsafe_allow_html=True)
        if st.button("🔓 Sign Out"):
            st.session_state.page = "landing"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
        st.markdown('</div>', unsafe_allow_html=True)      




    with tab5:  

        st.title("📊 High vs Low Price Comparison")

        @st.cache_data
        def load_data():
            df = yf.download("BTC-USD", period="5y", interval="1d")
        
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
        
            df = df.reset_index()
            return df
        
        df = load_data().dropna().tail(500)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Date"], y=df["High"], name="High"))
        fig.add_trace(go.Scatter(x=df["Date"], y=df["Low"], name="Low"))
        
        fig.update_layout(
            template="plotly_dark",
            title="Bitcoin High vs Low Price"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
        <div class="glass-container">
        <div class="glow-header">📌 Market Insight</div>
        
        • The gap between High and Low reflects daily volatility.  
        • Expanding spreads indicate market stress or breakout potential.  
        • Tight spreads suggest consolidation phases before major moves.  
        • Large wicks often signal liquidity hunts or sudden institutional activity.  
        
        </div>
        """, unsafe_allow_html=True)








        
    
        
    
