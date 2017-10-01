def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB]

    ### create classifier

    ### fit the classifier on the training features and labels

    ### return the fit classifier


        
    ### your code goes here!
    ########################## SVM #################################
    ### we handle the import statement and SVC creation for you here
    ### your code goes here!
    #from sklearn.naive_bayes import GaussianNB
    #######from sklearn.svm import SVC
    ########clf = GaussianNB()
    #######clf = SVC(kernel="rbf", gamma=1.0, C=10000)
    #######fit = clf.fit(features_train,labels_train)
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    fit = clf.fit(features_train, labels_train)

    return fit
