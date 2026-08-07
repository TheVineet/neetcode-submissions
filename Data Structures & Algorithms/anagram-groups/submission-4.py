class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ind = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ind[key].append(s)
        
        return list(ind.values())
        