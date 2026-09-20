import pandas as pd

df = pd.read_csv(r"C:\Users\Harshvardhan Bhosale\OneDrive\Desktop\Assignments vs code\EV_Energy_Consumption_Dataset (1).csv")
temp = df["Battery_Temperature_C"]

print("Mean:", temp.mean())
print("Median:", temp.median())
print("Mode:", temp.round().mode()[0])
print("Range:", temp.max() - temp.min())
print("Variance:", temp.var())
print("Standard deviation:", temp.std())
print("IQR:", temp.quantile(0.75) - temp.quantile(0.25))

print(temp.round().value_counts().head(10))
print(df["Driving_Mode"].value_counts())
print(df["Weather_Condition"].value_counts())

cols = ["Battery_Temperature_C", "Battery_Voltage_V", "Battery_State_%",
        "Speed_kmh", "Temperature_C", "Energy_Consumption_kWh"]
sub = df[cols]

table = pd.DataFrame()
table["Mean"] = sub.mean()
table["Median"] = sub.median()
table["Mode"] = sub.round().mode().iloc[0]
table["Range"] = sub.max() - sub.min()
table["Variance"] = sub.var()
table["Std Dev"] = sub.std()
table["IQR"] = sub.quantile(0.75) - sub.quantile(0.25)
print(table.round(2))
