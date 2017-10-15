"""
Denisa Valentina Licu and Camille Soetaert october 2018
Natural Language Processing Project
Analyzing sentiment from Tweet about US Airlines
"""
import classifier
import evaluation
import data_treatment
import json
import datetime
import numpy as np

# Separating the data and treat it
data = data_treatment.charging_tweets()
k_data = []
for i in range(0, 5):
    i_data = {'tweet_id': [], 'airline_sentiment': [], 'text': [], 'airline_sentiment_confidence': []}
    i_data['tweet_id'] = data['tweet_id'][i*len(data['tweet_id'])//5:(i+1)*len(data['tweet_id'])//5]
    i_data['airline_sentiment'] = data['airline_sentiment'][i*len(data['tweet_id'])//5:(i+1)*len(data['tweet_id'])//5]
    i_data['text'] = data['text'][i*len(data['tweet_id'])//5:(i+1)*len(data['tweet_id'])//5]
    i_data['airline_sentiment_confidence'] = data['airline_sentiment_confidence'][i*len(data['tweet_id'])//5:(i+1)*len(data['tweet_id'])//5]
    k_data.append(i_data)

training_data = {'tweet_id': [], 'airline_sentiment': [], 'text': [], 'airline_sentiment_confidence':[]}

accuracy = []
fpos = []
fneg = []
fneu = []
for i in range(0, 5):
    test_data = k_data[i]
    training_data['tweet_id'] = k_data[(i+1) % 5]['tweet_id']+k_data[(i+2) % 5]['tweet_id']+k_data[(i+3) % 5]['tweet_id']+k_data[(i+4) % 5]['tweet_id']
    training_data['airline_sentiment'] = k_data[(i+1) % 5]['airline_sentiment']+k_data[(i+2) % 5]['airline_sentiment']+k_data[(i+3) % 5]['airline_sentiment']+k_data[(i+4) % 5]['airline_sentiment']
    training_data['text'] = k_data[(i+1) % 5]['text']+k_data[(i+2) % 5]['text']+k_data[(i+3) % 5]['text']+k_data[(i+4) % 5]['text']
    training_data['airline_sentiment_confidence'] = k_data[(i + 1) % 5]['airline_sentiment_confidence'] + k_data[(i + 2) % 5]['airline_sentiment_confidence'] + k_data[(i + 3) % 5]['airline_sentiment_confidence'] + k_data[(i + 4) % 5]['airline_sentiment_confidence']

    # training the classifier
    pos_prob, neu_prob, neg_prob = classifier.train(training_data, 25)
    # testing
    test_sentiment = []
    for i in range(len(test_data['text'])):
        text = data_treatment.tokenizer(test_data['text'][i])
        sentiment = classifier.classify_sentiment(text, pos_prob, neg_prob, neu_prob)
        test_sentiment.append(sentiment)
    # evaluating
    acc,precision_positive,precision_negative,precision_neutral,recall_positive,recall_negative,recall_neutral,f_positive,f_negative,f_neutral = evaluation.evaluation(test_sentiment, test_data['airline_sentiment'])
    accuracy.append(acc)
    fpos.append(f_positive)
    fneg.append(f_negative)
    fneu.append(f_neutral)

mean_acc = np.mean(np.array(accuracy))
mean_fpos = np.mean(np.array(fpos))
mean_fneg = np.mean(np.array(fneg))
mean_fneu = np.mean(np.array(fneu))

experiment_description = "test"
with open(str(datetime.datetime.now())+".json", "w") as outfile:
    to_dump = {"description": experiment_description, "mean accuracy": mean_acc, "mean fpos": mean_fpos, "mean fneg": mean_fneg, "mean fneu": mean_fneu}
    json.dump(to_dump, outfile, indent=4)
print "finished"
