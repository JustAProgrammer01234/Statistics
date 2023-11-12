import math
import pandas as pd
import numpy as np 

def return_index(array, elem):
    for i in range(len(array)):
        if array[i] == elem:
            return i 

def count_data(array, elem):
    count = 0 
    for e in array:
        if e == elem:
            count += 1 
    return count 

def mode(ungrouped_data):
    data = np.empty(len(ungrouped_data.unique()))
    data[:] = np.nan

    occurence = np.zeros(len(ungrouped_data.unique()))

    working_index = 0 

    for i in range(len(ungrouped_data)):
        if ungrouped_data[i] not in data:
            data[working_index] = ungrouped_data[i]
            occurence[working_index] += 1
            working_index += 1  
        else:
            index = return_index(data, ungrouped_data[i])
            occurence[index] += 1 

    unique_mode = np.unique(occurence)

    if len(unique_mode) == 1:
        return "No mode"

    modes = np.empty(count_data(occurence, max(unique_mode)))
    modes[:] = np.nan

    working_index = 0 
    for i in range(len(occurence)):
        if occurence[i] == max(unique_mode):
            modes[working_index] = data[i]
            working_index += 1

    if len(modes) == 1:
        mode_type = "Unimodal"
    elif len(modes) == 2:
        mode_type = "Bimodal"
    elif len(modes) == 3:
        mode_type = "Trimodal"
    else:
        mode_type = "Multimodal"

    modes = modes.astype("int32")

    return f"{modes} ({mode_type})"

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
        index = int(i) + 1
        data = sorted_data[index]

    return data

def display_data(ungrouped_data):
    if len(ungrouped_data) <= 15:
        text = f"{ungrouped_data}" 
    else:
        text = f"{ungrouped_data[:3]}...{ungrouped_data[-3:]}"

    print(text.replace("[", "").replace("]", ""))
    print(f"Length of data set = {len(ungrouped_data)}")

def main_ungrouped_data():
    ungrouped_data = pd.read_csv("./data/ungrouped_data.csv")["Data"]
    sorted_data = ungrouped_data.sort_values(ascending = True).to_numpy()

    mean = sum(ungrouped_data) / len(ungrouped_data)

    print("Data from ./data/ungrouped_data.csv:")
    display_data(ungrouped_data.to_numpy())
    print()

    print("Measures of Central Tendency:")
    print(f"Mean = {mean:.2f}")
    print(f"Median = {mop(2, len(ungrouped_data), 4, sorted_data):.2f}")
    print(f"Mode = {mode(ungrouped_data)}")
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