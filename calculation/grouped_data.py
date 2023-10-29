import math 
import json 

import pandas as pd 

from utils import measure

class Row:
    def __init__(self, row):
        self.range = row[0]
        self.frequency = row[1]
        self.cf = 0
        self.i = (row[0][1] - row[0][0]) + 1

    def midpoint(self):
        r = self.range
        return (r[0] + r[1]) / 2

class MOP:
    def __init__(self, data_set, total_freq):
        self.data_set = data_set 

        range_row = data_set[0].range

        self.i = (range_row[1] - range_row[0]) + 1
        self.total_freq = total_freq

    def quartile(self, place):
        return measure.measure(place, self.data_set, 4, self.total_freq)

    def decile(self, place):
        return measure.measure(place, self.data_set, 10, self.total_freq)

    def percentile(self, place):
        return measure.measure(place, self.data_set, 100, self.total_freq)

def get_mean(data_set, total_freq):
    track = 0 

    for data in data_set:
        track += data.frequency * data.midpoint()

    return track / total_freq

def get_median(mop_instance):
    return mop_instance.quartile(2)

def get_mode(data_set):
    modal_freq = max([data.frequency for data in data_set]) 
    modal_class = None 
    index = 0

    for i in range(0, len(data_set)):
        if data_set[i].frequency == modal_freq:
            modal_class = data_set[i]
            index = i
            break

    lb_mo = modal_class.range[0] - 0.5 
    d_1 = modal_class.frequency if index == 0 else modal_class.frequency - data_set[index - 1].frequency
    d_2 = modal_class.frequency if index == (len(data_set)-1) else modal_class.frequency - data_set[index + 1].frequency
    i = (modal_class.range[1] - modal_class.range[0]) + 1

    return lb_mo + i * (d_1 / (d_1 + d_2))

def get_mad(data_set, mean, total_freq):
    track = 0 

    for data in data_set:
        track += (abs(data.midpoint() - mean) * data.frequency)

    return track / total_freq 

def get_var(data_set, mean, is_samp, total_freq):
    track = 0 

    for data in data_set:
        track += data.frequency * ((abs(data.midpoint() - mean))**2)

    if is_samp:
        return track / (total_freq - 1)
    
    return track / total_freq

def get_stdv(data_set, mean, is_samp, total_freq):
    return math.sqrt(get_var(data_set, mean, is_samp, total_freq))

def translate_data(grouped_data, data_set, length):
    range_list = []
    frequency_list = []

    cf = 0

    for r in grouped_data["Range"]:
        parsed_range = list(map(int, r.split("-")))
        range_list.append(parsed_range)

    for f in grouped_data["Frequency"]:
        frequency_list.append(f)

    for i in range(0, length):
        data_set.append(Row([range_list[i], frequency_list[i]]))
        cf += data_set[i].frequency
        data_set[i].cf = cf 

def main_grouped_data():
    total_freq = 0 
    data_set = []

    grouped_data = pd.read_csv("./data/grouped_data.csv")

    print("Data from ./data/grouped_data.csv:")
    translate_data(grouped_data, data_set, grouped_data.shape[0])
    print(grouped_data)

    for data in data_set:
        total_freq += data.frequency

    mop_instance = MOP(data_set, total_freq)

    print()

    print("Measures of Central Tendency:")
    mean = get_mean(data_set, total_freq)
    print(f"1. Mean = {mean:.2f}")

    median = get_median(mop_instance)
    print(f"2. Median = {median:.2f}")

    mode = get_mode(data_set)
    print(f"3. Mode = {mode:.2f}")

    print()

    print("Measures of Variability and Dispersion:")
    mad = get_mad(data_set, mean, total_freq)
    print(f"1. MAD = {mad:.2f}")

    variance = get_var(data_set, mean, False, total_freq)
    print(f"2. Variance (Population) = {variance:.2f}")

    variance_sample = get_var(data_set, mean, True, total_freq)
    print(f"3. Variance (Sample) = {variance_sample:.2f}")

    stdv = get_stdv(data_set, mean, False, total_freq)
    print(f"4. Standard Deviation (Population) = {stdv:.2f}")

    stdv_sample = get_stdv(data_set, mean, True, total_freq)
    print(f"5. Standard Deviation (Sample) = {stdv_sample:.2f}")

    print()

    print("Measures of Position:")

    q_i = 100 / 4
    d_i = 100 / 10 

    print()
    print(" Quartile:")
    for i in range(1, 4):
        print(f"  {q_i}% of the data = {mop_instance.quartile(i):.2f}")
        q_i += 25

    print()
    print(" Decile:")
    for i in range(1, 10):
        print(f"  {i * 10}% of the data = {mop_instance.decile(i):.2f}")

    print()
    print(" Percentile")
    for j in range(1, 100):
        print(f"  {j}% of the data = {mop_instance.percentile(j):.2f}")


if __name__ == "__main__":
    main()