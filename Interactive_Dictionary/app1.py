import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:  # check for accronyms
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, N for no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn == "n":
            return "Sorry the word you entered is not in this dictionary"
        else:
            return "Sorry I did not understand that"
    else:
        return "Sorry that is not a valid word"


word = input("Enter word to look up: ")


output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
