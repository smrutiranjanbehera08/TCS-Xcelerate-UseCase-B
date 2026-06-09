# TCS-Xcelerate-UseCase-B
## Multi-Agent Financial Research Analyst  using Google ADK | TCS Xcelerate Program


This project implements a Multi-Agent Financial Research Analyst system developed as part of the TCS Xcelerate Program (Use Case B).

The system automates investment research by coordinating multiple specialized agents that collect financial information, retrieve company news, analyze business filings, compare industry peers, and generate structured investment thesis reports.

The project also includes a Google ADK integration layer, demonstrating how agent-based tools can be orchestrated through reusable workflows.

Project Objectives

The objective of this project is to automate the equity research workflow using a multi-agent architecture.

The system gathers company information from multiple sources and generates a structured investment research report for investors and analysts.

Features
Financial Data Analysis
Latest News Retrieval
Company Filings Summary
Dynamic Peer Comparison Analysis
Investment Thesis Generation
Streamlit Web Interface
Automated Report Generation
Google ADK Integration
Session Management
Sector-Specific Peer Selection

## Project Architecture

![Architecture Diagram](images/architecture.png)

Agents Implemented
Coordinator Agent

Acts as the central controller and coordinates all specialist agents.

Financial Data Agent

Retrieves financial information such as:

Current Price
Market Cap
PE Ratio
Sector
Industry
News Agent

Retrieves recent company-related news headlines.

Filings Agent

Provides company profile and business overview information.

Peer Comparison Agent

Performs sector-specific peer comparison.

Examples:

Technology Sector:

TCS
Infosys
Wipro

Banking Sector:

HDFC Bank
ICICI Bank
SBI
Thesis Writer Agent

Generates a structured investment thesis containing:

Financial Summary
Latest News
Business Overview
Bull Case
Bear Case
Risks
Investment Thesis
Google ADK Integration

The project includes a dedicated ADK layer built on top of the existing agents.

ADK Components
Financial Tool

Provides company financial metrics.

News Tool

Retrieves recent company news.

Filings Tool

Retrieves company profile information.

Peer Comparison Tool

Performs sector-specific peer analysis.

Coordinator Tool

Combines outputs from all ADK tools into a single report.

Session Manager

Stores and retrieves contextual information during interactions.

ADK Workflow

User Request
↓
Coordinator Tool
↓
Financial Tool
↓
News Tool
↓
Filings Tool
↓
Peer Comparison Tool
↓
Session Manager
↓
Final Research Report

Technologies Used
Python
Streamlit
Google ADK
Yahoo Finance (yfinance)
Requests
BeautifulSoup4
Pandas
lxml
Git
GitHub
Project Files
Core Agents
financial_agent.py
news_agent.py
filings_agent.py
peer_comparison_agent.py
coordinator_agent.py
thesis_writer_agent.py
Streamlit UI
app.py
ADK Layer
adk/financial_tool.py
adk/news_tool.py
adk/filings_tool.py
adk/peer_tool.py
adk/coordinator_tool.py
adk/session_manager.py
Documentation
README.md
architecture_document.md
evaluation_report.md
DEPLOYMENT.md
Installation

Clone the repository:

git clone

Move into the project folder:

cd TCS-Xcelerate-UseCase-B

Create virtual environment:

python3 -m venv tcs_env

Activate environment:

source tcs_env/bin/activate

Install dependencies:

pip install -r requirements.txt

Running the Application

Run the Streamlit interface:

streamlit run app.py

or

python3 -m streamlit run app.py

Evaluation

The system was evaluated using 10 publicly listed Indian companies:

TCS
Infosys
Wipro
Reliance Industries
HDFC Bank
ICICI Bank
SBI
Larsen & Toubro
ITC
Bharti Airtel

Results are documented in evaluation_report.md.

Current Project Status

Completed:

Multi-Agent Architecture
Streamlit Web Application
Dynamic Peer Comparison
Google ADK Integration
Coordinator Workflow
Session Management
Evaluation Report
Project Documentation
Future Improvements
AI-Powered Investment Thesis Generation
Advanced News Filtering
Cloud Deployment
Persistent Database Storage
Enhanced Agent Memory
Author

Smrutiranjan Behera

TCS Xcelerate Program – Use Case B