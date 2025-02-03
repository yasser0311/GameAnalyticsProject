import streamlit as st
import pandas as pd
import base64

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Function to add a background image
def add_bg_image(image_file_path):
    with open(image_file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
        }}
        .stApp > div {{
            background-color: rgba(255, 255, 255, 0.2); /* More transparent background for the main content */
            border-radius: 10px;
            padding: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Homepage Dashboard
def homepage(engine):
    # Add your image file path
    image_file_path = "D:\\MTDM37\\MTDM37\\resources\\tennis.jpg"

    # Add background image
    add_bg_image(image_file_path)
    
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

# Add your Streamlit code here to fetch data and display the dashboard
if __name__ == "__main__":
    # Replace with your actual database engine
    engine = None
    homepage(engine)
