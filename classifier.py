from nltk.util import ngrams

def frequency_words(word_list,n_gram_nb = 1) :
    

def count_unique_n_grams(list_of_words):
    # function to count the number of unique n-grams in a list of words
    global LM
    nr_n_grams = {n:0 for n in range(1,MAX_N+1)}
    for i in range(0,len(list_of_words)):
        for n in range(1,MAX_N+1):
            ngram=ngrams(list_of_words[i],n)
            for item in ngram:
                LM[n][item]=LM[n].get(item,0)+1
            nr_n_grams[n] = len(LM[n])
    return nr_n_grams