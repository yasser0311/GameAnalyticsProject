import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import base64

# Function to fetch data from the database
def fetch_data(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Function to add custom CSS
def add_custom_css():
    image_file_path = "D:\\MTDM37\\MTDM37\\resources\\tennis2.jpg"
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
            background-color: rgba(255, 255, 255, 0.5); /* More transparent main content */
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

# Search and Filter Competitors
def search_and_filter(engine):
    # Add custom CSS
    add_custom_css()

    # Add a reset button
    if st.button("Reset Filters"):
        st.session_state['gender'] = 'All'
        st.session_state['country'] = 'All'

    # Base query
    query = "SELECT * FROM Competitors WHERE 1=1"
    
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Filter by Gender 🧑‍🤝‍🧑"):
            gender = st.selectbox("Select Gender", ['All', 'men', 'women', 'mixed'], key='gender')
            if gender != 'All':
                query += f" AND gender = '{gender}'"
    
    with col2:
        with st.expander("Filter by Year 📅"):
            years = fetch_data(engine, "SELECT DISTINCT year FROM Competitors")['year']
            year = st.selectbox("Select Year", years)
            if year:
                query += f" AND year = {year}"
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Filter by Country 🌍")
        countries = ['All'] + fetch_data(engine, "SELECT DISTINCT country_name FROM Competitors")['country_name'].tolist()
        country = st.selectbox("Select Country", countries, key='country')
        if country != 'All':
            query += f" AND country_name = '{country}'"
    
    with col4:
        st.subheader("Search by Competitor Name 👤")
        name = st.text_input("Enter Competitor Name")
        if name:
            query += f" AND competitor_name LIKE '%{name}%'"

    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Filter by Points Threshold 🔢")
        points_threshold = st.slider("Select Points Threshold", 0, 10000, 500)
        if points_threshold:
            query += f" AND points >= {points_threshold}"
    
    with col6:
        st.subheader("Filter by Rank Range ↔️")
        rank_range = st.slider("Select Rank Range", 1, 100, (1, 10))
        if rank_range:
            query += f" AND rank BETWEEN {rank_range[0]} AND {rank_range[1]}"
    
    filtered_data = fetch_data(engine, query)
    st.dataframe(filtered_data)

# Example usage
if __name__ == "__main__":
    # Assuming your database URL
    database_url = "sqlite:///D:\\MTDM37\\MTDM37\\data\\sports.db"
    engine = create_engine(database_url)
    search_and_filter(engine)
