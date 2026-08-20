# Pseudocode
# Idea: BFS

# Data structures:
## queue: next words (start with beginWord)
## set: seen words
## transformations counter

# Algorithm
## while len(seen_set) != len wordList:
## increment transformations coutner
## for everything in queue now, add unseen "close words" to queue
## if word was found return transformations counter

# Close words algorithm:
'''
k=length of word, n = len(listWords)
Ideas:
Brute-force (check each word to see if off by one)
Complexity: O(k * n) 

Trie (construct trie of words with one-off compatibility)
Complexity: O(k)

'''

# Trie algorithm

'''
Construct trie like normal
When finding if close word, traverse as normal. Once a letter is not found, record
then bfs down every path. For each path, if a letter isn't found, stop. Otherwise return all found words. If all letters match, then congrats, we found the word!

Realization: I need to consider if the first letter is not found but the rest are! 
New algorithm:
current node is self.begin
for each letter in the word:
    for each existing next letter:
        search, starting from the current node, whether the word, modified with the letter, is in the Trie
            if it is, add the modified word to result
                if it's also the real letter, then just return the word immediately.
            
    if the real letter is next in the trie, set the next node as the current one
    otherwise, break
return result

New realization: Trie isn't actually more efficient than a hashmap and it overcomplicates things. Instead, let's just iterate through every change of the word to see if it has a close word nearby.

Complexity: 26*k per word...damn

'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord: return 0
        generic_words = defaultdict(set)
        for word in wordList:
            for char_idx in range(len(word)):
                generic_words[word[:char_idx] + '*' + word[char_idx+1:]].add(word)
        queue = deque([beginWord])
        seen_words = set()
        transforms = 1
        while queue:
            transforms += 1
            q_length = len(queue)
            for _ in range(q_length):
                next_word = queue.pop()
                for char_idx, char in enumerate(next_word):
                        # let = chr(let_num + ord('a'))
                        # if let == char: continue
                    generic = next_word[:char_idx] + '*' + next_word[char_idx+1:]
                    if generic in generic_words:
                        for word in generic_words[generic]:
                            if word == endWord:
                                return transforms
                            if word not in seen_words:
                                seen_words.add(word)
                                queue.appendleft(word)
        return 0

                

