class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        Y.Teller
        
        The following is my solution to the Leet code problem two sum
        
        using list comprehension we iterate through the list of nums and check if the target - currentValue
        is in the list, if yes we return the current index +  the index of the second value.

        This is my solution written out in the traditional way for better readability.

        for i in range(len(nums)):
            if((target-nums[i]) in nums and nums.index(target-nums[i]) != i):
                return [i, nums.index(target-nums[i])]
        '''

        return [[i, nums.index(target - nums[i])] for i in range(len(nums)) if
                ((target - nums[i]) in nums) and (nums.index(target - nums[i]) != i)][0]
