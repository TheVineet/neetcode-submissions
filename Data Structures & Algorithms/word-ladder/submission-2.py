class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patternMap = collections.defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                patternMap[pattern].append(word)
        
        q = collections.deque()
        visit = set()

        q.append(beginWord)
        visit.add(beginWord)
        count = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for adj in patternMap[pattern]:
                        if adj in visit:
                            continue
                        q.append(adj)
                        visit.add(adj)
            count +=1
        return 0


