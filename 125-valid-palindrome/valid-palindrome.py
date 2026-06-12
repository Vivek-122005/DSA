class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(ch for ch in s if ch.isalnum()).lower()
        return result == result[::-1]
        