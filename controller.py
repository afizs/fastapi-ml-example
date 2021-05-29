from sklearn.datasets import load_iris 
from sklearn.naive_bayes import GaussianNB 

# Loading Iris Dataset 
iris = load_iris() 
  
# Getting our Features and Targets 
X = iris.data 
Y = iris.target 
  
# Creating and Fitting our Model 
clf = GaussianNB() 
clf.fit(X,Y) 