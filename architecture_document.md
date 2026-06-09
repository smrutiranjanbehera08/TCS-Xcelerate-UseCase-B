# 🏗️ Multi-Agent Financial Research Analyst

## System Architecture Document

### TCS Xcelerate Program – Use Case B

---

# 📌 Architecture Overview

The project follows a **Multi-Agent Architecture** where a central Coordinator Agent orchestrates multiple specialist agents to perform financial research and generate structured investment reports.

Each agent is responsible for a specific task and contributes information to the final research report.

The architecture is further enhanced using **Google ADK (Agent Development Kit)** to provide reusable tools, workflow orchestration, and session management.

---

# 🎯 Architecture Goals

The system is designed to:

* Automate financial research workflows
* Reduce manual analysis effort
* Provide structured investment reports
* Enable agent collaboration
* Demonstrate Google ADK integration
* Support future AI-powered enhancements

---

# 🤖 Core Agents

## 1️⃣ Coordinator Agent

### Responsibilities

* Receives stock symbol from the user
* Invokes all specialist agents
* Aggregates outputs
* Generates a unified report

### Input

```text
Stock Symbol
```

### Output

```text
Complete Company Research Report
```

---

## 2️⃣ Financial Data Agent

### Responsibilities

Retrieves financial information using Yahoo Finance.

### Data Collected

* Current Price
* Market Capitalization
* PE Ratio
* Sector
* Industry

### Example Output

```text
Company: TCS
Current Price: ₹2151
Market Cap: ₹7.7 Trillion
PE Ratio: 15.8
```

---

## 3️⃣ News Agent

### Responsibilities

Retrieves recent company-related news headlines.

### Data Collected

* Recent Headlines
* Company Developments
* Market Updates

### Example Output

```text
1. TCS launches SovereignSecure Cloud
2. TCS partners with Mistral AI
3. TCS expands AI initiatives
```

---

## 4️⃣ Filings Agent

### Responsibilities

Retrieves company profile information.

### Data Collected

* Business Summary
* Employee Count
* Website

### Example Output

```text
Employees: 584,519
Website: www.tcs.com
Business Summary: IT services and consulting
```

---

## 5️⃣ Peer Comparison Agent

### Responsibilities

Performs sector-specific peer analysis.

### Metrics Compared

* Current Price
* Market Capitalization
* PE Ratio

### Technology Sector Example

```text
TCS
Infosys
Wipro
```

### Banking Sector Example

```text
HDFC Bank
ICICI Bank
SBI
```

### Improvement Implemented

✅ Dynamic Peer Selection

The system now automatically selects peers based on the company sector instead of using fixed companies.

---

## 6️⃣ Thesis Writer Agent

### Responsibilities

Generates the final investment report.

### Sections Generated

* Financial Summary
* Latest News
* Business Overview
* Peer Comparison
* Bull Case
* Bear Case
* Risks
* Investment Thesis

---

# 🔄 Core Agent Workflow

```text
                    User Input
                         │
                         ▼
                 Coordinator Agent
                         │
     ┌───────────┬───────────┬───────────┐
     ▼           ▼           ▼           ▼
Financial     News       Filings      Peer
 Agent        Agent       Agent      Agent
     │           │           │           │
     └───────────┴───────────┴───────────┘
                         │
                         ▼
                Thesis Writer Agent
                         │
                         ▼
              Final Investment Report
```

---

# 🔗 Google ADK Integration

The project includes a dedicated Google ADK layer built on top of the existing agents.

The ADK layer converts agents into reusable tools.

---

# 🛠️ ADK Components

## Financial Tool

### Uses

* Financial Agent

### Purpose

Provides financial metrics for a company.

---

## News Tool

### Uses

* News Agent

### Purpose

Retrieves recent company news.

---

## Filings Tool

### Uses

* Filings Agent

### Purpose

Provides company profile information.

---

## Peer Tool

### Uses

* Peer Comparison Agent

### Purpose

Provides sector-specific peer analysis.

---

## Coordinator Tool

### Uses

* Financial Tool
* News Tool
* Filings Tool
* Peer Tool

### Purpose

Combines outputs into a unified report.

---

## Session Manager

### Purpose

Stores and retrieves contextual information.

### Stores

* Last Company Viewed
* Last Sector Accessed
* Session Context

### Example

```python
{
    "last_company": "TCS.NS",
    "last_sector": "Technology"
}
```

---

# 🔄 ADK Workflow

```text
                    User Request
                         │
                         ▼
                 Coordinator Tool
                         │
     ┌───────────┬───────────┬───────────┐
     ▼           ▼           ▼           ▼
Financial     News       Filings      Peer
 Tool         Tool        Tool       Tool
     │           │           │           │
     └───────────┴───────────┴───────────┘
                         │
                         ▼
                 Session Manager
                         │
                         ▼
               Final Research Report
```

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Data Sources

* Yahoo Finance

## Libraries

* yfinance
* requests
* beautifulsoup4
* pandas
* lxml

## Frameworks

* Streamlit
* Google ADK

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
TCS-Xcelerate-UseCase-B/
│
├── financial_agent.py
├── news_agent.py
├── filings_agent.py
├── peer_comparison_agent.py
├── coordinator_agent.py
├── thesis_writer_agent.py
├── app.py
│
├── adk/
│   ├── financial_tool.py
│   ├── news_tool.py
│   ├── filings_tool.py
│   ├── peer_tool.py
│   ├── coordinator_tool.py
│   └── session_manager.py
│
├── README.md
├── architecture_document.md
├── evaluation_report.md
├── DEPLOYMENT.md
└── requirements.txt
```

---

# ✅ Current Status

### Completed

* Multi-Agent Architecture
* Streamlit Application
* Financial Agent
* News Agent
* Filings Agent
* Dynamic Peer Comparison
* Thesis Writer
* Google ADK Integration
* Coordinator Tool
* Session Manager
* Evaluation Report
* Documentation

---

# 🚀 Future Enhancements

* AI-Powered Thesis Generation
* Advanced News Filtering
* Cloud Deployment
* Persistent Database Storage
* Enhanced Agent Memory
* Real-Time Market Data Integration
