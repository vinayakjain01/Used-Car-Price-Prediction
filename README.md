# Used Car Price Prediction
Project Overview
This project predicts used car prices using machine learning, offering a practical tool to estimate market value quickly. The workflow includes data cleaning, modeling, and a user-facing web interface for real-time predictions.

Objectives
Train a Random Forest regression model to accurately estimate used car prices.

Handle preprocessing: feature selection, encoding, and model training within a Jupyter Notebook.

Deploy a simple Flask-based web app allowing dynamic price prediction from user inputs.

Dataset
Format: Excel file (cardekho_data.xls)

Contents: Likely includes car-related features such as year, brand, kilometers driven, fuel type, location, and price.

Tools & Technologies
Python: For data processing, model training, and deployment.

Scikit-learn: Random Forest implementation for regression.

Flask: User interface to interact with the trained model.

Jupyter Notebook: Seamless workflow combining analysis and visualization.

Pickle (.pkl): Model and feature mapping storage for deployment.

Project Highlights
Trained a Random Forest regression model, serialized as car_price_model.pkl with feature mapping in model_columns.pkl.

Built a Flask app (app (1).py) to serve live predictions via the model.

Demonstrated application flow through a video demo (car_prediction3.mp4) and screenshot (car_prediction_img.JPG).

Repository Structure
├── cardekho_data.xls                # Source dataset  
├── Car_price_prediction_usingRandomForest.ipynb  # Modeling & analysis notebook  
├── car_price_model.pkl              # Trained regression model  
├── model_columns.pkl                # Feature list for model input  
├── app (1).py                       # Flask app for live prediction  
├── car_prediction3.mp4              # Demo video of model usage  
├── car_prediction_img.JPG           # Screenshot of prediction output  
└── README.md                        # Project documentation  
How to Use
Open the notebook to explore data processing and model metrics.

Run the Flask app:
python app\ \(1\).py
Input car features to receive a price prediction.

Check the demo video or screenshot for interface reference.

About the Author
Vinayak Jain
GitHub: vinayakjain01
