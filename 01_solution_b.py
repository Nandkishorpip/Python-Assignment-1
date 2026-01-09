def Insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

list_of_numbers = [7,3,5,6,8,2,9,1,5]
Insertion_sort(list_of_numbers)
print(list_of_numbers)