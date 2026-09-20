import pandas as pd
df = pd.read_csv(r"C:\Users\Harshvardhan Bhosale\OneDrive\Desktop\Assignments vs code\EV_Energy_Consumption_Dataset (1).csv")

def sort_list(data):
    
    a = data[:]
    n = 0
    for x in a:
        n = n + 1
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a
def get_stats(data):
    n = 0
    total = 0
    for x in data:
        n = n + 1
        total = total + x
    mean = total / n
    a = sort_list(data)
    if n % 2 == 1:
        median = a[n // 2]
    else:
        median = (a[n // 2 - 1] + a[n // 2]) / 2

    mode = 0
    best = 0
    count = 0
    prev = None
    for x in a:
        r = (x + 0.5) // 1
        if r == prev:
            count = count + 1
        else:
            prev = r
            count = 1
        if count > best:
            best = count
            mode = r
    data_range = a[n - 1] - a[0]
    ss = 0

    for x in data:
        ss = ss + (x - mean) ** 2
    variance = ss / (n - 1)
    std = variance ** 0.5

    q = []
    for k in [1, 3]:
        pos = k * (n - 1)
        i = pos // 4
        frac = (pos % 4) / 4
        q.append(a[i] + frac * (a[i + 1] - a[i]))
    iqr = q[1] - q[0]
    return mean, median, mode, data_range, variance, std, iqr

temp = df["Battery_Temperature_C"].tolist()
mean, median, mode, data_range, variance, std, iqr = get_stats(temp)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Range:", data_range)
print("Variance:", variance)
print("Standard deviation:", std)
print("IQR:", iqr)
cols = ["Battery_Temperature_C", "Battery_Voltage_V", "Battery_State_%",
        "Speed_kmh", "Temperature_C", "Energy_Consumption_kWh"]

for c in cols:
    m, md, mo, r, v, s, i = get_stats(df[c].tolist())
    print(c)
    print(f"  mean {m:.2f}  median {md:.2f}  mode {mo:.0f}  range {r:.2f}")
    print(f"  variance {v:.2f}  std {s:.2f}  iqr {i:.2f}")
