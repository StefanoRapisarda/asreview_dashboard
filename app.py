# app.py
import streamlit as st
import pandas as pd
from scripts.analyze import visualize_publications_per_month  # if you have analysis logic as functions

# Title
st.title("📊 My Data Dashboard")

# Load data
@st.cache_data.clear()
def load_data():
    return pd.read_csv("data/asreview_papers.csv")

df = load_data()
st.write("### Raw Data", df)

# Add interaction
if st.checkbox("Show summary stats"):
    st.write(df.describe())

# Visuals (example)
st.line_chart(df["Date"])  # replace with your actual column

# Run analysis
if st.button("Visualize Publications per Year"):
    fig = visualize_publications_per_year(df)
    st.pyplot(fig)

