# Iris Flower Classification (Updated for modern libraries)

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

names = ['sepal-length','sepal-width','petal-length','petal-width','class']

dataset = pd.read_csv(url, names=names)

# --------------------------------------------------
# 2. Explore Data
# --------------------------------------------------

print("Dataset shape:")
print(dataset.shape)

print("\nFirst 5 rows:")
print(dataset.head())

print("\nClass distribution:")
print(dataset.groupby('class').size())

print("\nStatistical summary:")
print(dataset.describe())

# --------------------------------------------------
# 3. Data Visualisation
# --------------------------------------------------

# Box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# Histograms
dataset.hist()
plt.show()

# Scatter matrix
pd.plotting.scatter_matrix(dataset)
plt.show()

# --------------------------------------------------
# 4. Split Data
# --------------------------------------------------

array = dataset.values

X = array[:,0:4]
y = array[:,4]

X_train, X_validation, Y_train, Y_validation = train_test_split(
    X, y, test_size=0.20, random_state=1
)

# --------------------------------------------------
# 5. Build Models
# --------------------------------------------------

models = []
models.append(('LR', LogisticRegression(max_iter=200)))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# --------------------------------------------------
# 6. Evaluate Models
# --------------------------------------------------

results = []
names = []

for name, model in models:
    kfold = KFold(n_splits=10, shuffle=True, random_state=1)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)

    print(f"{name}: {cv_results.mean():.3f} ({cv_results.std():.3f})")

# --------------------------------------------------
# 7. Compare Algorithms
# --------------------------------------------------

plt.boxplot(results, tick_labels=names)
plt.title('Algorithm Comparison')
plt.show()

# --------------------------------------------------
# 8. Make Predictions
# --------------------------------------------------

model = SVC()
model.fit(X_train, Y_train)

predictions = model.predict(X_validation)

print("\nAccuracy:", accuracy_score(Y_validation, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(Y_validation, predictions))
print("\nClassification Report:")
print(classification_report(Y_validation, predictions))

"""
What This Script Produces: You will see: 📊 Data exploration, dataset size, summary statistics, 📈 Graphs box plots,
histograms, scatter matrix, 🤖 Machine learning models tested, Logistic Regression, Linear Discriminant Analysis,
KNN, Decision Tree, Naive Bayes, Support Vector Machine, 📉 Evaluation cross-validation, accuracy model comparison plot
🎯Final prediction, accuracy score, confusion matrix, classification report, Typical Output

Example results:
LR: 0.975 (0.038)
LDA: 0.975 (0.038)
KNN: 0.983 (0.033)
CART: 0.967 (0.040)
NB: 0.975 (0.053)
SVM: 0.983 (0.033)

Accuracy usually ends up around 96–99%.
"""