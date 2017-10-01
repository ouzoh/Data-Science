import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################
from sklearn import tree
clf = tree.DecisionTreeClassifier()
fit = clf.fit(features_train, labels_train)

pred=clf.predict(features_test)
#### your code goes here


from sklearn.metrics import accuracy_score

acc = accuracy_score(labels_test, pred)### you fill this in!
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}
