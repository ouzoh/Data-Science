#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess



### features_train and features_test are the features for the training
### and testing datasets, respectively

features_train, features_test, labels_train, labels_test = preprocess()

### labels_train and labels_test are the corresponding item labels
### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB
### create classifier
clf = GaussianNB()

### fit the classifier on the training features and labels
t0 = time() # timing your NB Classifier
fit=clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s" #duration the NB Classifier takes

#print (clf.predict(features_test))
t0 = time() # timing of prediction
pred=clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s" #duration the NB Classifier takes

#########################################################
### your code goes here ###
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print "The accuracy is:",round(accuracy,4)
#########################################################
