class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result =[]
        for n in nums:
            if n in freq:
                freq[n] = freq[n]+1
            else:
                freq[n]=1
        

        sorted_freq = sorted(freq.items(), key=lambda x: x[1],reverse=True)
       
        i=0
        
        while k!=0:
            result.append(sorted_freq[i][0])
            k -=1
            i +=1
        return result


        