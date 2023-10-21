import math 
import json 

midpoint = lambda low, high: (low + high) / 2

class Row:
    def __init__(self, row):
        self.range = row[0]
        self.frequency = row[1]
        self.cf = 0 

def get_mean(data_set, total_freq):
    track = 0 

    for data in data_set:
        track += data.frequency * midpoint(data.range[0],  data.range[1]) 

    return track / total_freq

def get_median(data_set, total_freq):
    median_class = None 
    
    cf = 0 
    n_2 = total_freq / 2
    index = 0 
    less_cf = 0 

    for data in data_set: 
        cf += data.frequency 
        data.cf = cf 

        if index == 0 and float(data.cf) == n_2:
            median_class = data 
            break

        if index == len(data_set) and float(data.cf) == n_2:
            median_class = data 
            less_cf = data_set[index - 1].cf 

        if float(data_set[index-1].cf) < (n_2) <= float(data.cf) and median_class == None:
            median_class = data 
            less_cf = data_set[index - 1].cf 

        index += 1 

    lb_mc = median_class.range[0] - 0.5
    f_mc = median_class.frequency
    i = (median_class.range[1] - median_class.range[0]) + 1

    return lb_mc + i * ((n_2 - less_cf) / f_mc)
    

def get_mode(data_set):
    modal_freq = max([data.frequency for data in data_set]) 
    modal_class = None 
    index = 0

    for data in data_set:
        if data.frequency == modal_freq:
            modal_class = data 
            break
        index += 1 

    lb_mo = modal_class.range[0] - 0.5 
    d_1 = 0 if index == 0 else modal_class.frequency - data_set[index - 1].frequency
    d_2 = 0 if ndex == len(data_set) else modal_class.frequency - data_set[index + 1].frequency
    i = (modal_class.range[1] - modal_class.range[0]) + 1

    return lb_mo + i * (d_1 / (d_1 + d_2))

def get_mad(data_set, mean, total_freq):
    track = 0 

    for data in data_set:
        track += (abs(midpoint(data.range[0], data.range[1]) - mean) * data.frequency)

    return track / total_freq 

def get_var(data_set, mean, is_samp, total_freq):
    track = 0 

    for data in data_set:
        track += data.frequency * (abs(midpoint(data.range[0], data.range[1]) - mean))**2

    if is_samp:
        return track / (total_freq - 1)
    
    return track / total_freq

def get_stdv(data_set, mean, is_samp, total_freq):
    return math.sqrt(get_var(data_set, mean, is_samp, total_freq))

def main():
    total_freq = 0 

    with open("./data.json", "r") as f:
        json_data = json.load(f)

    data_set = []

    print("Range  Frequency")
    for row in json_data["data"]:
        data_set.append(Row(row))
        total_freq += row[1]

        print(f"{row[0][0]}-{row[0][1]}      {row[1]}")

    print()

    print("Measures of Central Tendency:")
    mean = get_mean(data_set, total_freq)
    print(f"1. Mean = {mean:.2f}")

    median = get_median(data_set, total_freq)
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
    print(f"4. Standard Deviation (Sample) = {stdv_sample:.2f}")

if __name__ == "__main__":
    main()