# Basic Regression using PySpark ML Pipeline
## Overview
I have implemented a simple regression solution using the pyspark machine learning pipeline component. 

## Dataset
Medical Cost Personal Dataset from kaggle was used in this implementation. 

The dataset has the following features :

- age: age of primary beneficiary
- sex: insurance contractor gender, female, male
- bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
- children: Number of children covered by health insurance / Number of dependents
- smoker: Smoking
- region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.
- charges: Individual medical costs billed by health insurance

Link to the dataset : https://www.kaggle.com/datasets/mirichoi0218/insurance


## High Level Design

<img width="869" alt="image" src="https://user-images.githubusercontent.com/89654615/205424415-433c4e8c-abf3-403b-8a09-a02058c067af.png">

1. We convert the raw text into tokens using the <code>pyspark.ml.feature.Tokenizer</code>
2. The tokenized text is transformed into feature vectors using the count vectorizer <code>pyspark.ml.feature.CountVectorizer</code>
3. The label is encoded to feed into the model using <code>pyspark.ml.feature.StringIndexer</code>
4. Finally, we train a logistic regression model with cross validation & hyper-parameter tuning, on the feature matrix <code>pyspark.ml.classification.LogisticRegression</code>
5. These sequence of steps are encapsulated within a pipeline using <code>pyspark.ml.Pipeline</code>
