# Customer Churn Prediction App

A Streamlit web application that predicts customer churn using a pre-trained Random Forest machine learning model.

## Overview

This application helps businesses identify customers who are likely to leave (churn) based on various customer attributes. The prediction model analyzes factors such as credit score, geography, age, account balance, and customer engagement metrics to assess churn risk.

## Features

- Interactive web interface built with Streamlit
- Real-time churn prediction using Random Forest classifier
- User-friendly input fields for customer data
- Instant visual feedback on churn likelihood
- Cached model and data loading for improved performance

## Prerequisites

Before running this application, ensure you have Python 3.7 or higher installed on your system.

## Installation

1. Clone this repository or download the project files:
```bash
git clone <https://github.com/OmarMahmoud1810/Epsilon-Project>
cd customer-churn-prediction
```

2. Install the required Python packages:
```bash
pip install streamlit pandas joblib scikit-learn
```

## Required Files

Ensure the following files are in your project directory:

- `main.py` - The main Streamlit application
- `churn_model.pkl` - Pre-trained Random Forest model (pickle file)
- `Churn_Modelling.csv` - Dataset containing customer information
- `README.md` - This file

## Usage

1. Navigate to the project directory in your terminal

2. Run the Streamlit app:
```bash
streamlit run main.py
```

3. The application will open in your default web browser (typically at `http://localhost:8501`)

4. Enter customer information in the input fields:
   - **Credit Score**: Customer's credit score (350-850)
   - **Geography**: Customer's location
   - **Gender**: Customer's gender
   - **Age**: Customer's age (18-100)
   - **Tenure**: Years with the bank (0-10)
   - **Balance**: Account balance
   - **Number of Products**: Number of bank products used (1-4)
   - **Has Credit Card**: Whether customer has a credit card (0 or 1)
   - **Is Active Member**: Whether customer is active (0 or 1)
   - **Estimated Salary**: Customer's estimated annual salary

5. Click the "Predict Churn" button to get the prediction

6. View the result:
   - Red error message: Customer is likely to churn
   - Green success message: Customer is unlikely to churn

## Model Information

The application uses a Random Forest classifier trained on historical customer data. The model considers 10 features to make predictions:
- Credit Score
- Geography (encoded)
- Gender (encoded)
- Age
- Tenure
- Balance
- Number of Products
- Credit Card status
- Active Member status
- Estimated Salary

## Data Format

The `Churn_Modelling.csv` file should contain the following columns:
- CreditScore
- Geography
- Gender
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary
- Exited (target variable)

## Technical Details

- **Framework**: Streamlit
- **ML Model**: Random Forest (scikit-learn)
- **Data Processing**: pandas
- **Model Serialization**: joblib
- **Caching**: Uses Streamlit's `@st.cache_resource` for efficient model and data loading

## Project Structure

```
customer-churn-prediction/
│
├── main.py                  # Main application file
├── churn_model.pkl          # Trained model file
├── Churn_Modelling.csv      # Dataset
└── README.md               # Documentation
```

## Troubleshooting

**Model file not found:**
- Ensure `churn_model.pkl` is in the same directory as `main.py`

**Data file not found:**
- Ensure `Churn_Modelling.csv` is in the same directory as `main.py`

**Import errors:**
- Verify all required packages are installed: `pip install streamlit pandas joblib scikit-learn`

**Port already in use:**
- Run Streamlit on a different port: `streamlit run main.py --server.port 8502`

## Future Enhancements

- Add model performance metrics and visualization
- Include feature importance analysis
- Allow users to upload custom datasets
- Add batch prediction capability
- Implement model retraining functionality
- Add export functionality for predictions
