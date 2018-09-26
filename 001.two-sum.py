
# coding: utf-8

# In[ ]:


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sort = sorted(enumerate(nums), key=lambda x:x[1])
        for i in range(len(nums_sort)):
            for j in range(i+1,len(nums_sort)):
                if nums_sort[i][1] + nums_sort[j][1] == target:
                    return [nums_sort[i][0],nums_sort[j][0]]             

