# app.py
import streamlit as st
import pandas as pd
from scripts.analyze import visualize_publications_per_month  # if you have analysis logic as functions

# Title
st.title("📊 My Data Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/asreview_papers.csv")

df = load_data()
st.write("### Raw Data", df)

# Add interaction
if st.checkbox("Test button"):
    st.write(df.describe())
 # replace with your actual column

fig = visualize_publications_per_month(df)
st.pyplot(fig)

