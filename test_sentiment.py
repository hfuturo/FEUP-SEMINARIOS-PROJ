import pandas as pd
from transformers import pipeline
from tqdm import tqdm

pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

df = pd.read_csv('spotify_lyrics.csv')

if 'Lyrics' not in df.columns:
    print("Error: 'Lyrics' column not found in CSV file")
    print(f"Available columns: {df.columns.tolist()}")
    exit(1)

print(f"Found {len(df)} songs to analyze")

sentiments = []
labels = []
scores = []

print("Analyzing sentiments...")
for idx, lyrics in enumerate(tqdm(df['Lyrics'], desc="Processing")):
    if pd.isna(lyrics) or lyrics == '':
        sentiments.append(None)
        labels.append(None)
        scores.append(None)
    else:
        # Truncate lyrics if too long (transformers have token limits)
        lyrics_text = str(lyrics)[:512]
        result = pipe(lyrics_text)[0]
        labels.append(result['label'])
        scores.append(result['score'])

df['sentiment_label'] = labels
df['sentiment_score'] = scores

cols = [col for col in df.columns if col != 'Lyrics'] + ['Lyrics']
df = df[cols]

output_file = 'spotify_sentiment.csv'
df.to_csv(output_file, index=False)
print(f"\nResults saved to {output_file}")

print("\n=== Sentiment Analysis Results ===")
print(f"Total songs analyzed: {len(df)}")
print(f"\nSentiment distribution:")
print(df['sentiment_label'].value_counts())
print(f"\nAverage confidence score: {df['sentiment_score'].mean():.4f}")

print("\n=== Sample Results ===")
for i in range(min(5, len(df))):
    print(f"\nSong: {df.iloc[i]['track_name']} - {df.iloc[i]['artists']}")
    print(f"Sentiment: {df.iloc[i]['sentiment_label']} (confidence: {df.iloc[i]['sentiment_score']:.4f})")
    print(f"Lyrics preview: {str(df.iloc[i]['Lyrics'])[:100]}...")
