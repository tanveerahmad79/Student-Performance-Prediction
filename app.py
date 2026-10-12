
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# Load Trained Machine Learning Model
MODEL_PATH = Path(__file__).parent / "student_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Application Title
st.title("🎓 Student Performance Prediction")

st.write(
    "This Machine Learning application predicts "
    "a student's Math score based on Reading "
    "and Writing scores using Linear Regression."
)

st.divider()

# Sidebar
st.sidebar.title("Project Information")
st.sidebar.write("Project: Student Performance Prediction")
st.sidebar.write("Algorithm: Linear Regression")
st.sidebar.write("Language: Python")
st.sidebar.write("Framework: Streamlit")
st.sidebar.write("Developer: Tanveer Ahmad")

# User Input Section
st.subheader("Enter Student Information")

reading_score = st.slider(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=70
)

writing_score = st.slider(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=75
)

# Prediction Button
if st.button("Predict Math Score", type="primary"):

    input_data = pd.DataFrame({
        "reading score": [reading_score],
        "writing score": [writing_score]
    })

    prediction = model.predict(input_data)[0]

    st.success("Prediction Completed Successfully!")

    st.metric(
        label="Predicted Math Score",
        value=f"{prediction:.2f}"
    )

    st.write("### Student Performance Details")

    results = pd.DataFrame({
        "Subject": [
            "Reading",
            "Writing",
            "Predicted Math"
        ],
        "Score": [
            reading_score,
            writing_score,
            prediction
        ]
    })

    st.dataframe(results, hide_index=True)

    # Bar Chart
    st.subheader("Performance Visualization")

    chart_data = results.set_index("Subject")
    st.bar_chart(chart_data)

    st.info(
        "This score is an estimate generated "
        "by the trained Linear Regression model. "
        "Actual results may differ."
    )

# Footer
st.divider()
st.caption(
    "Student Performance Prediction | "
    "Machine Learning Project"
)
