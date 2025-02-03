# Game Analytics Project

Project Title [Game Analytics: Unlocking Tennis Data with SportRadar API]

Welcome to the Game Analytics Project! This repository provides insightful data analysis and visualization for a variety of sports-related data.

## Project Overview
The SportRadar Event Explorer project is dedicated to creating a robust solution for managing, visualizing, and analyzing sports competition data sourced from the Sportradar API. This application will handle the parsing of JSON data, organize the structured information in a relational database, and offer clear insights into tournaments, competition hierarchies, and specific event details. This project aims to support sports enthusiasts, analysts, and organizations in better understanding competition structures and trends while enabling interactive exploration of detailed event information. It is built using Streamlit for the front end and SQLite for the backend database.

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

## Features

- **Navigation Menu**: Provides easy access to different sections:
  1. **Home**:
  - Displays a welcoming message and key statistics.
  - Total Competitors: 1000
  - Total Countries Represented: 79
  - Highest Points Scored: 10750
  2. **Search & Filter**
  - Ability to search and filter competitors by name, rank, country, points, gender, year, venue, and complex.
  - Allows users to filter and search competitors based on various criteria such as gender, year, country, name, points threshold, and rank range.
  3. **Leaderboard Analysis**
  - Display Country-wise Analysis, Top-Ranked Competitors and Competitors with Highest Points
  4. **Competition Analysis**
  - Display Competitions List, Competition Stats, Doubles Competitions, Search by Category and Analyze Distribution of Competition Types
  5. **Complexes Analysis**
  - Display List Venues with Complex Names, Count Venues in Each Complex, Venues in a Specific Country, Identify Venues and Timezones, Find Complexes with More Than One Venue, List Venues Grouped by Country and Venues in a Specific Complex 
  6. **Competitor Analysis**
  - Get All Competitors with Rank and Points, Find Competitors Ranked in the Top 5, List Competitors with No Rank Movement (Stable Rank), Get Total Points of Competitors from a Specific Country, Count the Number of Competitors per Country and Find Competitors with the Highest Points in the Current Week
  7. **Overview and About**
  -Project Summary and Details, Skills Takeaway From This Project, Domain, Technical tags and Problem Statement
