# 🚀 Airbnb Price Prediction

[![Python Version](https://img.shields.io/badge/Python-3.8-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![UI Framework](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Data Pipeline](https://img.shields.io/badge/DVC-134B5F?style=for-the-badge&logo=data-version-control&logoColor=white)](https://dvc.org/)
[![Docker Capable](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## Introduction
In today's fast-paced world, the way we travel and seek accommodations has undergone a remarkable transformation, thanks to platforms like Airbnb. This dynamic marketplace has empowered property owners and travellers, offering a diverse range of lodging options. However, one enduring challenge is setting the right price for a listing. Hosts aspire to optimize their earnings while ensuring competitive pricing, while guests seek value for their money. Balancing these interests can be intricate, and that's where the motivation for Airbnb price prediction comes in.

## Motivation 
To harness the power of data science and machine learning to provide more accurate and data-driven pricing strategies for Airbnb hosts and guests. By developing predictive models that factor in myriad variables such as location, property type, and market dynamics, the objective is to help hosts maximize their income and guests find fair deals. In this exploration of Airbnb price prediction, we will delve into methodologies, data sources, and emerging trends, shedding light on how technology is enhancing the overall Airbnb experience for both hosts and travellers.


# Installation Guide

This guide provides step-by-step instructions on how to install and set up the Airbnb Price Prediction project. You can choose to install it either directly from GitHub or using a Docker container from DockerHub.

### 📋 Prerequisites
Before you begin, ensure you have the core packages installed or available in your environment[cite: 6]:

* ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) **NumPy** — High-performance vector and matrix operations[cite: 6].
* ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) **Pandas** — Data structures and structural analysis workflows[cite: 6].
* ![Seaborn](https://img.shields.io/badge/Seaborn-4C9173?style=flat&logo=python&logoColor=white) **Seaborn** — Statistical data visualization plots[cite: 6].
* ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=python&logoColor=white) **Matplotlib** — Static, animated, and interactive visualizations.
* ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) **Scikit-learn** — Data mining and machine learning modeling[cite: 6].
* ![XGBoost](https://img.shields.io/badge/XGBoost-2C8E47?style=flat&logo=python&logoColor=white) **XGBoost** — Optimized distributed gradient boosting library[cite: 6].
* ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) **Flask** — Lightweight WSGI web application framework[cite: 6].
* ![Pillow](https://img.shields.io/badge/Pillow-11557C?style=flat&logo=python&logoColor=white) **Pillow** — Friendly Python Imaging Library wrapper[cite: 6].
* ![CatBoost](https://img.shields.io/badge/CatBoost-F3D110?style=flat&logo=yandex&logoColor=black) **CatBoost** — Gradient boosting on decision trees with categorical features support[cite: 6].
* ![DVC](https://img.shields.io/badge/DVC-134B5F?style=flat&logo=data-version-control&logoColor=white) **DVC** — Data Version Control for machine learning projects[cite: 6].

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/KalyanMurapaka45/Airbnb-Price-Prediction.git
     ```

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.
  
<br><br>
### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. **Pull the Docker Image**
   - Open your terminal or command prompt.
   - Run the following command to pull the Docker image from DockerHub:
     ```
     docker pull kalyan45/airbnb-app
     ```

2. **Run the Docker Container**
   - Start the Docker container by running the following command, mapping any necessary ports:
     ```
     docker run -p 5000:5000 kalyan45/airbnb-app
     ```

3. **Access the Project**
   - Open a web browser or the appropriate client to access the project.

## Troubleshooting

- If you encounter any issues during the installation process, Contact me at ```kalyanmurapaka274@gmail.com```


# Contributing

We welcome contributions from the community! If you have any ideas or suggestions for improving the project, please feel free to create an issue or submit a pull request.

# Acknowledgements

This project was inspired by the Kaggle dataset on AirBNB Price Prediction and the corresponding competition. We also acknowledge the open-source Python libraries used in this project and their contributors.
