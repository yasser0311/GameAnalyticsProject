import streamlit as st
import pandas as pd

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Homepage Dashboard
def homepage(engine):
    st.title("Tennis Event Explorer Dashboard 🎾")

    # Total number of competitors
    total_competitors = fetch_data(engine, "SELECT COUNT(*) AS total FROM Competitors")
    st.metric("Total Competitors 👥", total_competitors['total'][0])

    # Number of countries represented
    total_countries = fetch_data(engine, "SELECT COUNT(DISTINCT country_name) AS total FROM Competitors")
    st.metric("Total Countries Represented 📊", total_countries['total'][0])

    # Highest points scored by a competitor
    highest_points = fetch_data(engine, "SELECT MAX(points) AS highest FROM Competitors")
    st.metric("Highest Points Scored 🔝", highest_points['highest'][0])
