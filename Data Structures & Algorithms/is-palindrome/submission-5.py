class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                res += i.lower()
        return res == res[::-1]