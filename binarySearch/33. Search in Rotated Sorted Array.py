# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104



# 思路
# integer sort 的array 被rotate了 at k 导致array 被分成了两部分，前半部分是升序，后半部分是降序 
# 需要找到target 的index  如果他在nums 中，则返回index，否则返回-1
# range 是0 到len(nums) - 1 左合右合
# target 是nums[mid] 的值 然后判断target 的右边是否是升序，如果是升序，则target 在左边，否则在右边

# 时间复杂度：O(log n) 因为每次查找都将范围缩小一半
# 空间复杂度：O(1) 因为只用了常数个变量 没有使用额外的空间如数组等

class Solution:
    def search(self, nums: List[int], target: int) -> int: