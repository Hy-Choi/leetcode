class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        indexes = [i for i, value in enumerate(arr) if value == 0]
        for idx, i in enumerate(indexes):
            arr.insert(i+idx,0)
            arr.pop(-1)

