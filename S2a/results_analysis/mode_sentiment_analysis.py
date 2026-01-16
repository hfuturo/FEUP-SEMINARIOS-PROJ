import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("data/spotify_sentiment.csv")

df["mode_label"] = df["mode"].map({0: "Minor", 1: "Major"})

plt.figure(figsize=(7, 5))
sns.violinplot(
    data=df,
    x="mode_label",
    y="sentiment_score",
    inner="quartile"
)

plt.title("Lyrical Sentiment Score by Musical Mode")
plt.xlabel("Musical Mode")
plt.ylabel("Sentiment Score")
plt.tight_layout()

plt.savefig("mode_sentiment.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as mode_sentiment.png")
plt.close()