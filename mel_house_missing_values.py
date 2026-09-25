import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

#Load data from source
melb_data_filepath = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"
melb_data = pd.read_csv(melb_data_filepath)

#select target to predict
y = melb_data['Price']
#y = melb_data.Price

#To keep things simple, we'll use only numerical predictors
melb_predictors = melb_data.drop('Price', axis=1)
x = melb_predictors.select_dtypes(exclude=['object'])

#Divide data into training and validation subsets
x_train, x_valid, y_train, y_valid = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)

def score_dataset(x_train, y_train, x_valid, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(x_train, y_train)
    preds = model.predict(x_valid)
    return mean_absolute_error(y_valid, preds)

#Score from approach 1 (drop missing values)
col_missing_values = [col for col in x_train.columns
                      if x_train[col].isnull().any()]

#Drop columns in training and validation data
reduced_x_train = x_train.drop(col_missing_values, axis=1)
reduced_x_valid = x_valid.drop(col_missing_values, axis=1)

print("MAE from Approach 1 (Drop columns with missing values): ")
print(score_dataset(reduced_x_train, y_train, reduced_x_valid, y_valid))
print("--------------------------------------------------------------------------------")

#Score from Approach 2 (Imputation)
#Imputation
#my_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
my_imputer = SimpleImputer(strategy='mean')
imputed_x_train = pd.DataFrame(my_imputer.fit_transform(x_train))
imputed_x_valid = pd.DataFrame(my_imputer.transform(x_valid))

#Imputation removed column names; put them back
imputed_x_train.columns = x_train.columns
imputed_x_valid.columns = x_valid.columns

print("MAE from Approach 2 (Imputation): ")
print(score_dataset(imputed_x_train, y_train, imputed_x_valid, y_valid))
print("--------------------------------------------------------------------------------")

#Score from Approach 3 ( An Extension to Imputation)
#Make copy of the data so that imputation doesn't affect the original data
x_train_plus = x_train.copy()
x_valid_plus = x_valid.copy()

#make new columns indicating what will be imputed
for col in col_missing_values:
    x_train_plus[col + '_was_missing'] = x_train_plus[col].isnull()
    x_valid_plus[col + '_was_missing'] = x_valid_plus[col].isnull()

#Imputation
my_imputer =SimpleImputer()
imputed_x_train_plus = pd.DataFrame(my_imputer.fit_transform(x_train_plus))
imputed_x_valid_plus = pd.DataFrame(my_imputer.transform(x_valid_plus))

#Imputation removed column name; put them back
imputed_x_train_plus.columns = x_train_plus.columns
imputed_x_valid_plus.columns = x_valid_plus.columns

print("MAE from Approach 3 (An Extension to Imputation): ")
print(score_dataset(imputed_x_train_plus, y_train, imputed_x_valid_plus, y_valid))
print("----------------------------------------------------------------------------")

#Shape of training data(number of rows and columns)
print("Shape of training data (number of rows and columns): ")
print(x_train.shape)
print("Shape of valid data (number of rows and columns): ")
print(x_valid_plus.shape)
#Number of missing values in each column of training data
train_missing_val_count_by_column = (x_train.isnull().sum())
valid_missing_val_count_by_column = (x_valid.isnull().sum())
print("Total missing number of columns in the training data: ")
print(train_missing_val_count_by_column[train_missing_val_count_by_column > 0])
print("Total missing number of columns in the valid data: ")
print(valid_missing_val_count_by_column[valid_missing_val_count_by_column > 0])

