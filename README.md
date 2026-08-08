# 🚚 Factory-to-Customer Shipping Route Efficiency Analysis

## Nassau Candy Distributor

### 📌 Project Overview

This project analyzes factory-to-customer shipping routes for Nassau Candy Distributor to evaluate shipping efficiency, regional performance, shipping modes, and operational patterns.

The analysis uses order and shipment data to identify route-level trends, regional differences, high-volume shipping routes, and potential areas for further investigation.

The project follows an end-to-end data analytics workflow, from data preparation and exploratory analysis to interactive dashboard development and cloud deployment.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze shipping lead times between order and shipment dates.
- Evaluate factory-to-customer route performance.
- Compare shipping performance across regions.
- Analyze different shipping modes.
- Identify high-volume and potentially inefficient routes.
- Calculate key logistics and business KPIs.
- Identify geographic areas that may require further investigation.
- Provide actionable insights based on the available data.
- Develop and deploy an interactive analytics dashboard.

---

## 📊 Dataset

The dataset contains order, customer, product, sales, and shipping information.

### Major fields include:

- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- City
- State/Province
- Region
- Product ID
- Product Name
- Sales
- Units
- Gross Profit
- Cost
- Factory Region
- Factory State
- Shipping Lead Time
- Factory-to-Customer Route

---

## 🔧 Tools & Technologies

- **Python** — Core programming and analysis
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Jupyter Notebook** — Exploratory analysis
- **CSV** — Dataset format
- **Streamlit** — Interactive dashboard development
- **GitHub** — Version control and project hosting
- **Streamlit Community Cloud** — Dashboard deployment

---

## 🔍 Methodology

The project follows a structured analytical workflow.

### 1. Data Cleaning & Validation

- Checked dataset structure and data types.
- Identified missing values.
- Checked duplicate records.
- Validated date fields.
- Checked shipping lead-time calculations.
- Reviewed potential data-quality issues.

### 2. Feature Engineering

Shipping lead time was calculated using:

**Shipping Lead Time = Ship Date − Order Date**

Additional factory-to-customer route features were created to support geographic and route-level analysis.

### 3. Route Definition & Aggregation

Orders were grouped by factory and customer locations to evaluate:

- Shipment volume
- Average shipping lead time
- Sales
- Units shipped
- Regional performance
- Route performance

### 4. Efficiency Analysis

Routes, regions, and shipping modes were compared using key performance indicators to identify variations in shipment activity and calculated lead times.

### 5. Geographic Analysis

Regional and state-level analysis was performed to identify:

- High-volume shipment areas
- Important factory-to-customer routes
- Potential geographic bottlenecks
- Unusual shipping patterns

### 6. Shipping Mode Analysis

Shipping performance was evaluated across:

- Same Day
- First Class
- Second Class
- Standard Class

---

## 📈 Key KPIs

The completed dashboard provides the following overall KPIs:

| KPI | Result |
|---|---:|
| Total Shipments | 10,194 |
| Total Sales | $141,783.63 |
| Total Units | 38,654 |
| Average Calculated Lead Time | 1,320.8 days |

### Regional Shipment Distribution

| Region | Shipments |
|---|---:|
| Pacific | 3,253 |
| Atlantic | 2,986 |
| Interior | 2,335 |
| Gulf | 1,620 |

### Shipping Mode Distribution

| Shipping Mode | Shipments |
|---|---:|
| Standard Class | 6,120 |
| Second Class | 1,979 |
| First Class | 1,548 |
| Same Day | 547 |

---

## 📊 Analysis Areas

The completed analysis includes:

- Shipping lead-time analysis
- Regional shipment analysis
- Factory-to-customer route analysis
- State-level analysis
- Shipping-mode performance analysis
- Top shipment route analysis
- Sales and unit distribution
- Geographic bottleneck identification
- KPI analysis

---

## 🖥️ Interactive Streamlit Dashboard

The project includes an interactive Streamlit dashboard that allows users to explore the analysis using filters and visualizations.

### Dashboard Features

- 📊 KPI cards
- 🔎 Region filters
- 🚚 Shipping mode filters
- 🌎 Regional shipment analysis
- 📦 Shipping mode analysis
- 🛣️ Factory-to-customer route analysis
- 📈 Shipment visualizations
- 📋 Route summary tables
- ⚠️ Data-quality warning
- 📊 Dataset information

### 🔴 Live Dashboard

**[Open Live Streamlit Dashboard](https://sjtvna4mhw2rbvmlnz9sdj.streamlit.app/)**

---

## ⚠️ Data Quality & Interpretation Note

The calculated shipping lead times in the dataset are unusually high compared with typical operational shipping timelines.

The overall calculated average lead time is approximately **1,320.8 days**.

This may indicate historical, simulated, or source-data quality limitations. Therefore, the calculated lead-time values should be validated against the original business records before being used for real-world operational decision-making.

The analysis therefore focuses primarily on identifying **patterns, comparisons, and potential areas for investigation**, rather than treating the calculated lead-time values as confirmed operational benchmarks.

---

## 💡 Key Business Insights

Based on the completed analysis:

- **Pacific** has the highest shipment volume with **3,253 shipments**.
- **Atlantic** has the second-highest shipment volume with **2,986 shipments**.
- Pacific also records the highest total sales at approximately **$46,301.53**.
- **Standard Class** is the most frequently used shipping mode with **6,120 shipments**.
- **Same Day** has the lowest shipment volume with **547 shipments**.
- The calculated lead times are consistently very high across regions, highlighting the need for source-date validation.
- High-volume factory-to-customer routes can be prioritized for deeper operational investigation.

---

## 💼 Business Value

This analysis can help logistics and supply-chain teams:

- Identify high-volume shipping routes.
- Compare regional shipping activity.
- Understand shipping-mode distribution.
- Detect potentially inefficient or unusual routes.
- Prioritize routes for further investigation.
- Support data-driven logistics planning.
- Build a foundation for future route optimization.

---

## 🚀 Future Scope

Future improvements could include:

- Real-time logistics monitoring.
- Predictive shipping-delay analysis.
- Route optimization using geographic distance.
- Cost-based route optimization.
- Machine-learning-based delivery-time prediction.
- Geographic mapping.
- Automated KPI monitoring.
- Integration with validated live logistics data.
- Shipping cost and profitability analysis.

---

## 📁 Project Structure

```text
nassau-candy-shipping-analysis/
│
├── app.py
├── nassau_orders_final.csv
├── requirements.txt
├── README.md
├── analysis.ipynb
├── .gitignore
└── Project Report
