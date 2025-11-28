import os
from dotenv import load_dotenv
import pandas as pd
import lyricsgenius
import time

load_dotenv()

genius_token = os.getenv("GENIUS_ACCESS_TOKEN")
genius = lyricsgenius.Genius(genius_token)

print(genius_token)

df = pd.read_csv("mirdei.csv")

lyrics_list = []

# percorre dataset e tenta dar match com o genius
for index, row in df.iterrows():
    try:
        song = genius.search_song(row["Title"], row["Artist"])
        if song:
            lyrics_list.append(song.lyrics)
        else:
            lyrics_list.append(None)
        time.sleep(1)  # evitar bloqueio
    except:
        lyrics_list.append(None)

df["Lyrics"] = lyrics_list

# remove linhas sem lyrics
df = df.dropna(subset=["Lyrics"])

# guardar resultado
df.to_csv("mirdei_lyrics.csv", index=False)