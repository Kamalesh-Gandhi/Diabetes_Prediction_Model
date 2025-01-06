# Diabetes Prediction Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Information](#dataset-information)
3. [Tools and Technologies](#tools-and-technologies)
4. [Project Workflow](#project-workflow)
5. [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
6. [Model Evaluation](#model-evaluation)
7. [Streamlit UI](#streamlit-ui)
8. [Deployment on AWS EC2](#deployment-on-aws-ec2)
9. [Installation](#installation)

---

## Project Overview

The goal of this project is to develop a model that can predict whether an individual has diabetes based on various health and demographic parameters. This prediction can assist in early diagnosis and preventive measures for diabetes.

---

## Dataset Information

The dataset includes health-related features such as BMI, blood glucose level, HbA1c levels, and others to predict diabetes.

**Dataset Columns**:  

| Column Name          | Description                           |
|-----------------------|---------------------------------------|
| `gender`             | Gender of the individual (Male/Female)|
| `age`                | Age of the individual                |
| `hypertension`       | Hypertension status (1: Yes, 0: No)  |
| `heart_disease`      | Heart disease status (1: Yes, 0: No) |
| `smoking_history`    | Smoking history                      |
| `bmi`                | Body Mass Index                      |
| `HbA1c_level`        | Hemoglobin A1c level                 |
| `blood_glucose_level`| Blood glucose level                  |
| `diabetes`           | Diabetes status (1: Yes, 0: No)      |

---

## Tools and Technologies

- **Programming Language**: Python  
- **Libraries**:
  - Pandas
  - NumPy
  - Scikit-learn
  - Matplotlib
  - Seaborn  

---

## Project Workflow

1. **Data Collection**: Load the dataset.  
2. **Exploratory Data Analysis (EDA)**: Understand the data distribution and relationships.  
3. **Data Cleaning**: Handle missing values, duplicates, and incorrect data.  
4. **Feature Engineering**: Create new features or transform existing ones.  
5. **Data Visualization**: Visualize patterns, trends, and correlations.  
6. **Model Building**: Build machine learning models to predict diabetes.  
7. **Model Evaluation**: Evaluate models for accuracy, precision, and recall.  
8. **Final Deployment**: Deploy the model for predictions.  

---

## Data Cleaning and Preprocessing

1. **Handling Missing Values**:  
   - Analyze the dataset for null or missing values.  
   - Impute or drop missing records as necessary.  

2. **Outlier Detection**:  
   - Check for extreme outliers in numerical columns (e.g., BMI, blood glucose level).  

3. **Feature Transformation**:  
   - Convert categorical variables (`gender`, `smoking_history`) into numerical formats.  
   - Scale numerical features (e.g., `age`, `bmi`, `HbA1c_level`).  

4. **Encoding**:  
   - Use label encoding or one-hot encoding for categorical data.  

5. **Target Variable**:  
   - Ensure the `diabetes` column (1: Yes, 0: No) is the target variable for prediction.  

---

## Model Evaluation

- **Pre-Tuning Score**: Initial performance metrics of the GradientBoost model.
- **Post-Tuning Score**: Improved performance after hyperparameter tuning.

| Metric              | Before Tuning      | After Tuning |
|---------------------|--------------------|--------------|
| Accuracy            | 0.970947           | 0.9710165    |
| F1 Score            | 0.799041           | 0.8939322    |

---

## Streamlit UI

The web application provides a seamless experience for users. Below are sample screenshots:

1. **Before Prediction**  
   ![StreamUI Before Prediction](https://github.com/user-attachments/assets/7232ea79-1db2-49a6-bb3f-63b58fdd8fcd)

2. **After Prediction**  
   ![StreamUI After Prediction](https://github.com/user-attachments/assets/1233e4e3-b5d4-4bd4-99ae-183f76c7e3ca)


---

## Deployment on AWS EC2

The project is deployed on an AWS EC2 instance to ensure reliability, scalability, and accessibility. Users can interact with the web application through a public URL, accessing the prediction tool from anywhere without local setup. 

**Key benefits of AWS EC2 deployment:**
1. Scalable infrastructure to handle user requests efficiently.
2. Secure and reliable hosting for the application.
3. Easy accessibility via the internet.

**Steps for deployment:**
1. Set up an AWS EC2 instance with the required specifications.
2. Install the necessary libraries and dependencies on the instance.
3. Deploy the Streamlit application and configure it for public access.

### AWS EC2 Screenshots

1. **Deployed Streamlit UI on AWS EC2**
   
   ![image](https://github.com/user-attachments/assets/535d3064-712a-4e80-ad5e-9dd0ed9be063)

   ![image](https://github.com/user-attachments/assets/015ce9b1-c22b-4613-9d09-007aca64bf36)

   ![image](https://github.com/user-attachments/assets/7da6f9e9-4f9f-4493-82c7-c336ac260e13)

   
---

## Installation

Follow these steps to set up the environment:

1. Clone the repository:  
   ```bash
   git clone <repository_url>
   cd diabetes_prediction_project
