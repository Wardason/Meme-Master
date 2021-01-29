import json
import os
import random


async def get_momma_jokes():
    with open(os.path.join("data/jokes.json"), encoding="utf-8") as joke_file:
        jokes = json.load(joke_file)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult


async def get_song():
    with open(os.path.join("data/songs.json"), encoding="utf-8") as song_file:
        songs = json.load(song_file)
        songs = songs["songs"]
    songs = random.choice(list(songs))
    return songs
