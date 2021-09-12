from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    answer = [nums[i], nums[left], nums[right]]
                    if answer not in result:
                        result.append(answer)
                    left += 1
                    right -= 1
        return result
