class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            # length of string (can be multiple digits) + separator + actual string
            res += str(len(i)) + "é" + i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        start = 0
        while i < len(s):
            if s[i] == "é":
                length = int(s[start:i])
                res.append(s[i+1:length+i+1])
                i += 1 + length
                start = i
            else:
                i += 1
        return res
            