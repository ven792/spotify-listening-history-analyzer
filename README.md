# spotify-listening-history-analyzer
Analyze Spotify listening history using Python, Pandas, and Matplotlib.

# 🎵 Spotify Listening History Analyzer

Analyze Spotify listening history using **Python**, **Pandas**, and **Matplotlib** to discover listening habits, favorite artists, top songs, and playback trends.


This project analyzes exported Spotify listening history data and transforms it into meaningful insights using data analysis and visualization techniques.

Using **Pandas**, the dataset is cleaned and explored, while **Matplotlib** is used to generate charts that reveal listening behavior over time.

 ✨ Features

- 🎧 Top Artists Analysis
- 🎵 Top Songs Analysis
- ⏰ Listening Activity by Hour
- 📅 Listening Activity by Day
- ⏭️ Skip Analysis
- 📊 Data Visualization with Matplotlib

🛠 Technologies Used

- Python
- Pandas
- Matplotlib

 📂 Dataset

The project uses Spotify listening history exported as CSV files.


data/
├── spotify_history.csv
└── spotify_data_dictionary.csv
```
 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ven792/spotify-listening-history-analyzer.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python analysis.py
```



## 📁 Project Structure

```
spotify-listening-history-analyzer/
│
├── Images/
├── data/
├── analysis.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📊 Results

## 🎤 Top Artists

![Top Artists](Images/top_artists.png)

Displays the artists with the highest number of plays.

---

## 🎵 Top Songs

![Top Songs](Images/top_songs.png)

Shows the songs listened to most frequently.

---

## ⏰ Listening by Hour

![Listening by Hour](Images/listening_by_hour.png)

Visualizes the hours of the day when listening activity is highest.

---

## 📅 Listening by Day

![Listening by Day](Images/listening_by_day.png)

Shows listening activity across different days of the week.

---

## ⏭️ Skip Analysis

![Skip Analysis](Images/skip_analysis.png)

Compares skipped tracks with completed tracks.

---

# 📚 What I Learned

Through this project I learned how to:

- Read CSV datasets using Pandas
- Clean and manipulate data
- Perform exploratory data analysis
- Create visualizations using Matplotlib
- Organize a Python project
- Document projects using Markdown

---

# 🚀 Future Improvements

- Interactive dashboards using Plotly
- Monthly listening trends
- Genre analysis
- Spotify Web API integration
- Machine Learning recommendations

---

## 📄 License

This project is licensed under the MIT License.
