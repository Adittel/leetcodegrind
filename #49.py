# GROUP ANAGRAMs
#49. Group Anagrams

# https://leetcode.com/problems/group-anagrams/

#group anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        holder = dict()

        for i in range(len(strs)):
            if str(sorted(strs[i])) in holder:
                holder[str(sorted(strs[i]))].append(strs[i])
            else:
                holder[str(sorted(strs[i]))] = [strs[i]]
        main=[]
        print(holder)
        for key in (holder):
            main.append(holder[key])
                
        return main
                    
