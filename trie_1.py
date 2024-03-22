class Trie:
class Trie:
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return self.search_level(node, prefix, [])

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        for char in sorted(curkeys()):
            if char != self.end_symbol:
                self.search_level(cur[char], cur_prefix + char, words)
        return words


    def exists(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_symbol in node

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

