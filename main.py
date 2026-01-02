import streamlit as st
import pandas as pd
import joblib

st.title("Customer Churn Prediction")
st.write("This app predicts customer churn using a pre-trained Random Forest model.")

@st.cache_resource
def load_model():
    model = joblib.load('churn_model.pkl')
    return model

@st.cache_resource
def load_data():
    data = pd.read_csv('Churn_Modelling.csv')
    return data

df = load_data()
model = load_model()

def convert_to_num(x):
    mapping = {}
    for idx, val in enumerate(x):
        mapping[val] = idx
    return mapping

geo_map = convert_to_num(df['Geography'].unique())
gender_map = convert_to_num(df['Gender'].unique())

credit_score = st.number_input("Credit Score", min_value=350, max_value=850, value=600)
geography = st.selectbox("Geography", options=list(geo_map.keys()))
gender = st.selectbox("Gender", options=list(gender_map.keys()))
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=1000.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
has_cr_card = st.selectbox("Has Credit Card", options=[0, 1])
is_active_member = st.selectbox("Is Active Member", options=[0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geo_map[geography]],
    'Gender': [gender_map[gender]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
})

if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is unlikely to churn.")