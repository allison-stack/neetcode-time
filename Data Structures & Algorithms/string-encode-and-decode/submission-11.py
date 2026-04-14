class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))
            res += "é"
            res += i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != 'é':
                j += 1
            # keep track of length even when it is more than one digit
            length = int(s[i:j])
            # get index of actual string based on length
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res