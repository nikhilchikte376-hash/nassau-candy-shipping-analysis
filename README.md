# ðŸšš Factory-to-Customer Shipping Route Efficiency Analysis

## Nassau Candy Distributor

### ðŸ“Œ Project Overview

This project analyzes factory-to-customer shipping operations for Nassau Candy Distributor to evaluate shipment activity, regional performance, shipping modes, sales trends, route performance, and calculated shipping lead times.

The project follows an end-to-end data analytics workflow covering data preparation, exploratory analysis, KPI development, interactive visualization, business insight generation, and cloud deployment.

An interactive Streamlit dashboard allows users to dynamically explore the data by region, shipping mode, and date range.

---

## ðŸŽ¯ Project Objectives

The main objectives of this project are to:

- Analyze factory-to-customer shipping activity.
- Compare shipment performance across regions.
- Evaluate different shipping modes.
- Identify high-volume shipping routes.
- Analyze sales and shipment trends over time.
- Calculate logistics and business KPIs.
- Rank regions and routes based on shipment activity.
- Identify patterns and potential operational areas for investigation.
- Develop an interactive dashboard for decision support.

---

## ðŸ“Š Dataset

The final dataset contains **10,194 shipment records** with order, customer, product, sales, profitability, and shipping information.

### Major Fields

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

The dashboard covers records from approximately **January 2024 through December 2025**.

---

## ðŸ”§ Tools & Technologies

- **Python** â€” Core analysis and application development
- **Pandas** â€” Data cleaning, transformation, aggregation, and analysis
- **NumPy** â€” Numerical operations
- **Matplotlib** â€” Data visualization
- **Jupyter Notebook** â€” Exploratory data analysis
- **Streamlit** â€” Interactive dashboard development
- **Git & GitHub** â€” Version control and project hosting
- **Streamlit Community Cloud** â€” Live dashboard deployment

---

## ðŸ” Methodology

### 1. Data Cleaning & Validation

The dataset was reviewed for:

- Data structure and column types
- Missing values
- Duplicate records
- Date-field consistency
- Shipping lead-time calculations
- Potential source-data quality issues

### 2. Feature Engineering

Shipping lead time was calculated using:

**Shipping Lead Time = Ship Date âˆ’ Order Date**

Additional route-level features were created to support factory-to-customer analysis.

### 3. KPI Development

The dashboard calculates major performance indicators including:

- Total Shipments
- Total Sales
- Total Units
- Total Profit
- Average Shipping Lead Time
- Filtered Record Percentage

KPI values dynamically update according to the selected dashboard filters.

### 4. Regional Analysis

Regional performance is evaluated using:

- Shipment volume
- Shipment share (%)
- Sales
- Units
- Average lead time
- Regional ranking

### 5. Shipping Mode Analysis

Performance is compared across:

- Standard Class
- Second Class
- First Class
- Same Day

The dashboard highlights the leading shipping mode and allows users to evaluate mode performance dynamically.

### 6. Route Analysis

Factory-to-customer routes are ranked using shipment volume.

The dashboard displays the **Top 10 Routes**, including shipment counts and their percentage contribution to the currently filtered data.

### 7. Trend Analysis

Monthly trends are included for:

- Sales
- Shipment volume

Peak periods are visually highlighted to improve interpretation.

---

## ðŸ“ˆ Key KPIs

| KPI | Overall Result |
|---|---:|
| Total Shipments | 10,194 |
| Total Sales | $141,783.63 |
| Total Profit | $93,442.80 |
| Total Units | 38,654 |
| Average Calculated Lead Time | 1,320.84 days |

---

## ðŸŒŽ Regional Performance

| Rank | Region | Shipments | Shipment Share |
|---:|---|---:|---:|
| 1 | Pacific | 3,253 | 31.91% |
| 2 | Atlantic | 2,986 | 29.29% |
| 3 | Interior | 2,335 | 22.91% |
| 4 | Gulf | 1,620 | 15.89% |

The **Pacific region ranks first**, contributing approximately **31.9% of total shipments**.

---

## ðŸšš Shipping Mode Performance

| Shipping Mode | Shipments |
|---|---:|
| Standard Class | 6,120 |
| Second Class | 1,979 |
| First Class | 1,548 |
| Same Day | 547 |

**Standard Class** is the dominant shipping method, accounting for the largest share of shipment activity.

---

## ðŸ›£ï¸ Top Factory-to-Customer Routes

The route analysis identifies the highest-volume shipping routes.

The leading routes include:

1. Chocolate â†’ California â€” **1,948 shipments**
2. Chocolate â†’ New York â€” **1,081 shipments**
3. Chocolate â†’ Texas â€” **957 shipments**
4. Chocolate â†’ Pennsylvania â€” **558 shipments**
5. Chocolate â†’ Washington â€” **490 shipments**

The **Chocolate â†’ California** route is the largest route in the dataset, representing approximately **19.1% of total shipments**.

---

## ðŸ–¥ï¸ Interactive Streamlit Dashboard

The project includes a fully interactive Streamlit dashboard designed to support exploratory logistics analysis.

### Dashboard Features

- ðŸ“Š Dynamic KPI cards
- ðŸ”Ž Region filtering
- ðŸšš Shipping mode filtering
- ðŸ“… Date-range filtering
- ðŸ”„ Reset Filters button
- ðŸ“‹ Filtered record count and percentage
- ðŸ“ˆ Monthly sales trend
- ðŸ“¦ Monthly shipment trend
- ðŸŒŽ Regional performance ranking
- ðŸ“Š Regional shipment-share analysis
- ðŸšš Shipping-mode comparison
- ðŸ›£ï¸ Top 10 factory-to-customer routes
- ðŸ“Š Route contribution percentages
- ðŸ’¡ Dynamic business insights
- âš ï¸ Data-quality warning
- ðŸ“‹ Dataset information

All major KPIs, charts, tables, routes, and insights respond dynamically to the selected filters.

### ðŸ”´ Live Dashboard

**[Open Live Streamlit Dashboard](https://sjtvna4mhw2rbvmlnz9sdj.streamlit.app/)**

---

## ðŸ’¡ Key Business Insights

The completed analysis shows that:

- **Pacific** is the highest-volume region with **3,253 shipments**, representing approximately **31.9%** of total shipment activity.
- **Atlantic** ranks second with **2,986 shipments**.
- Pacific generates approximately **$46,301.53 in sales**, the highest among the four regions.
- **Standard Class** is the most frequently used shipping mode with **6,120 shipments**.
- **Same Day** has the lowest shipment volume with **547 shipments**.
- **Chocolate â†’ California** is the highest-volume factory-to-customer route with **1,948 shipments**.
- Monthly trend analysis makes it possible to identify changes and peak periods in sales and shipment activity.
- Regional rankings and shipment-share percentages provide clearer comparisons between geographic markets.

---

## âš ï¸ Data Quality & Interpretation Note

The calculated shipping lead times are unusually high compared with typical operational shipping timelines.

The overall calculated average lead time is approximately **1,320.84 days**.

This suggests that the Order Date and Ship Date fields may contain historical, simulated, transformed, or source-data quality limitations.

Therefore, shipping lead-time values should be validated against the original business records before being used for real-world operational decision-making.

The project primarily uses these values for **analytical comparison and pattern identification rather than treating them as confirmed operational benchmarks**.

---

## ðŸ’¼ Business Value

This analysis can help logistics and supply-chain teams:

- Identify high-volume shipping routes.
- Compare regional shipment activity.
- Understand shipping-mode utilization.
- Track sales and shipment trends.
- Rank regions by operational activity.
- Identify routes requiring deeper investigation.
- Support data-driven logistics planning.
- Establish a foundation for future route optimization.

---

## ðŸš€ Future Scope

Potential future improvements include:

- Geographic route mapping
- Validated delivery-time analysis
- Shipping-cost analysis
- Profitability analysis by route
- Predictive shipping-delay modeling
- Route optimization using geographic distance
- Automated KPI monitoring
- Integration with validated live logistics data
- Machine-learning-based delivery-time prediction

---

## ðŸ“ Project Structure

```text
nassau-candy-shipping-analysis/
â”‚
â”œâ”€â”€ app.py
â”œâ”€â”€ analysis.ipynb
â”œâ”€â”€ nassau_orders_final.csv
â”œâ”€â”€ Nassau_Candy_Shipping_Route_Efficiency_Report_Final.pdf
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ README.md
â””â”€â”€ .gitignore
```

---

## ðŸ“Œ Dashboard Improvement

The dashboard was enhanced following evaluator feedback to improve both usability and visual storytelling.

Major improvements include:

- Added KPI comparisons and contextual percentages.
- Added regional rankings and shipment-share percentages.
- Added monthly sales and shipment trend charts.
- Added filtered record count and percentage.
- Added a Reset Filters option.
- Improved consistency between filters, KPIs, charts, and tables.
- Improved chart styling and visual hierarchy.
- Added route contribution percentages.
- Improved business insight presentation.

These improvements make the dashboard more interactive, interpretable, and suitable for portfolio presentation.

---

## ðŸ‘¤ Author

**Nikhil Chikte**  
B.Tech â€” Computer Science & Engineering  
Aspiring Data Analyst

### Skills Demonstrated

`Python` â€¢ `Pandas` â€¢ `Data Analysis` â€¢ `Data Visualization` â€¢ `Streamlit` â€¢ `Git` â€¢ `GitHub` â€¢ `Business Analytics`

---

â­ If you find this project useful, consider giving the repository a star.

