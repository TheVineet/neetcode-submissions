class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] +=1
        inverted_count = []

        for num,freq in count.items():
            inverted_count.append((freq,num))
        
        inverted_count.sort()
        res = []
        for i in range(k):
            freq,num = inverted_count.pop()
            res.append(num)
        return res


