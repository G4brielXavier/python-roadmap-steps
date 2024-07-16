#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Bubble Sort ============

numbers = [2, 1, 7, 6, 8, 3, 4, 5, 6, 9]

def bubbleSort(arr):
    end_index = len(arr)
    
    while end_index > 0:
        j = 0
        while j < end_index - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        end_index -= 1
        
bubbleSort(numbers)
print(numbers)