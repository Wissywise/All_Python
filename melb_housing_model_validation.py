import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.tree import DecisionTreeRegressor



#Loading the data
melbourne_file_path = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
#Filter rows with missing price values
filter_melbourne_data = melbourne_data.dropna(subset=['Price'])
#select target and features
y = filter_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filter_melbourne_data[melbourne_features]
#split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
#Define model
melbourne_model = DecisionTreeRegressor(random_state=1)
#Fit model to training data
melbourne_model.fit(train_X,train_y)
#Predict with the model
predicted_home_prices = melbourne_model.predict(X)
print(predicted_home_prices)
#get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(y,predicted_home_prices))
print(mean_squared_error(y,predicted_home_prices))

#Evaluate the model
#mae = mean_absolute_error(val_y, val_predictions)
#mse = mean_squared_error(val_y, val_predictions)
#print("Mean Absolute Error:", mae)
#print("Mean Squared Error:", mse)