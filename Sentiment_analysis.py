#Import necessary libraries

import pandas as pd
import spacy 
#from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob
import random as rd

# loading  English small language package 
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')



# define a function to preprocess text data by removing stop word and punct  
# and adding  them to a dictionary

def clean_text(whole_review_data): 
    cleaned_reviews = {}
    for review in whole_review_data:
        doc = nlp(review)
        cleaned_text = ' '.join([token.text.lower().strip() for token in doc if not token.is_stop | token.is_punct])
        cleaned_reviews[review] = cleaned_text
    return cleaned_reviews


# define sentiment analysis on our clean data 

def sentiment_analysis(cleaned_data):
    for key, value in cleaned_data.items():
        doc = nlp(value)
        print(f'\nReview : {key}')
        print('\nsentiment :', doc._.blob.polarity)
        print('\nsentiment :', doc._.blob.sentiment)


# Load amazon prodoct review data set
amazon_data = pd.read_csv('amazon_product_reviews.csv', sep=',', low_memory=False)

# clean the dataset and using 'reviews.text' columns 
amazon_data = amazon_data.dropna(subset=['reviews.text'])

# run a test on sample reviews 
reviews_data = amazon_data['reviews.text'].iloc[[12,52, 67, 143, 252, 543, 1432, 4234, 8242, 14593, 20232]]

# perform sentiment analysis 
sentiment_analysis(clean_text(reviews_data))


# perform similarity between reviews

print('\n--------------------Similarity----------------------')

nlp = spacy.load('en_core_web_md')

def similarity(text1, text2):
    doc= nlp(text1)
    doc_2 = nlp(text2)
    similarity_result = doc.similarity(doc_2)
    return similarity_result

# using randit function to get random reviews 
random_index = rd.randint(0, len(amazon_data)-1)
random_index_2 = rd.randint(0, len(amazon_data)-1)


first_review_of_choice = amazon_data['reviews.text'][random_index]
second_review_of_choice = amazon_data['reviews.text'][random_index_2]


print(f'\nFirst review : {first_review_of_choice}')
print(f'\nSecond review : {second_review_of_choice}')
print(f'\nSimilarity : {similarity(first_review_of_choice, second_review_of_choice)}')
