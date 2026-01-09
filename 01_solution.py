def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
list_of_numbers = [7,3,5,6,8,2,9,1,5]
bubble_sort(list_of_numbers)
print(list_of_numbers)