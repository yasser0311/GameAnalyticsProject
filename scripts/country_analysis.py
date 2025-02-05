import streamlit as st
import pandas as pd
import altair as alt

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Country-Wise Analysis
def country_analysis(engine):
    st.title("Country-Wise Analysis🌍")
    country_data = fetch_data(engine, """
    SELECT country_name, COUNT(*) AS total_competitors, AVG(points) AS average_points
    FROM Competitors
    GROUP BY country_name
    """)
    
    # Create a bar chart using Altair
    chart = alt.Chart(country_data).mark_bar().encode(
        x='country_name:N',
        y='total_competitors:Q',
        color='average_points:Q',
        tooltip=['country_name', 'total_competitors', 'average_points']
    ).properties(
        width=600,
        height=400,
        title="Total Competitors and Average Points by Country"
    )
    
    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)


