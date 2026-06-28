import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/spotify_history.csv")

skip_counts = df["skipped"].value_counts()

plt.figure(figsize=(6,6))

skip_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Skipped vs Not Skipped")

plt.ylabel("")

plt.savefig("Images/skip_analysis.png")

plt.show()

