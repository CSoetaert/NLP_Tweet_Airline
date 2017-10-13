"""
Denisa Valentina Licu and Camille Soetaert october 2018
Natural Language Processing Project
Analyzing sentiment from Tweet about US Airlines
Getting the data and tokenization
"""
import string
import csv
from collections import defaultdict

def charging_tweets() :
    columns = defaultdict(list)  # each value in each column is appended to a list
    with open('Tweets.csv') as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k
    return columns



def tokenizer(text):
    # function to tokenize a text
    ## first we get rid of the punctuation
    replace_punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    no_punct = text.translate(replace_punctuation)
    ## then we put the text in lowercase
    low_case = no_punct.lower()
    ## then we split the text into a list of words
    splitted = low_case.split(" ")
    ## finally we get rid of empty words
    text_tokenized = [x for x in splitted if x != ""]
    return text_tokenized




data = charging_tweets()
tweet_id=data['tweet_id']
airline_sentiment=data['airline_sentiment']
text=data['text']
airline_sentiment_confidence=data['airline_sentiment_confidence']
print(tweet_id[0])
print(airline_sentiment[0])
print(text[0])
print(airline_sentiment_confidence[0])