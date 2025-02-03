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

def competition_analysis(engine):
    # Path to the sports.db file in the data directory
    db_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'sports.db'))

    # Add background image
    image_file_path = "D:\\MTDM37\\MTDM37\\resources\\bg2.png"
    add_bg_image(image_file_path)

    # Connect to SQLite database
    conn = sqlite3.connect(db_file_path)

    # List all competitions along with their category name
    query1 = '''
    SELECT 
        c.id AS competition_id, 
        c.name AS competition_name, 
        c.type, 
        c.gender, 
        c.category_name 
    FROM Competitions c;
    '''
    result1 = pd.read_sql_query(query1, conn)

    # Close the connection
    conn.close()

    # Streamlit UI
    st.title("Competition Analysis")

    # Use Streamlit columns to layout radio buttons and filters side by side
    col1, col2 = st.columns([1, 2])

    # Radio button for selecting different reports in col1
    with col1:
        report_type = st.radio("Select Report", [
            "Competitions List",
            "Competition Stats",
            "Doubles Competitions",
            "Search by Category",
            "Analyze Distribution of Competition Types"
        ])

    # Filters and results in col2 based on selected report
    with col2:
        if report_type == "Competitions List":
            st.header("Competitions List")
            st.text("View all competitions along with their category name")

            # Filter by category name with 'All' option
            categories = ['All'] + list(result1['category_name'].unique())
            selected_category = st.selectbox('Select Category', categories)

            if selected_category == 'All':
                filtered_result1 = result1
            else:
                filtered_result1 = result1[result1['category_name'] == selected_category]
            
            st.dataframe(filtered_result1)

        elif report_type == "Competition Stats":
            st.header("Competition Stats")
            st.text("Count the number of competitions in each category")
            query2 = '''
            SELECT 
                c.category_name, 
                COUNT(c.id) AS competition_count 
            FROM Competitions c
            GROUP BY c.category_name;
            '''
            conn = sqlite3.connect(db_file_path)
            result2 = pd.read_sql_query(query2, conn)
            conn.close()
            
            st.dataframe(result2)

        elif report_type == "Doubles Competitions":
            st.header("Doubles Competitions")
            st.text("Find all competitions of type 'doubles'")
            
            # Add 'All' filter for doubles competitions
            categories = ['All'] + list(result1['category_name'].unique())
            selected_category_doubles = st.selectbox('Select Category for Doubles', categories)

            conn = sqlite3.connect(db_file_path)
            if selected_category_doubles == 'All':
                query3 = '''
                SELECT 
                    id AS competition_id, 
                    name AS competition_name, 
                    type, 
                    gender, 
                    category_id 
                FROM Competitions 
                WHERE type = 'doubles';
                '''
                result3 = pd.read_sql_query(query3, conn)
            else:
                query3 = '''
                SELECT 
                    id AS competition_id, 
                    name AS competition_name, 
                    type, 
                    gender, 
                    category_id 
                FROM Competitions 
                WHERE type = 'doubles' AND category_name = ?;
                '''
                result3 = pd.read_sql_query(query3, conn, params=(selected_category_doubles,))
            
            conn.close()
            st.dataframe(result3)

        elif report_type == "Search by Category":
            st.header("Search by Category")
            st.text("Get competitions that belong to a specific category (e.g., ITF Men)")
            categories = ['All'] + list(result1['category_name'].unique())
            selected_category_for_query4 = st.selectbox('Select a specific Category', categories)

            conn = sqlite3.connect(db_file_path)
            if selected_category_for_query4 == 'All':
                query4 = '''
                SELECT 
                    id AS competition_id, 
                    name AS competition_name, 
                    type, 
                    gender, 
                    category_id 
                FROM Competitions
                '''
                result4 = pd.read_sql_query(query4, conn)
            else:
                query4 = '''
                SELECT 
                    id AS competition_id, 
                    name AS competition_name, 
                    type, 
                    gender, 
                    category_id 
                FROM Competitions 
                WHERE category_name = ?;
                '''
                result4 = pd.read_sql_query(query4, conn, params=(selected_category_for_query4,))
            
            conn.close()
            st.dataframe(result4)

        elif report_type == "Analyze Distribution of Competition Types":
            st.header("Analyze Competition Types")
            st.text("Analyze the distribution of competition types by category")
            
            # Add 'All' filter for analyzing distribution of competition types
            categories = ['All'] + list(result1['category_name'].unique())
            selected_category_distribution = st.selectbox('Select Category for Distribution', categories)

            conn = sqlite3.connect(db_file_path)
            if selected_category_distribution == 'All':
                query5 = '''
                SELECT 
                    c.category_name, 
                    c.type, 
                    COUNT(c.id) AS competition_count 
                FROM Competitions c
                GROUP BY c.category_name, c.type;
                '''
                result5 = pd.read_sql_query(query5, conn)
            else:
                query5 = '''
                SELECT 
                    c.category_name, 
                    c.type, 
                    COUNT(c.id) AS competition_count 
                FROM Competitions c
                WHERE category_name = ?
                GROUP BY c.category_name, c.type;
                '''
                result5 = pd.read_sql_query(query5, conn, params=(selected_category_distribution,))
            
            conn.close()
            st.dataframe(result5)

# Example usage
if __name__ == "__main__":
    database_url = "sqlite:///D:\\MTDM37\\MTDM37\\data\\sports.db"
    engine = None  # Replace with your actual database engine
    competition_analysis(engine)
