import os
from dotenv import load_dotenv
import pandas as pd
import lyricsgenius
import time
import re

load_dotenv()

genius_token = os.getenv("GENIUS_ACCESS_TOKEN")
genius = lyricsgenius.Genius(genius_token)

print(genius_token)

def clean_lyrics(text):
    if pd.isna(text):
        return text
    
    # Remove annotations in square brackets
    text = re.sub(r'\[.*?\]', '', text)
    
    # Remove blank lines and extra newlines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    text = ' '.join(lines)
    
    return text

df = pd.read_csv("spotify.csv")

lyrics_list = []
rows_list = []
genre_counter = 0
total_genres = df["track_genre"].nunique()

for genre in df["track_genre"].unique():

    subset = df[df["track_genre"] == genre]
    artists = set()
    songs_collected = 0

    for index, row in subset.iterrows():
        if songs_collected == 1:
            break

        artist = row["artists"].split(";")[0]

        if artist in artists:
            continue

        try:
            song = genius.search_song(row["track_name"], artist)

            if song:
                artists.add(artist)
                rows_list.append(row)
                lyrics_list.append(song.lyrics)
                songs_collected += 1
            
            time.sleep(1)

        except Exception as e:
            print(e)

    genre_counter += 1
    print(f"Collected {songs_collected} songs for genre '{genre}'. {genre_counter}/{total_genres}")

processed_df = pd.DataFrame(rows_list).copy()
processed_df["Lyrics"] = lyrics_list
processed_df["Lyrics"] = processed_df["Lyrics"].apply(clean_lyrics)
processed_df.to_csv("spotify_lyrics.csv", index=False)
