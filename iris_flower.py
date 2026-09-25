#Check the versions of the libraries used in this project
#Python version
import sys
print('Python: {}' .format(sys.version))
#Scipy
import scipy
print('Scipy: {}' .format(scipy.__version__))
#Numpy
import numpy
print('Numpy: {}' .format(numpy.__version__))
#Matplotlib
import matplotlib
print('Matplotlib: {}' .format(matplotlib.__version__))
#Seaborn
import seaborn
print('Seaborn: {}' .format(seaborn.__version__))
#Scikit-learn
import sklearn
print('sklearn: {}' .format(sklearn.__version__))
#Pandas
import pandas
print('Pandas: {}' .format(pandas.__version__))
#Statsmodels
import statsmodels
print('statsmodels: {}' .format(statsmodels.__version__))

#Load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.svm import SVR

#load dataset
###url = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\iris.csv"
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = pd.read_csv(url, names=names)

#url = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\iris.csv"
#url = "C:\\Users\\wisdo\\OneDrive\\Desktop\\COMPUTING\\ML\\iris.csv"
#url = "C:/Users/wisdo/OneDrive/Desktop/COMPUTING/ML/iris.csv"

#dataset.iloc[:,0:4] = dataset.iloc[:,0:4].apply(pd.to_numeric) #Force numeric conversion
#print(dataset.head())
#print(dataset.dtypes)
#print(dataset.describe())
#print(dataset.info())
#print(dataset.shape)
#print(dataset.groupby('class').size())
#dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
#dataset.hist()
#scatter_matrix(dataset)
#plt.show()

array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 6
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

seed = 6
scoring ='accuracy'
#Spot check algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
#Evaluate each model in turn
results = []
names = []
for name, model in models:
    #kfold = model_selection.KFold(n_splits=10, random_state=seed)
    kfold = model_selection.KFold(n_splits=10, shuffle=True, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

#Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()