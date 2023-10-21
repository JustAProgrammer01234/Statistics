import math 
import json 

import pandas as pd 

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
        data_set = self.data_set

        n_4 = (place * self.total_freq) / 4
        index = 0
        quartile_class = None 
        less_cf = 0 

        for data in data_set:
            if index == 0 and float(data.cf) == n_4:
                quartile_class = data 
                break 

            elif index != 0 and index < len(data_set) - 1:
                if float(data_set[index-1].cf) < (n_4) <= float(data.cf) and quartile_class == None:
                    quartile_class = data 
                    less_cf = data_set[index - 1].cf 
                    break

            elif index == len(data_set) and float(data.cf) == n_4:
                quartile_class = data
                less_cf = data_set[index - 1].cf 
                break

            index += 1 

        lb_qc = quartile_class.range[0] - 0.5
        f_qc = quartile_class.frequency 
        i = quartile_class.i

        return lb_qc + i * ((n_4 - less_cf) / 2)

    def decile(self, place):
        data_set = self.data_set

        n_10 = (place * self.total_freq) / 10
        index = 0
        decile_class = None 
        less_cf = 0 

        for data in data_set:
            if index == 0 and float(data.cf) == n_10:
                decile_class = data 
                break 

            elif index != 0 and index < len(data_set) - 1:
                if float(data_set[index-1].cf) < (n_10) <= float(data.cf) and decile_class == None:
                    decile_class = data 
                    less_cf = data_set[index - 1].cf 
                    break 

            elif index == len(data_set) and float(data.cf) == n_10:
                decile_class = data
                less_cf = data_set[index - 1].cf 
                break 

            index += 1 

        lb_dc = decile_class.range[0] - 0.5
        f_dc = decile_class.frequency 
        i = decile_class.i

        return lb_dc + i * ((n_10 - less_cf) / 2)

    def percentile(self, place):
        data_set = self.data_set

        n_100 = (place * self.total_freq) / 100
        index = 0
        percentile_class = None 
        less_cf = 0 

        for data in data_set:
            if index == 0 and float(data.cf) == n_100:
                decile_class = data 
                break 

            elif index != 0 and index < len(data_set) - 1:
                if float(data_set[index-1].cf) < (n_100) <= float(data.cf) and percentile_class == None:
                    percentile_class = data 
                    less_cf = data_set[index - 1].cf 
                    break 

            elif index == len(data_set) and float(data.cf) == n_100:
                percentile_class = data
                less_cf = data_set[index - 1].cf 
                break

            index += 1 

        lb_pc = percentile_class.range[0] - 0.5
        f_pc = percentile_class.frequency 
        i = percentile_class.i

        return lb_pc + i * ((n_100 - less_cf) / 2)

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
    d_1 = 0 if index == 0 else modal_class.frequency - data_set[index - 1].frequency
    d_2 = 0 if index == (len(data_set)-1) else modal_class.frequency - data_set[index + 1].frequency
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
        track += data.frequency * (abs(data.midpoint() - mean))**2

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

def main():
    total_freq = 0 
    data_set = []

    grouped_data = pd.read_csv("./data/data.csv")

    print("Data from ./data/data.csv:")
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

    print("Variability and Dispersion:")
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
        print(f"  {q_i}% of the data: {mop_instance.quartile(i):.2f}")
        q_i += 25

    print()
    print(" Decile:")
    for i in range(1, 10):
        print(f"  {d_i}% of the data: {mop_instance.decile(i):.2f}")
        d_i += 10

    print()
    print(" Percentile")
    for j in range(1, 100):
        print(f"  {j}% of the data: {mop_instance.percentile(j):.2f}")


if __name__ == "__main__":
    main()