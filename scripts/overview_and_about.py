import streamlit as st
import os
import base64

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
            background-color: rgba(255, 255, 255, 0.7); /* Adjust transparency as needed */
            border-radius: 10px;
            padding: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def overview_and_about():
    # Add background image
    bg_image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'bg2.png')
    add_bg_image(bg_image_path)

    # Path to the image of Mohammed Yasser
    image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'mohammed_yasser.jpg')

    st.title("Game Analytics: Unlocking Tennis Data with SportRadar API")
    
    # Resize the image and position it next to the name and About section using Streamlit columns
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(image_path, width=150)
        st.write("**M Mohammed Yasser**")
    with col2:
        st.write("""
        **About Me:**  
        Hello, I'm Yasser, an engaged Technical Advisor and an aspiring Data Scientist with over half a decade of experience in technical support across various industries. My journey through roles in client relationship management and problem resolution has honed my abilities to manage and excel in high-stress environments.
        I believe data is where the next wave of innovation lies, and I am currently enriching my knowledge with a Master's in Data Science. I have a knack for creating efficient workflows and ensuring tight security management. Whether it's driving customer satisfaction higher in B2B support or spearheading vulnerability assessments, I ensure precision and proactive solutions.
        I’ve developed strong skills in database querying, and data visualization, and maintain a clear focus on predictive analytics and algorithm optimization. Open to exploring opportunities where I can help your team make data-driven decisions, improve operations, and ensure customer success.
        """)

    st.header("Project Summary and Details")

    st.subheader("Skills Takeaway From This Project")
    st.write("- Python scripting\n"
             "- Data Collection using API integration\n"
             "- Data Management using SQL\n"
             "- Streamlit")

    st.subheader("Domain")
    st.write("Sports/Data Analytics")

    st.subheader("Problem Statement")
    st.write("The SportRadar Event Explorer project aims to develop a comprehensive solution for managing, "
             "visualizing, and analyzing sports competition data extracted from the Sportradar API. The application "
             "will parse JSON data, store structured information in a relational database, and provide intuitive "
             "insights into tournaments, competition hierarchies, and event details. This project is designed to "
             "assist sports enthusiasts, analysts, and organizations in understanding competition structures and "
             "trends while exploring detailed event-specific information interactively.")

    st.subheader("Technical Tags")
    st.write("- **Languages**: Python\n"
             "- **Database**: SQLite3\n"
             "- **Application**: Streamlit\n"
             "- **API Integration**: Sportradar API")

    st.subheader("Project Completed By")
    st.write("M Mohammed Yasser")

if __name__ == "__main__":
    overview_and_about()
