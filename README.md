# 🎓 Student Performance Prediction Using Machine Learning

A machine learning web application that predicts a student's **Math score** using their **Reading and Writing scores**. The model uses **Multiple Linear Regression** and the interactive interface is built with **Streamlit**.

## Project Overview

This project explores student exam performance, visualizes score patterns, trains a regression model, and uses that model to predict Math scores for new inputs.

**Inputs:** Reading score and Writing score (0–100)  
**Output:** Predicted Math score  
**Algorithm:** Linear Regression

> Predictions are estimates, not guaranteed exam results. The model was trained on an existing dataset and should not be used to make high-stakes decisions about students.

## Dataset

**Kaggle:** [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

The dataset contains **1,000 rows and 8 columns**:

- `gender`
- `race/ethnicity`
- `parental level of education`
- `lunch`
- `test preparation course`
- `math score`
- `reading score`
- `writing score`

The current prediction model uses only `reading score` and `writing score` as input features, with `math score` as the target. The dataset does **not** include study hours.

## Technologies

- Python
- Pandas and NumPy — data analysis
- Matplotlib and Seaborn — visualization
- Scikit-learn — Linear Regression and evaluation
- Joblib — saving and loading the trained model
- Streamlit — web interface
- Jupyter Notebook — experimentation and training

## Project Workflow

1. Load and explore the dataset.
2. Check missing values, duplicates, and data types.
3. Visualize score distributions and correlations.
4. Select Reading and Writing scores as features, and Math score as target.
5. Split the dataset into training (80%) and testing (20%) sets.
6. Train a Linear Regression model.
7. Evaluate predictions using **MAE**, **RMSE**, and **R²**.
8. Save the model as `student_model.pkl` and build a Streamlit app.

## Repository Structure

```text
Student-Performance-Prediction/
├── app.py
├── student_model.pkl
├── requirements.txt
└── README.md
```

Optional files: the training notebook (`.ipynb`) and the dataset CSV, if you choose to share them.

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/Student-Performance-Prediction.git
   cd Student-Performance-Prediction
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   streamlit run app.py
   ```

4. Open the local address shown in your terminal (usually `http://localhost:8501`).

**Important:** Keep `student_model.pkl` in the same folder as `app.py`. Use a compatible version of Scikit-learn when loading the trained model.

## Deploy on Streamlit Community Cloud

1. Upload `app.py`, `student_model.pkl`, `requirements.txt`, and `README.md` to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub and select your repository.
4. Choose the `main` branch and set the main file path to `app.py`.
5. Click **Deploy**.

## Model Evaluation

The model is evaluated on the held-out test set using:

- **MAE (Mean Absolute Error):** average absolute prediction error.
- **RMSE (Root Mean Squared Error):** emphasizes larger prediction errors.
- **R² Score:** proportion of variation explained relative to a mean-prediction baseline.

Add your measured results here after running the notebook:

| Metric | Result |
|---|---|
| MAE | Add your value |
| RMSE | Add your value |
| R² Score | Add your value |

## Author

**Tanveer Ahmad**  
BS Software Engineering

## Acknowledgment

Dataset: *Students Performance in Exams*, available on Kaggle.
