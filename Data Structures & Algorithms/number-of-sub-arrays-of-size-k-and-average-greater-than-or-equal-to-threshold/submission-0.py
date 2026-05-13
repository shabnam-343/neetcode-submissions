class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0 
        target = threshold*k
        c_sum = sum(arr[:k])
        if c_sum >= threshold*k:
                count = 1

        for i in range(k,len(arr)):
            c_sum +=arr[i] - arr[i - k]
            if c_sum >= target:
                count+=1
        return count
            