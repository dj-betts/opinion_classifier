import nltk
import string

import pandas as pd
import numpy as np

from collections import Counter

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# function to vectorize the type_of_material series into a y target vector.
def vectorize_y_ser(ser):
    y = ser.copy()
    y.replace({'Op-Ed': 1,'News': 0}, inplace=True)
    return y

#rate of correct predictions out of total predictions
def metrics_(tn, fp, fn, tp):
    accuracy = (tp + tn) / (tn + fn + tp + fp)
    print(f'accuracy = {accuracy}')
    recall = (tp) / (tp + fn)
    print(f'recall = {recall}')
    precision = (tp) / (tp + fp)
    print(f'precision = {precision}')
    print(f'tn:{tn} fp:{fp} fn:{fn} tp:{tp}')

#returns shape of news and oped
def oped_v_news(df):
    news_df = df[df.type_of_material == "News"]
    oped_df = df[df.type_of_material == "Op-Ed"]
    print(f"news shape:{news_df.shape}, oped shape:{oped_df.shape}, ratio: {oped_df.shape[0]/news_df.shape[0]}")

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
        
def filter_keyword(df):
    df['United States Politics and Government'] = df.apply(return_pol_gov, axis=1)    
    df = df[df['United States Politics and Government'] == True]
    oped_v_news(df)
    return df

#function that removes string.punctuation w/out the '?'
def punc_strip(document):
    for char in document:
        if char in '!"#$%&\'()*+—,-./:;<=>?@[\\]^_`{|}~”’':
            document = document.replace(char, " ") 
    return document

stop_words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','mr','ms','said']
