class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = 0
        i = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[1::], 1):
                if a + b == target and j != i:
                    return [i, j]

