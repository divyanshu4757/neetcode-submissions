class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zeroCount = 0
        result=[]
        for n in nums:
            if n==0:
                zeroCount += 1
                continue
            else:
                product = product * n

        for n in nums:
            if n!=0 and zeroCount > 0:
                result.append(0)
            elif n==0 and zeroCount == 1:
                result.append(product)
            elif n==0 and zeroCount > 1:
                result.append(0)
            else:
                result.append(int(product/n))
        return result
