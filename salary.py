import streamlit as st
import joblib
import pandas as pd

# Page config
st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.title {
    text-align: center;
    color: #00ffcc;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cccccc;
    font-size: 18px;
    margin-bottom: 30px;
}

.stNumberInput input {
    border-radius: 10px;
    border: 2px solid #00ffcc;
}

.stButton>button {
    background-color: #00ffcc;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.result {
    text-align: center;
    font-size: 28px;
    color: #00ffcc;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("salary_model.pkl")

# Title
st.markdown('<div class="title">💰 Salary Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your details to estimate salary</div>', unsafe_allow_html=True)

# Inputs
exp = st.slider("💼 Experience (Years)", 0.0, 15.0, 1.0)
skills = st.slider("🧠 Skills Score (1-10)", 1, 10, 5)
edu = st.selectbox("🎓 Education Level", 
                   ["School (1)", "Graduate (2)", "Postgraduate (3)"])

# Convert education to number
edu_map = {
    "School (1)": 1,
    "Graduate (2)": 2,
    "Postgraduate (3)": 3
}
edu_val = edu_map[edu]

# Predict button
if st.button("🚀 Predict Salary"):
    inp = pd.DataFrame([[exp, skills, edu_val]],
                       columns=["experience","skills_score","education_level"])
    
    result = model.predict(inp)
    
    st.markdown(
        f'<div class="result">💰 Estimated Salary: ₹{round(result[0], 2)}</div>',
        unsafe_allow_html=True
    )