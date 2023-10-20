import math 

# the format for the data set is:
# [(x_m, f)]
#  Where:
#  x_m - midpoint 
#  f - frequency 

data_set = [(15, 4), (22, 9), (29, 7), (36, 6)]

def get_mean(data_set):
    track = 0 
    sum_f = 0 
    for data in data_set:
        track += data[0] * data[1]
        sum_f += data[1] 
    return track / sum_f

def get_median(data_set):
    pass 

def get_mode(data_set):
    mod_freq = max([data[1] for data in data_set]) 

def get_mad(data_set, mean):
    track = 0 
    freq = 0 
    for data in data_set:
        track += (abs(data[0] - mean) * data[1])
        freq += data[1] 
    return track / freq 

def get_var(data_set, mean, is_samp):
    track = 0 
    freq = 0 
    for data in data_set:
        track += data[1] * (abs(data[0] - mean))**2
        freq += data[1]

    if is_samp:
        return track / (freq - 1)
    
    return track / freq

def get_stdv(data_set, mean, is_samp):
    return math.sqrt(get_var(data_set, mean, is_samp))

mean = get_mean(data_set)

print(f"Mean: {mean:.2f}")
print(f"MAD: {get_mad(data_set, mean):.2f}")

print()

print(f"Population Variance: {get_var(data_set, mean, False):.2f}")
print(f"Sample Variance: {get_var(data_set, mean, True):.2f}")

print()

print(f"Population Standard Deviation: {get_stdv(data_set, mean, False):.2f}")
print(f"Sample Standard Deviation: {get_stdv(data_set, mean, True):.2f}")
