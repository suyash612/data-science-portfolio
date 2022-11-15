# Search Engine for Question & Answering system
## Problem Statement
Given a question, we have to find similar questions from a repository of question & answers. A relevant example of where this is applicable is Stack overflow

![image](https://user-images.githubusercontent.com/89654615/201689740-9fe362ff-282b-4f08-a09e-ba355f3f4b87.png)

## Dataset
StackSample dataset from kaggle was used in this implementation and it contains 10% of Stack Overflow Q&A. Due to memory constriant of the local system, a sample set of 200K questions was used for experimentation
https://www.kaggle.com/datasets/stackoverflow/stacksample



## High Level Design
The most important fields to find the similar question are the Title and the Body of the questions. In this implementation, we will consider only the title of the questions from the data store. We check combined similarity using keyword search as well as semantic similarity. Cosine similarity function within ElasticSearch is used for computing the similarity<br/>  
Tech Stack :
  - ElasticSearch for storing the questions repository and retrieving top similar questions, to the query question
  - Pre-trained Universal Sentence Encoder (USE) for generating title vectors/embeddings
  - Docker for containerisation of the application  
  - Flask for creating a web app of the solution
