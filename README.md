# AI Data Analytics Copilot

AI Data Analytics Copilot is an intelligent data analysis application built with Streamlit that helps users analyze CSV and Excel datasets with minimal effort. It automates data profiling, exploratory data analysis, dashboard creation, AI-powered insights, DAX generation, and natural language interaction with datasets.

The application is designed for analysts, students, and business users who want quick insights without writing SQL or Python code.

---

## Features

- Upload CSV and Excel datasets
- Automatic data cleaning
- Exploratory Data Analysis (EDA)
- Dataset profiling
- Dynamic dashboard generation
- AI-powered DAX measure generation
- AI business insights
- Chat with your dataset
- Export complete analysis as a PDF report

---

## Screenshots

### Home Page

![Home Page](YOUR_IMAGE_LINK_HERE)

---

### Dataset Upload

![Upload Dataset](YOUR_IMAGE_LINK_HERE)

---

### Data Cleaning

![Data Cleaning](YOUR_IMAGE_LINK_HERE)

---

### Dataset Profiling

![Dataset Profiling](YOUR_IMAGE_LINK_HERE)

---

### Smart Dashboard

![Dashboard](YOUR_IMAGE_LINK_HERE)

---

### AI DAX Generator

![DAX Generator](YOUR_IMAGE_LINK_HERE)

---

### AI Business Insights

![Business Insights](YOUR_IMAGE_LINK_HERE)

---

### AI Chatbot

![Chatbot](YOUR_IMAGE_LINK_HERE)

---

### PDF Report

![PDF Report](YOUR_IMAGE_LINK_HERE)

---

## Project Structure

```
AI_Data_Analytics_Copilot/
│
├── agents/
│   ├── chat_agent.py
│   ├── cleaning_agent.py
│   ├── dashboard_agent.py
│   ├── dax_agent.py
│   ├── eda_agent.py
│   ├── insight_agent.py
│   ├── profiler_agent.py
│   ├── query_agent.py
│   └── intent_agent.py
│
├── components/
│   ├── chat_ui.py
│   ├── dashboard.py
│   ├── dashboard_report.py
│   ├── dax_report.py
│   ├── eda_report.py
│   ├── export_report.py
│   ├── insight_report.py
│   ├── profiler_report.py
│   └── uploader.py
│
├── services/
│   ├── chart_service.py
│   ├── llm_service.py
│   └── pdf_service.py
│
├── assets/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## Technology Stack

### Frontend

- Streamlit

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Plotly

### AI

- Google Gemini / Groq (OpenAI Compatible)

### Report Generation

- ReportLab

---

## Workflow

```
Upload Dataset
        │
        ▼
Data Cleaning
        │
        ▼
EDA
        │
        ▼
Dataset Profiling
        │
        ▼
Dashboard Generation
        │
        ├───────────────┐
        ▼               ▼
 AI Insights      DAX Generator
        │               │
        └───────┬───────┘
                ▼
          AI Chatbot
                │
                ▼
         Export PDF Report
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Data_Analytics_Copilot.git
```

Move into the project directory

```bash
cd AI_Data_Analytics_Copilot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Environment Variables

Create a `.env` file in the project root.

Example

```env
GROQ_API_KEY=YOUR_API_KEY
```

or

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Supported Dataset Formats

- CSV
- XLSX

---

## Modules

### Data Cleaning

- Removes duplicate rows
- Handles missing values
- Converts appropriate data types

### Exploratory Data Analysis

- Summary statistics
- Missing values
- Duplicate records
- Data distribution

### Dataset Profiling

- Numeric columns
- Categorical columns
- Date columns
- Dataset information

### Dashboard

Creates visualizations dynamically depending on the uploaded dataset.

Possible charts include:

- Line Chart
- Bar Chart
- Pie Chart
- Histogram
- Box Plot
- Scatter Plot
- Correlation Heatmap

### AI DAX Generator

Generates Power BI DAX measures based on dataset schema.

### AI Business Insights

Generates business-oriented observations and recommendations.

### AI Chatbot

Allows users to ask questions in natural language about the uploaded dataset.

### PDF Export

Exports the analysis into a downloadable PDF report.

---

## Future Improvements

- Database connectivity
- Power BI integration
- Multi-file analysis
- User authentication
- Role-based access
- Cloud deployment
- Scheduled reports
- Advanced AI analytics

---

## Author

Kailash J Choudhary



---

## License

This project is intended for educational and portfolio purposes.
