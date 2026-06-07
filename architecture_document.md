# Multi-Agent Financial Research Analyst

## Architecture Overview

The system follows a multi-agent architecture where a Coordinator Agent orchestrates multiple specialist agents to generate an investment research report.

## Agents and Responsibilities

### 1. Coordinator Agent

* Acts as the entry point.
* Receives the stock symbol from the user.
* Invokes all specialist agents.
* Collects outputs and returns a unified report.

### 2. Financial Data Agent

* Retrieves financial information using Yahoo Finance.
* Provides:

  * Current Price
  * Market Capitalization
  * PE Ratio
  * Sector
  * Industry

### 3. News Agent

* Retrieves recent company news.
* Extracts important headlines.
* Provides recent developments affecting the company.

### 4. Filings Agent

* Retrieves company profile information.
* Extracts business summary.
* Provides employee count and company website.

### 5. Peer Comparison Agent

* Retrieves comparable company metrics.
* Compares:

  * Current Price
  * Market Capitalization
  * PE Ratio (Price-to-Earnings Ratio)

### 6. Thesis Writer Agent

* Synthesizes outputs from all agents.
* Generates:

  * Financial Summary
  * Business Overview
  * Bull Case
  * Bear Case
  * Risks
  * Investment Thesis

## Workflow

                          User Input
                              ↓
                       Coordinator Agent
                              ↓
                        Financial Agent
                              ↓
                          News Agent
                              ↓
                        Filings Agent
                              ↓
                    Peer Comparison Agent
                              ↓
                     Thesis Writer Agent
                              ↓
                   Final Investment Thesis

## Technology Stack

* Python
* yfinance
* Streamlit
* GitHub

## Future Enhancements

* Google Agent Development Kit (ADK)
* NewsAPI Integration
* Google Cloud Run Deployment
* Evaluation Framework
