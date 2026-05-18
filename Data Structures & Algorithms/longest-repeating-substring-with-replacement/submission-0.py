class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        max_length = 0
        hmap = {}

        for right in range(n):
            hmap[s[right]] = hmap.get(s[right], 0) + 1
            if (right-left+1)-max(hmap.values())>k:
                hmap[s[left]]-=1
                left+=1
            max_length =  max(max_length,right-left+1)

        return max_length

        