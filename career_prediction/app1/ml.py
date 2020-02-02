# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:09:25 2019

@author: DELL
"""
def model():
    import pandas as pd
    import numpy as np
    import pickle
    import matplotlib.pyplot as plt
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath=os.path.join(BASE_DIR,"app1")
    file2=os.path.join(filepath,"roo_data.csv")
    dataset = pd.read_csv(file2)
    data = dataset.iloc[:, :-1].values
    label = dataset.iloc[:, -1].values
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder = LabelEncoder()
    for i in range(14, 36):
        data[:, i] = labelencoder.fit_transform(data[:, i])
    with open('labelencoder.bin','wb') as ff:
        pickle.dump(labelencoder,ff)
    #print(data[:, 15])
    from sklearn.preprocessing import Normalizer
    data1 = data[:, :14]
    normalized_data = Normalizer().fit_transform(data1)
    #print(normalized_data.shape)
    data2 = data[:, 14:]
    df1 = np.append(normalized_data, data2, axis=1)
    #print(df1.shape)
    X1 = pd.DataFrame(df1, columns=['Acedamic percentage in Operating Systems', 'percentage in Algorithms',
                                'Percentage in Programming Concepts',
                                'Percentage in Software Engineering', 'Percentage in Computer Networks',
                                'Percentage in Electronics Subjects',
                                'Percentage in Computer Architecture', 'Percentage in Mathematics',
                                'Percentage in Communication skills', 'Hours working per day',
                                'Logical quotient rating', 'hackathons', 'coding skills rating',
                                'public speaking points', 'can work long time before system?',
                                'self-learning capability?', 'Extra-courses did', 'certifications',
                                'workshops', 'talenttests taken?', 'olympiads',
                                'reading and writing skills', 'memory capability score',
                                'Interested subjects', 'interested career area ', 'Job/Higher Studies?',
                                'Type of company want to settle in?',
                                'Taken inputs from seniors or elders', 'interested in games',
                                 'Salary Range Expected',
                                'In a Realtionship?', 'Gentle or Tuff behaviour?',
                                'Management or Technical', 'hard/smart worker',
                                'worked in teams ever?', 'Introvert'])
    label = labelencoder.fit_transform(label)
    y = pd.DataFrame(label, columns=["Suggested Job Role"])
    #y.head()
    from sklearn import tree
    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    from sklearn.metrics import accuracy_score
    X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.3, random_state=10)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    with open('model_pickel.bin','wb') as f:
        pickle.dump(clf,f)
    """from sklearn.metrics import confusion_matrix, accuracy_score
    y_pred = clf.predict(X_test)
    y_pred
    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    print("confusion matrics=", cm)
    print("  ")
    print("accuracy=", accuracy * 100)"""
    print("yes")


