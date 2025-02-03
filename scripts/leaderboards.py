import streamlit as st
import pandas as pd
import base64

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Function to add custom CSS
def add_custom_css():
    image_file_path = "D:\\MTDM37\\MTDM37\\resources\\tennis4.jpg"
    with open(image_file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
        }}
        .main {{
            background-color: rgba(255, 255, 255, 0.1); /* More transparent main content */
            border-radius: 10px;
            padding: 10px;
        }}
        .stButton button {{
            background-color: #4CAF50;
            color: white;
        }}
        .stExpander {{
            border: none;
        }}
        .stSelectbox, .stSlider, .stTextInput {{
            border: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Leaderboards
def leaderboards(engine):
    # Add custom CSS
    add_custom_css()

    # Top-ranked competitors
    st.title("Top-Ranked Competitors🏅")
    top_ranked = fetch_data(engine, "SELECT * FROM Competitors ORDER BY rank ASC LIMIT 10")
    st.dataframe(top_ranked)

    # Competitors with the highest points
    st.title("Competitors with Highest Points 🤼‍♂️")
    highest_points = fetch_data(engine, "SELECT * FROM Competitors ORDER BY points DESC LIMIT 10")
    st.dataframe(highest_points)

# Example usage
if __name__ == "__main__":
    # Assuming your database engine is created and passed to the leaderboards function
    database_url = "sqlite:///D:\\MTDM37\\MTDM37\\data\\sports.db"
    engine = create_engine(database_url)
    leaderboards(engine)
