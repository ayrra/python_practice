import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yOrN =  input("Did you mean %s instead? Enter Y if yes or N if no." % get_close_matches(word, data.keys())[0])
        if yOrN == "Y" or yOrN == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yOrN == "N" or yOrN == "n":
            return "The word does not exist."
        else:
            return "Invalid input."    
    else:
        return "The word does not exist."

word = input("Enter a word to return its definition: ")

out = translate(word)

if type(out) == list:
    for definition in out:
        print(definition)
else:
    print(out)