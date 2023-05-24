from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cont = True
        changes = False
        i = 0
        if len(nums) == 1:
            return 1
        while cont == True and i < len(nums):
            if i == len(nums) - 1:
                break
            if nums[i] == '_':
                cont = False
            elif nums[i] == nums[i + 1]:
                nums.pop(i)
                nums.append('_')
                changes = True
            else:
                i += 1
        if changes == True:
            return i
        else:
            return len(nums)