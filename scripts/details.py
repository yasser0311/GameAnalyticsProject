import streamlit as st
import pandas as pd

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Competitor Details Viewer
def competitor_details(engine):

    competitor_id = st.text_input("Enter Competitor ID 👤")
    if competitor_id:
        details = fetch_data(engine, f"""
        SELECT * FROM Competitors
        WHERE competitor_id = '{competitor_id}'
        """)
        st.dataframe(details)
