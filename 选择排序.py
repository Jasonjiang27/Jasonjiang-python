#选择排序

def select_sort(array):
    n = len(array)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if array[j] < array[min_idx]:

                array[j],array[min_idx] = array[min_idx],array[j]
    return array

print(select_sort([4,5,2,1,7,6,0]))
