class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append('#')
        
        s = 0
        out = []
        
        for i in range(1, len(nums)):
            if nums[i-1]+1!=nums[i]:
                if i-1>s:
                    out.append(str(nums[s])+'->'+str(nums[i-1]))
                else:
                    out.append(str(nums[s]))
                s = i

        return out