import math
import pandas as pd
import numpy as np  

def mad(ungrouped_data, mean):
    track = 0 

    for data in ungrouped_data:
        track += abs(data - mean)

    return track / len(ungrouped_data)

def variance(ungrouped_data, mean, is_sample):
    track = 0 

    for data in ungrouped_data:
        track += abs(data - mean) ** 2

    if is_sample:   
        return track / (len(ungrouped_data) - 1)

    return track / len(ungrouped_data) 

def mop(k, n, divisor, sorted_data):
    if divisor == 4:
        if n % 2 == 0:
            i = (((k * n) / 4) + 0.5) - 1
        else:
            i = ((k / 4) * (n + 1)) - 1

        if int(i) != i:
            decimal_part = i - int(i) 
            return (sorted_data[int(i)] + (decimal_part * (sorted_data[int(i) + 1] - sorted_data[int(i)])))
        else:
            return sorted_data[int(i)]

    i = ((k * n) / divisor) - 1

    if int(i) == i:
        i = int(i)
        data = (sorted_data[i] + sorted_data[i + 1]) / 2
    else:
        data = sorted_data[int(i)]

    return data

def main_ungrouped_data():
    ungrouped_data = pd.read_csv("./data/ungrouped_data.csv")["Data"]
    sorted_data = ungrouped_data.sort_values(ascending = True).to_numpy()

    mean = sum(ungrouped_data) / len(ungrouped_data)

    print("Data:")
    print(ungrouped_data)
    print()

    print("Measures of Central Tendency:")

    print(f"Mean = {mean:.2f}")
    print(f"Median = {mop(5, len(ungrouped_data), 10, sorted_data):.2f}")
    print("Mode = no mode yet :clown:")
    print() 

    print("Measures of Variability and Dispersion:")
    print(f"MAD = {mad(ungrouped_data, mean):.2f}")
    print(f"Variance (Population) = {variance(ungrouped_data, mean, False):.2f}")
    print(f"Variance (Sample) = {variance(ungrouped_data, mean, True):.2f}")
    print(f"Standard Deviation (Population) = {math.sqrt(variance(ungrouped_data, mean, False)):.2f}")
    print(f"Standard Deviation (Sample) = {math.sqrt(variance(ungrouped_data, mean, True)):.2f}")
    print()

    print("Measures of Position:")

    q_i = 100 / 4 
 
    print(" Quartile:")
    for i in range(1, 4):
        print(f"  {q_i}% of the Data: {mop(i, len(ungrouped_data), 4, sorted_data)}")
        q_i += 25

    print()
    print(" Decile:")
    for j in range(1, 10):
        print(f"  {j * 10}% of the Data: {mop(j, len(ungrouped_data), 10, sorted_data)}")

    print()
    print(" Percentile:")
    for k in range(1, 100):
        print(f"  {k}% of the Data: {mop(k, len(ungrouped_data), 100, sorted_data)}")