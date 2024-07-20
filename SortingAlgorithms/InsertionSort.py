#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Insertion Sort ============

numbers = [5, 4, 6, 7, 8, 1, 2, 3]

def insertionSort(arr):
    for i in range(1, len(arr)):
        a = arr[i]
        j = i - 1
    
        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = a
    
    return arr

insertionSort(numbers)
print(numbers)
 