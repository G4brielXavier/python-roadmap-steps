#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Bubble Sort ============

from random import sample

numbers = sample(range(100, 1000), 100)

def bubble_sort(arr):
    last_element = len(arr)
    while last_element > 0:
        i = 0
        while i < last_element-1:
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                
            i += 1
        last_element -= 1


# bubble_sort(numbers)
# print(numbers)