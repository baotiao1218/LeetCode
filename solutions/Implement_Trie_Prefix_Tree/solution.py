#(Recursive)
class TrieNode:
    def __init__(self):
        # 存下以這個字母為底的詞彙
        self.words = []
        self.child = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.child[c]

        cur.words.append(word)

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return word in cur.words

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]

        return True


#Optimized 1:
class TrieNode:
    def __init__(self):
        # 用isEnd Flag作為有詞存在
        self.isEnd = False
        self.child = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.child[c]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]

        return True