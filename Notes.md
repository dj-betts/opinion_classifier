# Classifying "Op-Ed" vs "News"

## Background:
##### Format matters. As the modern consumer is bombarded with news and opinion from multiple sources via multiple formats it is becoming increasingly difficult for a consumer to distinguish what they should take as fact from what they should, by design, read as an opinion. I was interested in building a model that classified stories written for the "Op-Ed" desk and those written for the "News" desk, the two formats that coexist in every newsroom, print or broadcast.

## Objectives:

##### 1. Build a classification model that predicts "Op-Ed" from "News" pieces using NLP on the body of the articles themselves.


## The Data:

##### 2019-2020. Print. Keyword='United States Politics and Government'.

![Number of Op-Ed and News articles](img/num_opednews_2019.png)

---
## The Model:
stop_words = ['said']


## Model Performance: 

![Confusion Matrix](img/confusion_matrix.png)

accuracy = 0.9162162162162162
recall = 0.9036458333333334
precision = 0.6995967741935484
tn:1687 fp:149 fn:37 tp:347

## Analysis:

###### Important features: Many features are political and are causing the model to predict based on topic, not sentiment. 

![Important Features](img/feature_imporance.png)



## Next Steps:

##### 1. Engineer data sets that control for the topic to discover features that differentiate bias in a specific topic. (eg. classifying political Op-Ed from news stories about politics. Connect model results to EDA.
##### 2. Optimize RF
##### 3. Build a [XGBoost] (https://xgboost.readthedocs.io/en/latest/#)
##### 5. Flask app interactivity. 