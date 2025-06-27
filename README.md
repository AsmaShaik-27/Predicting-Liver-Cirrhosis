#  Liver Disease Prediction

##  Goal

To develop a web application using **Flask**, **HTML**, and **CSS** to predict whether a person is suffering from liver disease, using machine learning algorithms trained on a medical dataset.

---

##  About the Dataset

This machine learning project aims to predict liver disease based on clinical features. The dataset was sourced from **Kaggle** and contains:

-  **441 male** and  **142 female** patients  
-  **416 liver patients** and **167 non-liver patients**
-  Collected from the **North East region of Andhra Pradesh, India**

Patients aged over 89 are all recorded as "90".  
The target column, **"Dataset"**, classifies:
- `1`: Liver disease
- `2`: No liver disease

###  Feature Columns

- Age
- Gender
- Total Bilirubin
- Direct Bilirubin
- Alkaline Phosphotase
- Alamine Aminotransferase (SGPT)
- Aspartate Aminotransferase (SGOT)
- Total Proteins
- Albumin
- Albumin and Globulin Ratio
- Dataset (Target variable)

---

##  Problem Type

**Binary Classification**: Predict if the person has liver disease (`1`) or not (`2`)

---

##  Project Description

### 1.  Exploratory Data Analysis (EDA)

- Checked class balance using count plots
- Created factor plots for Age, Gender, and Target
- Plotted histograms and scatter plots to analyze feature distributions
- Correlation heatmap to identify strong relationships
- Jointplot of Total Proteins vs Albumin

### 2.  Feature Engineering

- Handled missing values in `Albumin_and_Globulin_Ratio` using mean
- Applied **Label Encoding** on Gender (1 = Male, 0 = Female)
- Remaining NaNs were filled with `0.94` (domain-based imputation)
- Split data into `X` (features) and `y` (target)

### 3.  Feature Selection

Selected features based on domain knowledge:
- Total_Bilirubin
- Direct_Bilirubin
- Alkaline_Phosphotase
- Alamine_Aminotransferase
- Total_Protiens
- Albumin
- Albumin_and_Globulin_Ratio
- Age
- Gender
- Aspartate_Aminotransferase

### 4.  Model Building

- Used train-test split for training and validation
- Tried various models, finalized:
  - Logistic Regression
  - Random Forest Classifier
  - Decision Tree Classifier
- Evaluated using accuracy, confusion matrix, and classification report

### 5.  Hyperparameter Optimization

- Used `GridSearchCV` for tuning the Random Forest model
- Improved accuracy and reduced false positives/negatives

### 6.  Model Saving

- Trained model was saved as a `.pkl` using `joblib`
- Enables reloading during deployment without retraining

### 7.  Deployment

- Deployed locally on `localhost:5000` using Flask
- Backend: Python + Flask  
- Frontend: HTML & CSS (minimal styling)

---

### Future Enhancements
- Add more features to improve model accuracy
- Deploy app on cloud platforms:
    - Heroku
    - AWS
    - Render
    - Google Cloud / Azure
- Add visual analytics for input interpretation
- Integrate explainability tools like SHAP

---
### Technology Stack
 - Python
 - Flask
 - Scikit-learn
 - Pandas, NumPy
 - Matplotlib, Seaborn
 - HTML & CSS

