class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = []
        max_length = 0

        for right in s:

            while right in current_string:
                current_string.pop(0)
                
            current_string.append(right)
            max_length = max(max_length,len(current_string))

        return max_length 