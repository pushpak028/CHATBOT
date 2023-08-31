import load_json
import json
from difflib import get_close_matches
import random

def find_tag(tags,data):

    tags = get_close_matches(tags,[i["tag"] for i in data["intents"]],n=1,cutoff=0.6)
    if tags:
        for i in data["intents"]:
            if i["tag"]==tags[0]:
                return random.choice(i["responses"])


def chatbot():
    data:dict = load_json.load1("intents.json")
    tag:list = [i["tag"] for i in data["intents"] ]
    for i in range(len(tag)):
        print(i,".",tag[i])
    while True:
        print("enter quit to exit")
        tags = input("bot enter a tag: ")
        if tags.lower() == "quit":
            break
        answer = find_tag(tags,data)
        print(answer)


if __name__ == "__main__":
    chatbot()