class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        # { 1:1, 2:2, 3:3}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        #  0    1   2   3  - count, frequence of how many times each elemtn 
        # [[], [1], [2], []]
        
        for num, count in seen.items():
            # 1 (number), 1(count)
            # 2 (number), 2(count)
            # 3 (number), 3(count)
            bucket[count].append(num)
        
        #range(start, end, step)
        #range(4) assume 0,1,2,4
        #range(i, len(nums)) #0, 4
        #range(len(nums), -1, -1) #4, 3, 2, 1

        res = [] 
        for i in range(len(nums), -1, -1):
            for num in bucket[i]: 
                res.append(num)
            if len(res) == k:
                return res

            
        
        

            

