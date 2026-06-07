# TCS-Xcelerate-UseCase-B
## Multi-Agent Financial Research Analyst  using Google ADK | TCS Xcelerate Program


This project implements a Multi-Agent Financial Research Analyst system developed as part of the TCS Xcelerate Program. The system automates investment research by coordinating multiple specialized agents that collect financial information, analyze company data, retrieve recent news, compare industry peers, and generate an investment thesis.

---

## Project Objectives

The objective of this project is to automate the equity research workflow using a multi-agent architecture. The system gathers company information from multiple sources and generates a structured investment research report.

---

## Features

* Financial Data Analysis
* Latest News Retrieval
* Company Filings Summary
* Peer Comparison Analysis
* Investment Thesis Generation
* Streamlit Web Interface
* Automated Report Generation

---

## Project Architecture

User
↓
Streamlit UI (app.py)
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

---

## Agents Implemented

### Coordinator Agent

Acts as the central controller and coordinates all specialist agents.

### Financial Data Agent

Retrieves financial information such as:

* Current Price
* Market Cap
* PE Ratio
* Sector
* Industry

### News Agent

Retrieves recent company-related news headlines.

### Filings Agent

Provides company profile and business overview information.

### Peer Comparison Agent

Compares company metrics with industry peers.

### Thesis Writer Agent

Generates a structured investment thesis containing:

* Financial Summary
* Business Overview
* Bull Case
* Bear Case
* Risks
* Investment Thesis

---

## Technologies Used

* Python
* Streamlit
* Yahoo Finance (yfinance)
* Git & GitHub

---

## Project Files

* financial_agent.py
* news_agent.py
* filings_agent.py
* peer_comparison_agent.py
* coordinator_agent.py
* thesis_writer_agent.py
* app.py
* architecture_document.md
* evaluation_report.md

---

## Installation

Clone the repository:

git clone <repository-url>

Move into the project folder:

cd TCS-Xcelerate-UseCase-B

Create virtual environment:

python3 -m venv tcs_env

Activate environment:

source tcs_env/bin/activate

Install dependencies:

pip install yfinance streamlit

---

## Running the Application

Run the Streamlit interface:

streamlit run app.py

or

python3 -m streamlit run app.py

---

## Evaluation

The system was evaluated using 10 publicly listed Indian companies:

* TCS
* Infosys
* Wipro
* Reliance
* HDFC Bank
* ICICI Bank
* SBI
* Larsen & Toubro
* ITC
* Bharti Airtel

Results are documented in evaluation_report.md.

---

## Future Improvements

* Google ADK Integration
* Dynamic Industry Peer Selection
* Advanced News Summarization
* Cloud Deployment using Google Cloud Run
* Persistent Agent Memory

---

## Author

Smrutiranjan Behera

TCS Xcelerate Program – Use Case B
