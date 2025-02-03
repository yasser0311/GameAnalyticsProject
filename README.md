# Game Analytics Project

Project Title [Game Analytics: Unlocking Tennis Data with SportRadar API]

Welcome to the Game Analytics Project! This repository provides insightful data analysis and visualization for Tennis sports-related data.

## Project Overview
Game Analytics: Unlocking Tennis Data with SportRadar API project is dedicated to creating a robust solution for managing, visualizing, and analyzing sports competition data sourced from the Sportradar API. This application will handle the parsing of JSON data, organize the structured information in a relational database, and offer clear insights into tournaments, competition hierarchies, and specific event details. This project aims to support sports enthusiasts, analysts, and organizations in better understanding competition structures and trends while enabling interactive exploration of detailed event information. It is built using Streamlit for the front end and SQLite for the backend database.

## Setup Instructions
Follow these steps to set up and run the project:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yasser0311/GameAnalyticsProject.git
   cd GameAnalyticsProject
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run scripts/app.py
   ```

## Project Objectives
- **Data Collection:** Fetch and store data from sports APIs.
- **Data Analysis:** Provide insights into competitor performance, country representation, rankings, and more.
- **Visualization:** Create interactive visualizations and dashboards using Streamlit.
- **User Interaction:** Allow users to search, filter, and explore the data through an intuitive interface.

## Demo Walkthrough
1. **Homepage:**
   - Overview of the project and key statistics.

2. **Search & Filter Competitors:**
   - Ability to search and filter competitors by name, rank, country, points, gender, year, venue, and complex.

3. **Competitor Details:**
   - Detailed information about each competitor.

4. **Country Analysis:**
   - Analysis of competitors by country.

5. **Leaderboards:**
   - View top competitors in various categories.



