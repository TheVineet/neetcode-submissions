class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(curr, i):
            if i == len(word):
                return curr.endOfWord

            c = word[i]
            if c == ".":
                for val in curr.children.values():
                    res = dfs(val, i + 1)
                    if res:
                        return True
                return False

            if c not in curr.children:
                return False

            curr = curr.children[c]

            res = dfs(curr, i + 1)
            return res
            
        res = dfs(curr,0)
        return res

        
