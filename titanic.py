import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


#titanic = pd.read_csv(r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\Titanic-Dataset.csv")

titanic_data = pd.read_csv("Titanic-Dataset.csv")
#print(titanic_data.head(10))
#print(titanic_data.info())
#print(titanic_data.describe())
#Counting the number of passengers onboard the Titanic
print("Number of passengers in original dataset:" +str(len(titanic_data.index)))
#Counting the of number of passengers who survived
print("Number of passengers who survived:" +str(len(titanic_data[titanic_data["Survived"] == 1].index)))
#Counting the number of passengers who did not survive
print("Number of passengers who did not survive:" +str(len(titanic_data[titanic_data["Survived"] == 0].index)))
#Calculating the percentage of passengers who survived
survival_rate = (len(titanic_data[titanic_data["Survived"] == 1].index) / len(titanic_data.index)) * 100
print("Percentage of passengers who survived: " + str(survival_rate) + "%")
#Calculating the percentage of passengers who did not survive
death_rate = (len(titanic_data[titanic_data["Survived"] == 0].index) / len(titanic_data.index)) * 100
print("Percentage of passengers who did not survive: " + str(death_rate) + "%")
'''
#Plotting the survival rate of passengers onboard the Titanic
sns.countplot(x="Survived", data=titanic_data)
plt.title("Survival Rate of Passengers on the Titanic")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()
'''
'''
#Plotting male and female survival
sns.countplot(x="Survived", hue="Sex", data=titanic_data)
plt.title("Survival Rate of Male and Female on the Titanic")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()
'''
'''
#The class where passengers sat
sns.countplot(x="Survived", hue="Pclass", data=titanic_data)
plt.title("Survival Rate of seating classes on the Titanic")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()
'''
'''
#Plotting the age distribution of passengers who survived and did not survive (titanic_data["Age"].plot.hist())
sns.histplot(data=titanic_data, x="Age", hue="Survived", kde=True, bins=30)
plt.title("Age Distribution of Passengers on the Titanic")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
'''
'''
#plotting the fare distribution (titanic_data["Fare"].plot.hist(bin=20, figsize=(10,5)))
sns.countplot(x="Survived", hue="Fare", data=titanic_data)
plt.title("Survival Rate of Passengers based on Fare on the Titanic")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()
'''
'''
#Plotting sibling relations onboard
sns.countplot(x="Survived", hue="SibSp", data=titanic_data)
plt.title("Survival Rate of Passengers based on Siblings/Spouses on the Titanic")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()
'''
'''
#Plotting parent/child relations onboard
sns.countplot(x="Survived", hue="Parch", data=titanic_data)
plt.title("Survival Rate of Passengers based on Parents/Children on the Titanic")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()
'''
#checking for data wraggling
print(titanic_data.isnull())
print(titanic_data.isnull().sum())
'''
sns.heatmap()(titanic_data.isnull(), cmap="viridis")
plt.title("Missing Data Heatmap")
plt.show()

sns.boxplot(x="Pclass", y="Age", data=titanic_data)
plt.title("Age Distribution of Passengers on the Titanic")
plt.xlabel("Age")
plt.ylabel("Count")
'''

