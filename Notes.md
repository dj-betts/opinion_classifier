# Classifying "Op-Ed" vs "News"

## Background:
##### Format matters. As the modern consumer is bombarded with news and opinion from multiple sources via multiple formats it is becoming increasingly difficult for a consumer to distinguish what they should take as fact from what they should, by design, read as an opinion. I was interested in building a model that classified stories written for the "Op-Ed" desk and those written for the "News" desk, the two formats that coexist in every newsroom, print or broadcast.

## Objectives:

##### 1. Build a classification model that predicts "Op-Ed" from "News" pieces using NLP on the body of the articles themselves.


## The Data:

##### 2020. Print. Keyword='United States Politics and Government'. word_net.lemmetizer

![Number of Op-Ed and News articles](img/oped_news_hist.png)

## The Vectorizer:

Number of features: 1088, Numbers of stop words: 42854
analyzer: word
binary: False
decode_error: strict
dtype: <class 'numpy.float64'>
encoding: utf-8
input: content
lowercase: True
max_df: 0.9
max_features: None
min_df: 0.1
ngram_range: (1, 1)
norm: l2
preprocessor: <function punc_strip at 0x7fafefad9050>
smooth_idf: True
stop_words: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
strip_accents: None
sublinear_tf: False
token_pattern: (?u)\b\w\w+\b
tokenizer: <function wordnet_tokenize at 0x7fafefaef560>
use_idf: True
vocabulary: None

---
## The Model:


## Model Performance: 

![Confusion Matrix](img/confusion_matrix.png)

Accuracy: 0.94
Recall: 0.9
Precision: 0.78
TN:915 FP:48 FN:18 TP:166

## Analysis:

![Important Features](img/feature_imporance.png)



## Next Steps:
.do full year of printed material.

