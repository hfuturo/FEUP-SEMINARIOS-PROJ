import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("data/spotify_sentiment.csv")

sns.residplot(x=df["valence"], y=df["sentiment_score"], lowess=True)
plt.title("Residual Plot (Shows No Linear Relationship)")
plt.legend()

plt.savefig("valence_sentiment_residual.png", dpi=300, bbox_inches="tight")
print("Saved scatter plot as valence_sentiment_residual.png")
plt.close()