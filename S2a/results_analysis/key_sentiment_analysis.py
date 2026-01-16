import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("data/spotify_sentiment.csv")

plt.figure(figsize=(12, 5))
sns.boxplot(
    data=df,
    x="key",
    y="sentiment_score"
)

plt.title("Lyrical Sentiment Score by Musical Key")
plt.xlabel("Musical Key (0 = C, 1 = C♯/D♭, … 11 = B)")
plt.ylabel("Sentiment Score")
plt.tight_layout()

plt.savefig("key_sentiment.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as key_sentiment.png")
plt.close()
