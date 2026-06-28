Spotify Listening History Analyzer 🎵
Overview

This project analyzes Spotify listening history using Python, Pandas, and Matplotlib. It processes exported Spotify data to uncover listening habits, identify favorite artists and songs, analyze skipped tracks, and visualize listening patterns.

Features
Analyze Spotify listening history
Discover top artists
Discover top songs
Analyze skipped vs. completed tracks
Visualize listening trends with charts
Save all visualizations as PNG images

Technologies Used:
Python
Pandas
Matplotlib

Project Structure:
spotify-listening-history-analyzer/
│
├── data/
│   ├── spotify_history.csv
│   └── spotify_data_dictionary.csv
│
├── Images/
│   ├── top_artists.png
│   ├── top_songs.png
│   ├── skip_analysis.png
│   ├── listening_by_day.png
│   └── listening_by_hour.png
│
├── analysis.py
├── requirements.txt
└── README.md





Installation:
git clone https://github.com/ven792/spotify-listening-history-analyzer.git

cd spotify-listening-history-analyzer

pip install -r requirements.txt


Run the Project
python analysis.py


Output

The program generates visualizations such as:

Top Artists
Top Songs
Listening Activity by Day
Listening Activity by Hour
Skip Analysis

All graphs are automatically saved inside the Images folder.


Skills Demonstrated:
-Data Analysis
-Data Cleaning
-Data Visualization
-Python Programming
-Working with CSV Files
-Exploratory Data Analysis (EDA)

Future Improvements:
-Interactive dashboard using Plotly
-Streamlit web application
-Genre analysis
-Monthly listening trends
-Spotify API integration






