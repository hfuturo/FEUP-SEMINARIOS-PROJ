import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/spotify_sentiment.csv")

# pearson correlation
pearson_corr = df["valence"].corr(df["sentiment_score"])
print("Pearson Correlation (valence vs sentiment_score):", pearson_corr)

# scatter plot with regression line
plt.figure(figsize=(10, 6))

plt.scatter(df["valence"], df["sentiment_score"], alpha=0.6, s=20, label="Data Points")

m, b = np.polyfit(df["valence"], df["sentiment_score"], 1)
plt.plot(df["valence"], m * df["valence"] + b, label="Trend Line")

plt.xlabel("Valence")
plt.ylabel("Sentiment Score")
plt.title("Valence vs Sentiment Score")
plt.grid(True)
plt.legend()

plt.savefig("valence_sentiment_scatter.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as valence_sentiment_scatter.png")
plt.close()