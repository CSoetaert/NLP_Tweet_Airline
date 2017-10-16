"""
Denisa Valentina Licu and Camille Soetaert october 2018
Natural Language Processing Project
Analyzing sentiment from Tweet about US Airlines
Functions to classify our datas
"""
import data_treatment
from math import log

N_VOC = 25
WITH_CONFIDENCE = False

def countingWords(word_list,confidence_list):
    """
    Function that compute the number of occurrences of each word and the occurrences using the confidence
    :param word_list: list of tweets in the form of list of words
    :param confidence_list: list of the confidence for each tweet
    :return: the dictionary containing the number of occurrences of each word and the other dictionary containing
    the occurrences using the tweets.
    """
    dict_count = {}
    dict_count_confidence = {}
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            if word_list[i][j] in dict_count.keys():
                dict_count[word_list[i][j]] += 1.
                dict_count_confidence[word_list[i][j]] += confidence_list[i]
            else:
                dict_count.update({word_list[i][j]: 1.})
                dict_count_confidence.update({word_list[i][j]: confidence_list[i]})
    return dict_count, dict_count_confidence


def makeVocabulary(words_count, threshold):
    """
    Function to make the vocabulary from a dictionary containing the words and their count
    :param words_count: dictionary containing the words and their count
    :param threshold: minimum number of occurrences of the word to be in the vocabulary
    :return: the list of the words in the vocabulary
    """
    VOCABULARY=[]
    for key in words_count.keys():
        if words_count.get(key) >= threshold:
            VOCABULARY.append(str(key))
    return VOCABULARY
#        VOCABULARY.append(str(key).strip('()').strip('\',\''))


def compute_probabilities(words_count, vocabulary, total_nr_words, k_smoothing=0):
    """
    Function to compute the probability of each word to occur in the data set.
    :param words_count: dictionary of the words associated with their number of occurrences
    :param vocabulary: list of the words in the vocabulary
    :param total_nr_words: the total number of words in our data set
    :param k_smoothing: the factor used in the Laplace smoothing
    :return: the dictionary containing the probabilities for each word in the vocabulary and the unknown word.
    """
    vocabulary_size = len(vocabulary) + 1  # because we add <UNK> for the unknown words
    WORDS_PROBABILITIES = {word: 0 for word in vocabulary}
    WORDS_PROBABILITIES.update({'<UNK>': 0})

    for word in words_count:
        for word_voc in vocabulary:
            if (word == word_voc):
                WORDS_PROBABILITIES[word] = words_count.get(word)
            else:
                WORDS_PROBABILITIES['<UNK>'] = WORDS_PROBABILITIES.get('<UNK>') + 1.
                # compute probability for each word in vocabulary + <UNK> words
    for word in WORDS_PROBABILITIES:
        WORDS_PROBABILITIES[word] = log(WORDS_PROBABILITIES[word] + k_smoothing) - log(
            total_nr_words + vocabulary_size * k_smoothing)

    return WORDS_PROBABILITIES


def train(training_data, threshold_voc=N_VOC):
    # sorting the tweets by sentiment
    pos_tweet, pos_confidence, neu_tweet, neu_confidence, neg_tweet, neg_confidence = data_treatment.sorting_tweets_by_sentiment(training_data)
    # tokenizing the tweets
    for i in range(len(pos_tweet)):
        pos_tweet[i] = data_treatment.tokenizer(pos_tweet[i])
    for i in range(len(neu_tweet)):
        neu_tweet[i] = data_treatment.tokenizer(neu_tweet[i])
    for i in range(len(neg_tweet)):
        neg_tweet[i] = data_treatment.tokenizer(neg_tweet[i])
    # making the vocabulary
    dict_pos_count, dict_pos_count_confidence = countingWords(pos_tweet, pos_confidence)
    dict_neu_count, dict_neu_count_confidence = countingWords(neu_tweet, neu_confidence)
    dict_neg_count, dict_neg_count_confidence = countingWords(neg_tweet, neg_confidence)
    if WITH_CONFIDENCE:
        pos_voc = makeVocabulary(dict_pos_count_confidence, threshold_voc)
        neu_voc = makeVocabulary(dict_pos_count_confidence, threshold_voc)
        neg_voc = makeVocabulary(dict_pos_count_confidence, threshold_voc)
    else:
        pos_voc = makeVocabulary(dict_pos_count, threshold_voc)
        neu_voc = makeVocabulary(dict_pos_count, threshold_voc)
        neg_voc = makeVocabulary(dict_pos_count, threshold_voc)
    # computing probabilities
    nb_pos_word = 0
    for key in dict_pos_count.keys():
        nb_pos_word += dict_pos_count[key]
    pos_prob = compute_probabilities(dict_pos_count,pos_voc,nb_pos_word,1)
    nb_neu_word = 0
    for key in dict_neu_count.keys():
        nb_neu_word += dict_neu_count[key]
    neu_prob = compute_probabilities(dict_neu_count, neu_voc, nb_neu_word, 1)
    nb_neg_word = 0
    for key in dict_neg_count.keys():
        nb_neg_word += dict_neg_count[key]
    neg_prob = compute_probabilities(dict_neg_count, neg_voc, nb_neg_word, 1)
    return pos_prob, neu_prob, neg_prob


def compute_sentiment_probability(text_test, sentiment_probabilities):
    final_probability = 0

    for word in text_test:
        if word in sentiment_probabilities:
            final_probability += sentiment_probabilities.get(word)
        else:
            final_probability += sentiment_probabilities.get('<UNK>')

    return final_probability


def classify_sentiment(text_test, positive_probabilities, negative_probabilities, neutral_probabilities):
    positive_prob = compute_sentiment_probability(text_test, positive_probabilities)
    negative_prob = compute_sentiment_probability(text_test, negative_probabilities)
    neutral_prob = compute_sentiment_probability(text_test, neutral_probabilities)
    prob_list = [positive_prob, neutral_prob, negative_prob]
    maxim = max(prob_list)
    if positive_prob == maxim and negative_prob != maxim:
        return "positive"
    elif negative_prob == maxim and positive_prob != maxim:
        return "negative"
    else:
        return "neutral"
