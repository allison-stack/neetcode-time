class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += i
            res += "á"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for i in s:
            if i == "á":
                res.append(word)
                word = ""
            else:
                word += i
        return res