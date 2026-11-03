class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = []
        res = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num, count in hashmap.items():
            bucket[count].append(num)
        
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res