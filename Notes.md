# Classifying "Op-Ed" vs "News"

## Background:
##### Format matters. As the modern consumer is bombarded with news and opinion from multiple sources via multiple formats it is becoming increasingly difficult for a consumer to distinguish what they should take as fact from what they should, by design, read as an opinion. I was interested in building a model that classified stories written for the "Op-Ed" desk and those written for the "News" desk, the two formats that coexist in every newsroom, print or broadcast.

## Objectives:

##### 1. Build a classification model that predicts "Op-Ed" from "News" pieces using NLP on the body of the articles themselves.


## The Data:

##### 2019-2020. Print. Keyword='United States Politics and Government'.

![Number of Op-Ed and News articles](img/oped_news_hist.png)

---
## The Model:
stop_words = NONE

## Model Performance: 

![Confusion Matrix](img/confusion_matrix.png)

accuracy = 0.9241499564080209
recall = 0.9293478260869565
precision = 0.6979591836734694
tn:889 fp:74 fn:13 tp:171

## Analysis:

###### Important features: Many features are political and are causing the model to predict based on topic, not sentiment. 

![Important Features](img/feature_imporance.png)



## Next Steps:

