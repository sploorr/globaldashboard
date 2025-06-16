import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Sample dataset for hunger problem only
DATA = [
    {"Country": "Nigeria", "ISO3": "NGA", "Estimated Cost (Billion USD)": 12},
    {"Country": "India", "ISO3": "IND", "Estimated Cost (Billion USD)": 25},
    {"Country": "Ethiopia", "ISO3": "ETH", "Estimated Cost (Billion USD)": 6},
    {"Country": "Bangladesh", "ISO3": "BGD", "Estimated Cost (Billion USD)": 5}
]

# Create DataFrame
country_df = pd.DataFrame(DATA)

# Streamlit page config
st.set_page_config(page_title="Global Problem Selector", layout="wide")

# Initial landing layout style
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 90vh;
        flex-direction: column;
    }
    .selectbox-container {
        width: 300px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Centered landing page prompt
with st.container():
    st.markdown("""
    <div class="centered">
        <h1 style='font-size: 60px;'>I want to solve:</h1>
        <div class="selectbox-container">
    """, unsafe_allow_html=True)

    problem = st.selectbox("", ["", "End Hunger", "Access to Clean Water", "Eradicate Malaria", "Universal Basic Education", "Universal Electricity Access"], index=0)

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# Show interactive map only after a valid problem is selected
if problem and problem != "":
    st.markdown(f"### 🌍 Estimated Cost to {problem} by Country")

    # Create animated-style hover map
    fig = go.Figure(data=go.Choropleth(
        locations=country_df['ISO3'],
        z=country_df['Estimated Cost (Billion USD)'],
        text=country_df['Country'],
        colorscale='Reds',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Billions USD',
        hovertemplate='<b>%{text}</b><br>Cost: $%{z}B'<br><extra></extra>
    ))

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='natural earth'
        ),
        margin={"r":0,"t":30,"l":0,"b":0},
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

# Footer
st.caption("Sample data only. Real-world estimates sourced from UN, World Bank, WHO, etc.")
