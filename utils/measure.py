def measure(place, data_set, divisor, total_freq):
    n_divisor = (place * total_freq) / divisor 
    index = 0 
    measure_class = None 
    less_cf = 0 

    for data in data_set:
        if index == 0 and n_divisor <= float(data.cf):
            measure_class = data 
            break 

        elif index != 0:
            if float(data_set[index-1].cf) < n_divisor <= float(data.cf):
                measure_class = data 
                less_cf = data_set[index - 1].cf 
                break

        index += 1

    lb_c = measure_class.range[0] - 0.5 
    f_c = measure_class.frequency 
    i = measure_class.i 

    return lb_c + i * ((n_divisor - less_cf) / f_c)