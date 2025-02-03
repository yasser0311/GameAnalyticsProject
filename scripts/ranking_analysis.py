import streamlit as st
import sqlite3
import pandas as pd
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

def ranking_analysis(engine):
    # Add background image
    image_file_path = "D:\\MTDM37\\MTDM37\\resources\\bg2.png"
    add_bg_image(image_file_path)

    # Path to the sports.db file in the data directory
    db_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'sports.db'))

    # Connect to SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    st.title("Ranking Analysis")

    # Use Streamlit columns to layout radio buttons and filters side by side
    col1, col2 = st.columns([1, 2])

    # Radio button for selecting different reports in col1
    with col1:
        report_type = st.radio("Select Report", [
            "Get All Competitors with Rank and Points",
            "Find Competitors Ranked in the Top 5",
            "List Competitors with No Rank Movement (Stable Rank)",
            "Get Total Points of Competitors from a Specific Country",
            "Count the Number of Competitors per Country",
            "Find Competitors with the Highest Points in the Current Week"
        ])

    # Filters and results in col2 based on selected report
    with col2:
        if report_type == "Get All Competitors with Rank and Points":
            query1 = '''
            SELECT 
                competitor_id, 
                competitor_name AS name, 
                rank, 
                points 
            FROM Competitors;
            '''
            result1 = pd.read_sql_query(query1, conn)
            st.subheader("Get all competitors with their rank and points:")
            st.dataframe(result1)

        elif report_type == "Find Competitors Ranked in the Top 5":
            query2 = '''
            SELECT 
                competitor_id, 
                competitor_name AS name, 
                rank, 
                points 
            FROM Competitors 
            WHERE rank <= 5
            ORDER BY rank ASC;
            '''
            result2 = pd.read_sql_query(query2, conn)
            st.subheader("Find competitors ranked in the top 5:")
            st.dataframe(result2)

        elif report_type == "List Competitors with No Rank Movement (Stable Rank)":
            query3 = '''
            SELECT 
                competitor_id, 
                competitor_name AS name, 
                rank, 
                points 
            FROM Competitors 
            WHERE movement = 0;
            '''
            result3 = pd.read_sql_query(query3, conn)
            st.subheader("List competitors with no rank movement (stable rank):")
            st.dataframe(result3)

        elif report_type == "Get Total Points of Competitors from a Specific Country":
            countries = ['All'] + list(pd.read_sql_query('SELECT DISTINCT country_name FROM Competitors;', conn)['country_name'])
            selected_country = st.selectbox('Select Country', countries)

            if selected_country == 'All':
                query4 = '''
                SELECT 
                    country_name, 
                    SUM(points) AS total_points 
                FROM Competitors 
                GROUP BY country_name;
                '''
                result4 = pd.read_sql_query(query4, conn)
            else:
                query4 = '''
                SELECT 
                    country_name, 
                    SUM(points) AS total_points 
                FROM Competitors 
                WHERE country_name = ? 
                GROUP BY country_name;
                '''
                result4 = pd.read_sql_query(query4, conn, params=(selected_country,))
            
            st.subheader("Get the total points of competitors from a specific country:")
            st.dataframe(result4)

        elif report_type == "Count the Number of Competitors per Country":
            query5 = '''
            SELECT 
                country_name, 
                COUNT(competitor_id) AS competitor_count 
            FROM Competitors 
            GROUP BY country_name;
            '''
            result5 = pd.read_sql_query(query5, conn)
            st.subheader("Count the number of competitors per country:")
            st.dataframe(result5)

        elif report_type == "Find Competitors with the Highest Points in the Current Week":
            query6 = '''
            SELECT 
                competitor_id, 
                competitor_name AS name, 
                rank, 
                points 
            FROM Competitors 
            ORDER BY points DESC
            LIMIT 1;
            '''
            result6 = pd.read_sql_query(query6, conn)
            st.subheader("Find competitors with the highest points in the current week:")
            st.dataframe(result6)

    # Close the connection
    conn.close()

# Example usage
if __name__ == "__main__":
    database_url = "sqlite:///D:\\MTDM37\\MTDM37\\data\\sports.db"
    engine = None  # Replace with your actual database engine
    ranking_analysis(engine)
