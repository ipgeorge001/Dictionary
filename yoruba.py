# COS 101 Individual Project
# English to Yoruba Dictionary

yoruba_dictionary = {
    "water": "omi",
    "food": "ounje",
    "house": "ile",
    "book": "iwe",
    "school": "ile-iwe",
    "sun": "oorun",
    "moon": "osupa",
    "man": "okunrin",
    "woman": "obinrin",
    "child": "omo",
    "love": "ife",
    "money": "owo",
    "road": "ona",
    "fire": "ina",
    "rain": "ojo",
    "friend": "ore",
    "family": "ebi",
    "tree": "igi",
    "market": "oja",
    "king": "oba"
}

print("English to Yoruba Dictionary")

word = input("Enter an English word: ").lower()

if word in yoruba_dictionary:
    print("Yoruba translation:", yoruba_dictionary[word])
else:
    print("Sorry, word not found in the dictionary.")
