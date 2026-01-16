import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("data/spotify_sentiment.csv")

df["mode_label"] = df["mode"].map({0: "Minor", 1: "Major"})

sentiment_counts = (
    df.groupby(["mode_label", "sentiment_label"])
    .size()
    .groupby(level=0)
    .apply(lambda x: x / x.sum())
    .unstack()
)

sentiment_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5)
)

plt.title("Distribution of Lyrical Sentiment Labels by Musical Mode")
plt.xlabel("Musical Mode")
plt.ylabel("Proportion of Songs")
plt.legend(title="Sentiment Label", bbox_to_anchor=(1.05, 1))
plt.tight_layout()

plt.savefig("mode_sentiment_barchart.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as mode_sentiment_barchart.png")
plt.close()