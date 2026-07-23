class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += chr(len(string))
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0
        while idx < len(s):
            length = ord(s[idx])
            idx += 1
            decoded.append(s[idx:idx+length])
            idx += length
        return decoded