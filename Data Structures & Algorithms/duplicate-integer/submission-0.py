class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)    # [1, 2, 3, 3] -> (1, 2, 3)

        if len(nums) != len(nums_set):
            return True
        return False