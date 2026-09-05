class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # I DID HAVE CYCLE INTUITION I HAD THE FUCKIN CYCLE INTUITION

        # iterate through the list, go to the index of the value written 
        # (since the range is [1,n]). it's going to go to
        # the same index, then it's going to make a loop back and 
        # fourth between the two numbers. 

        current = -1 

        for i in range (len(nums) + 1): 

            prev = current 

            if current == -1 :
                current = nums[i]
            else: 
                current = nums[nums[i]]
                if prev == nums[current] and current == nums[prev]: 
                    return nums[prev]
            
        return -1




        

