"""
Denisa Valentina Licu and Camille Soetaert october 2018
Natural Language Processing Project
Analyzing sentiment from Tweet about US Airlines
"""
import classifier
import evaluation
import data_treatment

# Separating the data and treat it
data = data_treatment.charging_tweets()
tweet_id = data['tweet_id']
airline_sentiment = data['airline_sentiment']
text = data['text']
airline_sentiment_confidence=data['airline_sentiment_confidence']
training_data = {'tweet_id': [], 'airline_sentiment': [], 'text': [], 'airline_sentiment_confidence':[]}
training_data['tweet_id'] = data['tweet_id'][:5000]
training_data['airline_sentiment'] = data['airline_sentiment'][:5000]
training_data['text'] = data['text'][:5000]
training_data['airline_sentiment_confidence'] = data['airline_sentiment_confidence'][:5000]

test_data = {'tweet_id': [], 'airline_sentiment': [], 'text': [], 'airline_sentiment_confidence':[]}
test_data['tweet_id'] = data['tweet_id'][5000:6000]
test_data['airline_sentiment'] = data['airline_sentiment'][5000:6000]
test_data['text'] = data['text'][5000:6000]
test_data['airline_sentiment_confidence'] = data['airline_sentiment_confidence'][5000:6000]

# training the classifier
pos_prob, neu_prob, neg_prob = classifier.train(training_data, 25)
test_sentiment = []
for i in range(len(test_data['text'])):
    text = data_treatment.tokenizer(test_data['text'][i])
    sentiment = classifier.classify_sentiment(text, pos_prob, neg_prob, neu_prob)
    test_sentiment.append(sentiment)

print evaluation.evaluation(test_sentiment, test_data['airline_sentiment'])

# test the classifier
