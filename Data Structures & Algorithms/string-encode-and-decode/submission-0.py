class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)).zfill(3)
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0
        while idx < len(s):
            length = int(s[idx:idx+3])
            idx += 3
            decoded.append(s[idx:idx+length])
            idx += length
        return decoded