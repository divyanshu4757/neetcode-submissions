class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =[]
        d={}
        for i in range(len(strs)):
           sortedS = ''.join(sorted(strs[i]))
           if sortedS in d:
            d[sortedS].append(i)
           else:
            d[sortedS]= [i]
        
        for value in d.values():
            temp = []
            for n in value:
                temp.append(strs[n])
            result.append(temp)


            
        return result



                
                
        