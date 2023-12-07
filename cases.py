"""
Fill in the blank exercises to perfect cases.
"""

from googletrans import Translator
import random
import spacy

nlp = spacy.load('de_core_news_sm')

def getRandomSentence():
    with open("sentences.txt", 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

while True:
    # Get random sentence
    randomSentence = getRandomSentence()

    # Translate this sentence
    translator = Translator()
    translation = translator.translate(randomSentence, src='en', dest='de')
    translated = translation.text

    # Process the text using the German language model
    doc = nlp(translated)
    answer = ""
    words = [token.text for token in doc]
    articles = ["DET"]
    adjectives = ["ADJ"]
    article_indices = [i for i, token in enumerate(doc) if token.pos_ in articles]
    adjective_indices = [i for i, token in enumerate(doc) if token.pos_ in adjectives]
    words_to_replace_indices = article_indices + adjective_indices
    if words_to_replace_indices:
        random_index = random.choice(words_to_replace_indices)
        answer = words[random_index]
        words[random_index] = "_______"
        modified_sentence = ' '.join(words)
        modified_sentence = modified_sentence.replace(" .", ".")

    # Print the original and the translated
    yourAnswer = input(randomSentence + " " + modified_sentence + " ")

    # Validate your answer
    if (yourAnswer.lower() == answer.lower()):
        print("Correct")
    else:
        print("Wrong: " + answer)
    print()
