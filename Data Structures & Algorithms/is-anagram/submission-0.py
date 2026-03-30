class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(s), sorted(t)
        s, t= "".join(s), "".join(t)
        return s.lower() == t.lower()
        