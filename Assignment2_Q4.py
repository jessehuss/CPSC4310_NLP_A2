# Name: Jesse Huss
# ID: 001209444
# Project: Assignment 2 Q4
from collections import defaultdict
from nltk.corpus import brown,stopwords
from nltk import trigrams
import random
import nltk

# DATASET STORES TRIGRAM, CATEGORY
dataset = []

# FEATURESET FREQUENCY AND CATEGORY
featureset = list()
stopwords = stopwords.words("english")


input(
    "Welcome !\n"
    "This program uses trigram language model to train and test the brown corpus based on category\n" +
    "Initially tested using single word language model and got an average of 2%\n" +
    "Next attempted with bigram language model and was getting an average of 25%\n" +
    "Lastly used the trigram model to try and get a better accuracy which is around 27%\n"
    "Press enter to continue...\n\n")

print("GENERATING DATASET...\n")
# APPEND DATASET WITH TRIGRAMS AFTER REMOVING STOPWORDS, AND SMALL WORDS THAT COULD BE PUNCTUATION: WORDS <= 2 CHARS
for cat in brown.categories():
    for sent in brown.sents(categories=cat):
        words = [w.lower() for w in sent if w not in stopwords and len(w) > 2]
        dataset.append(([((w1, w2), w3) for (w1, w2, w3) in trigrams(words, pad_right=True, pad_left=True)], cat))

# GET FREQUENCY OF TRIGRAMS IN SET
def get_frequency(trigram):
    frec = defaultdict(int)
    for w12, w3 in trigram:
        frec[((w12), w3)] += 1

    return frec


# TRAIN AND TEST TRIGRAM MODEL
def train_and_test(featureset, trainpercent):

    random.shuffle(featureset)
    # SPLIT TRAIN = 70% OF DATASET AND TEST = 30%
    split = int((len(featureset) * trainpercent) / 100)

    train = featureset[:split]
    test = featureset[split:]

    print("\nTRAINING...\n")
    # NAIVE BAYES CLASSIFIER TRAIN
    classifier = nltk.NaiveBayesClassifier.train(train)

    print("\nTESTING...\n")
    # TEST AND RETURN ACCURACY
    return nltk.classify.accuracy(classifier, test)

print("\nGENERATING FEATURESET WITH FREQUENCIES...\n")
# GET FEATURESET WITH FREQUENCY AND CATEGORY
for trigram, category in dataset:
    featureset.append((get_frequency(trigram), category))

# PRINT ACCURACY FOR THE USER ~27% USING TRIGRAMS
print("Accuracy: ",train_and_test(featureset, 70))