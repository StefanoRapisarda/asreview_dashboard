# scripts/analyze.py
import pandas as pd
import streamlit as st
# scripts/analyze.py
import pandas as pd
import streamlit as st

def visualize_publications_per_year(df, date_column="publication_date"):
    # Ensure date column is datetime
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=[date_column])

    # Extract year
    df["year"] = df[date_column].dt.year

    # Count publications per year
    yearly_counts = df["year"].value_counts().sort_index()

    # Compute cumulative publications
    cumulative_counts = yearly_counts.cumsum()

    # Display chart
    st.write("### 📈 Cumulative Publications per Year")
    st.bar_chart(cumulative_counts)
