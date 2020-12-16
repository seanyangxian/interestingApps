import json


data = json.load(open("JSON+Data+Inside/data.json"))


def translate(word):
    return data[word]


def eng_dictionary():
    print(data['rain'])


def main():
    eng_dictionary()


if __name__ == '__main__':
    main()
