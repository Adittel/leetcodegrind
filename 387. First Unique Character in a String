#387. First Unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=dict();
        for i in s:
            if(i in x):
                x[i]+=1
            else:
                x[i]=1
        for i in range(len(s)):
            if(x[s[i]]==1):
                return i
        return -1
