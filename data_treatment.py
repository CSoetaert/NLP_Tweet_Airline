"""
Denisa Valentina Licu and Camille Soetaert october 2018
Natural Language Processing Project
Analyzing sentiment from Tweet about US Airlines
Getting the data and tokenization
"""
import string
import csv
from collections import defaultdict


def charging_tweets():
    """
    Function to charge and store the tweets from the dataset.
    :return: dictionnary containing the tweets and the attributes
    """
    columns = defaultdict(list)  # each value in each column is appended to a list
    with open('Tweets.csv') as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k
    return columns

def addNot(splitted_text):
    """
    Function to add 'NOT' before a word in a negative sentence.
    :param splitted_text: text splitted by word
    :return: the list of the word of the sentence with the punctuation
    """
    for i in range(0, len(splitted_text)):
        if splitted_text[i]=="not":
            while(not(splitted_text[i+1] in FINAL_SENTENCE_PUNCTUATION)):
                splitted_text[i+1]="NOT"+splitted_text[i+1]
                i+=1
    return splitted_text

def list_values(inputlist):
    """
    List the possible values of a given feature in a dataset
    :param inputlist: list of the values
    :return: list of possible values
    """
    values = set([])
    for x in inputlist:
        values.add(x)
    return list(values)


def sorting_tweets_by_sentiment(data):
    """
    Function to sort the tweets according to the sentiment they were associated with.
    TO IMPROVE NOT ADAPTED TO OUR CASE
    :param data: the data set you want to sort
    :return:
    """
    # TODO : modify so that the confidence is considered
    sentiment = data['airline_sentiment']
    tweets = data['text']
    sent_list = list_values(sentiment)
    dict_sorted_tweet = {s: [] for s in sent_list}
    for tweet_no in range(len(data['airline_sentiment'])) :
        for sent in sent_list:
            if sentiment[tweet_no] == sent :
                dict_sorted_tweet[sent].append(tweets[tweet_no])
    return dict_sorted_tweet


def replace_mention(splitted_text):
    """
    Replace the '@Twitter_account' by 'NameMentionToken'
    :param splitted_text: text splitted by word
    :return: the modified list of words
    """
    for i in range(len(splitted_text)):
        if "@" in splitted_text[i]:
            splitted_text[i] = "NameMentionToken"
    return splitted_text


def tokenizer(text):
    """
    Function to tokenize the text
    :param text: the text to tokenize
    :return: the list of words tokenized
    """
    # TODO : Modify it to fit to our new kind of data
    # function to tokenize a text
    # first we get rid of the punctuation
    replace_punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    no_punct = text.translate(replace_punctuation)
    # then we put the text in lowercase
    low_case = no_punct.lower()
    # then we split the text into a list of words
    splitted = low_case.split(" ")
    # finally we get rid of empty words
    text_tokenized = [x for x in splitted if x != ""]
    return text_tokenized


""" TESTING ZONE """
data = charging_tweets()
tweet_id = data['tweet_id']
airline_sentiment = data['airline_sentiment']
text = data['text']
airline_sentiment_confidence=data['airline_sentiment_confidence']
# print(tweet_id[0])
# print(airline_sentiment[0])
print(text[0])
splitted = text[0].split(' ')
splitted = replace_mention(splitted)
print splitted
# print(airline_sentiment_confidence[0])
