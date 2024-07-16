# Phishing URL Detection Project

## Description
This project aims to detect phishing URLs using machine learning techniques. By analyzing various features of the URLs, the model can classify whether a URL is legitimate or potentially harmful.

<div align="center">
    <img src="image.jpg" alt="Project Image" width="600">
</div>

## Table of Contents
- [Description](#description)
- [Feature Engineering](#feature-engineering)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Training](#model-training)
- [Results](#results)
- [Voting Classifier](#voting-classifier)
- [Frontend Development](#frontend-development)
- [Contact](#contact)

## Feature Engineering
During the feature engineering phase, the following 12 features were extracted from the URLs:
- **domain**: The domain of the URL.
- **domain_length**: Length of the domain.
- **tld**: Top-level domain.
- **tld_length**: Length of the top-level domain.
- **is_HTTP**: Indicates if the URL uses HTTP.
- **is_IP**: Indicates if the URL is an IP address.
- **no_of_Subdomains**: Number of subdomains present.
- **url_depth**: Depth of the URL structure.
- **redirection**: Indicates if the URL has redirection.
- **contain_@**: Indicates if the URL contains "@" symbol.
- **contain_hyphen**: Indicates if the URL contains a hyphen.
- **contains_suspicious_keywords**: Presence of suspicious keywords in the URL.

## Exploratory Data Analysis (EDA)
EDA was performed on the extracted features to derive useful insights and understand the underlying patterns within the dataset. Visualizations and statistical analyses were conducted to assess feature significance and relationships.

## Model Training
Various machine learning models were trained to classify phishing URLs, including:
- Logistic Regression
- Support Vector Classifier (SVC)
- Decision Tree
- Random Forest
- LightGBM

## Results
The performance of the models was evaluated, and the results are as follows:
- **SVC**: Achieved the highest precision of **0.9718**.
- **Decision Tree**: Achieved the highest accuracy of **0.9774**.

## Voting Classifier
To further improve the classification performance, a voting classifier was implemented, combining the predictions from the SVC and Decision Tree models.

## Frontend Development
The frontend of the application was developed using **Streamlit**, allowing users to interactively input URLs and receive predictions on their legitimacy.

## Contact
Prateek Singh - prateek12301singh@gmail.com
