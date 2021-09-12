from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()
                if stack:
                    left = stack[-1]
                    distance = i - left - 1
                    water = min(height[left], h) - height[top]
                    volume += distance * water
                else:
                    break
            stack.append(i)
        return volume