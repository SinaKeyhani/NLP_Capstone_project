# Sentiment Analysis of Amazon Product Reviews

# Table of Contents
1. Project overview
2. Installation and Usage
3. Dataset Description
4. Evaluation of Results
5. Strengths and Limitations
7. Credits


# Project Overview
This project delves into the sentiment analysis of Amazon product reviews, employing advanced Natural Language Processing (NLP) techniques to decipher the underlying sentiments expressed by customers. The project aims to parse through an extensive dataset of reviews, applying the pandas library for data handling and the TextBlob library for conducting sentiment analysis. The insights garnered from this analysis are intended to shed light on customer satisfaction levels across various products, providing valuable feedback to businesses aiming to enhance their product offerings and customer service.

## Installation and Usage
To run this project locally, follow these steps:

1. Ensure Python is installed on your machine.
2. Clone this repository or download the project files.
3. Install the required Python libraries for this project.

# Dataset Description
This comprehensive dataset contains customer reviews for a wide array of products available on Amazon. This dataset has been crucial in providing a textual overview of customer feedback, encapsulating experiences, satisfaction levels, and varied opinions on the products purchased. Such a dataset is instrumental in extracting insights into consumer sentiment, offering a broad perspective on customer perceptions across different product categories.

# Evaluation of Results
1. Sentiment Analysis: Sentiment analysis was performed on a subset of the dataset using the TextBlob library through the SpacyTextBlob extension. The sentiment analysis provided polarity and sentiment scores for each review, indicating the overall sentiment expressed in the text.
2. Similarity Analysis: A similarity analysis was conducted using spaCy's word embeddings model. Random pairs of reviews were selected from the dataset, and their similarity scores were computed. The similarity score indicates how closely related the semantic meanings of two reviews are.

# Strengths and Limitations
While the sentiment analysis model has proven effective in categorizing sentiments of reviews, it faces limitations in detecting nuanced expressions of human emotions, such as sarcasm. Future work could explore more sophisticated models or incorporate additional linguistic features to enhance the accuracy of sentiment detection. Additionally, It would be good to use Large English language package to increase the accuracy in both semantic analysis and similarity.



