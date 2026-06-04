class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d={}
        for i in range(len(strs)):
           count = [0]*26
           for j in strs[i]:
            count[ord(j)-ord('a')] +=1
           if tuple(count) in d:
            d[tuple(count)].append(strs[i])
           else:
            d[tuple(count)] =[strs[i]]
        
       

            
        return list(d.values())



                
                
        