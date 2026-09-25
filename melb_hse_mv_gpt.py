# Import pandas for data handling
import pandas as pd

# Import function to split dataset
from sklearn.model_selection import train_test_split

# Import machine learning model
from sklearn.ensemble import RandomForestRegressor

# Import evaluation metric
from sklearn.metrics import mean_absolute_error


# -------------------------------
# LOAD DATA
# -------------------------------

# File path to dataset
melb_data_filepath = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"

# Read CSV into DataFrame
melb_data = pd.read_csv(melb_data_filepath)

# Remove rows where target ('Price') is missing
# We cannot train a model without target values
melb_data = melb_data.dropna(subset=['Price'])


# -------------------------------
# DEFINE TARGET AND FEATURES
# -------------------------------

# Target variable (what we want to predict)
y = melb_data['Price']

# Feature variables (input data)
# Drop target column so it is not used as input
X = melb_data.drop('Price', axis=1)

# Keep only numerical columns (drop text columns)
# RandomForest cannot directly handle strings
X = X.select_dtypes(exclude=['object'])


# -------------------------------
# SPLIT DATA
# -------------------------------

# Split into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y,
    test_size=0.2,     # 20% for validation
    random_state=0     # ensures reproducibility
)


# -------------------------------
# APPROACH 1: DROP COLUMNS WITH MISSING VALUES
# -------------------------------

# Identify columns that contain missing values in training data
cols_with_missing = [
    col for col in X_train.columns
    if X_train[col].isnull().any()
]

# Drop those columns from training data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)

# Drop the same columns from validation data
# (important to keep both datasets aligned)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)


# -------------------------------
# MODEL FUNCTION
# -------------------------------

def score_dataset(X_train, y_train, X_valid, y_valid):
    """
    Train a model and return Mean Absolute Error.
    """

    # Create Random Forest model
    model = RandomForestRegressor(
        n_estimators=10,
        random_state=0
    )

    # Train model on training data
    model.fit(X_train, y_train)

    # Predict on validation data
    preds = model.predict(X_valid)

    # Return MAE (lower is better)
    return mean_absolute_error(y_valid, preds)


# -------------------------------
# EVALUATE MODEL
# -------------------------------

print("MAE from Approach 1 (Drop columns with missing values):")

# Call function with processed datasets
print(score_dataset(
    reduced_X_train,
    y_train,
    reduced_X_valid,
    y_valid
))

print("-------------------------------------------------------------------------------------------")

# Import pandas
import pandas as pd

# Import tools from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer   # for filling missing values


# -------------------------------
# LOAD DATA
# -------------------------------

melb_data_filepath = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"

# Read dataset
melb_data = pd.read_csv(melb_data_filepath)

# Drop rows where target is missing
melb_data = melb_data.dropna(subset=['Price'])


# -------------------------------
# DEFINE TARGET AND FEATURES
# -------------------------------

# Target variable
y = melb_data['Price']

# Feature variables
X = melb_data.drop('Price', axis=1)

# Keep only numeric columns
X = X.select_dtypes(exclude=['object'])


# -------------------------------
# SPLIT DATA
# -------------------------------

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y,
    test_size=0.2,
    random_state=0
)


# -------------------------------
# APPROACH 2: IMPUTATION
# -------------------------------

# Create imputer object
# strategy='mean' → replace missing values with column mean
imputer = SimpleImputer(strategy='mean')

# Fit imputer on training data and transform it
# (learn mean from training data ONLY)
imputed_X_train = pd.DataFrame(
    imputer.fit_transform(X_train)
)

# Apply same transformation to validation data
# (use the same means learned earlier)
imputed_X_valid = pd.DataFrame(
    imputer.transform(X_valid)
)

# After transformation, column names are lost → restore them
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns


# -------------------------------
# MODEL FUNCTION
# -------------------------------

def score_dataset(X_train, y_train, X_valid, y_valid):
    """
    Train model and return MAE.
    """

    # Create model
    model = RandomForestRegressor(
        n_estimators=10,
        random_state=0
    )

    # Train model
    model.fit(X_train, y_train)

    # Predict
    preds = model.predict(X_valid)

    # Evaluate performance
    return mean_absolute_error(y_valid, preds)


# -------------------------------
# EVALUATE MODEL
# -------------------------------

print("MAE from Approach 2 (Imputation):")

print(score_dataset(
    imputed_X_train,
    y_train,
    imputed_X_valid,
    y_valid
))

print("--------------------------------------------------------------------------------")

# Import pandas for data handling
import pandas as pd

# Import function to split dataset into training and validation sets
from sklearn.model_selection import train_test_split

# Import the machine learning model (Random Forest)
from sklearn.ensemble import RandomForestRegressor

# Import evaluation metric (Mean Absolute Error)
from sklearn.metrics import mean_absolute_error

# Import tool for handling missing values (imputation)
from sklearn.impute import SimpleImputer


# -------------------------------
# LOAD AND PREPARE DATA
# -------------------------------

# File path to your dataset (Melbourne housing data)
melb_data_filepath = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"

# Read the CSV file into a pandas DataFrame
melb_data = pd.read_csv(melb_data_filepath)

# Remove rows where the target variable 'Price' is missing
# (because we cannot train a model without the correct output)
melb_data = melb_data.dropna(subset=['Price'])


# -------------------------------
# DEFINE TARGET AND FEATURES
# -------------------------------

# Target variable (what we want to predict)
y = melb_data['Price']

# Feature set (input variables)
# Drop the target column so it is not used as input
X = melb_data.drop('Price', axis=1)

# Keep only numerical columns (drop text/categorical columns)
# This simplifies the model since RandomForest needs numeric input
X = X.select_dtypes(exclude=['object'])


# -------------------------------
# SPLIT DATA INTO TRAIN/VALIDATION
# -------------------------------

# Split data into:
# - Training set (80%) → used to train the model
# - Validation set (20%) → used to evaluate performance
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y,
    test_size=0.2,      # 20% validation data
    random_state=0      # ensures reproducibility
)


# -------------------------------
# APPROACH 3: ADD MISSING VALUE INDICATORS
# -------------------------------

# Create copies so we don't modify the original datasets
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()

# Identify columns that contain missing values in training data
cols_with_missing = [
    col for col in X_train.columns
    if X_train[col].isnull().any()
]

# For each column with missing data:
for col in cols_with_missing:

    # Create a new column that stores True/False
    # True = value was missing, False = value was present
    X_train_plus[col + "_was_missing"] = X_train[col].isnull()
    X_valid_plus[col + "_was_missing"] = X_valid[col].isnull()


# -------------------------------
# IMPUTE (FILL) MISSING VALUES
# -------------------------------

# Create an imputer object
# strategy='mean' → replace missing values with column mean
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on training data and transform it
# (learn mean values from training set only)
imputed_X_train = pd.DataFrame(
    imputer.fit_transform(X_train_plus)
)

# Apply the same transformation to validation data
# (use means learned from training data)
imputed_X_valid = pd.DataFrame(
    imputer.transform(X_valid_plus)
)

# After imputation, column names are lost → restore them
imputed_X_train.columns = X_train_plus.columns
imputed_X_valid.columns = X_valid_plus.columns


# -------------------------------
# MODEL TRAINING AND EVALUATION FUNCTION
# -------------------------------

def score_dataset(X_train, y_train, X_valid, y_valid):
    """
    Train a RandomForest model and return MAE score.

    Parameters:
    X_train → training features
    y_train → training target
    X_valid → validation features
    y_valid → validation target

    Returns:
    Mean Absolute Error (lower is better)
    """

    # Create the model
    model = RandomForestRegressor(
        n_estimators=10,   # number of trees
        random_state=0     # reproducibility
    )

    # Train the model on training data
    model.fit(X_train, y_train)

    # Make predictions on validation data
    preds = model.predict(X_valid)

    # Calculate and return MAE
    return mean_absolute_error(y_valid, preds)


# -------------------------------
# EVALUATE MODEL
# -------------------------------

# Print evaluation result for Approach 3
print("MAE from Approach 3 (Imputation + Indicators):")

# Call the function with processed datasets
print(score_dataset(
    imputed_X_train,
    y_train,
    imputed_X_valid,
    y_valid
))

print("------------------------------------------------------------------------------")
'''Raw data
   ↓
ColumnTransformer
   ├── Impute numeric columns (+ missing indicators)
   ↓
RandomForest model'''

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# NEW imports for pipeline approach
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


# -------------------------------
# LOAD DATA
# -------------------------------

melb_data_filepath = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\melb_data.csv"
melb_data = pd.read_csv(melb_data_filepath)

# Remove rows with missing target
melb_data = melb_data.dropna(subset=['Price'])


# -------------------------------
# DEFINE TARGET AND FEATURES
# -------------------------------

y = melb_data['Price']

X = melb_data.drop('Price', axis=1)

# Select only numeric columns
numeric_cols = X.select_dtypes(exclude=['object']).columns


# -------------------------------
# SPLIT DATA
# -------------------------------

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y,
    test_size=0.2,
    random_state=0
)


# -------------------------------
# PREPROCESSING PIPELINE
# -------------------------------

# Step for numeric data:
# - Fill missing values with mean
# - Add indicator columns automatically
numeric_transformer = SimpleImputer(
    strategy='mean',
    add_indicator=True   # 🔥 this replaces your manual indicator step
)

# Combine transformations (only numeric in this case)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols)
    ]
)


# -------------------------------
# FULL PIPELINE (PREPROCESS + MODEL)
# -------------------------------

model = RandomForestRegressor(
    n_estimators=10,
    random_state=0
)

# Pipeline ensures steps happen in correct order
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', model)
])


# -------------------------------
# TRAIN MODEL
# -------------------------------

pipeline.fit(X_train, y_train)


# -------------------------------
# MAKE PREDICTIONS
# -------------------------------

preds = pipeline.predict(X_valid)


# -------------------------------
# EVALUATE MODEL
# -------------------------------

print("MAE with Pipeline (Imputation + Indicators):")
print(mean_absolute_error(y_valid, preds))