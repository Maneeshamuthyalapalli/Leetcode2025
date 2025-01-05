class Solution:
    from math import gcd
    from functools import reduce 
    def lcm(a, b):
        return a * b // gcd(a, b)
    def maxLength(self, nums: List[int]) -> int:
        n, max_length = len(nums), 0
        for i in range(n):
            sub_gcd, sub_lcm, sub_prod = nums[i], nums[i], nums[i]
            for j in range(i, n):
                if j > i:
                    sub_gcd = gcd(sub_gcd, nums[j])
                    sub_lcm = lcm(sub_lcm, nums[j])
                    sub_prod *= nums[j]
                if sub_prod == sub_gcd * sub_lcm:
                    max_length = max(max_length, j - i + 1)
        return max_length
            
        
   

©leetcode
