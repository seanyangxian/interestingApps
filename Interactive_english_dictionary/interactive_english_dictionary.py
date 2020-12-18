import json
from difflib import get_close_matches

DATA = json.load(open("JSON+DATA+Inside/DATA.json"))


def ask_for_similarity(word):
    display_suggested_words(word)
    user_decision = input(
        f"If yes, please enter the associated item number of the words. Enter N if no wanted matches.\n")
    if user_decision == 'N':
        return F"Sorry, {word} does not exist"
    try:
        user_decision = int(user_decision)
    except ValueError:
        return "Invalid input option."
    else:
        if 1 <= user_decision <= len(get_close_matches(word, DATA.keys())):
            return DATA[get_close_matches(word, DATA.keys())[user_decision - 1]]
        else:
            return "Invalid input option."


def display_suggested_words(word):
    print(f"I am sorry but we can't find a perfect match for {word}.\nDo you mean: ")
    for index, item in enumerate(get_close_matches(word, DATA.keys())[0:3], 1):
        print(f"{index}. {item}")


def translate(word):
    word = word.strip().lower()
    if word in DATA:
        return DATA[word]
    elif len(get_close_matches(word, DATA.keys())) > 0:
        return ask_for_similarity(word)
    else:
        return "Sorry the word doesn't exist, please try again."


def display_translation_result(definition):
    if type(definition) == list and len(definition) > 1:
        for index, item in enumerate(definition,1):
            print(f"Definition {index}.\n{item}")
    else:
        print(*definition)


def eng_dictionary():
    word = input("Please enter a word you wanted to translate:\n")
    display_translation_result(translate(word))


def main():
    eng_dictionary()


if __name__ == '__main__':
    main()
