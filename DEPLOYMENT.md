# 🚀 Deployment Guide

## Multi-Agent Financial Research Analyst

This document describes the setup, installation, execution, and deployment process of the Multi-Agent Financial Research Analyst developed under the TCS Xcelerate Program.

---

# 📋 System Requirements

The project requires the following software components:

* Python 3.10 or higher
* Git
* Virtual Environment (venv)
* Internet Connection

---

# 📦 Project Dependencies

The application uses the following libraries:

* yfinance
* streamlit
* requests
* beautifulsoup4
* pandas
* lxml
* google-adk

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# ⚙️ Environment Setup

### Clone Repository

```bash
git clone <repository-url>
cd TCS-Xcelerate-UseCase-B
```

### Create Virtual Environment

```bash
python3 -m venv tcs_env
```

### Activate Virtual Environment

#### macOS / Linux

```bash
source tcs_env/bin/activate
```

#### Windows

```bash
tcs_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🖥️ Running the Application

The Streamlit interface can be launched using:

```bash
streamlit run app.py
```

or

```bash
python3 -m streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

# 🤖 Multi-Agent Execution Flow

The deployed application follows the workflow below:

```text
User
  ↓
Streamlit Interface
  ↓
Thesis Writer Agent
  ↓
Coordinator Agent
  ├── Financial Data Agent
  ├── News Agent
  ├── Filings Agent
  └── Peer Comparison Agent
  ↓
Investment Thesis Report
```

---

# 🧠 Google ADK Integration

The project has been extended with Google Agent Development Kit (ADK) to demonstrate agent-based orchestration and tool integration.

### Implemented ADK Components

* Financial Tool
* News Tool
* Filings Tool
* Peer Comparison Tool
* Coordinator Tool
* Session Manager

---

# 📊 Available Features

### Financial Analysis

* Current Price
* Market Capitalization
* PE Ratio
* Sector Information
* Industry Classification

### News Analysis

* Latest Company Headlines
* Recent Market Developments

### Company Research

* Business Summary
* Employee Information
* Corporate Website

### Peer Comparison

* Dynamic Sector-Based Peer Selection
* Price Comparison
* PE Ratio Comparison

### Investment Thesis Generation

* Financial Summary
* Business Overview
* Bull Case
* Bear Case
* Risk Analysis
* Final Investment Thesis

---

# 🔍 Testing

The project includes dedicated testing modules for all ADK-integrated tools:

```text
test_financial_tool.py
test_news_tool.py
test_filings_tool.py
test_peer_tool.py
test_coordinator_tool.py
test_session_manager.py
```

These tests verify successful communication between agents and ADK tools.

---

# ☁️ Future Deployment Options

The project architecture supports deployment on:

* Streamlit Cloud
* Google Cloud Run
* Render
* Railway
* Docker-Based Infrastructure

---

# ✅ Deployment Status

| Component              | Status    |
| ---------------------- | --------- |
| Streamlit UI           | Completed |
| Financial Agent        | Completed |
| News Agent             | Completed |
| Filings Agent          | Completed |
| Peer Comparison Agent  | Completed |
| Thesis Writer Agent    | Completed |
| Dynamic Peer Selection | Completed |
| Google ADK Integration | Completed |
| Session Manager        | Completed |
| Cloud Deployment       | Planned   |

```
```
