import streamlit as st
import pandas as pd

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Country-Wise Analysis
def country_analysis(engine):

    country_data = fetch_data(engine, """
    SELECT country_name, COUNT(*) AS total_competitors, AVG(points) AS average_points
    FROM Competitors
    GROUP BY country_name
    """)
    st.dataframe(country_data)
