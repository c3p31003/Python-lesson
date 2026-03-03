def get_average():
    with open("files\data.txt") as file:
        temparatures_lists = file.readlines()
    
    print(temparatures_lists)
    temparatures_lists = temparatures_lists[1:]
    print(temparatures_lists)
    sum_t = 0
    # for val in temparatures_lists:
    #     if val != '\n':
    #         sum_t += float(val)
    # sum_t += [int(val) for val in tem]
    if '\n' in temparatures_lists:
        temparatures_lists.remove('\n')
        print('success remove',temparatures_lists)
    sum_t = [float(val) for val in temparatures_lists]

    ave = sum(sum_t) / (len(temparatures_lists) -1 )
    return float(ave)

print(f"temparature averaeg equals {get_average()}")