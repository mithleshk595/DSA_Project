#selection sor
def sortArray(nums):
        n = len(nums)


        for i in range(n):
            mn = nums[i]
            ind = i
            for j in range(i+1, n):
                if nums[j]<mn:
                   mn = nums[i]
                   ind = j
                   
            
            temp = nums[i]
            nums[i] = nums[ind]
            nums[ind] = temp
        
        return nums
        

            
        
