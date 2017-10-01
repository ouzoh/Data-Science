#!/usr/bin/python

"""
    This is the code to accompany the Nearest Neighbor classifier

    Use a Nearest Neighbor classifier to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time



sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
### we handle the import statement and Nearest Neighbor classifier creation for you here
from sklearn.neighbors import KNeighborsClassifier


clf = KNeighborsClassifier(n_neighbors=1) 
print clf

#### now your job is to fit the classifier
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
#### using the training features/labels, and to
#### make a set of predictions on the test data
t0 = time() # timing your Classifier
fit=clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s" #duration the NB Classifier takes

#### store your predictions in a list named pred
t0 = time() # timing of prediction
pred=clf.predict(features_test)
#a=pred.tolist()

print "pred:", pred
print "label:",labels_train
#print "a:",a
#print "a count:", a.count(1)



print "predicting time:", round(time()-t0, 3), "s" #duration the Classifier takes


from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)
print "The accuracy is:", acc

def submitAccuracy():
    return acc
