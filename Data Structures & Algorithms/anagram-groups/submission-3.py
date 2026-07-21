class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_to_words: dict[frozenset[tuple[str, int]], List[str]] = {}
        for word in strs:
            freq_dict = {}
            for char in word:
                freq_dict[char] = freq_dict.get(char, 0) + 1
            freq_set = frozenset((char, count) for char, count in freq_dict.items())
            group_to_words.setdefault(freq_set, []).append(word)
        return list(group_to_words.values())