import nltk
import string

import pandas as pd
import numpy as np

from collections import Counter

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#combine print, type, text columns in the list. input is file, not dataframe.
def df_printed(file):
    print_cols = ['_id','print_page','pub_date','keywords','type_of_material','lead_paragraph','text']    
    df = pd.read_csv(file, usecols=print_cols, index_col='_id', low_memory=False)
    
    #remove articles that do NOT have a printed page, meaning that these articles were NOT printed, but published online.
    df = df[df.print_page.isna() == False]
    
    #remove articles that did not have text. Ex: podcast place holders
    df = df[~df.text.isna() == True]
    return df

#returns articles w/ 'United States Politics and Government' as a keyword
#keywords is a column in NYT API
def return_keyword(row, value='United States Politics and Government'):
    list_dict = eval(row.keywords)
    for (dic) in (list_dict):
        if dic.get('value') == value:
            return True
        
#value from previous function is used as a key in this function
def filter_keyword(df, keyword='United States Politics and Government'):
    df[keyword] = df.apply(return_keyword, axis=1)
    df = df[df[keyword] == True]
    return df
                
# function to vectorize the type_of_material series into a y target vector.
def vectorize_y_ser(ser):
    y = ser.copy()
    y.replace({'Op-Ed': 1,'News': 0}, inplace=True)
    return y

# rate of correct predictions out of total predictions
def metrics_(tn, fp, fn, tp):
    accuracy = (tp + tn) / (tn + fn + tp + fp)
    print(f'Accuracy: {round(accuracy, 2)}')
    recall = (tp) / (tp + fn)
    print(f'Recall: {round(recall, 2)}')
    precision = (tp) / (tp + fp)
    print(f'Precision: {round(precision, 2)}')
    print(f'TN:{tn} FP:{fp} FN:{fn} TP:{tp}')
#    return (accuracy, recall, precision)

#prints number of features, stop words and parameters for vectorizer
def print_vector_params(vectorizer):
    #features
    feat_names = vectorizer.get_feature_names()
    num_feat = len(feat_names)
    
    #stop words
    stop_words = vectorizer.stop_words_
    num_stop = len(stop_words)

    params = vectorizer.get_params()
    
    print(f'Number of features: {num_feat}, Numbers of stop words: {num_stop}')
      
    for key, val in params.items():
        print(f'{key}: {val}')

#returns quick check of balance
#shape and histogram of news and oped
#safe fig also included.
def oped_v_news(df):
    df.type_of_material.hist()
    news = sum(df.type_of_material == "News")
    oped = sum(df.type_of_material == "Op-Ed")
    print(f'News: {news} Oped: {oped}, Total: {oped+news}, Op-Ed {round(oped/(oped+news), 2)} of total')
    #plt.savefig('img/oped_news_hist.png')

#change News stories that had mislabeled section name
def change_oped(x):
    if (x.section_name == "Opinion") & (x.type_of_material == "News"):
        x.type_of_material = "Op-Ed"
    else:
        x.type_of_material

#returns articles w/ 'United States Politics and Government' as a keyword
def return_pol_gov(row):
    list_dict = eval(row.keywords)
    for (dic) in (list_dict):
        if dic.get('value') == 'United States Politics and Government':
            return True

#filter articles by keyword reference. default: 'United States Politics and Government'  
def filter_keyword(df, keyword='United States Politics and Government'):
    df[keyword] = df.apply(return_pol_gov, axis=1)
    df = df[df[keyword] == True]
    return df

#remove capitalized words EX: first words of sentences. proper nouns.
def remove_cap_words(row):
    temp = row.split()
    for i, word in enumerate(temp):
        if word[0].isupper():
            temp[i] = ""
            
    return " ".join(temp)

#function that removes string.punctuation w/out the '?'
def punc_strip(doc):
    for char in word_tokenize(doc):
        if char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~—':
            doc = doc.replace(char, " ")
        #I decided the easiest way to deal with various contractions was to delete all apostrophes 
        if char == "’":
            doc = doc.replace(char, "")
    return doc

#wordnet lemmatizer and lowercase words.
def wordnet_tokenize(doc):
    wordnet = WordNetLemmatizer()
    return  [wordnet.lemmatize(word) for word in word_tokenize(doc.lower())]
#split article and return quote

#split document into article body and quotation
def text_parse(document):
    article = []
    quote_list = []
    
    open_quote = "“"
    close_quote = "”"
    
    close_split = document.split(close_quote)
    
    for string in close_split:

        quote = string.split(open_quote)
        article.append(quote.pop(0))
        quote_list += quote
    
    article = " ".join(article)
    quotation = " ".join(quote_list)
        
    return(article, quotation)

#return list of quotes instaed of string to count how many times sources were quoted instead of volume of quotes.
def return_quote_list(document):
    article = []
    quote_list = []
    
    open_quote = "“"
    close_quote = "”"
    
    close_split = document.split(close_quote)
    
    for string in close_split:

        quote = string.split(open_quote)
        article.append(quote.pop(0))
        quote_list.append(quote)
    
    article = " ".join(article)
        
    return(quote_list)

#split article and return quote
def return_article(document):
    article = []
    quote_list = []
    #start count of quotes just because
    quote_count = 0
    
    open_quote = "“"
    close_quote = "”"
    
    close_split = document.split(close_quote)
    
    for string in close_split:

        quote = string.split(open_quote)
        article.append(quote.pop(0))
        quote_list += quote
        quote_count += 1
        
    article = " ".join(article)
    quotation = " ".join(quote_list)
    
    return(article)