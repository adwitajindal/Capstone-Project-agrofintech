# import streamlit as st
# import requests

# # FastAPI URL
# API_URL = "http://127.0.0.1:8000/predict"

# st.set_page_config(
#     page_title="Agro FinTech",
#     page_icon="🌾",
#     layout="wide"
# )

# st.title("🌾 Agro FinTech")
# st.subheader("Farmer Loan Risk & Approval Prediction")

# # -------------------------
# # Farmer Details
# # -------------------------

# col1, col2 = st.columns(2)

# with col1:
#     Gender = st.selectbox("Gender", ["Male", "Female"])

#     Age = st.number_input(
#         "Age",
#         min_value=18,
#         max_value=100,
#         value=30
#     )

#     Soil_Type = st.selectbox(
#         "Soil Type",
#         ["Clay", "Loamy", "Sandy", "Black", "Red"]
#     )

#     Irrigation_Type = st.selectbox(
#         "Irrigation Type",
#         ["Canal", "Drip", "Rainfed", "Sprinkler"]
#     )

#     Crop = st.text_input("Crop")

#     Season = st.selectbox(
#         "Season",
#         ["Kharif", "Rabi", "Zaid"]
#     )

#     Crop_Area_Acres = st.number_input(
#         "Crop Area (Acres)",
#         min_value=0.0
#     )

#     Production_Cost = st.number_input(
#         "Production Cost",
#         min_value=0.0
#     )

#     Yield_Ton = st.number_input(
#         "Yield (Ton)",
#         min_value=0.0
#     )

#     Existing_Loan = st.number_input(
#         "Existing Loan",
#         min_value=0.0
#     )

#     Outstanding_Loan = st.number_input(
#         "Outstanding Loan",
#         min_value=0.0
#     )

#     Previous_Default = st.selectbox(
#         "Previous Default",
#         ["Yes", "No"]
#     )

#     Insurance_Claim_Count = st.number_input(
#         "Insurance Claim Count",
#         min_value=0
#     )

# with col2:

#     Rainfall_mm = st.number_input("Rainfall (mm)")
#     Temperature_C = st.number_input("Temperature (°C)")
#     Humidity_Percent = st.number_input("Humidity (%)")
#     Soil_Moisture = st.number_input("Soil Moisture")
#     Market_Price_Per_Ton = st.number_input("Market Price Per Ton")
#     MSP = st.number_input("MSP")
#     Price_Volatility = st.number_input("Price Volatility")
#     Weather_Risk_Score = st.number_input("Weather Risk Score")
#     District_Risk_Score = st.number_input("District Risk Score")
#     Profit = st.number_input("Profit")
#     Profit_Margin = st.number_input("Profit Margin")
#     Loan_Income_Ratio = st.number_input("Loan Income Ratio")
#     Yield_per_Acre = st.number_input("Yield per Acre")
#     Price_Gap = st.number_input("Price Gap")
#     Weather_Severity = st.number_input("Weather Severity")

#     Farm_Size = st.selectbox(
#         "Farm Size",
#         ["Small", "Medium", "Large"]
#     )

#     Income_Category = st.selectbox(
#         "Income Category",
#         ["Low", "Medium", "High"]
#     )

#     Credit_Category = st.selectbox(
#         "Credit Category",
#         ["Poor", "Average", "Good"]
#     )

# # -------------------------
# # Prediction
# # -------------------------

# if st.button("Predict"):

#     payload = {
#         "Gender": Gender,
#         "Age": Age,
#         "Soil_Type": Soil_Type,
#         "Irrigation_Type": Irrigation_Type,
#         "Crop": Crop,
#         "Season": Season,
#         "Crop_Area_Acres": Crop_Area_Acres,
#         "Production_Cost": Production_Cost,
#         "Yield_Ton": Yield_Ton,
#         "Existing_Loan": Existing_Loan,
#         "Outstanding_Loan": Outstanding_Loan,
#         "Previous_Default": Previous_Default,
#         "Insurance_Claim_Count": Insurance_Claim_Count,
#         "Rainfall_mm": Rainfall_mm,
#         "Temperature_C": Temperature_C,
#         "Humidity_Percent": Humidity_Percent,
#         "Soil_Moisture": Soil_Moisture,
#         "Market_Price_Per_Ton": Market_Price_Per_Ton,
#         "MSP": MSP,
#         "Price_Volatility": Price_Volatility,
#         "Weather_Risk_Score": Weather_Risk_Score,
#         "District_Risk_Score": District_Risk_Score,
#         "Profit": Profit,
#         "Profit_Margin": Profit_Margin,
#         "Loan_Income_Ratio": Loan_Income_Ratio,
#         "Yield_per_Acre": Yield_per_Acre,
#         "Price_Gap": Price_Gap,
#         "Weather_Severity": Weather_Severity,
#         "Farm_Size": Farm_Size,
#         "Income_Category": Income_Category,
#         "Credit_Category": Credit_Category
#     }

#     try:
#         response = requests.post(API_URL, json=payload)

#         if response.status_code == 200:
#             result = response.json()
#             st.success("Prediction Successful")
#             st.json(result)

#         else:
#             st.error(response.text)

#     except Exception as e:
#         st.error(f"Could not connect to FastAPI.\n\n{e}")

import streamlit as st
import requests

# =========================================================
# CONFIGURATION
# =========================================================

API_URL = "https://smitten-slick-deserving.ngrok-free.dev/predict"

st.set_page_config(
    page_title="AgroFinTech",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ========================================================
   GLOBAL
======================================================== */

.stApp {
    background: #f4f7f5;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ========================================================
   HERO SECTION
======================================================== */

.hero {
    position: relative;
    overflow: hidden;

    display: flex;
    justify-content: space-between;
    align-items: center;

    min-height: 330px;

    padding: 3rem 3.5rem;

    border-radius: 26px;

    background:
        radial-gradient(
            circle at 85% 20%,
            rgba(255,255,255,0.18),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #063b24 0%,
            #087443 55%,
            #0e8f55 100%
        );

    color: white;

    box-shadow:
        0 15px 40px rgba(6, 59, 36, 0.20);

    margin-bottom: 2rem;
}


/* Decorative circles */

.hero::before {
    content: "";
    position: absolute;

    width: 300px;
    height: 300px;

    border-radius: 50%;

    right: -90px;
    top: -110px;

    background: rgba(255,255,255,0.06);
}

.hero::after {
    content: "";
    position: absolute;

    width: 190px;
    height: 190px;

    border-radius: 50%;

    right: 180px;
    bottom: -110px;

    background: rgba(255,255,255,0.05);
}


/* Hero left */

.hero-left {
    max-width: 760px;
    position: relative;
    z-index: 2;
}


/* Category */

.hero-tag {
    display: inline-block;

    padding: 7px 15px;

    border-radius: 30px;

    background: rgba(255,255,255,0.12);

    border: 1px solid rgba(255,255,255,0.18);

    font-size: 0.73rem;

    font-weight: 700;

    letter-spacing: 1.2px;

    margin-bottom: 1rem;
}


/* Main title */

.hero-title {
    font-size: 3.5rem;

    font-weight: 800;

    line-height: 1.05;

    letter-spacing: -1.5px;

    margin-bottom: 0.5rem;
}


/* FinTech highlight */

.hero-title span {
    color: #b7f7d0;
}


/* Subtitle */

.hero-subtitle {
    font-size: 1.35rem;

    font-weight: 500;

    color: #e1f7e9;

    margin-bottom: 1rem;
}


/* Description */

.hero-description {
    max-width: 700px;

    font-size: 0.98rem;

    line-height: 1.65;

    color: rgba(255,255,255,0.82);

    margin-bottom: 1.5rem;
}


/* Feature pills */

.hero-features {
    display: flex;

    flex-wrap: wrap;

    gap: 10px;
}

.hero-features div {

    padding: 8px 14px;

    border-radius: 20px;

    background: rgba(255,255,255,0.11);

    border: 1px solid rgba(255,255,255,0.12);

    font-size: 0.78rem;

    color: white;
}


/* Hero right */

.hero-right {

    position: relative;

    z-index: 2;

    width: 270px;

    display: flex;

    flex-direction: column;

    align-items: center;

    gap: 15px;
}


/* Agriculture icon */

.farm-icon {

    width: 125px;

    height: 125px;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 4.5rem;

    background: rgba(255,255,255,0.10);

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 10px 30px rgba(0,0,0,0.10);
}


/* Hero stats */

.hero-stat {

    width: 100%;

    padding: 13px 18px;

    border-radius: 13px;

    background: rgba(255,255,255,0.09);

    border: 1px solid rgba(255,255,255,0.10);

    display: flex;

    justify-content: space-between;

    align-items: center;
}

.hero-stat span {

    font-size: 0.65rem;

    color: rgba(255,255,255,0.65);

    letter-spacing: 1px;
}

.hero-stat strong {

    font-size: 0.75rem;

    color: #d7ffe5;
}


/* ========================================================
   INFO CARDS
======================================================== */

.info-card {

    background: white;

    border: 1px solid #e4ebe7;

    border-radius: 16px;

    padding: 1.1rem;

    text-align: center;

    min-height: 100px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    box-shadow:
        0 3px 12px rgba(0,0,0,0.035);
}

.info-icon {
    font-size: 1.5rem;
    margin-bottom: 5px;
}

.info-title {
    font-size: 0.82rem;
    font-weight: 650;
    color: #16452f;
}

.info-description {
    font-size: 0.68rem;
    color: #7a8580;
    margin-top: 3px;
}


/* ========================================================
   SECTION HEADERS
======================================================== */

.section-header {

    background: white;

    border-radius: 16px;

    padding: 1.25rem 1.5rem;

    margin-top: 1.5rem;
    margin-bottom: 1rem;

    border: 1px solid #e4ebe7;

    box-shadow:
        0 3px 12px rgba(0,0,0,0.035);
}

.section-title {

    font-size: 1.25rem;

    font-weight: 700;

    color: #123d29;

    margin-bottom: 3px;
}

.section-description {

    font-size: 0.82rem;

    color: #40534a;
}


/* ========================================================
   INPUTS
======================================================== */

div[data-testid="stWidgetLabel"],
div[data-testid="stWidgetLabel"] *,
label[data-testid="stWidgetLabel"],
label[data-testid="stWidgetLabel"] * {

    color: #173f2b !important;

    font-weight: 650 !important;
}

div[data-baseweb="select"] > div {

    border-radius: 10px;
}

.stTextInput input,
.stNumberInput input {

    border-radius: 10px !important;
}


/* ========================================================
   PREDICT BUTTON
======================================================== */

.predict-container {

    background: white;

    border-radius: 18px;

    padding: 1.5rem;

    margin-top: 2rem;

    border: 1px solid #e4ebe7;

    box-shadow:
        0 5px 18px rgba(0,0,0,0.05);
}

.stButton > button {

    width: 100%;

    height: 3.4rem;

    border-radius: 12px;

    background: linear-gradient(
        135deg,
        #086b3c,
        #14975a
    );

    color: white;

    font-size: 1.05rem;

    font-weight: 650;

    border: none;

    box-shadow:
        0 6px 18px rgba(8,107,60,0.22);

    transition: all 0.2s ease;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 9px 23px rgba(8,107,60,0.28);
}


/* ========================================================
   RESULT
======================================================== */

.result-wrapper {

    background: white;

    border-radius: 20px;

    padding: 2rem;

    margin-top: 1.5rem;

    border: 1px solid #dfe8e3;

    box-shadow:
        0 7px 25px rgba(0,0,0,0.06);

    text-align: center;
}

.result-heading {

    color: #63716a;

    font-size: 0.85rem;

    text-transform: uppercase;

    letter-spacing: 1.2px;

    margin-bottom: 0.4rem;
}

.result-subheading {

    color: #183d2b;

    font-size: 1.4rem;

    font-weight: 700;
}


/* ========================================================
   ALERT MESSAGES
======================================================== */

[data-testid="stAlert"] {

    background: #fff4cc !important;

    border: 1px solid #e0a800 !important;

    color: #3d2f00 !important;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] [data-testid="stMarkdownContainer"] {

    color: #3d2f00 !important;

    font-weight: 600 !important;
}


/* ========================================================
   FOOTER
======================================================== */

.footer {

    text-align: center;

    color: #8a958f;

    font-size: 0.75rem;

    margin-top: 3rem;

    padding-top: 1rem;

    border-top: 1px solid #e1e7e3;
}


/* ========================================================
   RESPONSIVE
======================================================== */

@media (max-width: 900px) {

    .hero {
        padding: 2rem;
    }

    .hero-right {
        display: none;
    }

    .hero-title {
        font-size: 2.7rem;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-left">

        <div class="hero-tag">
            🌾 AGRICULTURE × FINANCE
        </div>

        <div class="hero-title">
            Agro<span>FinTech</span>
        </div>

        <div class="hero-subtitle">
            Smart Credit Assessment for Farmers
        </div>

        <p class="hero-description">
            AI-powered agricultural lending that combines
            <b>farmer profiles, crop performance, financial health,
            market conditions and weather risks</b> to support
            smarter and data-driven credit decisions.
        </p>

        <div class="hero-features">

            <div>🌱 Crop Analytics</div>

            <div>💳 Credit Risk</div>

            <div>🌦️ Weather Intelligence</div>

            <div>🤖 AI Prediction</div>

        </div>

    </div>


    <div class="hero-right">

        <div class="farm-icon">
            🌾
        </div>

        <div class="hero-stat">

            <span>LOAN RISK</span>

            <strong>AI ASSESSMENT</strong>

        </div>

        <div class="hero-stat">

            <span>DATA SIGNALS</span>

            <strong>30+ FACTORS</strong>

        </div>

    </div>

</div>
""")


# =========================================================
# OVERVIEW CARDS
# =========================================================

info1, info2, info3, info4 = st.columns(4)

with info1:

    st.html("""
    <div class="info-card">

        <div class="info-icon">🌱</div>

        <div class="info-title">
            Crop Intelligence
        </div>

        <div class="info-description">
            Analyze agricultural performance
        </div>

    </div>
    """)


with info2:

    st.html("""
    <div class="info-card">

        <div class="info-icon">💳</div>

        <div class="info-title">
            Credit Assessment
        </div>

        <div class="info-description">
            Evaluate borrower financial health
        </div>

    </div>
    """)


with info3:

    st.html("""
    <div class="info-card">

        <div class="info-icon">🌦️</div>

        <div class="info-title">
            Weather Risk
        </div>

        <div class="info-description">
            Account for environmental conditions
        </div>

    </div>
    """)


with info4:

    st.html("""
    <div class="info-card">

        <div class="info-icon">🤖</div>

        <div class="info-title">
            ML Prediction
        </div>

        <div class="info-description">
            Data-driven lending decision
        </div>

    </div>
    """)


# =========================================================
# FARMER PROFILE
# =========================================================

st.html("""
<div class="section-header">

    <div class="section-title">
        🧑‍🌾 Farmer Profile
    </div>

    <div class="section-description">
        Basic demographic and agricultural profile
    </div>

</div>
""")


col1, col2, col3, col4 = st.columns(4)

with col1:

    Gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:

    Age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=26
    )

with col3:

    Farm_Size = st.selectbox(
        "Farm Size",
        ["Small", "Medium", "Large"],
        index=2
    )

with col4:

    Income_Category = st.selectbox(
        "Income Category",
        ["Low", "Medium", "High"],
        index=1
    )


# =========================================================
# FARM & CROP
# =========================================================

st.html("""
<div class="section-header">

    <div class="section-title">
        🌱 Farm & Crop Information
    </div>

    <div class="section-description">
        Agricultural production and crop characteristics
    </div>

</div>
""")


col1, col2, col3, col4 = st.columns(4)

with col1:

    Soil_Type = st.selectbox(
        "Soil Type",
        ["Loamy", "Red", "Alluvial", "Black", "Clay"]
    )

with col2:

    Irrigation_Type = st.selectbox(
        "Irrigation Type",
        ["Borewell", "Canal", "Drip", "Rainfed", "Sprinkler"]
    )

with col3:

    Crop = st.text_input(
        "Crop",
        value="Maize",
        placeholder="e.g. Wheat"
    )

with col4:

    Season = st.selectbox(
        "Season",
        ["Kharif", "Rabi", "Zaid"],
        index=2
    )


col1, col2, col3, col4 = st.columns(4)

with col1:

    Crop_Area_Acres = st.number_input(
        "Crop Area (Acres)",
        min_value=0.0,
        step=0.1,
        value=33.58
    )

with col2:

    Production_Cost = st.number_input(
        "Production Cost",
        min_value=0.0,
        step=1000.0,
        value=881185.3
    )

with col3:

    Yield_Ton = st.number_input(
        "Yield (Ton)",
        min_value=0.0,
        step=0.1,
        value=64.3
    )

with col4:

    Yield_per_Acre = st.number_input(
        "Yield per Acre",
        min_value=0.0,
        step=0.1,
        value=1.91
    )


# =========================================================
# WEATHER & ENVIRONMENT
# =========================================================

st.html("""
<div class="section-header">

    <div class="section-title">
        🌦️ Environmental & Weather Risk
    </div>

    <div class="section-description">
        Weather and environmental conditions affecting agricultural risk
    </div>

</div>
""")


col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    Rainfall_mm = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=59.4
    )

with col2:

    Temperature_C = st.number_input(
        "Temperature (°C)",
        value=34.2
    )

with col3:

    Humidity_Percent = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=89.6
    )

with col4:

    Soil_Moisture = st.number_input(
        "Soil Moisture",
        min_value=0.0,
        value=25.0
    )

with col5:

    Weather_Severity = st.number_input(
        "Weather Severity",
        min_value=0.0,
        value=56.5
    )


col1, col2, col3 = st.columns(3)

with col1:

    Weather_Risk_Score = st.number_input(
        "Weather Risk Score",
        min_value=0.0,
        value=61.0
    )

with col2:

    District_Risk_Score = st.number_input(
        "District Risk Score",
        min_value=0.0,
        value=52.0
    )

with col3:

    Price_Volatility = st.number_input(
        "Price Volatility",
        min_value=0.0,
        value=22.43
    )


# =========================================================
# MARKET & PROFITABILITY
# =========================================================

st.html("""
<div class="section-header">

    <div class="section-title">
        📈 Market & Profitability
    </div>

    <div class="section-description">
        Crop prices, profitability and income indicators
    </div>

</div>
""")


col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    Market_Price_Per_Ton = st.number_input(
        "Market Price / Ton",
        min_value=0.0,
        value=28595.01
    )

with col2:

    MSP = st.number_input(
        "MSP",
        min_value=0.0,
        value=20904.0
    )

with col3:

    Price_Gap = st.number_input(
        "Price Gap",
        min_value=0.0,
        value=7691.01
    )

with col4:

    Profit = st.number_input(
        "Profit",
        min_value=-1000000000.0,
        value=-365226.4
    )

with col5:

    Profit_Margin = st.number_input(
        "Profit Margin",
        min_value=-100.0,
        value=-0.4145
    )


# =========================================================
# LOAN & CREDIT
# =========================================================

st.html("""
<div class="section-header">

    <div class="section-title">
        💳 Loan & Credit Information
    </div>

    <div class="section-description">
        Existing financial obligations and borrower credit history
    </div>

</div>
""")


col1, col2, col3, col4 = st.columns(4)

with col1:

    Existing_Loan = st.selectbox(
        "Existing Loan",
        ["No", "Yes"],
        index=0
    )

with col2:

    Outstanding_Loan = st.number_input(
        "Outstanding Loan",
        min_value=0.0,
        value=1814844.0
    )

with col3:

    Loan_Income_Ratio = st.number_input(
        "Loan / Income Ratio",
        min_value=0.0,
        value=3.5174
    )

with col4:

    Insurance_Claim_Count = st.number_input(
        "Insurance Claims",
        min_value=0,
        value=3
    )


col1, col2 = st.columns(2)

with col1:

    Previous_Default = st.selectbox(
        "Previous Default",
        ["Yes", "No"],
        index=0
    )

with col2:

    Credit_Category = st.selectbox(
        "Credit Category",
        ["Poor", "Average", "Excellent"],
        index=1
    )


# =========================================================
# PREDICTION
# =========================================================

st.html("""
<div class="predict-container">

</div>
""")


predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])

with predict_col2:

    if st.button(
        "🔍  Predict Agricultural Loan Risk",
        use_container_width=True
    ):

        # ---------------------------------------------
        # Validation
        # ---------------------------------------------

        if not Crop.strip():

            st.warning(
                "🌱 Please enter the crop name before prediction."
            )

        else:

            # -----------------------------------------
            # API PAYLOAD
            # -----------------------------------------

            payload = {

                "Gender": Gender,

                "Age": Age,

                "Soil_Type": Soil_Type,

                "Irrigation_Type": Irrigation_Type,

                "Crop": Crop,

                "Season": Season,

                "Crop_Area_Acres": Crop_Area_Acres,

                "Production_Cost": Production_Cost,

                "Yield_Ton": Yield_Ton,

                "Existing_Loan": Existing_Loan,

                "Outstanding_Loan": Outstanding_Loan,

                "Previous_Default": Previous_Default,

                "Insurance_Claim_Count": Insurance_Claim_Count,

                "Rainfall_mm": Rainfall_mm,

                "Temperature_C": Temperature_C,

                "Humidity_Percent": Humidity_Percent,

                "Soil_Moisture": Soil_Moisture,

                "Market_Price_Per_Ton": Market_Price_Per_Ton,

                "MSP": MSP,

                "Price_Volatility": Price_Volatility,

                "Weather_Risk_Score": Weather_Risk_Score,

                "District_Risk_Score": District_Risk_Score,

                "Profit": Profit,

                "Profit_Margin": Profit_Margin,

                "Loan_Income_Ratio": Loan_Income_Ratio,

                "Yield_per_Acre": Yield_per_Acre,

                "Price_Gap": Price_Gap,

                "Weather_Severity": Weather_Severity,

                "Farm_Size": Farm_Size,

                "Income_Category": Income_Category,

                "Credit_Category": Credit_Category

            }

            # -----------------------------------------
            # API REQUEST
            # -----------------------------------------

            try:

                with st.spinner(
                    "🤖 Analyzing agricultural and financial risk..."
                ):

                    response = requests.post(
                        API_URL,
                        json=payload,
                        timeout=60
                    )


                # -------------------------------------
                # SUCCESS
                # -------------------------------------

                if response.status_code == 200:

                    result = response.json()


                    st.html("""
                    <div class="result-wrapper">

                        <div class="result-heading">
                            AI-POWERED AGRICULTURAL CREDIT ASSESSMENT
                        </div>

                        <div class="result-subheading">
                            Loan Risk Prediction
                        </div>

                    </div>
                    """)


                    prediction = result.get("Prediction", result)
                    loan_prediction = prediction.get("Loan_Approval")
                    risk_prediction = prediction.get("Risk_Level")

                    loan_status = {
                        0: "Approved",
                        1: "Rejected"
                    }.get(loan_prediction, str(loan_prediction))

                    risk_status = {
                        0: "Low",
                        1: "Medium",
                        2: "High"
                    }.get(risk_prediction, str(risk_prediction))

                    if loan_status == "Approved":
                        st.success(f"### 🟢 Loan: {loan_status}")
                    else:
                        st.error(f"### 🔴 Loan: {loan_status}")

                    if risk_status == "High":
                        st.error(f"### 🔴 Risk Level: {risk_status}")
                    elif risk_status == "Medium":
                        st.warning(f"### 🟡 Risk Level: {risk_status}")
                    else:
                        st.success(f"### 🟢 Risk Level: {risk_status}")


                    # ---------------------------------
                    # DETAILS
                    # ---------------------------------

                    with st.expander(
                        "📋 View Prediction Details"
                    ):

                        st.json(result)


                # -------------------------------------
                # API ERROR
                # -------------------------------------

                else:

                    st.error(
                        f"❌ Prediction failed\n\n"
                        f"{response.text}"
                    )


            # -----------------------------------------
            # CONNECTION ERROR
            # -----------------------------------------

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to FastAPI.\n\n"
                    "Please make sure your FastAPI server "
                    "is running on port 8000."
                )


            # -----------------------------------------
            # TIMEOUT
            # -----------------------------------------

            except requests.exceptions.Timeout:

                st.error(
                    "⏳ The prediction request timed out. "
                    "Please try again."
                )


            # -----------------------------------------
            # OTHER ERROR
            # -----------------------------------------

            except Exception as e:

                st.error(
                    f"⚠️ Unexpected error:\n\n{e}"
                )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    🌾 <b>AgroFinTech</b>
    &nbsp; • &nbsp;
    AI-Powered Agricultural Credit Risk Assessment
    &nbsp; • &nbsp;
    Data-Driven Lending

</div>
""")