class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # I DID HAVE CYCLE INTUITION I HAD THE FUCKIN CYCLE INTUITION

        # iterate through the list, go to the index of the value written 
        # (since the range is [1,n]). it's going to go to
        # the same index, then it's going to make a loop back and 
        # fourth between the two numbers. 

        current = nums[0]

        while True : 

            prev = current 

            current = nums[current]

            if prev == nums[current] and current == nums[prev]: 
                return nums[current]


            
        return -1




        

