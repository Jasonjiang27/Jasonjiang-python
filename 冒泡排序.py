def bubble_sort(array):
    n=len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
print(bubble_sort([2,4,5,1,8,5,7]))
