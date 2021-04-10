class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        sortedBoxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        
        c = 0
        units = 0
        for bt in sortedBoxTypes:
            tmp = truckSize - (c + bt[0])
            # print(tmp, bt)
            c += bt[0]
            
            if tmp >= 0:
                units += bt[0] * bt[1]
                
            elif (tmp < 0):
                units += (bt[0] + tmp) * bt[1]
            
            # print(units)
            if c > truckSize:
                break
        return units
            