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


def add_not(splitted_text):
    """
    Function to add 'NOT' before a word in a negative sentence.
    :param splitted_text: text splitted by word
    :return: the list of the word of the sentence with the punctuation
    """
    FINAL_SENTENCE_PUNCTUATION = ["!", "?", ".", ",", ";"]
    for i in range(0, len(splitted_text)):
        if splitted_text[i]=="not":
            while(i+1<len(splitted_text) and not(splitted_text[i+1] in FINAL_SENTENCE_PUNCTUATION)):
                splitted_text[i+1]="NOT"+splitted_text[i+1]
                i+=1
    return splitted_text


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
    text = text.lower()
    text = text.split(' ')
    text = replace_mention(text)
    text = add_not(text)
    replace_punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    for i in range(len(text)):
        text[i] = text[i].translate(replace_punctuation)
        text[i] = text[i].replace(' ','')
    return text


def sorting_tweets_by_sentiment(data):
    """
    Function to sort the tweets according to the sentiment they were associated with.
    :param data: the data set you want to sort
    :return: the list of positive tweets, the list of the confidence of the positive tweet and the same lists for
    neutral and negative tweets
    """
    # TODO : modify so that the confidence is considered
    sentiment = data['airline_sentiment']
    tweets = data['text']
    confidence = data['airline_sentiment_confidence']
    sent_list = list_values(sentiment)
    dict_sorted_tweet = {s: [] for s in sent_list}
    dict_sorted_confidence = {s: [] for s in sent_list}
    for tweet_no in range(len(data['airline_sentiment'])):
        for sent in sent_list:
            if sentiment[tweet_no] == sent:
                dict_sorted_tweet[sent].append(tweets[tweet_no])
                dict_sorted_confidence[sent].append(confidence[tweet_no])
    return dict_sorted_tweet['positive'], dict_sorted_confidence['positive'], dict_sorted_tweet['neutral'], dict_sorted_confidence['neutral'], dict_sorted_tweet['negative'], dict_sorted_confidence['negative']

# """ TESTING ZONE """
# data = charging_tweets()
# tweet_id = data['tweet_id']
# airline_sentiment = data['airline_sentiment']
# text = data['text']
# airline_sentiment_confidence=data['airline_sentiment_confidence']
# print(tweet_id[0])
# print(airline_sentiment[0])
# print(text[0])
# print(tokenizer(text[0]))
# print list_values(airline_sentiment)
# print(airline_sentiment_confidence[0])
