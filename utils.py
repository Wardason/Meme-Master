import json
import os
import random


async def get_momma_jokes():
    with open(os.path.join("data/jokes.json"), encoding="utf-8") as joke_file:
        jokes = json.load(joke_file)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult


