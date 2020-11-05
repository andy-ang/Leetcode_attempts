# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:17:41 2020

@author: andya
"""

class Solution:
           
        
    def twoSum(self, list_nums, target):
        answer = []
        
        for i, num_i in enumerate(list_nums):
            for j, num_j in enumerate(list_nums):
                if i!= j and num_i+num_j == target:
                    answer = sorted([i, j])
        return answer
    
Solution().twoSum([3,1,3],6)




class Solution:
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
            print(h, n)
