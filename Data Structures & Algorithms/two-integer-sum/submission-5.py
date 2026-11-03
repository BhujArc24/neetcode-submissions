class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recordedNums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in recordedNums:
                return [recordedNums[diff], i]
            recordedNums[n] = i