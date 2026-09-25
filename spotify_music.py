import pandas as pd
import seaborn as sns
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt


#path to the Spotify data to read
spotify_file_path = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\spotify.csv"
spotify_data = pd.read_csv(spotify_file_path, index_col="Date", parse_dates=True)
#Print the first 5 rows of the spotify dataset
#print(spotify_data.head())
print("---------------------------------------------------------------------------------------")
#Print the last 5 rows of the dataset
#print(spotify_data.tail())
print("---------------------------------------------------------------------------------------")
#Print the column names of the dataset
print(spotify_data.columns)
print("---------------------------------------------------------------------------------------")
#Print the data types of each column
#print(spotify_data.dtypes)
print("---------------------------------------------------------------------------------------")
#Print the summary statistics of the dataset
#print(spotify_data.describe())
print("---------------------------------------------------------------------------------------")
#Print the number of missing values in each column
#print(spotify_data.isnull().sum())
print("---------------------------------------------------------------------------------------")
#Print the number of unique values in each column
#print(spotify_data.nunique())
print("---------------------------------------------------------------------------------------")
#Print the correlation matrix of the dataset
#print(spotify_data.corr())
print("---------------------------------------------------------------------------------------")
#Create a heatmap of the correlation matrix
#sns.heatmap(spotify_data.corr(), annot=True, cmap="coolwarm")
print("---------------------------------------------------------------------------------------")

#Line chart showing daily global streams of each song
'''plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.title("Daily Global Streams of Each Song")
plt.xlabel("Date")
plt.ylabel("Daily Global Streams")
plt.legend()
plt.show()'''

print(list(spotify_data.columns))

#plotting subset of the data
#set the width and height of the figure
plt.figure(figsize=(14, 6))
#Add title
plt.title("daily global streams of popular songs in 2017-2018")
#Line chart showing daily global streams of 'Shape of you'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")
#Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
plt.legend()
plt.xlabel("Date")
plt.show()