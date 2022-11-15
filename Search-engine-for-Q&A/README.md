# Search Engine for Question & Answering system
## Project Structure
![image](https://user-images.githubusercontent.com/89654615/201868784-49765b44-894f-415c-a9b9-0d48d11faf08.png)

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

### Solution Architecture 
There are 2 parts to the solution. One part involves indexing the 200K question information (title, title vectors) into ElasticSearch. The other part is about searching for the top similar questions to the query question.

![image](https://user-images.githubusercontent.com/89654615/201850777-d8902ceb-2b1a-4adf-b59c-eae291019ceb.png)

### Deployment Architecture 

Two docker containers are used to deploy the solution. One docker container for running the ElasticSearch instance and the other for running the flask application. The flask application is the entrypoint of the solution

![image](https://user-images.githubusercontent.com/89654615/201852392-876c1cd9-d147-430b-98ea-aa95321f3dba.png)




