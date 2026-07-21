class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            char_to_freq = [0]*26
            for char in word:
                char_to_freq[ord(char)-ord('a')]+=1
            groups[tuple(char_to_freq)].append(word)
        return list(groups.values())
