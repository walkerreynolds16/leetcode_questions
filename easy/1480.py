'''
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.

    Example 1:

        Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
        Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        for i in range(0, len(nums)):
            if len(sums) == 0:
                sums.append(nums[i])
            else:
                sums.append(nums[i] + sums[i-1])

        return sums