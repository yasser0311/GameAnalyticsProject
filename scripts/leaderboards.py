import streamlit as st
import pandas as pd

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Leaderboards
def leaderboards(engine):
    # Top-ranked competitors
    top_ranked = fetch_data(engine, "SELECT * FROM Competitors ORDER BY rank ASC LIMIT 10")
    st.subheader("Top-Ranked Competitors🏅")
    st.dataframe(top_ranked)

    # Competitors with the highest points
    highest_points = fetch_data(engine, "SELECT * FROM Competitors ORDER BY points DESC LIMIT 10")
    st.subheader("Competitors with Highest Points 🤼‍♂️")
    st.dataframe(highest_points)
