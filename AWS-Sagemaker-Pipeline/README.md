# AWS Sagemaker pipeline with conditional step
## Overview
I have implemented a regression problem using the AWS Sagemaker pipeline, with a conditional performance threshold step. 

## Dataset
Abalone Data Set from UCI ML repository was used in this implementation. The aim for this task is to determine the age of an abalone snail from its physical measurements. The number of rings turns out to be a good approximation for age (age is rings + 1.5). We use the dataset to build a predictive model of the variable rings through these other physical measurements

The dataset has the following features :

- Data Set Characteristics: Multivariate
- Number of Instances: 4177
- Number of Attributes: 8
- Attribute Characteristics: Categorical, Integer, Real
- Associated Tasks: Regression

Link to the dataset : https://archive.ics.uci.edu/ml/datasets/abalone 


## High Level Design

<img width="836" alt="image" src="https://user-images.githubusercontent.com/89654615/206904331-9231c980-d996-46b7-acb6-1e65ab694733.png">

1. We convert the raw text into tokens using the <code>pyspark.ml.feature.Tokenizer</code>
2. The tokenized text is transformed into feature vectors using the count vectorizer <code>pyspark.ml.feature.CountVectorizer</code>
3. The label is encoded to feed into the model using <code>pyspark.ml.feature.StringIndexer</code>
4. Finally, we train a logistic regression model with cross validation & hyper-parameter tuning, on the feature matrix <code>pyspark.ml.classification.LogisticRegression</code>
5. These sequence of steps are encapsulated within a pipeline using <code>pyspark.ml.Pipeline</code>
