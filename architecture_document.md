# Multi-Agent Financial Research Analyst

## Architecture Overview

The system follows a Multi-Agent Architecture where a Coordinator Agent orchestrates multiple specialist agents to generate a complete investment research report.

The architecture was further extended with a Google ADK (Agent Development Kit) layer that wraps existing agents into reusable tools and workflows.

---

# Agents and Responsibilities

## 1. Coordinator Agent

* Acts as the entry point.
* Receives the stock symbol from the user.
* Invokes all specialist agents.
* Collects outputs and returns a unified report.

---

## 2. Financial Data Agent

Retrieves financial information using Yahoo Finance.

Provides:

* Current Price
* Market Capitalization
* PE Ratio
* Sector
* Industry

---

## 3. News Agent

Retrieves recent company news.

Provides:

* Latest News Headlines
* Company Developments
* Market Updates

---

## 4. Filings Agent

Retrieves company profile information.

Provides:

* Business Summary
* Employee Count
* Company Website

---

## 5. Peer Comparison Agent

Performs sector-specific peer comparison.

Compares:

* Current Price
* Market Capitalization
* PE Ratio

Examples:

Technology Sector:

* TCS
* Infosys
* Wipro

Banking Sector:

* HDFC Bank
* ICICI Bank
* SBI

---

## 6. Thesis Writer Agent

Synthesizes outputs from all agents.

Generates:

* Financial Summary
* Latest News Summary
* Business Overview
* Bull Case
* Bear Case
* Risks
* Investment Thesis

---

# Core Workflow

```
                     User Input
                          |
                          v
                 Coordinator Agent
                          |
    ------------------------------------------------
    |                |               |             |
    v                v               v             v
```

Financial Agent    News Agent    Filings Agent   Peer Agent
|                |               |             |
------------------------------------------------
|
v
Thesis Writer Agent
|
v
Final Investment Thesis

---

# Google ADK Integration

The project includes a dedicated Google ADK layer.

The ADK layer wraps the existing agents into reusable tools.

---

## ADK Components

### 1. Financial Tool

Uses:

* Financial Agent

Provides:

* Company Financial Metrics

---

### 2. News Tool

Uses:

* News Agent

Provides:

* Recent News Headlines

---

### 3. Filings Tool

Uses:

* Filings Agent

Provides:

* Company Profile Information

---

### 4. Peer Comparison Tool

Uses:

* Peer Comparison Agent

Provides:

* Sector-Specific Peer Analysis

---

### 5. Coordinator Tool

Combines:

* Financial Tool
* News Tool
* Filings Tool
* Peer Tool

Produces:

* Unified Research Report

---

### 6. Session Manager

Stores:

* User Context
* Previous Company Information
* Session State

Provides:

* Context Retrieval
* Session Continuity

---

# ADK Workflow

```
                     User Request
                          |
                          v
                 Coordinator Tool
                          |
    ------------------------------------------------
    |                |               |             |
    v                v               v             v
```

Financial Tool     News Tool     Filings Tool    Peer Tool
|                |               |             |
------------------------------------------------
|
v
Session Manager
|
v
Final Research Report

---

# Technology Stack

* Python
* Streamlit
* Google ADK
* yfinance
* Requests
* BeautifulSoup4
* Pandas
* lxml
* Git
* GitHub

---

# Project Components

## Core Agents

* financial_agent.py
* news_agent.py
* filings_agent.py
* peer_comparison_agent.py
* coordinator_agent.py
* thesis_writer_agent.py

---

## Streamlit Interface

* app.py

---

## ADK Layer

* adk/financial_tool.py
* adk/news_tool.py
* adk/filings_tool.py
* adk/peer_tool.py
* adk/coordinator_tool.py
* adk/session_manager.py

---

## Documentation

* README.md
* architecture_document.md
* evaluation_report.md
* DEPLOYMENT.md

---

# Current Status

Completed:

✓ Multi-Agent System

✓ Streamlit Web Application

✓ Dynamic Peer Comparison

✓ Google ADK Integration

✓ Coordinator Workflow

✓ Session Management

✓ Project Documentation

✓ Evaluation Framework

---

# Future Enhancements

* AI-Powered Investment Thesis Generation
* Advanced News Filtering
* Cloud Deployment
* Persistent Database Storage
* Enhanced Agent Memory
