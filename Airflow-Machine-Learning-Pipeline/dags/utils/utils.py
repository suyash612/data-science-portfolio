# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:31:38 2022

@author: suyash.pawar
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
import os.path
from sklearn import model_selection
from utils import config
import joblib
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from datetime import datetime

test_size = config.params["test_split_ratio"]
db_engine = config.params["db_engine"]
db_schema = config.params["db_schema"]
table_batch = config.params["db_batch_table"] 
table_name = config.params["db_experiments_table"] 

def save_files(df_list):
    '''
    accepts dataframe list as input
    saves each dataframe in the tmp folder as csv
    the file name corresponds to the dataframe "name" attribute
    '''
    [ df.to_csv('/opt/airflow/data/' + df.name + '.csv' , sep=',', index=False) for df in df_list ]



def load_files(names_list):
    '''
    accepts a list of names (str) as input
    load each csv file from the tmp folder with the input names
    returns a list of loaded dataframes
    '''
    df_list = []
    [ df_list.append(pd.read_csv("/opt/airflow/data/" + name + ".csv")) for name in names_list if os.path.isfile('/opt/airflow/data/' + name + '.csv') ]

    return df_list    

def load_data():
    breast_ds = load_breast_cancer()
    labels = np.reshape(breast_ds.target, (569,1))
    breast_data = np.concatenate([breast_ds.data, labels], axis=1)
    df = pd.DataFrame(breast_data)
    df.columns = np.append(breast_ds.feature_names, 'label')
    df.name="df"
    save_files([df])
    
    

def preprocess_data():

    df = load_files(['df'])[0]
    x_train, x_test, y_train, y_test = model_selection.train_test_split(df.iloc[:,:-1], 
                                                                        df['label'], 
                                                                        test_size=test_size)
    x_train.name = 'x_train'
    x_test.name = 'x_test'
    y_train.name = 'y_train'
    y_test.name = 'y_test'
    save_files([x_train, x_test, y_train, y_test])


def save_batch_data():
    df = load_files(['df'])[0]
    engine = create_engine(db_engine)
    df.to_sql(table_batch, engine, schema=db_schema, if_exists='replace', index=False)
    
    
    
def experiment():

    x_train, x_test, y_train, y_test = load_files(['x_train', 'x_test', 'y_train', 'y_test'])
    
    # the maximum number of principal components to investigate cannot be higher than the number of coolumns in the dataset 
    max_pca_components = config.params["max_pca_components"] if config.params["max_pca_components"] <= x_train.shape[1] else x_train.shape[1]
    cv_folds = config.params["cv_folds"] 
    logreg_maxiter = config.params["logreg_maxiter"]

    # pipeline definition
    std_scaler = StandardScaler()
    pca = PCA(max_pca_components-1)
    log_reg = LogisticRegression(max_iter=logreg_maxiter)

    pipe = Pipeline(steps=[('std_scaler', std_scaler),
                        ('pca', pca), 
                        ('log_reg', log_reg)])

    # parameters for hyper-parameter tuning
    params = {
        'pca__n_components': list(range(1, max_pca_components)),
        'log_reg__C': np.logspace(0.05, 0.1, 1)
    }

    # cross-validated training through grid search
    grid_search = GridSearchCV(pipe, params, cv=cv_folds)
    grid_search.fit(x_train, y_train)

    # selection of the best parameters 
    best_c = round(grid_search.best_params_.get("log_reg__C"),2)
    best_princ_comp = grid_search.best_params_.get("pca__n_components")
    
    # performances on test set
    y_test_predicted = grid_search.best_estimator_.predict(x_test)
    test_set_accuracy = round(accuracy_score(y_test, y_test_predicted),3)

    # save esperiments information for historical persistence
    now = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

    exp_info = pd.DataFrame([[now,
                          cv_folds,
                          logreg_maxiter,
                          max_pca_components,
                          best_c,
                          best_princ_comp,
                          test_set_accuracy]],
                          columns=['experiment_datetime',
                                   'cv_folds',
                                   'logreg_maxiter',
                                   'max_pca_components', 
                                   'best_logreg_c',
                                   'best_pca_components',
                                   'test_set_accuracy'
                                   ])
    exp_info.name = 'exp_info'

    save_files([exp_info])    
    
    
def track_experiments_info():
    df = load_files(['exp_info'])[0]
    engine = create_engine(db_engine)
    df.to_sql(table_name, engine, schema=db_schema, if_exists='append', index=False)    
    
    
def fit_best_model():
    
    df, best_params = load_files(['df', 'exp_info'])
    pipe = Pipeline([('scaler', StandardScaler()),
                 ('pca', PCA(n_components = best_params['best_pca_components'].values[0])),
                 ('log_reg', LogisticRegression(C=best_params['best_logreg_c'].values[0]))
                 ])     
    pipe.fit(df.iloc[:,:-1], df['label'])

    # save best model
    now = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    filename = 'model_' + now + '.pkl'
    joblib.dump(pipe, '/opt/airflow/models/' + filename, compress=1)    