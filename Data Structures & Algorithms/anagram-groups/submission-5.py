class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ind = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for letter in s:
                key = ord(letter) - ord("a")
                arr[key] += 1
            ind[tuple(arr)].append(s)
        
        return list(ind.values())


        