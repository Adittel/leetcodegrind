# GROUP ANAGRAMs
#49. Group Anagrams

# https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        x=[str(sorted(a)) for a in strs]
        
        holder = dict()

        for i in range(len(x)):
            if x[i] in holder:
                holder[x[i]].append(strs[i])
            else:
                holder[x[i]] = [strs[i]]
        main=[]
        print(holder)
        for key in (holder):
            main.append(holder[key])
                
        return main
                    
