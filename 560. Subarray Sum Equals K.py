class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_s_c = {0:1}
        cnt=0
        s,p=0,0
        while(p<len(nums)):
            s+=nums[p]
            if s-k in pre_s_c.keys():
                cnt+=pre_s_c[s-k]
            if s in pre_s_c.keys():
                pre_s_c[s]+=1
            else:
                pre_s_c[s] = 1
            p+=1
        return cnt

