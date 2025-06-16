import streamlit as st
import pandas as pd
import plotly.express as px

# Sample dataset
DATA = [
    {
        "Problem": "End Hunger",
        "Estimated Global Cost (Annual)": 152.5,
        "People Affected (Millions)": 735,
        "Cost per Person (USD)": 207,
        "Breakdown Available": "Some",
        "Source": "UN FAO, IFPRI, Ceres2030"
    },
    {
        "Problem": "Universal Access to Clean Water",
        "Estimated Global Cost (Annual)": 114,
        "People Affected (Millions)": 2200,
        "Cost per Person (USD)": 52,
        "Breakdown Available": "Yes",
        "Source": "World Bank, WHO, UNICEF"
    },
    {
        "Problem": "Eradicate Malaria",
        "Estimated Global Cost (Annual)": 3.4,
        "People Affected (Millions)": 249,
        "Cost per Person (USD)": 13,
        "Breakdown Available": "Yes",
        "Source": "WHO Global Technical Strategy"
    },
    {
        "Problem": "Universal Basic Education",
        "Estimated Global Cost (Annual)": 39,
        "People Affected (Millions)": 244,
        "Cost per Person (USD)": 160,
        "Breakdown Available": "Yes",
        "Source": "UNESCO"
    },
    {
        "Problem": "Universal Electricity Access",
        "Estimated Global Cost (Annual)": 35,
        "People Affected (Millions)": 675,
        "Cost per Person (USD)": 52,
        "Breakdown Available": "Yes",
        "Source": "IEA, World Bank"
    },
    {
        "Problem": "Inadequate Housing",
        "Estimated Global Cost (Annual)": None,
        "People Affected (Millions)": 1600,
        "Cost per Person (USD)": None,
        "Breakdown Available": "Partial",
        "Source": "UN-Habitat"
    }
]

# Create DataFrame
df = pd.DataFrame(DATA)

# Streamlit page config
st.set_page_config(page_title="Global Problem Solving Cost Dashboard", layout="wide")
st.title("🌍 Global Problem Solving Cost Dashboard")

# Sidebar Filters
with st.sidebar:
    st.header("🔎 Filter")
    selected_problem = st.multiselect("Select Problem(s):", options=df["Problem"].unique(), default=df["Problem"].unique())
    cost_min = float(df["Estimated Global Cost (Annual)"].min(skipna=True))
    cost_max = float(df["Estimated Global Cost (Annual)"].max(skipna=True))
    cost_range = st.slider("Max Annual Cost (Billion USD):", cost_min, cost_max, (cost_min, cost_max))

# Filtered Data
filtered_df = df[
    df["Problem"].isin(selected_problem) &
    (
        df["Estimated Global Cost (Annual)"].isna() |
        (
            (df["Estimated Global Cost (Annual)"] >= cost_range[0]) &
            (df["Estimated Global Cost (Annual)"] <= cost_range[1])
        )
    )
]

# Data Table
st.subheader("📊 Problem Summary Table")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# Scatter Plot
st.subheader("💰 Estimated Cost vs. People Affected")
plot_df = filtered_df.dropna(subset=["Estimated Global Cost (Annual)", "People Affected (Millions)"])

if not plot_df.empty:
    fig = px.scatter(
        plot_df,
        x="Estimated Global Cost (Annual)",
        y="People Affected (Millions)",
        color="Problem",
        size="Cost per Person (USD)",
        hover_name="Problem",
        labels={
            "Estimated Global Cost (Annual)": "Annual Cost (Billion USD)",
            "People Affected (Millions)": "People Affected (Millions)"
        },
        size_max=60
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data to display in the chart based on current filters.")

# Footer
st.caption("Data sources: UN FAO, WHO, UNICEF, IEA, UNESCO, World Bank, UN-Habitat")
