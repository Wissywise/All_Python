#Importing modules to use
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#Load the melbourne data
melbourne_file_path = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
#filtering out rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
#Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]


# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#We build a random forest model similarly to how we built a decision tree in scikit-learn - this time using the RandomForestRegressor
#class instead of DecisionTreeRegressor
forest_model = RandomForestRegressor(random_state=1)
#Fit the model to the training data
forest_model.fit(X_train, y_train)
# get predicted prices on validation data
melb_preds = forest_model.predict(X_test)
#Calculate MAE
melb_mae = mean_absolute_error(y_test, melb_preds)
print("Mean Absolute Error:", melb_mae)
print("--------------------------------------------------------------------------------------------------------")
print(melbourne_data["Price"])
print("----------------------------------------------------------------------------------------------------------")
print(filtered_melbourne_data["Price"])
print("-----------------------------------------------------------------------------------------------------------")
print(filtered_melbourne_data.describe())
print("-------------------------------------------------------------------------------------------------------------")
print(filtered_melbourne_data.head())
print("--------------------------------------------------------------------------------------------------------------")
print(melb_preds)