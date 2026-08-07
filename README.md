# Factory-to-Customer Shipping Route Efficiency Analysis

## Nassau Candy Distributor

### 📌 Project Overview

This project analyzes factory-to-customer shipping routes for Nassau Candy Distributor to evaluate shipping efficiency, regional performance, shipment modes, and operational patterns.

The analysis uses historical order and shipment data to identify route-level trends, regional bottlenecks, and shipping performance indicators that can support data-driven logistics decisions.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze shipping lead times between order and shipment dates.
- Evaluate factory-to-customer route efficiency.
- Compare shipping performance across regions.
- Analyze different shipping modes.
- Identify high-volume and potentially inefficient routes.
- Calculate key logistics and business KPIs.
- Identify geographic areas that may require further investigation.
- Provide actionable insights based on the available data.

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

- **Python**
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Jupyter Notebook** — Analysis environment
- **Excel/CSV** — Data source and validation
- **Streamlit** — Interactive dashboard development

---

## 🔍 Methodology

The project follows a structured analytical workflow:

### 1. Data Cleaning & Validation

- Checked dataset structure and data types.
- Identified missing values.
- Checked duplicate records.
- Validated date fields.
- Checked for invalid or negative shipping lead times.

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

### 4. Efficiency Benchmarking

Routes and regions were compared using key performance indicators to identify variations in shipping performance.

### 5. Geographic Bottleneck Analysis

State and regional-level analysis was performed to identify areas with high shipment volumes or unusual shipping lead times.

### 6. Ship Mode Analysis

Shipping performance was evaluated across:

- Same Day
- First Class
- Second Class
- Standard Class

---

## 📈 Key KPIs

The project evaluates the following logistics and business KPIs:

| KPI | Description |
|---|---|
| Total Shipments | Number of shipment records |
| Average Lead Time | Average time between order and shipment |
| Total Sales | Total sales value |
| Total Units | Total units shipped |
| Regional Shipments | Shipment volume by region |
| Route Performance | Shipment and lead-time performance by route |
| Ship Mode Performance | Performance across shipping modes |

---

## 📊 Analysis Areas

The completed analysis includes:

- Shipping lead-time analysis
- Regional shipment analysis
- Factory-to-customer route analysis
- State-level analysis
- Ship-mode performance analysis
- Top shipment route analysis
- Sales and unit distribution
- Geographic bottleneck identification

---

## ⚠️ Data Quality & Interpretation Note

The calculated shipping lead times in the dataset are unusually high compared with typical operational shipping timelines.

This may indicate historical, simulated, or source-data quality limitations. Therefore, the calculated lead-time values should be validated against the original business records before being used for real-world operational decision-making.

The analysis therefore focuses primarily on identifying **patterns, comparisons, and potential areas for investigation** rather than treating the lead-time values as confirmed operational benchmarks.

---

## 💡 Business Value

This analysis can help logistics and supply-chain teams:

- Identify high-volume shipping routes.
- Compare regional shipping performance.
- Detect potentially inefficient routes.
- Understand shipment-mode distribution.
- Prioritize routes for further investigation.
- Support data-driven logistics planning.

---

## 🚀 Future Scope

Future improvements could include:

- Interactive Streamlit dashboard.
- Real-time logistics monitoring.
- Predictive shipping-delay analysis.
- Route optimization using geographic distance.
- Cost-based route optimization.
- Machine-learning-based delivery-time prediction.
- Integration with live logistics data.

---

## 📁 Project Structure

```text
nassau-candy-shipping-analysis/
│
├── analysis.ipynb
├── requirements.txt
├── README.md
└── .gitignore


## 👨‍💻 Author

**Nikhil Chikte**

B.Tech Computer Science & Engineering

Interested in Data Analytics, Business Intelligence, Python, SQL, and Data Visualization.

---

## ⭐ Project Status

**Analysis Completed ✅**

**GitHub Repository Setup ✅**

**Interactive Dashboard — In Progress 🚧**

**Deployment — Upcoming 🚧**


