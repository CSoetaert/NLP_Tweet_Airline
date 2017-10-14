

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
            if word_list[i, j] in dict_count.keys():
                dict_count[word_list[i, j]] += 1
                dict_count_confidence[word_list[i, j]] += confidence_list[i]
            else:
                dict_count.update({word_list[i, j]: 1})
                dict_count_confidence.update({word_list[i, j]: confidence_list[i]})
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
                WORDS_PROBABILITIES['<UNK>'] = WORDS_PROBABILITIES.get('<UNK>') + 1
                # compute probability for each word in vocabulary + <UNK> words
    for word in WORDS_PROBABILITIES:
        WORDS_PROBABILITIES[word] = log(WORDS_PROBABILITIES[word] + k_smoothing) - log(
            total_nr_words + vocabulary_size * k_smoothing)

    return WORDS_PROBABILITIES