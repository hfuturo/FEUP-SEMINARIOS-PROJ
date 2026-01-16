import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("data/spotify_sentiment.csv")

plt.figure(figsize=(10, 6))
sns.kdeplot(
    x=df["valence"],
    y=df["sentiment_score"],
    fill=True,
    thresh=0.05,
    levels=30,
    cmap="viridis"
)
plt.title("Valence vs Sentiment Score (KDE Density Plot)")
plt.legend()

plt.savefig("valence_sentiment.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as valence_sentiment.png")
plt.close()