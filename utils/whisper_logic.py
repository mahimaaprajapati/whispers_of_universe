import json
import random

# Load all whispers from the JSON file
def load_whispers(filepath="data/whispers.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

# Get a random whisper
def get_random_whisper(whispers):
    return random.choice(whispers)

# Get whispers by tag
def get_whispers_by_tag(whispers, tag):
    return [w for w in whispers if tag.lower() in [t.lower() for t in w.get("tags", [])]]

# Get all available tags
def get_all_tags(whispers):
    tag_set = set()
    for w in whispers:
        for tag in w.get("tags", []):
            tag_set.add(tag)
    return sorted(list(tag_set))
