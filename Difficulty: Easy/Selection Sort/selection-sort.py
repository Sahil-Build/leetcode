class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            min = i
            for j in range(i+1,len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[min],arr[i] = arr[i],arr[min]
        return arr