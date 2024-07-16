#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Selection Sort ============

numbers = [7, 5, 2, 4, 8, 6, 1, 2, 3]

def selectionSort(arr, size):
    for s in range(size):
        min_index = s
        
        for i in range(s + 1, size):
            if arr[i] < arr[min_index]:
                min_index = i
                
        (arr[s], arr[min_index]) = (arr[min_index], arr[s])
        
selectionSort(numbers, len(numbers))
print(numbers)