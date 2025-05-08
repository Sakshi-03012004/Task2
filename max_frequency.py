def most_frequent_element(lst):
    frequency = {}  
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent
my_list = [3, 1, 2, 3, 4, 3, 2, 1, 2, 2]
print("Most frequent element:", most_frequent_element(my_list))
