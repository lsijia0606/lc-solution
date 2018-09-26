
# coding: utf-8

# In[ ]:


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        length = len(x)
        if length%2 == 0:
            for i in range(length/2):
                if x[i] == x[length - i-1]:
                    continue
                else:
                    return False
            return True
        else:
            for j in range((length-1)/2):
                if x[j] == x[length-1-j]:
                    continue
                else:
                    return False
            return True
    
                

