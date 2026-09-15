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
# CHART COLOR PALETTE
# ============================================================

NAVY = "#0E1621"
BLUE = "#2E86DE"
LIGHT_BLUE = "#74B9FF"
ORANGE = "#F39C12"
LIGHT_ORANGE = "#F8C471"
TEXT = "#F5F6FA"
MUTED_TEXT = "#B2BEC3"
GRID = "#34495E"


# ============================================================
# CHART HELPER
# ============================================================

def style_chart(ax, title, xlabel="", ylabel=""):

    ax.set_facecolor(NAVY)
    ax.figure.set_facecolor(NAVY)

    ax.set_title(
        title,
        fontsize=16,
        fontweight="bold",
        color=TEXT,
        pad=15
    )

    ax.set_xlabel(
        xlabel,
        fontsize=10,
        color=TEXT
    )

    ax.set_ylabel(
        ylabel,
        fontsize=10,
        color=TEXT
    )

    ax.tick_params(
        axis="both",
        colors=TEXT,
        labelsize=9
    )

    ax.grid(
        linestyle="--",
        alpha=0.22,
        color=GRID
    )

    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)


# ============================================================
# TITLE
# ============================================================

st.title("🚚 Nassau Candy Distributor")

st.markdown(
    "## Factory-to-Customer Shipping Route Efficiency Dashboard"
)

st.caption(
    "Interactive analysis of shipping performance, regional "
    "distribution, shipping modes and factory-to-customer routes."
)

st.markdown("---")


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    app_folder = Path(__file__).resolve().parent

    csv_path = (
        app_folder / "nassau_orders_final.csv"
    )

    if not csv_path.exists():

        raise FileNotFoundError(
            f"Could not find dataset: {csv_path}"
        )

    return pd.read_csv(csv_path)


try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "❌ nassau_orders_final.csv was not found."
    )

    st.info(
        "Place 'nassau_orders_final.csv' in the "
        "same folder as app.py."
    )

    st.stop()

except Exception as e:

    st.error(
        f"❌ Error loading dataset: {e}"
    )

    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

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


if (
    "Shipping_Lead_Time" not in df.columns
    and "Order Date" in df.columns
    and "Ship Date" in df.columns
):

    df["Shipping_Lead_Time"] = (
        df["Ship Date"]
        - df["Order Date"]
    ).dt.days


# ============================================================
# FILTER OPTIONS
# ============================================================

regions = (
    sorted(
        df["Region"]
        .dropna()
        .unique()
        .tolist()
    )
    if "Region" in df.columns
    else []
)


ship_modes = (
    sorted(
        df["Ship Mode"]
        .dropna()
        .unique()
        .tolist()
    )
    if "Ship Mode" in df.columns
    else []
)


# ============================================================
# DATE LIMITS
# ============================================================

if "Order Date" in df.columns:

    valid_dates = (
        df["Order Date"]
        .dropna()
    )

    if not valid_dates.empty:

        min_date = (
            valid_dates.min().date()
        )

        max_date = (
            valid_dates.max().date()
        )


# ============================================================
# SESSION STATE
# ============================================================

if "selected_regions" not in st.session_state:

    st.session_state.selected_regions = regions


if "selected_ship_modes" not in st.session_state:

    st.session_state.selected_ship_modes = ship_modes


if (
    "Order Date" in df.columns
    and not valid_dates.empty
):

    if "start_date" not in st.session_state:

        st.session_state.start_date = min_date

    if "end_date" not in st.session_state:

        st.session_state.end_date = max_date


# ============================================================
# RESET FILTERS
# ============================================================

def reset_filters():

    st.session_state.selected_regions = regions

    st.session_state.selected_ship_modes = ship_modes

    if (
        "Order Date" in df.columns
        and not valid_dates.empty
    ):

        st.session_state.start_date = min_date
        st.session_state.end_date = max_date


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header(
    "🔎 Dashboard Filters"
)


st.sidebar.button(
    "🔄 Reset Filters",
    on_click=reset_filters,
    use_container_width=True
)


if "Region" in df.columns:

    st.sidebar.multiselect(
        "🌎 Select Region",
        options=regions,
        key="selected_regions"
    )


if "Ship Mode" in df.columns:

    st.sidebar.multiselect(
        "🚚 Select Ship Mode",
        options=ship_modes,
        key="selected_ship_modes"
    )


if (
    "Order Date" in df.columns
    and not valid_dates.empty
):

    st.sidebar.markdown(
        "### 📅 Order Date"
    )

    st.sidebar.date_input(
        "Start Date",
        min_value=min_date,
        max_value=max_date,
        key="start_date"
    )

    st.sidebar.date_input(
        "End Date",
        min_value=min_date,
        max_value=max_date,
        key="end_date"
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if "Region" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["Region"].isin(
            st.session_state.selected_regions
        )
    ]


if "Ship Mode" in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df["Ship Mode"].isin(
            st.session_state.selected_ship_modes
        )
    ]


if (
    "Order Date" in filtered_df.columns
    and "start_date" in st.session_state
    and "end_date" in st.session_state
):

    start_date = pd.Timestamp(
        st.session_state.start_date
    )

    end_date = pd.Timestamp(
        st.session_state.end_date
    )

    if start_date > end_date:

        st.error(
            "❌ Start Date cannot be later "
            "than End Date."
        )

        st.stop()

    filtered_df = filtered_df[
        (
            filtered_df["Order Date"]
            >= start_date
        )
        &
        (
            filtered_df["Order Date"]
            <= end_date
        )
    ]


# ============================================================
# FILTER STATUS
# ============================================================

filtered_records = len(filtered_df)

total_records = len(df)


record_percentage = (
    filtered_records
    / total_records
    * 100
    if total_records
    else 0
)


st.info(
    f"📊 Showing **{filtered_records:,} of "
    f"{total_records:,} records** — "
    f"**{record_percentage:.1f}% of the full dataset**"
)


if filtered_df.empty:

    st.warning(
        "⚠️ No records match the selected filters. "
        "Change the filters or click Reset Filters."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_shipments = len(filtered_df)


total_sales = (
    filtered_df["Sales"].sum()
    if "Sales" in filtered_df.columns
    else 0
)


total_units = (
    filtered_df["Units"].sum()
    if "Units" in filtered_df.columns
    else 0
)


avg_lead_time = (
    filtered_df[
        "Shipping_Lead_Time"
    ].mean()
    if "Shipping_Lead_Time"
    in filtered_df.columns
    else 0
)


profit_column = None


if "Gross Profit" in filtered_df.columns:

    profit_column = "Gross Profit"

elif "Profit" in filtered_df.columns:

    profit_column = "Profit"


total_profit = (
    filtered_df[
        profit_column
    ].sum()
    if profit_column
    else 0
)


# ============================================================
# FULL DATASET KPI VALUES
# ============================================================

full_sales = (
    df["Sales"].sum()
    if "Sales" in df.columns
    else 0
)


full_units = (
    df["Units"].sum()
    if "Units" in df.columns
    else 0
)


full_profit = (
    df[profit_column].sum()
    if profit_column
    else 0
)


sales_share = (
    total_sales
    / full_sales
    * 100
    if full_sales
    else 0
)


unit_share = (
    total_units
    / full_units
    * 100
    if full_units
    else 0
)


profit_share = (
    total_profit
    / full_profit
    * 100
    if full_profit
    else 0
)


# ============================================================
# KPI DASHBOARD
# ============================================================

st.header(
    "📌 Performance Overview"
)


if profit_column:

    k1, k2, k3, k4, k5 = (
        st.columns(5)
    )

else:

    k1, k2, k3, k4 = (
        st.columns(4)
    )


k1.metric(
    "Total Shipments",
    f"{total_shipments:,}"
)

k1.caption(
    f"{record_percentage:.1f}% "
    "of full dataset"
)


k2.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

k2.caption(
    f"{sales_share:.1f}% "
    "of total sales"
)


k3.metric(
    "Total Units",
    f"{total_units:,.0f}"
)

k3.caption(
    f"{unit_share:.1f}% "
    "of total units"
)


k4.metric(
    "Avg. Lead Time",
    f"{avg_lead_time:,.1f} days"
)

k4.caption(
    "Based on current filters"
)


if profit_column:

    k5.metric(
        "Total Profit",
        f"${total_profit:,.2f}"
    )

    k5.caption(
        f"{profit_share:.1f}% "
        "of total profit"
    )


st.markdown("---")


# ============================================================
# MONTHLY PERFORMANCE TREND
# ============================================================

st.header(
    "📈 Monthly Performance Trend"
)


if (
    "Order Date" in filtered_df.columns
    and "Sales" in filtered_df.columns
):

    trend_df = (
        filtered_df
        .dropna(
            subset=["Order Date"]
        )
        .copy()
    )

    trend_df["Month"] = (
        trend_df["Order Date"]
        .dt.to_period("M")
        .dt.to_timestamp()
    )


    monthly_summary = (
        trend_df
        .groupby("Month")
        .agg(
            Sales=(
                "Sales",
                "sum"
            ),
            Shipments=(
                "Order ID",
                "count"
            )
        )
        .reset_index()
        .sort_values("Month")
    )


    if not monthly_summary.empty:

        trend1, trend2 = (
            st.columns(2)
        )


        # ====================================================
        # SALES TREND
        # ====================================================

        with trend1:

            fig, ax = plt.subplots(
                figsize=(8, 4.8)
            )

            style_chart(
                ax,
                "Monthly Sales Trend",
                "Month",
                "Sales ($)"
            )

            ax.plot(
                monthly_summary["Month"],
                monthly_summary["Sales"],
                color=BLUE,
                marker="o",
                linewidth=2.5,
                markersize=6
            )

            ax.fill_between(
                monthly_summary["Month"],
                monthly_summary["Sales"],
                color=BLUE,
                alpha=0.12
            )

            if len(monthly_summary) > 0:

                peak_index = (
                    monthly_summary[
                        "Sales"
                    ].idxmax()
                )

                peak = (
                    monthly_summary
                    .loc[peak_index]
                )

                ax.scatter(
                    peak["Month"],
                    peak["Sales"],
                    color=ORANGE,
                    s=90,
                    zorder=5
                )

                ax.annotate(
                    f"${peak['Sales']:,.0f}",
                    (
                        peak["Month"],
                        peak["Sales"]
                    ),
                    xytext=(0, 12),
                    textcoords="offset points",
                    ha="center",
                    color=ORANGE,
                    fontweight="bold"
                )

            plt.xticks(
                rotation=45
            )

            plt.tight_layout()

            st.pyplot(
                fig,
                use_container_width=True
            )

            plt.close(fig)


        # ====================================================
        # SHIPMENT TREND
        # ====================================================

        with trend2:

            fig, ax = plt.subplots(
                figsize=(8, 4.8)
            )

            style_chart(
                ax,
                "Monthly Shipment Trend",
                "Month",
                "Shipments"
            )

            ax.plot(
                monthly_summary["Month"],
                monthly_summary["Shipments"],
                color=LIGHT_BLUE,
                marker="o",
                linewidth=2.5,
                markersize=6
            )

            ax.fill_between(
                monthly_summary["Month"],
                monthly_summary[
                    "Shipments"
                ],
                color=LIGHT_BLUE,
                alpha=0.12
            )

            if len(monthly_summary) > 0:

                peak_index = (
                    monthly_summary[
                        "Shipments"
                    ].idxmax()
                )

                peak = (
                    monthly_summary
                    .loc[peak_index]
                )

                ax.scatter(
                    peak["Month"],
                    peak["Shipments"],
                    color=ORANGE,
                    s=90,
                    zorder=5
                )

                ax.annotate(
                    f"{int(peak['Shipments']):,}",
                    (
                        peak["Month"],
                        peak["Shipments"]
                    ),
                    xytext=(0, 12),
                    textcoords="offset points",
                    ha="center",
                    color=ORANGE,
                    fontweight="bold"
                )

            plt.xticks(
                rotation=45
            )

            plt.tight_layout()

            st.pyplot(
                fig,
                use_container_width=True
            )

            plt.close(fig)


st.markdown("---")


# ============================================================
# REGIONAL PERFORMANCE
# ============================================================

st.header(
    "🌎 Regional Performance & Ranking"
)


# ------------------------------------------------------------
# IMPORTANT:
# Region ranking uses the complete dataset after applying
# Ship Mode + Date filters, but BEFORE the Region filter.
#
# This prevents Pacific from incorrectly appearing as
# "100%" simply because only Pacific was selected.
# ------------------------------------------------------------

region_base_df = df.copy()


if "Ship Mode" in region_base_df.columns:

    region_base_df = region_base_df[
        region_base_df[
            "Ship Mode"
        ].isin(
            st.session_state.selected_ship_modes
        )
    ]


if (
    "Order Date" in region_base_df.columns
    and "start_date" in st.session_state
    and "end_date" in st.session_state
):

    region_base_df = region_base_df[
        (
            region_base_df["Order Date"]
            >= start_date
        )
        &
        (
            region_base_df["Order Date"]
            <= end_date
        )
    ]


if (
    "Region" in region_base_df.columns
    and not region_base_df.empty
):

    region_summary = (
        region_base_df
        .groupby("Region")
        .agg(
            Total_Shipments=(
                "Order ID",
                "count"
            ),
            Total_Sales=(
                "Sales",
                "sum"
            ),
            Total_Units=(
                "Units",
                "sum"
            ),
            Average_Lead_Time=(
                "Shipping_Lead_Time",
                "mean"
            )
        )
        .reset_index()
    )


    region_summary[
        "Shipment_Share_%"
    ] = (
        region_summary[
            "Total_Shipments"
        ]
        / region_summary[
            "Total_Shipments"
        ].sum()
        * 100
    )


    region_summary["Rank"] = (
        region_summary[
            "Total_Shipments"
        ]
        .rank(
            method="dense",
            ascending=False
        )
        .astype(int)
    )


    region_summary = (
        region_summary
        .sort_values("Rank")
    )


    display_region = (
        region_summary.copy()
    )


    display_region[
        "Shipment_Share_%"
    ] = (
        display_region[
            "Shipment_Share_%"
        ].round(2)
    )


    display_region[
        "Average_Lead_Time"
    ] = (
        display_region[
            "Average_Lead_Time"
        ].round(2)
    )


    display_region = (
        display_region.rename(
            columns={
                "Rank": "Rank",
                "Region": "Region",
                "Total_Shipments":
                    "Total Shipments",
                "Shipment_Share_%":
                    "Shipment Share (%)",
                "Total_Sales":
                    "Total Sales ($)",
                "Total_Units":
                    "Total Units",
                "Average_Lead_Time":
                    "Avg. Lead Time (Days)"
            }
        )
    )


    st.caption(
        "Regional ranking compares all regions "
        "under the selected date and shipping-mode filters."
    )


    st.dataframe(
        display_region,
        use_container_width=True,
        hide_index=True
    )


    region1, region2 = (
        st.columns(2)
    )


    # ========================================================
    # REGIONAL SHIPMENTS
    # ========================================================

    with region1:

        chart_data = (
            region_summary
            .sort_values(
                "Total_Shipments",
                ascending=False
            )
        )


        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        style_chart(
            ax,
            "Shipments by Region",
            "Region",
            "Shipments"
        )

        # Blue by default.
        # Orange only when specific regions are selected.
        all_regions_selected = (
            len(st.session_state.selected_regions) == len(regions)
        )

        bar_colors = [
            BLUE
            if all_regions_selected
            else (
                ORANGE
                if region in st.session_state.selected_regions
                else BLUE
            )
            for region in chart_data["Region"]
        ]

        bars = ax.bar(
            chart_data["Region"],
            chart_data[
                "Total_Shipments"
            ],
            color=bar_colors,
            width=0.65
        )


        max_shipments = (
            chart_data[
                "Total_Shipments"
            ].max()
        )


        for (
            bar,
            shipments,
            share
        ) in zip(
            bars,
            chart_data[
                "Total_Shipments"
            ],
            chart_data[
                "Shipment_Share_%"
            ]
        ):

            ax.text(
                bar.get_x()
                + bar.get_width() / 2,
                bar.get_height()
                + max_shipments * 0.02,
                f"{shipments:,}\n"
                f"{share:.1f}%",
                ha="center",
                va="bottom",
                color=TEXT,
                fontsize=9,
                fontweight="bold"
            )


        ax.set_ylim(
            0,
            max_shipments * 1.18
        )


        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


    # ========================================================
    # REGIONAL SALES
    # ========================================================

    with region2:

        sales_region = (
            region_summary
            .sort_values(
                "Total_Sales",
                ascending=False
            )
        )


        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        style_chart(
            ax,
            "Sales by Region",
            "Region",
            "Sales ($)"
        )


        # Light blue by default.
        # Orange only when specific regions are selected.
        all_regions_selected = (
            len(st.session_state.selected_regions) == len(regions)
        )

        sales_colors = [
            LIGHT_BLUE
            if all_regions_selected
            else (
                ORANGE
                if region in st.session_state.selected_regions
                else LIGHT_BLUE
            )
            for region in sales_region["Region"]
        ]


        bars = ax.bar(
            sales_region["Region"],
            sales_region[
                "Total_Sales"
            ],
            color=sales_colors,
            width=0.65
        )


        max_sales = (
            sales_region[
                "Total_Sales"
            ].max()
        )


        for bar, value in zip(
            bars,
            sales_region[
                "Total_Sales"
            ]
        ):

            ax.text(
                bar.get_x()
                + bar.get_width() / 2,
                bar.get_height()
                + max_sales * 0.02,
                f"${value:,.0f}",
                ha="center",
                va="bottom",
                color=TEXT,
                fontsize=9,
                fontweight="bold"
            )


        ax.set_ylim(
            0,
            max_sales * 1.18
        )


        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


st.markdown("---")


# ============================================================
# SHIPPING MODE PERFORMANCE
# ============================================================

st.header(
    "🚚 Shipping Mode Performance"
)


if "Ship Mode" in filtered_df.columns:

    mode_summary = (
        filtered_df
        .groupby("Ship Mode")
        .agg(
            Total_Shipments=(
                "Order ID",
                "count"
            ),
            Total_Sales=(
                "Sales",
                "sum"
            ),
            Total_Units=(
                "Units",
                "sum"
            ),
            Average_Lead_Time=(
                "Shipping_Lead_Time",
                "mean"
            )
        )
        .reset_index()
    )


    mode_summary[
        "Shipment_Share_%"
    ] = (
        mode_summary[
            "Total_Shipments"
        ]
        / mode_summary[
            "Total_Shipments"
        ].sum()
        * 100
    )


    mode_summary["Rank"] = (
        mode_summary[
            "Total_Shipments"
        ]
        .rank(
            method="dense",
            ascending=False
        )
        .astype(int)
    )


    mode_summary = (
        mode_summary
        .sort_values("Rank")
    )


    display_mode = (
        mode_summary.copy()
    )


    display_mode[
        "Shipment_Share_%"
    ] = (
        display_mode[
            "Shipment_Share_%"
        ].round(2)
    )


    display_mode[
        "Average_Lead_Time"
    ] = (
        display_mode[
            "Average_Lead_Time"
        ].round(2)
    )


    display_mode = (
        display_mode.rename(
            columns={
                "Rank": "Rank",
                "Ship Mode":
                    "Ship Mode",
                "Total_Shipments":
                    "Total Shipments",
                "Shipment_Share_%":
                    "Shipment Share (%)",
                "Total_Sales":
                    "Total Sales ($)",
                "Total_Units":
                    "Total Units",
                "Average_Lead_Time":
                    "Avg. Lead Time (Days)"
            }
        )
    )


    st.caption(
        "Percentages are based on the "
        "current filtered dataset."
    )


    st.dataframe(
        display_mode,
        use_container_width=True,
        hide_index=True
    )


    mode1, mode2 = (
        st.columns(2)
    )


    # ========================================================
    # SHIPPING MODE SHIPMENTS
    # ========================================================

    with mode1:

        mode_chart = (
            mode_summary
            .sort_values(
                "Total_Shipments",
                ascending=False
            )
        )


        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        style_chart(
            ax,
            "Shipments by Shipping Mode",
            "Shipping Mode",
            "Shipments"
        )


        colors = [
            ORANGE
        ] + [
            BLUE
            for _ in range(
                len(mode_chart) - 1
            )
        ]


        bars = ax.bar(
            mode_chart[
                "Ship Mode"
            ],
            mode_chart[
                "Total_Shipments"
            ],
            color=colors,
            width=0.65
        )


        max_mode = (
            mode_chart[
                "Total_Shipments"
            ].max()
        )


        for (
            bar,
            shipments,
            percentage
        ) in zip(
            bars,
            mode_chart[
                "Total_Shipments"
            ],
            mode_chart[
                "Shipment_Share_%"
            ]
        ):

            ax.text(
                bar.get_x()
                + bar.get_width() / 2,
                bar.get_height()
                + max_mode * 0.02,
                f"{shipments:,}\n"
                f"{percentage:.1f}%",
                ha="center",
                va="bottom",
                color=TEXT,
                fontsize=9,
                fontweight="bold"
            )


        ax.set_ylim(
            0,
            max_mode * 1.2
        )


        plt.xticks(
            rotation=20
        )


        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


    # ========================================================
    # SHIPPING MODE SALES
    # ========================================================

    with mode2:

        mode_sales = (
            mode_summary
            .sort_values(
                "Total_Sales",
                ascending=False
            )
        )


        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        style_chart(
            ax,
            "Sales by Shipping Mode",
            "Shipping Mode",
            "Sales ($)"
        )


        sales_colors = [
            ORANGE
        ] + [
            LIGHT_BLUE
            for _ in range(
                len(mode_sales) - 1
            )
        ]


        bars = ax.bar(
            mode_sales[
                "Ship Mode"
            ],
            mode_sales[
                "Total_Sales"
            ],
            color=sales_colors,
            width=0.65
        )


        max_mode_sales = (
            mode_sales[
                "Total_Sales"
            ].max()
        )


        for bar, value in zip(
            bars,
            mode_sales[
                "Total_Sales"
            ]
        ):

            ax.text(
                bar.get_x()
                + bar.get_width() / 2,
                bar.get_height()
                + max_mode_sales * 0.02,
                f"${value:,.0f}",
                ha="center",
                va="bottom",
                color=TEXT,
                fontsize=9,
                fontweight="bold"
            )


        ax.set_ylim(
            0,
            max_mode_sales * 1.18
        )


        plt.xticks(
            rotation=20
        )


        plt.tight_layout()

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)


st.markdown("---")


# ============================================================
# FACTORY-TO-CUSTOMER ROUTE ANALYSIS
# ============================================================

st.header(
    "🛣️ Factory-to-Customer Route Performance"
)


route_column = None


if "Factory_State_Route" in filtered_df.columns:

    route_column = (
        "Factory_State_Route"
    )

elif "Factory_Region_Route" in filtered_df.columns:

    route_column = (
        "Factory_Region_Route"
    )


if route_column:

    route_summary = (
        filtered_df
        .groupby(route_column)
        .agg(
            Total_Shipments=(
                "Order ID",
                "count"
            ),
            Total_Sales=(
                "Sales",
                "sum"
            ),
            Total_Units=(
                "Units",
                "sum"
            ),
            Average_Lead_Time=(
                "Shipping_Lead_Time",
                "mean"
            )
        )
        .reset_index()
    )


    route_summary[
        "Shipment_Share_%"
    ] = (
        route_summary[
            "Total_Shipments"
        ]
        / route_summary[
            "Total_Shipments"
        ].sum()
        * 100
    )


    route_summary = (
        route_summary
        .sort_values(
            "Total_Shipments",
            ascending=False
        )
    )


    route_summary["Rank"] = range(
        1,
        len(route_summary) + 1
    )


    top_routes = (
        route_summary
        .head(10)
        .copy()
    )


    display_routes = (
        top_routes.copy()
    )


    display_routes[
        "Shipment_Share_%"
    ] = (
        display_routes[
            "Shipment_Share_%"
        ].round(2)
    )


    display_routes[
        "Average_Lead_Time"
    ] = (
        display_routes[
            "Average_Lead_Time"
        ].round(2)
    )


    route_display_name = (
        "Factory → State Route"
        if route_column
        == "Factory_State_Route"
        else "Factory → Region Route"
    )


    display_routes = (
        display_routes.rename(
            columns={
                "Rank": "Rank",
                route_column:
                    route_display_name,
                "Total_Shipments":
                    "Total Shipments",
                "Shipment_Share_%":
                    "Shipment Share (%)",
                "Total_Sales":
                    "Total Sales ($)",
                "Total_Units":
                    "Total Units",
                "Average_Lead_Time":
                    "Avg. Lead Time (Days)"
            }
        )
    )


    st.subheader(
        "🏆 Top 10 Routes"
    )


    st.caption(
        "Ranked by shipment volume. Percentages "
        "are based on the current filtered data."
    )


    st.dataframe(
        display_routes,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # ATTRACTIVE TOP 10 ROUTES CHART
    # ========================================================

    chart_routes = (
        top_routes
        .sort_values(
            "Total_Shipments",
            ascending=True
        )
    )


    fig, ax = plt.subplots(
        figsize=(11, 6.5)
    )


    style_chart(
        ax,
        "Top 10 Factory-to-Customer Routes",
        "Number of Shipments",
        "Factory → Customer Route"
    )


    highest_route = (
        top_routes
        .iloc[0][route_column]
    )


    route_colors = [
        ORANGE
        if route == highest_route
        else BLUE
        for route
        in chart_routes[
            route_column
        ]
    ]


    bars = ax.barh(
        chart_routes[
            route_column
        ].astype(str),
        chart_routes[
            "Total_Shipments"
        ],
        color=route_colors,
        height=0.62
    )


    max_route = (
        chart_routes[
            "Total_Shipments"
        ].max()
    )


    for (
        bar,
        shipments,
        percentage
    ) in zip(
        bars,
        chart_routes[
            "Total_Shipments"
        ],
        chart_routes[
            "Shipment_Share_%"
        ]
    ):

        ax.text(
            bar.get_width()
            + max_route * 0.015,
            bar.get_y()
            + bar.get_height() / 2,
            f"{shipments:,}  |  "
            f"{percentage:.1f}%",
            va="center",
            color=TEXT,
            fontsize=10,
            fontweight="bold"
        )


    ax.set_xlim(
        0,
        max_route * 1.28
    )


    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


else:

    st.warning(
        "⚠️ Factory route columns were not "
        "found in the dataset."
    )


st.markdown("---")


# ============================================================
# KEY BUSINESS INSIGHTS
# ============================================================

st.header(
    "💡 Key Business Insights"
)


insights = []


# ============================================================
# REGION INSIGHT
# ============================================================

if (
    "region_summary" in locals()
    and not region_summary.empty
):

    overall_region = (
        region_summary
        .sort_values(
            "Total_Shipments",
            ascending=False
        )
        .iloc[0]
    )


    if len(
        st.session_state.selected_regions
    ) == 1:

        selected_region_name = (
            st.session_state
            .selected_regions[0]
        )


        selected_region_data = (
            region_summary[
                region_summary["Region"]
                == selected_region_name
            ]
        )


        if not selected_region_data.empty:

            selected_region_row = (
                selected_region_data
                .iloc[0]
            )


            insights.append(
                f"🌎 **{selected_region_name}** "
                f"accounts for "
                f"**{selected_region_row['Shipment_Share_%']:.1f}%** "
                f"of shipments in the regional comparison "
                f"and ranks "
                f"**#{int(selected_region_row['Rank'])}**."
            )

    else:

        insights.append(
            f"🌎 **{overall_region['Region']}** "
            f"ranks #1 by shipment volume with "
            f"**{overall_region['Total_Shipments']:,} "
            f"shipments** "
            f"({overall_region['Shipment_Share_%']:.1f}%)."
        )


# ============================================================
# SHIPPING MODE INSIGHT
# ============================================================

if (
    "mode_summary" in locals()
    and not mode_summary.empty
):

    top_mode = (
        mode_summary
        .sort_values(
            "Total_Shipments",
            ascending=False
        )
        .iloc[0]
    )


    insights.append(
        f"🚚 **{top_mode['Ship Mode']}** "
        f"is the most-used shipping mode with "
        f"**{top_mode['Total_Shipments']:,} shipments** "
        f"({top_mode['Shipment_Share_%']:.1f}% "
        f"of filtered shipments)."
    )


# ============================================================
# ROUTE INSIGHT
# ============================================================

if (
    route_column
    and "route_summary" in locals()
    and not route_summary.empty
):

    top_route = (
        route_summary.iloc[0]
    )


    insights.append(
        f"🛣️ The highest-volume route is "
        f"**{top_route[route_column]}**, with "
        f"**{top_route['Total_Shipments']:,} shipments** "
        f"({top_route['Shipment_Share_%']:.1f}% "
        f"of filtered shipments)."
    )


# ============================================================
# SALES INSIGHT
# ============================================================

if "Sales" in filtered_df.columns:

    insights.append(
        f"💰 The current filter selection represents "
        f"**{sales_share:.1f}% of total dataset sales**, "
        f"worth **${total_sales:,.2f}**."
    )


for insight in insights:

    st.markdown(insight)


# ============================================================
# DATA QUALITY NOTE
# ============================================================

st.markdown("---")


st.warning(
    "⚠️ **Data Quality Note:** Calculated shipping "
    "lead times are unusually high compared with "
    "typical operational shipping timelines. "
    "The underlying Order Date and Ship Date values "
    "should be validated before using lead-time "
    "results for real-world operational decisions."
)


# ============================================================
# DATASET INFORMATION
# ============================================================

st.header(
    "📊 Dataset Information"
)


info1, info2, info3, info4 = (
    st.columns(4)
)


info1.metric(
    "Total Dataset Rows",
    f"{len(df):,}"
)


info2.metric(
    "Filtered Rows",
    f"{len(filtered_df):,}"
)


info3.metric(
    "Columns",
    f"{len(df.columns):,}"
)


info4.metric(
    "Missing Values",
    f"{df.isnull().sum().sum():,}"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")


st.caption(
    "Nassau Candy Shipping Route Efficiency Analysis | "
    "Python • Pandas • Matplotlib • Streamlit | "
    "Developed by Nikhil Chikte"
)