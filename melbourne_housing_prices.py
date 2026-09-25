#Import panda library for data manipulation
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import numpy as np

#Save filepath to variable for easier access
melbourne_file_path = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"
#Read the data and store it in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
#Print the summary of the data in melbourne_data
#print(melbourne_data.describe())
#print(melbourne_data.head())
#print(melbourne_data.columns)
# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)
#Choosing the prediction target
y = melbourne_data["Price"]
#Selecting the features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
#By convention this features is called
x = melbourne_data[melbourne_features]
print(x.describe())
print("--------------------------------------------------------------------------------------------")
print(x.head())
print("--------------------------------------------------------------------------------------------")

# Define the model and Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)
#Fitting the model
melbourne_model.fit(x, y)
#Making predictions for the first 5 houses
print("Making predictions for the following 5 houses")
print(x.head())
print("Predictions are:")
print(melbourne_model.predict(x.head()))
#print(melbourne_model.predict(x[melbourne_features[:5]]))





