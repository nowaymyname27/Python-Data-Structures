def insert_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while j > -1 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list
        
        
print(insert_sort([3,2,1]))