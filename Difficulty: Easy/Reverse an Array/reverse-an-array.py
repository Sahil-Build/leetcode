class Solution:
    def reverseArray(self, arr):
        # code here
        def rev(f,l):
            if (f>=l):
                return arr
            arr[f],arr[l]=arr[l],arr[f]
            rev(f+1,l-1)
        rev(0,len(arr)-1)
        
        