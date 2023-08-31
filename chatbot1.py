import json
from difflib import get_close_matches

def load_kb(file_path):
    with open(file_path,'r') as file:
        data : dict = json.load(file)
    
    return data

def find_match(userin , kb):

    matches = get_close_matches(userin,[i["question"] for i in kb["questions"]],n=1,cutoff=0.6)
    if matches:
        return matches[0]
    else:
        return None

def bot_reply(question,kb):

    for i in kb["questions"]:
        if i["question"] == question:
            return i["answer"]


def save_kb(data,file_path):
    with open(file_path,'w') as file:
        json.dump(data,file,indent=2)


def chatbot():
    kb : dict = load_kb("knowledge.json")

    while True:
        userin = input("you: ")

        if userin=="quit":
            break

        question = find_match(userin , kb)
        if question:
            answer = bot_reply(question,kb)
            print(f"bot: {answer}")
        else:
            print("bot: I cant understand can you please teach me")
            print("1)if you want to teach me type the answer below")
            print("2) if you dont want to teach please type skip")
            train = input("you: ")
            if train.lower()!="skip":
                kb["questions"].append({"question":userin , "answer":train})
                save_kb(kb,"knowledge.json")
                print("thank you for teaching me.")

if __name__ == "__main__":
    chatbot()
