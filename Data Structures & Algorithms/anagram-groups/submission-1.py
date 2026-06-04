class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =[]
        d={}
        for i in range(len(strs)):
           sortedS = ''.join(sorted(strs[i]))
           if sortedS in d:
            d[sortedS].append(strs[i])
           else:
            d[sortedS] = [strs[i]]
        
       

            
        return list(d.values())



                
                
        