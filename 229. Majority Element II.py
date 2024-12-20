class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i]+=1
        k = int(len(nums)/3)
        res=[]
        for i in d.keys():
            if d[i] > k:
                res.append(i)
        return res
