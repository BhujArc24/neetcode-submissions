class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recNums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in recNums:
                return [recNums[diff], i]
            recNums[n] = i