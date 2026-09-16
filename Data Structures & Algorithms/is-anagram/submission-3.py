class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}
        if len(s) != len(t):
            return False

        for char in s:
            char_s[char] = 1 + char_s.get(char,0)

        for char in t:
            char_t[char] = 1 + char_t.get(char,0)   

        if char_s != char_t:
            return False

        return True             