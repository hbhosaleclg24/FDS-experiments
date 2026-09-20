import pandas as pd
import numpy as np

# 1.
df = pd.read_csv(r"C:\Users\Harshvardhan Bhosale\OneDrive\Desktop\Assignments vs code\EV_Energy_Consumption_Dataset (1).csv")

# 2 & 3. 
print("Dataset Info:")
df.info()
print("\nDataset Description:")
print(df.describe())

# 4. 
null_counts = df.isnull().sum()
print("\nNull Values Count:\n", null_counts)
if null_counts.sum() == 0:
    df.loc[0:10, 'Speed_kmh'] = np.nan
print("\nNulls in Speed_kmh before imputation:", df['Speed_kmh'].isnull().sum())

# 5.
df.fillna({'Speed_kmh': df['Speed_kmh'].mean()}, inplace=True)
print("Nulls in Speed_kmh after imputation:", df['Speed_kmh'].isnull().sum())

# 6.
top_5_filtered = df[df['Speed_kmh'] > 100].sort_values(by='Energy_Consumption_kWh', ascending=False).head(5)
print("\nTop 5 Records (Speed > 100) by Energy Consumption:\n", top_5_filtered[['Vehicle_ID', 'Energy_Consumption_kWh']])

# 7.
freq_driving_mode = df['Driving_Mode'].value_counts()
freq_weather = df['Weather_Condition'].value_counts()
print("\nDriving Mode Frequencies:\n", freq_driving_mode)
print("\nWeather Condition Frequencies:\n", freq_weather) 

# 8. 
explicit_sort = df.set_index('Vehicle_ID').sort_index().loc[:, ['Speed_kmh', 'Battery_State_%']].head(3)

implicit_sort = df.sort_values(by='Timestamp').iloc[:3, [0, 2, 4]]
print("\nExplicit indexing (loc, sorted by Vehicle_ID label):\n", explicit_sort)  
print("\nImplicit indexing (iloc, first 3 rows by position):\n", implicit_sort)  

# 9.
cond1 = df[(df['Driving_Mode'] == 1) & (df['Speed_kmh'] > 110)][['Vehicle_ID', 'Speed_kmh']].head(2)
cond2 = df[(df['Traffic_Condition'] == 3) | (df['Temperature_C'] < 0)][['Vehicle_ID', 'Temperature_C']].head(2)
cond3 = df[(df['Slope_%'] > 5) & (df['Battery_State_%'] < 20) & (df['Driving_Mode'] == 2)][['Vehicle_ID', 'Battery_State_%']].head(2)
print("\nCase 1 (Driving_Mode==1 & Speed>110):\n", cond1) 
print("\nCase 2 (Traffic_Condition==3 | Temperature<0):\n", cond2)  
print("\nCase 3 (Slope>5 & Battery<20 & Driving_Mode==2):\n", cond3)  

# 10. 
min_energy = df['Energy_Consumption_kWh'].min()
max_energy = df['Energy_Consumption_kWh'].max()
print(f"\nMin Energy Consumption: {min_energy:.4f} kWh")  
print(f"Max Energy Consumption: {max_energy:.4f} kWh")   

# 11. 
group_mean_energy = df.groupby('Driving_Mode')['Energy_Consumption_kWh'].mean()
group_max_speed = df.groupby(['Traffic_Condition', 'Weather_Condition'])['Speed_kmh'].max()
print("\nMean Energy Consumption by Driving_Mode:\n", group_mean_energy)          
print("\nMax Speed by Traffic_Condition x Weather_Condition:\n", group_max_speed) 

# 12.
df['Energy_per_km'] = df['Energy_Consumption_kWh'] / df['Distance_Travelled_km']
print("\nNew column Energy_per_km:\n", df[['Energy_Consumption_kWh', 'Distance_Travelled_km', 'Energy_per_km']].head()) 

# 13. 
agg_1 = df.groupby('Driving_Mode').agg({'Energy_Consumption_kWh': ['mean', 'std']})
agg_2 = df.groupby('Weather_Condition').agg({'Speed_kmh': 'max', 'Distance_Travelled_km': 'sum'})
print("\nAggregate 1 (mean/std energy by Driving_Mode):\n", agg_1)  
print("\nAggregate 2 (max speed, total distance by Weather_Condition):\n", agg_2)  

# 14. 
grouped_by_mode = df.groupby('Driving_Mode')
eco_mode_group = grouped_by_mode.get_group(1).head(3)
print("\nDriving_Mode == 1 group (first 3 rows):\n", eco_mode_group) 

# 15.
correlation = df['Speed_kmh'].corr(df['Energy_Consumption_kWh'])
print(f"\nCorrelation between Speed and Energy Consumption: {correlation:.4f}")

# 16.
df['Speed_Normalized'] = (df['Speed_kmh'] - df['Speed_kmh'].min()) / (df['Speed_kmh'].max() - df['Speed_kmh'].min())
print("\nNormalized Speed (Min-Max):\n", df[['Speed_kmh', 'Speed_Normalized']].head())  

# 17. 
df_part1 = df[['Vehicle_ID', 'Speed_kmh']].head(5)
df_part2 = df[['Vehicle_ID', 'Battery_State_%']].head(5)

merged_df = pd.merge(df_part1, df_part2, on='Vehicle_ID')
print("\nMerged DataFrame:\n", merged_df)  
concat_df = pd.concat([df_part1, df.iloc[5:10][['Vehicle_ID', 'Speed_kmh']]], axis=0)
print("\nConcatenated DataFrame:\n", concat_df)  
joined_df = df_part1.set_index('Vehicle_ID').join(df_part2.set_index('Vehicle_ID'))
print("\nJoined DataFrame (index-based join):\n", joined_df)  
