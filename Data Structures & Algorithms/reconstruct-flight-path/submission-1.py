class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create adjMap

        adjMap = collections.defaultdict(list)
        tickets.sort(reverse = True)

        for src,dest in tickets:
            adjMap[src].append(dest)

        res = []

        def dfs(src):
            while adjMap[src]:
                dest = adjMap[src].pop()
                dfs(dest)

            res.append(src)

        dfs("JFK")

        return res[::-1]


                
