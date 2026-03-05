
# 🌐 VolatiX AI

## Crypto Volatility Visualizer  
### Simulating Market Swings with Mathematics for AI and Python


### CRS Artificial Intelligence – Maths for A.I.  

---

## 👤 Student Details

- **Student Name:** Nishtha priyesh shah 
- **Candidate Registration Number:** 1000436  
- **CRS Name:** Artificial Intelligence  
- **Course Name:** Maths for A.I. 
- **School Name:** Aspee Nutan Academy
- **Live Link:** https://cryptip-vfanzppzzdvyc3xbapgrbt.streamlit.app/
-**Course:** Mathematics for AI-II  
-**Assessment:** Formative Assessment-2 (FA-2)  
-**Marks:** 20  

---

# 🚀 Purpose / Rationale

**VolatiX AI** is an *AI-powered crypto volatility intelligence platform* designed to simulate and visualize cryptocurrency price swings.

In **FA-1**, the dashboard design was planned and storyboarded.  
In **FA-2**, the project has been fully implemented using **Python** and **Streamlit** to demonstrate mathematical modeling of crypto markets.

The project demonstrates:

* Wave-like price swings using mathematical functions *(sine / cosine)*  
* Sudden random jumps to simulate **market shocks**  
* Long-term drift representing **market trends**  
* Interactive charts with **real-time user controls**

This platform allows users to **explore real-world cryptocurrency volatility** and understand how different mathematical factors influence price movement.

---


## 🚀 Project Overview

**Crypto Volatility Visualizer** is a financial analytics application that merges:

- Real-world cryptocurrency data (BTC-USD)
- Statistical indicators (MA50, MA200, RSI, Volatility)
- Mathematical stochastic modeling
- Advanced UI/UX financial dashboard styling

Built using:

- <a href="https://streamlit.io/" target="_blank">Streamlit</a>  
- <a href="https://plotly.com/python/" target="_blank">Plotly</a>  
- <a href="https://pandas.pydata.org/" target="_blank">Pandas</a>  
- <a href="https://numpy.org/" target="_blank">NumPy</a>  
- <a href="https://pypi.org/project/yfinance/" target="_blank">yFinance</a>  

---
## 🧩 Project Storyboard

Below is the original design storyboard for the application:
<img width="1036" height="580" alt="Screenshot 2026-03-04 162747" src="https://github.com/user-attachments/assets/c03b938e-ce0a-4e18-b2bf-928e6d953c6d" />

# 📊 Features

## 1️⃣ Interactive Dashboard (Streamlit)

The application provides a **dynamic dashboard interface** with interactive controls.

### Sidebar Controls
Users can adjust:

* Price swing **pattern** (wave / random noise)
* Swing **amplitude**
* Swing **frequency**
* Long-term **market drift**

Charts update **in real-time** based on these inputs.

---

## 📈 Visualizations

### Price Over Time
*Line graph showing cryptocurrency **Close Price** trends over time.*

### High vs Low Comparison
*Displays daily volatility using **High** and **Low** price differences.*

### Volume Analysis
*Bar chart showing **trading volume** and how it correlates with price swings.*

### Stable vs Volatile Periods
*Highlights periods of **low volatility vs high volatility**.*

All graphs are **interactive using Plotly**, allowing users to hover and view precise data values.

---

### 🎨 2. Advanced UI Design

#### ✔ Glassmorphism Theme
- Blurred panels
- Gradient background
- Soft neon glow
- Modern fintech aesthetic

#### ✔ Animated Particles Background
- Interactive JavaScript particle system
- Subtle moving grid for financial theme

#### ✔ Styled Sidebar Controls
- Custom toggles
- Custom sliders
- Neon buttons
- Market Mode switch (Bull/Bear)

---

## 📊 Real Market Analysis (Tab 1)

Uses live data from Yahoo Finance:

```python
yf.download("BTC-USD", period="5y", interval="1d")
```
### Includes:

#### 📈 1. Bitcoin Close Price

Interactive time-series line chart

#### 📊 2. Volume Analysis

Daily trading volume bar chart

#### 📉 3. Rolling Volatility Index

10-period rolling standard deviation of returns:
``` python
Volatility = pct_change().rolling(10).std()
```
#### 📊 4. Technical Indicators (If CSV Uploaded)

MA50 (50-day moving average)

MA200 (200-day moving average)

RSI (14-period Relative Strength Index)

## 📈 Mathematical Simulation (Tab 2)
### Geometric Brownian Motion (GBM)

Implements stochastic differential equation:

``` python
dS = μSdt + σSdW
```
Discrete version used:

```python
(t+1) = S(t) * exp((μ - 0.5σ²)dt + σ√dt * Z)
```
Where:

μ = Drift (trend direction)

σ = Volatility

Z = Random normal shock

### 🎛 Simulation Controls
#### Market Mode

Bull Market → μ = 0.25

Bear Market → μ = -0.15

#### Adjustable Parameters

Volatility (σ)

Time Steps

Noise

Drift

Amplitude

Frequency

### Pattern Type

#### 🔁 Comparison Mode

Toggle option:

Switches to high vs low volatility comparison page

Enables scenario-based analysis

## 📂 Dataset Options
### Option 1 — Auto Fetch (Default)

Fetches BTC data using `yfinance`

Last 5 years daily data

Cached using `@st.cache_data`

### Option 2 — Upload CSV

Upload Kaggle Bitcoin dataset:

Must contain `Timestamp`

Must contain `Close`

Must contain `Volume`

Automatically computes:

Moving averages

RSI

Volatility metrics

## 🧠 Core Function
```python
def gbm_simulation(S0, mu, sigma, T=1, steps=252):
    dt = T / steps
    prices = [S0]

    for _ in range(steps):
        shock = np.random.normal(0, 1)
        St = prices[-1] * np.exp((mu - 0.5 * sigma**2)*dt + sigma*np.sqrt(dt)*shock)
        prices.append(St)

    return prices
```
## 🛠 Installation
### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/crypto-volatility-visualizer.git
cd crypto-volatility-visualizer
```
### 2️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install streamlit pandas numpy plotly yfinance
```
### 3️⃣ Run the Application
```bash
streamlit run app.py
```
## 📦 Requirements.txt
```txt
streamlit
pandas
numpy
plotly
yfinance
```
## 📐 Mathematical Concepts Used

Stochastic Processes

Geometric Brownian Motion

Drift & Diffusion Modeling

Rolling Standard Deviation

Technical Analysis Indicators

Time Series Simulation

## 🖥 Architecture Overview
Streamlit Frontend
        ↓
Sidebar Controls
        ↓
Data Layer (yFinance / CSV Upload)
        ↓
Analytics Engine (Pandas + NumPy)
        ↓
Simulation Engine (GBM Model)
        ↓
Plotly Visualization Layer
🎓 Academic Context

## Designed for:
Mathematics for AI-II

Financial Modeling

Volatility Simulation

Market Behavior Analysis

## ⚡ Performance Optimizations

`@st.cache_data` for dataset caching

Limited dataset to last 500 rows for speed

Efficient NumPy-based GBM simulation

Session-state splash screen control

## 📊 Example Use Cases

Understanding crypto volatility

Demonstrating stochastic models

Comparing bullish vs bearish simulations

Teaching financial mathematics

AI-based market modeling experiments

## 🔮 Future Improvements

Monte Carlo multiple path simulation

Value at Risk (VaR)

Sharpe Ratio calculation

Portfolio optimization

Live WebSocket crypto feed

AI-based volatility prediction model

## 📜 License

This project is built for educational and academic purposes.


## ⭐ If You Like This Project

### Consider:

Starring the repository

Forking for improvements

Adding advanced financial metrics

### Crypto Volatility Visualizer — Where Mathematics Meets Market Chaos 📈

# 🗂 Dataset Preparation

**Dataset Source:**  
https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory

### Columns Used
* Timestamp  
* Open  
* High  
* Low  
* Close  
* Volume  

### Data Cleaning Steps

1. Loaded dataset using `pandas.read_csv()`
2. Inspected dataset structure using `head()`
3. Converted **Timestamp column to datetime format**
4. Selected **Close Price** for main analysis
5. Removed missing values using:
   * `dropna()`
   * `fillna()` (when necessary)
6. Selected subset of data *(e.g., last 30 days)* for clarity
7. Simplified column names where needed

---

# 📊 Visualizations & Analysis

### Line Graph – Price Over Time
Shows **market trends and price movement patterns**.

### High vs Low Comparison
Highlights **daily volatility peaks and troughs**.

### Volume Analysis
Identifies **days with high trading activity** and corresponding price movement.

### Stable vs Volatile Periods
Visually distinguishes between **calm markets and highly volatile markets**.

---

# ⚙️ Streamlit Interface

The application includes:

* **Interactive sidebar controls**
* **Real-time chart updates**
* **Dynamic visualization of price patterns**

### UI Design

The dashboard features:

* Glassmorphism style layout
* Neon gradient highlights
* Clear display of key metrics

---
###App Screenshots
*Loading Page
<img width="1531" height="669" alt="image" src="https://github.com/user-attachments/assets/7e37f668-5d92-4ad9-a286-4cc0ece311f2" />
*Landing page
<img width="1643" height="851" alt="image" src="https://github.com/user-attachments/assets/e448c5ff-199a-4fc4-a2aa-32033f4cee5d" />
*Sign up Page 
*Dashboard
<img width="1643" height="744" alt="image" src="https://github.com/user-attachments/assets/15333d2b-a56f-4e64-ac5a-32cbcd5fdc30" />
*Side bar
<img width="124" height="711" alt="image" src="https://github.com/user-attachments/assets/291d7ab9-e400-45f0-8d41-8f79bda67a7f" />
*Home page and Tabs 
<img width="1696" height="817" alt="image" src="https://github.com/user-attachments/assets/fcd55f28-8bf6-4850-b575-5f3caae2e9fe" />
*Comparison Mode 
<img width="1794" height="566" alt="image" src="https://github.com/user-attachments/assets/97e8036f-53ae-49e7-88ce-e217c1f0b672" />




# 🛠 Installation & Running Locally

### 1️⃣ Clone the Repository


git clone https://github.com/<your-username>/VolatiX-AI.github


###2️⃣ Navigate to the Project Folder

cd VolatiX-AI
###3️⃣ Install Required Libraries

pip install -r requirements.txt
###4️⃣ Run the Streamlit App

streamlit run app.py


# ☁️ Deployment

The project is deployed using **Streamlit Cloud**.

🔗 **Live Application:**  
https://volatix-ai-ko7es7v6u8tu8xh5sfzzej.streamlit.app/


---

# 📚 References

* Streamlit Documentation  
* Plotly Express Tutorial  
* Pandas Data Cleaning Guide  
* Matplotlib Plot Types  
* Dashboard UX Inspiration  

---

# ✅ Checklist of Evidence

* ✔ Dataset loaded and cleaned  
* ✔ Multiple graphs created  
* ✔ Interactive visualizations implemented  
* ✔ Sidebar controls integrated  
* ✔ Dynamic chart updates working  
* ✔ Key metrics displayed  
* ✔ Application deployed on Streamlit Cloud  
* ✔ GitHub repository link included  

---

# 🏆 Assessment Rubrics

| Criteria | Distinguished (5) | Proficient (4) | Apprentice (3) | Novice (2) | Marks |
|----------|-------------------|----------------|----------------|------------|-------|
| Data Preparation | Thorough cleaning, timestamp conversion, subset selected | Basic cleaning with minor issues | Minimal cleaning | Data loading issues | 5 |
| Visualizations | Multiple clear interactive graphs with explanations | 2–3 graphs with basic titles | Basic charts only | Unclear or missing graphs | 10 |
| Streamlit Interface & Deployment | Fully functional app with deployment | Basic working app | Partial functionality | Not functional | 5 |

**Total: 20 / 20**

---
## 👨‍💻 Authors

Mann Paresh Patel- WACP Candidate Registration Number- 1000428

Jashith Hemendra Rathod- WACP Candidate Registration Number- 1000422

Nishtha Priyesh Shah- WACP Candidate Registration Number- 1000436

*Mathematics for AI-II | FA-2*
