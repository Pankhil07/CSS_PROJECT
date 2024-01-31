# CSS_Project:Sentiment Analysis and Topic Modelling based Stock Price movement prediction. 
Pankhil Gawade

##  Overall goal of the project
Aim is to compare the two different approches i.e Sentiment Analysis and Topic Modelling for the purpose of Tesla Stock price movement prediction. 

## Framework used and inclusion 
In the case of Sentiment Analysis I will use the FinBERT. It is a Bidirectional Encoder Representation of a Transformer (BERT) pretrained on large corpus of financial data. 
For Topic Modlling I am using gensim library which is general purpouse library for Topic modelling and NLP. I will be using Hierarchical Dirichlet process (HDP)  and Latent Dirichlet allocation (LDA)
model from gensim.As in Topic modelling the data is converted to topic vector, classification is performed later to predict the final movement of stock based on topic features for this purpouse I am using Linear Model, random forest and XGboost. 

## Initial Data
Data is taken from Mediacloud for 6 months . I am collecting all the news titles from media cloud about tesla for last 6 months i.e Aug 23 - Jan 24. 
Data for stock price of TSLA is taken from scraping the yahoo finance website. It contains Open High Low Close Volume and ADJ Close for eaach day for 6 months. 


