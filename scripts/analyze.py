# scripts/analyze.py
import pandas as pd
import streamlit as st

def visualize_publications_per_year(df, date_column="publication_date"):
    # Ensure date column is in datetime format
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

    # Drop missing or invalid dates
    df = df.dropna(subset=[date_column])

    # Extract year
    df["year"] = df[date_column].dt.year

    # Count publications per year
    yearly_counts = df["year"].value_counts().sort_index()

    # Visualize
    st.write("### Number of Publications per Year")
    st.bar_chart(yearly_counts)
