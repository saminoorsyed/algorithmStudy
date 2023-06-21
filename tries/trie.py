class TrieNode:
    def __init__(self):
        self.next_chars = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        word = [x for x in word[::-1]]
        chars = self.root
        while word:
            current_char = word.pop()
            # if the current char is not stored, make an entry
            if current_char not in chars.next_chars:
                chars.next_chars[current_char] = TrieNode()
            # set dictionary to check to the next char in the list
            chars = chars.next_chars[current_char]
        chars.isEnd = True

    def search(self, word: str) -> bool:
        word = [x for x in word[::-1]]
        chars = self.root
        while word:
            current_char = word.pop()
            if current_char in chars.next_chars:
                chars = chars.next_chars[current_char]
            else:
                return False
        if chars.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        prefix = [x for x in prefix[::-1]]
        chars = self.root
        while prefix:
            current_char = prefix.pop()
            if current_char in chars.next_chars:
                chars = chars.next_chars[current_char]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    new_trie = Trie()
    new_trie.insert("apple")
    # should output True, False, True
    print(new_trie.search("apple"), new_trie.search("app"), new_trie.startsWith("app"));
