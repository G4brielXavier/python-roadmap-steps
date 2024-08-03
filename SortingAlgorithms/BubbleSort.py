#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Bubble Sort ============

numbers = [2, 1, 7, 6, 8, 3, 4, 5, 6, 9]

def BubbleSort(arr):
    
    end_index = len(arr)
    
    while end_index > 0:
        
        i = 0
        
        while i < end_index - 1:
            
            if arr[i] > arr[i + 1]:
                
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                
            i += 1
            
        end_index -= 1