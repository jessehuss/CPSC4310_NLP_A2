# Name: Jesse Huss
# ID: 001209444
# Project: Assignment 2 Q3
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
import random

input(
    "Welcome !\n"
    "This program uses two different language models (bigram and trigram)\n" +
    "to generate random sentences based on starting word(s) provided by you and using the reuters corpus.\n" +
    "We use a random probability threshold to ensure a good randomness and probability of creating a sentence.\n"+
    "Press enter to continue...\n\n")

# MODEL PLACEHOLDER
model = defaultdict(lambda: defaultdict(lambda: 0))

# ASK USER FOR MODEL TYPE: BIGRAM/TRIGRAM
valid_input = False
model_type = ""
while not valid_input:
    model_type = input("Please specify which model you would like to use ('bigram' or 'trigram'):")
    if model_type.lower() == 'bigram' or model_type.lower() == 'trigram':
        valid_input = True
        print("\nGENERATING MODEL...\n")

if model_type.lower() == 'bigram':
    # COUNT FREQUENCY OF OCCURRENCE
    for sent in reuters.sents():
        for word1, word2 in bigrams(sent, pad_right=True, pad_left=True):
            model[word1][word2] += 1

    # GET PROBABILITIES FROM COUNT
    for word1 in model:
        total_count = float(sum(model[word1].values()))
        for word2 in model[word1]:
            model[word1][word2] /= total_count

    # GET STARTING WORDS FROM USER
    valid_input = False
    user_selection = ""

    while not valid_input:
        user_selection = input("Please specify your starting word - Type a single word:")
        if len(user_selection.split()) == 1:
            valid_input = True
            print("\nGENERATING RANDOM SENTENCE...\n")

    
    # STARTING WORDS
    generated_sentence = [user_selection]
    sentence_done = False

    while not sentence_done:
        # SELECT RANDOM PROBABILITY THRESHOLD
        rand = random.random()
        acc = .0

        for word in model[generated_sentence[-1]].keys():
            acc += model[generated_sentence[-1]][word]
            
            # SELECT WORDS ABOVE PROBABILITY THRESHOLD
            if acc >= rand:
                generated_sentence.append(word)
                break
        
        # DONE ONCE WE HAVE 2 NONES IN A ROW
        if (generated_sentence[-1:] == [None]):
            sentence_done = True

    print(' '.join([w for w in generated_sentence if w]))

elif model_type.lower() == 'trigram':
    # COUNT FREQUENCY OF OCCURRENCE
    for sent in reuters.sents():
        for word1, word2, word3 in trigrams(sent, pad_right=True, pad_left=True):
            model[(word1, word2)][word3] += 1

    # GET PROBABILITIES FROM COUNT
    for word1and2 in model:
        total_count = float(sum(model[word1and2].values()))
        for word3 in model[word1and2]:
            model[word1and2][word3] /= total_count

    # GET STARTING WORDS FROM USER
    valid_input = False
    user_selection = ""

    while not valid_input:
        user_selection = input("Please specify your starting words - Type two words separated by a space:")
        if len(user_selection.split()) == 2:
            valid_input = True
            print("\nGENERATING RANDOM SENTENCE...\n")

    # STARTING WORDS
    generated_sentence = [user_selection.split()[0], user_selection.split()[1]]
    sentence_done = False

    while not sentence_done:
        # SELECT RANDOM PROBABILITY THRESHOLD
        rand = random.random()
        acc = .0

        for word in model[tuple(generated_sentence[-2:])].keys():
            acc += model[tuple(generated_sentence[-2:])][word]
            
            # SELECT WORDS ABOVE PROBABILITY THRESHOLD
            if acc >= rand:
                generated_sentence.append(word)
                break
        
        # DONE ONCE WE HAVE 2 NONES IN A ROW
        if (generated_sentence[-2:] == [None, None]):
            sentence_done = True

    print(' '.join([w for w in generated_sentence if w]))
