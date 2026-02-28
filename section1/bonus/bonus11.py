def get_average():
    with open("files\data.txt") as file:
        temparatures_lists = file.readlines()
    
    print(temparatures_lists)
    temparatures_lists = temparatures_lists[1:]
    print(temparatures_lists)
    sum_t = 0
    for val in temparatures_lists:
        sum_t += int(val)
    
    ave = sum_t / (len(temparatures_lists) -1 )
    return int(ave)

print(f"temparature averaeg equals {get_average()}")