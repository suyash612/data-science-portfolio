# Basic Clustering using PySpark ML 
## Overview
I have implemented a simple Clustering solution using the pyspark machine learning library spark.ml 

## Dataset
Online Retail Data Set from kaggle was used from UCI ML repository. This is a transactional data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail

The dataset has the following features :

- InvoiceNo: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation.
- StockCode: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.
- Description: Product (item) name. Nominal.
- Quantity: The quantities of each product (item) per transaction. Numeric.
- InvoiceDate: Invice Date and time. Numeric, the day and time when each transaction was generated.
- UnitPrice: Unit price. Numeric, Product price per unit in sterling.
- CustomerID: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.
- Country: Country name. Nominal, the name of the country where each customer resides.

Link to the dataset : https://archive.ics.uci.edu/ml/datasets/online+retail#  


## High Level Design

<img width="869" alt="image" src="https://user-images.githubusercontent.com/89654615/205424415-433c4e8c-abf3-403b-8a09-a02058c067af.png">

1. We convert the raw text into tokens using the <code>pyspark.ml.feature.Tokenizer</code>
2. The tokenized text is transformed into feature vectors using the count vectorizer <code>pyspark.ml.feature.CountVectorizer</code>
3. The label is encoded to feed into the model using <code>pyspark.ml.feature.StringIndexer</code>
4. Finally, we train a logistic regression model with cross validation & hyper-parameter tuning, on the feature matrix <code>pyspark.ml.classification.LogisticRegression</code>
5. These sequence of steps are encapsulated within a pipeline using <code>pyspark.ml.Pipeline</code>
