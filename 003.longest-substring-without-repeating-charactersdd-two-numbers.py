
# coding: utf-8

# In[ ]:


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        count = 1
        temp = 1
        sub = ""+s[0]
        f = 0
        for i in range(1,len(s)):
            if sub.find(s[i]) == -1:
                sub += s[i]
                temp +=1
            else:
                f = sub.find(s[i]) + 1
                sub = sub[f::]+s[i]
                temp = temp - f+1
            if temp > count:
                count = temp
        return count
        

