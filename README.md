# CSS_Project: Sentiment Analysis and Topic Modelling based Stock Price movement prediction. 
Pankhil Gawade

##  Overall goal of the project
The aim is to compare the two different approaches i.e. Sentiment Analysis and Topic Modelling for Tesla Stock price movement prediction. 

## Framework used and inclusion 
In the case of Sentiment Analysis, I will use the FinBERT. It is a Bidirectional Encoder Representation of a Transformer (BERT) pre-trained on a large corpus of financial data. 
For Topic Modelling, I am using gensim library which is general general-purpose library for Topic modelling and NLP. I will be using the Hierarchical Dirichlet process (HDP)  and Latent Dirichlet allocation (LDA)
model from gensim.As in Topic modelling the data is converted to a topic vector by using Google's word2vec(it takes text corpus as input and outputs word vector.), and classification is performed later to predict the final movement of a stock based on topic features for this purpose I am using a Linear Model, random forest and XGboost. 

## Initial Data
Data is taken from Mediacloud for 6 months. I am collecting all the news titles from the media cloud about Tesla for the last 6 months i.e. Aug 23 - Jan 24. 
Data for the stock price of TSLA is taken from scraping the Yahoo finance website. It contains Open High Low Close Volume and ADJ Close for each day for 6 months. 


