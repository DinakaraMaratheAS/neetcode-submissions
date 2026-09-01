class Solution:
    def isPalindrome(self, s: str) -> bool:
        newSt=""
        for c in s:
            if c.isalnum():
                newSt+=c.lower()
        return newSt==newSt[::-1]