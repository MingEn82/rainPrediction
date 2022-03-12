from math import comb
import os
import pandas as pd

filenames = [os.path.join(os.getcwd(), 'csv', file) for _, _, files in os.walk('./csv') for file in files]

colnames=['Station', 'Year', 'Month', 'Day', 'Daily Rainfall Total (mm)', 'Highest 30 Min Rainfall (mm)','Highest 60 Min Rainfall (mm)','Highest 120 Min Rainfall (mm)','Mean Temperature (°C)','Maximum Temperature (°C)','Minimum Temperature (°C)','Mean Wind Speed (km/h)','Max Wind Speed (km/h)'] 
combined_csv = pd.concat([pd.read_csv(file, skiprows=1, names=colnames) for file in filenames])
print(combined_csv)

combined_csv.to_csv('combined.csv')
