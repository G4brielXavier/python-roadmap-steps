from random import sample

vector = sample(range(100, 1000), 100)

def bubbleSort(arr):
    last = len(arr)
    while last > 0:
        i = 0
        while i < last-1:
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                
            i += 1
        last -= 1
        
bubbleSort(vector)
print(vector)