class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        
        output = [[]]
        
        t = 1
        for l in range(1, length+1):            
            tmp = nums[:]
            
            # print(tt)
            for o in output: 
                for tt in tmp:
                    if tt not in o:
                        tmp2 = sorted(o[:] + [tt])

                        if tmp2 not in output:
                            output.append(tmp2)
                            # print("in", output)
    
        return output
                