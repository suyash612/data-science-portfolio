# Basic Text classification using PySpark ML Pipeline
## Overview
I have implemented a simple multi-class text classification solution using the pyspark machine learning pipeline component. 

## Dataset
Ecommerce text dataset from kaggle was used in this implementation

The dataset has the following features :

- Data Set Characteristics: Multivariate
- Number of Instances: 50425
- Number of classes: 4
- Area: Computer science
- Attribute Characteristics: Real
- Number of Attributes: 1
- Associated Tasks: Multi-class Classification

Link to dataset : https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification  


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

## Instructions for Running the project
1. Build the elasticsearch docker image from the ./docker images/elasticsearch/ </br>
 <code>docker build -t es_deploy . </code>
2. Run the elasticsearch docker image in a container </br>
 <code>docker run --net=host -m 3G --publish 9200:9200 -e "discovery.type=single-node" --name es_deploy es_deploy </code>
3. Build the flask application docker image from the root/outermost directory </br> 
<code>docker build -t flask-app . </code>
4. Run the flask application docker image in a container </br> 
<code>docker run --net=host flask-app</code>

Hit the flask app URL with the search query/question. The result will contain top matching questions through default keyword search (KW) and through semantic similarity respectively (Example below)

![image](https://user-images.githubusercontent.com/89654615/201875300-6453952c-a384-4345-bf79-90beec3efce4.png)



