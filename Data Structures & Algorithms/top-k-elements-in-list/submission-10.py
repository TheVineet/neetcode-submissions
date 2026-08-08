class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ind = {}

        for num in nums:
            curr = ind.get(num,0)
            ind[num] = curr + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num,count in ind.items():
            bucket[count].append(num)
        
        res = []
        
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res
        return res

        
        