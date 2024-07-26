from sklearn import tree

#[height, weight, shoe size]
x = [[181,80,44], [177, 70, 43], [165, 55, 30], [170, 60, 39], [173, 62, 40], [200, 100, 50], [190,89,49], [150,40,30]]

y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[165, 55, 30]])

print(prediction)
