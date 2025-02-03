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

# Create the database file path
db_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sports.db')
if not os.path.exists(db_file_path):
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
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
image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'tennis.jpg')

# Sidebar image
sidebar_image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'SRAD_BIG.png')
st.sidebar.image(sidebar_image_path, use_container_width=True)

# Import other modules
from scripts.dashboard import homepage as home
from scripts.search_filter import search_and_filter
from scripts.details import competitor_details
from scripts.country_analysis import country_analysis
from scripts.leaderboards import leaderboards
from scripts.competition_analysis import competition_analysis
from scripts.complexes_analysis import complexes_analysis
from scripts.ranking_analysis import ranking_analysis
from scripts.overview_and_about import overview_and_about

# Custom CSS for page background
st.markdown(f"""
    <style>
    .reportview-container {{
        background: url("{image_path}") no-repeat center center fixed;
        background-size: cover;
    }}
    .main {{
        background-color: rgba(255, 255, 255, 0.5);
    }}
    .sidebar .sidebar-content h1 {{
        font-size: 24px;
        font-weight: bold;
        color: #6A0572;
    }}
    .sidebar .sidebar-content .element-container {{
        margin-bottom: 20px;
    }}
    .sidebar .sidebar-content .stButton button {{
        font-size: 18px;
        color: #6A0572;
        background-color: #E4A6F0;
    }}
    .stMetric {{
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("Menu")

# Define pages and their corresponding functions
pages = {
    "🏠 Home": home,
    "🔎 Search & Filter ": search_and_filter,
    "🏆 Leaderboard Analysis": lambda engine: (country_analysis(engine), st.write("---"), leaderboards(engine)),
    "📊 Competition Analysis": competition_analysis,
    "🏟️ Complexes Analysis": complexes_analysis,
    "🎖️ Competitor Analysis": ranking_analysis,
    "📈 Overview and About": overview_and_about
}

# Navigation with radio buttons
page = st.sidebar.radio("Navigate to", list(pages.keys()))

# Main Content
st.title(page)
st.write(f"Welcome to the {page.split()[1].lower()} page!")

if page == "🔎 Search & Filter Competitors":
    search_and_filter(engine)
    st.write("---")
    competitor_details(engine)
elif page == "🏆 Leaderboard Analysis":
    country_analysis(engine)
    st.write("---")
    leaderboards(engine)
elif page == "📈 Overview and About":
    overview_and_about()
else:
    pages[page](engine)
