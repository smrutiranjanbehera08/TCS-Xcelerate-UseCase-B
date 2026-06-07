# Deployment Guide

## Local Deployment

### 1. Clone Repository

git clone <repository-url>

### 2. Enter Project Directory

cd TCS-Xcelerate-UseCase-B

### 3. Create Virtual Environment

python3 -m venv tcs_env

### 4. Activate Environment

source tcs_env/bin/activate

### 5. Install Dependencies

pip install -r requirements.txt

### 6. Run Streamlit Application

streamlit run app.py

### 7. Open Browser

http://localhost:8501

---

## Future Cloud Deployment

The application can be containerized using Docker and deployed to:

* Google Cloud Run
* Streamlit Cloud
* AWS
* Azure
