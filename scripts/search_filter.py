import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Search and Filter Competitors
def search_and_filter(engine):
    with st.expander("Filter by Gender 🧑‍🤝‍🧑"):
        gender = st.selectbox("Select Gender", ['Male', 'Female'])
        filtered_gender = fetch_data(engine, f"SELECT * FROM Competitors WHERE gender = '{gender}'")
        st.dataframe(filtered_gender)
    
    with st.expander("Filter by Year 📅"):
        year = st.selectbox("Select Year", fetch_data(engine, "SELECT DISTINCT year FROM Competitors")['year'])
        filtered_year = fetch_data(engine, f"SELECT * FROM Competitors WHERE year = {year}")
        st.dataframe(filtered_year)

    with st.expander("Search by Competitor Name 👤"):
        name = st.text_input("Enter Competitor Name")
        if name:
            results = fetch_data(engine, f"SELECT * FROM Competitors WHERE competitor_name LIKE '%{name}%'")
            st.dataframe(results)
    
    with st.expander("Filter by Rank Range ↔️"):
        rank_range = st.slider("Select Rank Range", 1, 100, (1, 10))
        filtered_rank = fetch_data(engine, f"SELECT * FROM Competitors WHERE rank BETWEEN {rank_range[0]} AND {rank_range[1]}")
        st.dataframe(filtered_rank)
    
    with st.expander("Filter by Country 🌍"):
        country = st.selectbox("Select Country", fetch_data(engine, "SELECT DISTINCT country_name FROM Competitors")['country_name'])
        if country:
            results = fetch_data(engine, f"SELECT * FROM Competitors WHERE country_name = '{country}'")
            st.dataframe(results)
    
    with st.expander("Filter by Points Threshold 🔢"):
        points_threshold = st.slider("Select Points Threshold", 0, 10000, 500)
        filtered_points = fetch_data(engine, f"SELECT * FROM Competitors WHERE points >= {points_threshold}")
        st.dataframe(filtered_points)
