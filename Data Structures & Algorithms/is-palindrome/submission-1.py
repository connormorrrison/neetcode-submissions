class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(c for c in s.lower() if 'a' <= c <= 'z' or '0' <= c <= '9')

        left_ptr = 0
        right_ptr = len(cleaned_s) - 1

        while left_ptr < right_ptr:
            if cleaned_s[left_ptr] != cleaned_s[right_ptr]:
                return False
            else:
                left_ptr += 1
                right_ptr -= 1

        return True