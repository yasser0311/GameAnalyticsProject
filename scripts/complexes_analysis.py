import sqlite3
import pandas as pd
import streamlit as st
import os
import base64

def fetch_data(query, db_file_path, params=()):
    conn = sqlite3.connect(db_file_path)
    result = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return result

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

def complexes_analysis(engine):
    # Add background image
    image_file_path = "D:\\MTDM37\\MTDM37\\resources\\bg2.png"
    add_bg_image(image_file_path)

    # Path to the sports.db file in the data directory
    db_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'sports.db'))

    # Connect to SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    st.title("Tennis Venues Analysis")

    # Create the Complexes Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Complexes (
        complex_id TEXT PRIMARY KEY,
        complex_name TEXT NOT NULL
    )
    ''')

    # Create the Venues Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Venues (
        venue_id TEXT PRIMARY KEY,
        venue_name TEXT NOT NULL,
        city_name TEXT NOT NULL,
        country_name TEXT NOT NULL,
        country_code CHAR(3) NOT NULL,
        timezone TEXT NOT NULL,
        complex_id TEXT,
        FOREIGN KEY (complex_id) REFERENCES Complexes(complex_id)
    )
    ''')

    # Use Streamlit columns to layout radio buttons and filters side by side
    col1, col2 = st.columns([1, 2])

    # Radio button for selecting different reports in col1
    with col1:
        report_type = st.radio("Select Report", [
            "List Venues with Complex Names",
            "Count Venues in Each Complex",
            "Venues in a Specific Country",
            "Identify Venues and Timezones",
            "Find Complexes with More Than One Venue",
            "List Venues Grouped by Country",
            "Venues in a Specific Complex"
        ])

    # Filters and results in col2 based on selected report
    with col2:
        if report_type == "List Venues with Complex Names":
            query1 = '''
            SELECT 
                v.venue_id, 
                v.venue_name, 
                v.city_name, 
                v.country_name, 
                v.timezone, 
                c.complex_name 
            FROM Venues v
            JOIN Complexes c ON v.complex_id = c.complex_id;
            '''
            result1 = pd.read_sql_query(query1, conn)
            st.subheader("List all venues along with their associated complex name:")
            st.dataframe(result1)

        elif report_type == "Count Venues in Each Complex":
            query2 = '''
            SELECT 
                c.complex_name, 
                COUNT(v.venue_id) AS venue_count 
            FROM Venues v
            JOIN Complexes c ON v.complex_id = c.complex_id
            GROUP BY c.complex_name;
            '''
            result2 = pd.read_sql_query(query2, conn)
            st.subheader("Count the number of venues in each complex:")
            st.dataframe(result2)

        elif report_type == "Venues in a Specific Country":
            countries = ['All'] + list(pd.read_sql_query('SELECT DISTINCT country_name FROM Venues;', conn)['country_name'])
            selected_country = st.selectbox('Select Country', countries)

            if selected_country == 'All':
                query3 = '''
                SELECT 
                    venue_id, 
                    venue_name, 
                    city_name, 
                    country_name, 
                    country_code, 
                    timezone, 
                    complex_id 
                FROM Venues;
                '''
                result3 = pd.read_sql_query(query3, conn)
            else:
                query3 = '''
                SELECT 
                    venue_id, 
                    venue_name, 
                    city_name, 
                    country_name, 
                    country_code, 
                    timezone, 
                    complex_id 
                FROM Venues 
                WHERE country_name = ?;
                '''
                result3 = pd.read_sql_query(query3, conn, params=(selected_country,))
            
            st.subheader("Get details of venues in a specific country:")
            st.dataframe(result3)

        elif report_type == "Identify Venues and Timezones":
            query4 = '''
            SELECT 
                venue_id, 
                venue_name, 
                timezone 
            FROM Venues;
            '''
            result4 = pd.read_sql_query(query4, conn)
            st.subheader("Identify all venues and their timezones:")
            st.dataframe(result4)

        elif report_type == "Find Complexes with More Than One Venue":
            query5 = '''
            SELECT 
                c.complex_name, 
                COUNT(v.venue_id) AS venue_count 
            FROM Venues v
            JOIN Complexes c ON v.complex_id = c.complex_id
            GROUP BY c.complex_name
            HAVING COUNT(v.venue_id) > 1;
            '''
            result5 = pd.read_sql_query(query5, conn)
            st.subheader("Find complexes that have more than one venue:")
            st.dataframe(result5)

        elif report_type == "List Venues Grouped by Country":
            query6 = '''
            SELECT 
                country_name, 
                COUNT(venue_id) AS venue_count 
            FROM Venues 
            GROUP BY country_name;
            '''
            result6 = pd.read_sql_query(query6, conn)
            st.subheader("List venues grouped by country:")
            st.dataframe(result6)

        elif report_type == "Venues in a Specific Complex":
            complexes = ['All'] + list(pd.read_sql_query('SELECT DISTINCT complex_name FROM Complexes;', conn)['complex_name'])
            selected_complex = st.selectbox('Select Complex', complexes)

            if selected_complex == 'All':
                query7 = '''
                SELECT 
                    v.venue_id, 
                    v.venue_name, 
                    v.city_name, 
                    v.country_name, 
                    v.timezone 
                FROM Venues v
                JOIN Complexes c ON v.complex_id = c.complex_id;
                '''
                result7 = pd.read_sql_query(query7, conn)
            else:
                query7 = '''
                SELECT 
                    v.venue_id, 
                    v.venue_name, 
                    v.city_name, 
                    v.country_name, 
                    v.timezone 
                FROM Venues v
                JOIN Complexes c ON v.complex_id = c.complex_id
                WHERE c.complex_name = ?;
                '''
                result7 = pd.read_sql_query(query7, conn, params=(selected_complex,))
            
            st.subheader("Find all venues for a specific complex:")
            st.dataframe(result7)

    # Close the connection
    conn.close()

# Example usage
if __name__ == "__main__":
    database_url = "sqlite:///D:\\MTDM37\\MTDM37\\data\\sports.db"
    engine = None  # Replace with your actual database engine
    complexes_analysis(engine)
