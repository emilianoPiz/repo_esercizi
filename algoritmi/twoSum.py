def twoSum(nums,target):
        ret =[]
       
        i,j=0,0
        while i < len(nums):
            diff = (target - nums[j]) 
            if diff == nums[i] and i !=j:
                ret += [i,j]  
                break
            if j == len(nums)-1:
                i+=1
                j=i    
            j+=1    

        return ret

print(twoSum([2,7,11,15],9))