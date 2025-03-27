# scripts/analyze.py
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator


def visualize_publications_per_month(df, date_column="Date"):
    # Convert to datetime and filter
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")
    df = df.dropna(subset=[date_column])
    df = df[df[date_column] >= "2021-01-01"]

    # Create 'year-month' column
    df["year_month"] = df[date_column].dt.to_period("M").dt.to_timestamp()

    # Count publications per month
    monthly_counts = df["year_month"].value_counts().sort_index()

    # Fill missing months
    all_months = pd.date_range(start="2021-01-01", end=pd.Timestamp.today(), freq="MS")
    monthly_counts = monthly_counts.reindex(all_months, fill_value=0)

    # Plot
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(monthly_counts.index, monthly_counts.values, width=20, align="center", color="steelblue")
    ax.set_title("Publications Per Month (Since Jan 2021)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Publications")

    # Set ticks every 3 months
    tick_locs = pd.date_range(start="2021-01-01", end=pd.Timestamp.today(), freq="3MS")
    ax.set_xticks(tick_locs)
    ax.set_xticklabels([d.strftime("%Y-%m") for d in tick_locs], rotation=45)

    # Format axis
    ax.margins(x=0.01)
    ax.grid(axis="y", linestyle=":", alpha=0.6)

    # Fix layout to prevent cutoff
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.2)

    return fig

if __name__ == "__main__":
    df = pd.read_csv("data/asreview_papers.csv")
    fig = visualize_publications_per_month(df)
    plt.show()
