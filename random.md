# 🏠 House Price Prediction

## Project Description

House Price Prediction is a Machine Learning project that predicts the estimated price of a house based on different house features.

## Objective

The main objective of this project is to predict house prices using Machine Learning and provide an easy-to-use interface for users.

## Features Used

The model uses the following features:

- Area (sq ft)
- Bedrooms
- Bathrooms
- Floors
- Age
- Parking
- Location
- Furnished

## Target Variable

- Price

The house price is represented in Lakhs.

## Dataset

The dataset contains 1000 house records from different cities in Maharashtra.

The dataset includes:

- House_ID
- Area
- Bedrooms
- Bathrooms
- Floors
- Age
- Parking
- Location
- Furnished
- Price

## Data Preprocessing

The following preprocessing steps were performed:

1. Checked missing values.
2. Checked duplicate records.
3. Separated features and target variable.
4. Identified numerical and categorical features.
5. Applied One-Hot Encoding to categorical features.
6. Split the dataset into 80% training data and 20% testing data.

## Exploratory Data Analysis

The following visualizations were performed:

- Location-wise average price
- Area vs Price
- Bedrooms vs Price
- Bathrooms vs Price
- Floors vs Price
- Furnished vs Price
- Parking vs Price
- Price Distribution
- Price Boxplot
- Furnished Distribution Pie Chart
- Correlation Analysis
- Correlation Heatmap
- Pair Plot

## Machine Learning Model

Random Forest Regressor was used for house price prediction.

The model uses multiple decision trees and combines their predictions to produce the final result.

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results

- MAE: 9.52 Lakhs
- RMSE: 12.12 Lakhs
- R² Score: 0.94

The model achieved an R² score of 0.94, which indicates good prediction performance on the test data.

## Model Saving

The trained model pipeline was saved using Joblib as:

`house_price_model.pkl`

## User Interface

A Streamlit web application was created for prediction.

The user can enter:

- Area
- Bedrooms
- Bathrooms
- Floors
- Age
- Parking
- Location
- Furnished

The application then displays the estimated house price in Lakhs.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## Project Flow

Dataset
→ Data Cleaning
→ EDA
→ Preprocessing
→ Random Forest Model
→ Model Evaluation
→ Model Saving
→ Streamlit Application