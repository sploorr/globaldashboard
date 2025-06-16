import streamlit as st
import pandas as pd
import plotly.express as px

# Sample dataset
DATA = [
    {
        "Country": "Nigeria",
        "Problem": "End Hunger",
        "Estimated Cost (Billion USD)": 12,
        "People Affected (Millions)": 98
    },
    {
        "Country": "India",
        "Problem": "End Hunger",
        "Estimated Cost (Billion USD)": 25,
        "People Affected (Millions)": 189
    },
    {
        "Country": "Ethiopia",
        "Problem": "Universal Access to Clean Water",
        "Estimated Cost (Billion USD)": 5,
        "People Affected (Millions)": 57
    },
    {
        "Country": "Democratic Republic of the Congo",
        "Problem": "Universal Access to Clean Water",
        "Estimated Cost (Billion USD)": 4,
        "People Affected (Millions)": 50
    },
    {
        "Country": "Mozambique",
        "Problem": "Eradicate Malaria",
        "Estimated Cost (Billion USD)": 0.6,
        "People Affected (Millions)": 30
    },
    {
        "Country": "Bangladesh",
        "Problem": "Universal Basic Education",
        "Estimated Cost (Billion USD)": 2.5,
        "People Affected (Millions)": 20
    },
    {
        "Country": "Pakistan",
        "Problem": "Universal Electricity Access",
        "Estimated Cost (Billion USD)": 4,
        "People Affected (Millions)": 45
    }
]

# Create DataFrame
country_df = pd.DataFrame(DATA)

# Streamlit page config
st.set_page_config(page_title="Global Problem Country Breakdown", layout="wide")
st.title("🌍 Global Problem Solving Dashboard – Country Breakdown")

# Sidebar Filters
with st.sidebar:
    st.header("🔎 Filters")
    selected_problem = st.multiselect("Select Problem(s):", options=country_df["Problem"].unique(), default=country_df["Problem"].unique())
    selected_country = st.multiselect("Select Country/Countries:", options=country_df["Country"].unique(), default=country_df["Country"].unique())

# Filtered Data
filtered_df = country_df[
    country_df["Problem"].isin(selected_problem) &
    country_df["Country"].isin(selected_country)
]

# Display Table
st.subheader("📊 Country-Level Problem Cost Table")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# Interactive Map
st.subheader("🗺️ Estimated Cost by Country (Map View)")
if not filtered_df.empty:
    fig_map = px.choropleth(
        filtered_df,
        locations="Country",
        locationmode="country names",
        color="Estimated Cost (Billion USD)",
        hover_name="Country",
        hover_data={"Problem": True, "Estimated Cost (Billion USD)": True, "People Affected (Millions)": True},
        color_continuous_scale="Viridis",
        title="Estimated Cost by Country"
    )
    fig_map.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.info("No data to display based on selected filters.")

# Footer
st.caption("Sample data only. Sources include WHO, UN FAO, World Bank, UNICEF, IEA, UNESCO.")
