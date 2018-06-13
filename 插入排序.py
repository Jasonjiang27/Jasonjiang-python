#插入排序

def insert_sort(array):
    n = len(array)
    for i in range(1,n):
        value = array[i]

        pos = i
        while pos >0 and value < array[pos-1]:
            array[pos] = array[pos-1]
            pos -= 1
        array[pos] = value
    return array

print(insert_sort([3,4,2,4,5,5,8]))
            
