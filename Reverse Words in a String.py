class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(map(str,s.split()))
        s=s[::-1]
        return " ".join(s)