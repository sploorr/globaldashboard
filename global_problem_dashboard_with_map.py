import streamlit as st
import pandas as pd
import plotly.express as px

# Sample dataset for hunger problem only
DATA = [
    {"Country": "Nigeria", "Estimated Cost (Billion USD)": 12},
    {"Country": "India", "Estimated Cost (Billion USD)": 25},
    {"Country": "Ethiopia", "Estimated Cost (Billion USD)": 6},
    {"Country": "Bangladesh", "Estimated Cost (Billion USD)": 5}
]

# Create DataFrame
country_df = pd.DataFrame(DATA)

# Streamlit page config
st.set_page_config(page_title="Global Problem Selector", layout="wide")

# Landing Page Prompt
st.markdown("""
    <div style='text-align: center; margin-top: 100px;'>
        <h1 style='font-size: 50px;'>I want to solve:</h1>
    </div>
""", unsafe_allow_html=True)

# Problem selection
problem = st.selectbox("", ["End Hunger", "Access to Clean Water", "Eradicate Malaria", "Universal Basic Education", "Universal Electricity Access"], index=0)

# When a problem is selected
if problem:
    st.markdown(f"### 🌍 Cost to {problem} by Country")
    
    # Interactive map for selected problem (sample for Hunger only)
    fig = px.choropleth(
        country_df,
        locations="Country",
        locationmode="country names",
        color="Estimated Cost (Billion USD)",
        hover_name="Country",
        hover_data={"Estimated Cost (Billion USD)": True},
        color_continuous_scale="Reds",
        title=f"Estimated Cost to {problem}"
    )
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.caption("Sample data only. Real-world estimates sourced from UN, World Bank, WHO, etc.")
