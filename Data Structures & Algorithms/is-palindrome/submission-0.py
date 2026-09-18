class Solution:
    def isPalindrome(self, s: str) -> bool:
      clean_s = [char.lower() for char in s if char.isalnum()]
      L = 0
      R = len(clean_s) - 1

      while L < R:
        if clean_s[L] != clean_s[R]:
          return False  # Mismatch! Not a palindrome.
        L += 1
        R -= 1

      return True  # All characters matched!