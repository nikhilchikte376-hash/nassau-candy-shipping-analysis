import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Nassau Candy Shipping Analysis",
    page_icon="🚚",
    layout="wide"
)

# ============================================================
# TITLE
# ============================================================

st.title("🚚 Nassau Candy Shipping Route Efficiency Analysis")

st.markdown("### Factory-to-Customer Shipping Route Analysis")

st.markdown("---")

# ============================================================
# LOAD FINAL DATASET
# ============================================================

@st.cache_data
def load_data():

    # Folder containing app.py
    app_folder = Path(__file__).resolve().parent

    # Final processed CSV
    csv_path = app_folder / "nassau_orders_final.csv"

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Could not find: {csv_path}"
        )

    return pd.read_csv(csv_path)


try:
    df = load_data()

except FileNotFoundError as e:

    st.error("❌ Final CSV file not found.")

    st.info(
        "Make sure 'nassau_orders_final.csv' is in the "
        "same folder as app.py."
    )

    st.stop()

except Exception as e:

    st.error(f"❌ Error loading dataset: {e}")

    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

# Convert dates

if "Order Date" in df.columns:

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )


if "Ship Date" in df.columns:

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        errors="coerce"
    )


# Calculate Shipping Lead Time if needed

if "Shipping_Lead_Time" not in df.columns:

    if (
        "Order Date" in df.columns
        and "Ship Date" in df.columns
    ):

        df["Shipping_Lead_Time"] = (
            df["Ship Date"] - df["Order Date"]
        ).dt.days


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Filters")

filtered_df = df.copy()


# -------------------------
# Region Filter
# -------------------------

if "Region" in df.columns:

    regions = sorted(
        df["Region"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_regions = st.sidebar.multiselect(
        "Select Region",
        options=regions,
        default=regions
    )

    filtered_df = filtered_df[
        filtered_df["Region"].isin(selected_regions)
    ]


# -------------------------
# Ship Mode Filter
# -------------------------

if "Ship Mode" in df.columns:

    ship_modes = sorted(
        df["Ship Mode"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_ship_modes = st.sidebar.multiselect(
        "Select Ship Mode",
        options=ship_modes,
        default=ship_modes
    )

    filtered_df = filtered_df[
        filtered_df["Ship Mode"].isin(
            selected_ship_modes
        )
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_shipments = len(filtered_df)


if "Sales" in filtered_df.columns:
    total_sales = filtered_df["Sales"].sum()
else:
    total_sales = 0


if "Units" in filtered_df.columns:
    total_units = filtered_df["Units"].sum()
else:
    total_units = 0


if "Shipping_Lead_Time" in filtered_df.columns:

    avg_lead_time = (
        filtered_df["Shipping_Lead_Time"].mean()
    )

else:

    avg_lead_time = 0


# ============================================================
# KPI CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Shipments",
    f"{total_shipments:,}"
)


col2.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)


col3.metric(
    "Total Units",
    f"{total_units:,.0f}"
)


col4.metric(
    "Avg. Lead Time",
    f"{avg_lead_time:,.1f} days"
)


st.markdown("---")


# ============================================================
# REGIONAL ANALYSIS
# ============================================================

st.header("🌎 Regional Shipment Analysis")


if "Region" in filtered_df.columns:

    region_summary = (
        filtered_df
        .groupby("Region")
        .agg(
            Total_Shipments=("Order ID", "count"),
            Average_Lead_Time=(
                "Shipping_Lead_Time",
                "mean"
            ),
            Total_Sales=("Sales", "sum"),
            Total_Units=("Units", "sum")
        )
        .reset_index()
    )


    st.dataframe(
        region_summary,
        use_container_width=True
    )


    fig, ax = plt.subplots()

    ax.bar(
        region_summary["Region"],
        region_summary["Total_Shipments"]
    )

    ax.set_title("Shipments by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Number of Shipments")

    plt.xticks(rotation=30)

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# SHIPPING MODE ANALYSIS
# ============================================================

st.header("🚚 Shipping Mode Analysis")


if "Ship Mode" in filtered_df.columns:

    mode_summary = (
        filtered_df
        .groupby("Ship Mode")
        .agg(
            Total_Shipments=("Order ID", "count"),
            Average_Lead_Time=(
                "Shipping_Lead_Time",
                "mean"
            ),
            Total_Sales=("Sales", "sum"),
            Total_Units=("Units", "sum")
        )
        .reset_index()
    )


    st.dataframe(
        mode_summary,
        use_container_width=True
    )


    fig, ax = plt.subplots()

    ax.bar(
        mode_summary["Ship Mode"],
        mode_summary["Total_Shipments"]
    )

    ax.set_title("Shipments by Shipping Mode")
    ax.set_xlabel("Shipping Mode")
    ax.set_ylabel("Number of Shipments")

    plt.xticks(rotation=30)

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# FACTORY-TO-CUSTOMER ROUTE ANALYSIS
# ============================================================

st.header("🛣️ Factory-to-Customer Route Analysis")


# Prefer the state-level route because it provides
# more detailed geographic information.

route_column = None

if "Factory_State_Route" in filtered_df.columns:

    route_column = "Factory_State_Route"

elif "Factory_Region_Route" in filtered_df.columns:

    route_column = "Factory_Region_Route"


if route_column is not None:

    route_summary = (
        filtered_df
        .groupby(route_column)
        .agg(
            Total_Shipments=("Order ID", "count"),
            Average_Lead_Time=(
                "Shipping_Lead_Time",
                "mean"
            ),
            Total_Sales=("Sales", "sum"),
            Total_Units=("Units", "sum")
        )
        .reset_index()
        .sort_values(
            "Total_Shipments",
            ascending=False
        )
    )


    st.subheader(
        "Top Factory-to-Customer Routes"
    )


    st.dataframe(
        route_summary.head(20),
        use_container_width=True
    )


    # -------------------------
    # Top 10 Routes Chart
    # -------------------------

    top_routes = (
        route_summary
        .head(10)
        .sort_values("Total_Shipments")
    )


    fig, ax = plt.subplots()

    ax.barh(
        top_routes[route_column].astype(str),
        top_routes["Total_Shipments"]
    )

    ax.set_title(
        "Top 10 Factory-to-Customer Routes"
    )

    ax.set_xlabel("Number of Shipments")
    ax.set_ylabel("Route")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


else:

    st.warning(
        "Factory route columns were not found "
        "in the final dataset."
    )


# ============================================================
# ROUTE REGION SUMMARY
# ============================================================

if "Factory_Region_Route" in filtered_df.columns:

    st.subheader(
        "📍 Factory-to-Customer Regional Routes"
    )


    region_route_summary = (
        filtered_df
        .groupby("Factory_Region_Route")
        .agg(
            Total_Shipments=("Order ID", "count"),
            Average_Lead_Time=(
                "Shipping_Lead_Time",
                "mean"
            ),
            Total_Sales=("Sales", "sum"),
            Total_Units=("Units", "sum")
        )
        .reset_index()
        .sort_values(
            "Total_Shipments",
            ascending=False
        )
    )


    st.dataframe(
        region_route_summary,
        use_container_width=True
    )


# ============================================================
# DATA QUALITY WARNING
# ============================================================

st.markdown("---")

st.warning(
    "Data Quality Note: Calculated shipping lead times are "
    "unusually high compared with typical operational shipping "
    "timelines. The underlying Order Date and Ship Date values "
    "should be validated before using lead-time values for "
    "real-world operational decisions."
)


# ============================================================
# DATASET INFORMATION
# ============================================================

st.markdown("---")

st.header("📊 Dataset Information")


info_col1, info_col2, info_col3 = st.columns(3)


info_col1.metric(
    "Rows",
    f"{len(df):,}"
)


info_col2.metric(
    "Columns",
    f"{len(df.columns):,}"
)


info_col3.metric(
    "Missing Values",
    f"{df.isnull().sum().sum():,}"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Nassau Candy Shipping Route Efficiency Analysis | "
    "Developed by Nikhil Chikte"
)