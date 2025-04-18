# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# 思路：
# 1. 题目问了O(log n) 的时间复杂度，所以需要使用二分查找
# 2. array 是升序sorted 的，如果target 在 array 中，则返回target 的index，否则返回-1
# 3. range 是0 到len(nums) - 1 左合右合
# 4. target 是nums[mid] 的值

# 时间复杂度：O(log n) 因为每次查找都将范围缩小一半
# 空间复杂度：O(1) 因为只用了常数个变量 没有使用额外的空间如数组等
import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = left +(right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1 

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print("target 9 is in nums: ", Solution().search(nums, target))

    target = 2
    print("target 2 is in nums: ", Solution().search(nums, target))