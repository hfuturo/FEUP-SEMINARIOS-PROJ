import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/spotify_sentiment.csv")

plt.figure(figsize=(10, 6))
plt.hexbin(df["valence"], df["sentiment_score"], gridsize=40, cmap='Blues')
plt.colorbar(label='Point Density')
plt.xlabel("Valence")
plt.ylabel("Sentiment Score")
plt.title("Valence vs Sentiment Score (Hexbin Density Plot)")
plt.grid(False)
plt.legend()

plt.savefig("valence_sentiment_hexbin.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as valence_sentiment_scatter.png")
plt.close()