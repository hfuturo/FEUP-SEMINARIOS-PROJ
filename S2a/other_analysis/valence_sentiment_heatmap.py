import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("data/spotify_sentiment.csv")

corr = df[["valence", "sentiment_score"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.legend()

plt.savefig("valence_sentiment_heatmap.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as valence_sentiment_heatmap.png")
plt.close()