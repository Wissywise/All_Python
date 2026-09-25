import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Flight data path
flight_filepath = r"C:\Users\wisdo\OneDrive\Desktop\COMPUTING\ML\flight_delays.csv"
#Read the data and store it in DataFrame titled flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month")
#Print the summary of the data in flight_data
print(flight_data.describe())
print("--------------------------------------------------------------------------------------------")
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
print(flight_data)
print("--------------------------------------------------------------------------------------------")
print(flight_data.columns)
print("--------------------------------------------------------------------------------------------")
#Plotting the distribution of flight delays
#sns.histplot(data=flight_data, x="Delay", bins=30, kde=True)
plt.figure(figsize=(10, 6)) #Set the width and height of the figure
plt.title("Average arrival delay for Spirit Airlines Flights, by Month") #add title
#Bar chart showing averagearrival delay for Spirit Airlines Flights bu Month
sns.barplot(x=flight_data.index, y=flight_data['NK'])
plt.ylabel("Arrival delay(in minutes)")
plt.show()

#set the width and height of the figure
plt.figure(figsize=(14,7))
#add title
plt.title("Average Arrival Dealay for Each Airlin, by Month")
#heatmap showing arrival delay for each airline, by month
sns.heatmap(data=flight_data, annot=True)
#add label for horizontal axis
plt.xlabel("Airline")
plt.show()