import sys
import os
import sqlite3
import streamlit as st
from sqlalchemy import create_engine

# Add the project root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set page configuration as the first Streamlit command
st.set_page_config(
    page_title="Game Analytics",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Create the database file if it doesn't exist using an absolute path
db_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/sports.db'))
if not os.path.exists(db_file_path):
    os.makedirs(os.path.dirname(db_file_path), exist_ok=True)
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Create the Competitors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Competitors (
        id INTEGER PRIMARY KEY,
        competitor_name TEXT,
        country_name TEXT,
        rank INTEGER,
        points INTEGER,
        gender TEXT,
        year INTEGER
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Replace with your actual database URL
DATABASE_URL = f'sqlite:///{db_file_path}'
engine = create_engine(DATABASE_URL)

# Correct the image path
image_path = os.path.join(os.path.dirname(__file__), "../resources/SRAD_BIG.png")

# Sidebar
st.sidebar.image(image_path, use_container_width=True)

# Import other modules
from scripts.dashboard import homepage
from scripts.search_filter import search_and_filter
from scripts.details import competitor_details
from scripts.country_analysis import country_analysis
from scripts.leaderboards import leaderboards

# Custom CSS for sidebar
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #F0F2F6;
        color: #2E2E2E;
        padding: 10px;
    }
    .sidebar .sidebar-content h1 {
        font-size: 24px;
        font-weight: bold;
        color: #FF5733;
    }
    .sidebar .sidebar-content .element-container {
        margin-bottom: 20px;
    }
    .sidebar .sidebar-content .stButton {
        font-size: 18px;
        color: #2E86C1;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("Menu")

# Define pages and their corresponding functions
pages = {
    "🏠 Homepage": homepage,
    "🔎 Search & Filter Competitors": search_and_filter,
    "👤 Competitor Details": competitor_details,
    "🌍 Country Analysis": country_analysis,
    "🏆 Leaderboards": leaderboards
}

# Navigation with radio buttons
page = st.sidebar.radio("Go to", list(pages.keys()))

# Main Content
st.title(page)
st.write(f"Welcome to the {page.split()[1].lower()} page!")
pages[page](engine)

# Custom CSS for better styling
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #dfe3e8;
    }
    </style>
    """, unsafe_allow_html=True)
