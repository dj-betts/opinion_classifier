# Classifying "Op-Ed" vs "News"

## Background:
##### Format matters. As the modern consumer is bombarded with news and opinion from multiple sources via multiple formats it is becoming increasingly difficult for a consumer to distinguish what they should take as fact from what they should, by design, read as an opinion. I was interested in building a model that classified stories written for the "Op-Ed" desk and those written for the "News" desk, the two formats that coexist in every newsroom, print or broadcast.

## Objectives:

##### 1. Build a classification model that predicts "Op-Ed" from "News" pieces using NLP on the body of the articles themselves.


## The Data:

##### In 2019, the New York Times published 41,748 articles, not all of them were published in print. I obtained metadata from each article via the TImes Archive API, and scrapped each URL for the body of each article. In total, my final corpus of documents was 26,472 News articles and 2,012 Op-Ed articles. 

![Number of Op-Ed and News articles](img/num_opednews_2019.png)

---
## The Model:


## Model Performance: 

![Confusion Matrix](img/confusion_matrix.png)

accuracy = 0.8272626931567328
recall = 0.8388671875
precision = 0.2686053783614759
tn:11133 fp:2339 fn:165 tp:859

## Analysis:

###### Important features: Many features are political and are causing the model to predict based on topic, not sentiment. 

![Important Features](img/confusion_matrix.png)



## Next Steps:

##### 1. Engineer data sets that control for the topic to discover features that differentiate bias in a specific topic. (eg. classifying political Op-Ed from news stories about politics. Connect model results to EDA.
##### 2. Optimize RF
##### 3. Build a [XGBoost] (https://xgboost.readthedocs.io/en/latest/#)
##### 5. Flask app interactivity. 