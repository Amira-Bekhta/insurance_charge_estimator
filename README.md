#### The estimation application can be found in this link: <code>https://insurance-charge-estimator.onrender.com/</code>

# Insurance charge estimation app 📊

This project is one in which I have built a machine learning model that helps estimate the cost of insurance and embedded it into and HTML web application to help users estimate their charges by entering their information

## Technologies 🛠️
- **Python**
- **Flask**
- **Pandas**
- **scikit-learn**
- **HTML and CSS**
- **Random Forest Regressor** (for estimation)

## Folder Structure 📁
```
/project-root
│
├── /.venv                 # The virtual environement with all required packages and dependencies
├── /app                   # Templates and Python code for the application
├── /data                  # Dataset, raw and preprocessed
├── /model                 # Saved model with X_test and y_test data
├── /notebooks             # Jupyter notebooks for EDA, preprocessing, and evaluation
├── /src                   # Source code for loading data and training
├── Requirements.txt       # Python dependencies
└── README.md              # This README file
```

## Installation 📦
1. Clone this repository:
   ```bash
   git clone https://github.com/Amira-Bekhta/Spam_detector 
   ```

2. Install the required libraries:
   ```bash
   pip install -r Requirements.txt
   ```

3. Run the application on your local machine:
   ```bash
   python app/app.py
   ```

## Model 🧠
**Random Forest regressor**
- **Accuracy Score**: 0.95 

## Dataset 📊
This project uses the [Medical Insurance Price Prediction](https://www.kaggle.com/datasets/harishkumardatalab/medical-insurance-price-prediction)