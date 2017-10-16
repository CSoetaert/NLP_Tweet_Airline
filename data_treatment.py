"""
Denisa Valentina Licu and Camille Soetaert october 2018
Natural Language Processing Project
Analyzing sentiment from Tweet about US Airlines
Getting the data and tokenization
"""
import string
import csv
from collections import defaultdict

ADD_NOT = True

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


def check_punctuation_within_word(word):
    FINAL_SENTENCE_PUNCTUATION = ["!", "?", ".", ",", ";"]
    boolean=False
    for p in FINAL_SENTENCE_PUNCTUATION:
        if p in word:
            boolean=True
    return boolean

def check_punctuation_alone(word):
    FINAL_SENTENCE_PUNCTUATION = ["!", "?", ".", ",", ";"]
    boolean=False
    if word in FINAL_SENTENCE_PUNCTUATION:
        boolean=True
    return boolean

def check_NOT(word):
    NOT_WORDS = ["not", "n't", "cannot"]
    boolean=False
    for n in NOT_WORDS:
        if n in word:
            boolean=True
    return boolean

def add_not(splitted_text):
    """
    Function to add 'NOT' before a word in a negative sentence.
    :param splitted_text: text splitted by word
    :return: the list of the word of the sentence with the punctuation
    """
    for i in range(0, len(splitted_text)):

        if check_NOT(splitted_text[i])==True:
            while(i+1<len(splitted_text) and check_punctuation_alone(splitted_text[i+1])==False ):
                splitted_text[i+1]="NOT"+splitted_text[i+1]
                if(check_punctuation_within_word(splitted_text[i+1])==True):
                    break;
                else:
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
    if ADD_NOT:
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


