# AWS SageMaker pipeline with conditional step
## Overview
I have implemented a regression problem using the AWS SageMaker pipeline, with a conditional performance threshold step. 

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

1. Define a set of Pipeline parameters that can be used to parametrize a SageMaker Pipeline.
2. Define a Processing step that performs cleaning, feature engineering, and splitting the input data into train and test data sets.
3. Define a Training step that trains a model on the preprocessed train data set.
4. Define a Processing step that evaluates the trained model's performance on the test dataset.
5. Define a Conditional step that measures a condition based on output from prior steps and conditionally executes other steps.
6. Define a Create Model step that creates a model from the model artifacts used in training.
7. Define a Transform step that performs batch transformation based on the model that was created.
8. Define a Register Model step that creates a model package from the estimator and model artifacts used to train the model.
9. Define a Fail step with a customized error message indicating the cause of the execution failure.
10. Define and create a Pipeline definition in a DAG, with the defined parameters and steps.
11. Start a Pipeline execution and wait for execution to complete.

