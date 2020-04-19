def max_min_mean_median(list_numbers):

    minN = min(list_numbers)

    maxN = max(list_numbers)

    l = len(list_numbers)
    list_numbers.sort()
    if l % 2 == 0:
        medianone = list_numbers[l//2]
        mediantwo = list_numbers[l//2 - 1]
        median = round((medianone+mediantwo)/2)
    else:
        median = list_numbers[l//2]

    mean = sum(list_numbers)/len(list_numbers)

    list = []

    list.append(minN)
    list.append(maxN)
    list.append(median)
    list.append(mean)

    return list

    
    

print(max_min_mean_median([2,3,7,10]))