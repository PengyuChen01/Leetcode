# This is an interactive problem.

# You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

# returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
# returns 231 - 1 if the i is out of the boundary of the array.
# You are also given an integer target.

# Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: secret = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in secret and its index is 4.
# Example 2:

# Input: secret = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in secret so return -1.

#思路
# 1. 找到target的边界，这题是没告诉数组大小，所以需要自己找边界， 可以每次把end*2，直到找到target
# 2. 找到边界后，用二分查找找到target

# 时间复杂度：O(logn)
# 空间复杂度：O(1)

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start, end = 0, 1
        while reader.get(end) < target:
            start = end
            end *= 2

        while start + 1 < end:
            mid = (start + end) // 2
            val = reader.get(mid)
            if val < target:
                start = mid
            elif val > target:
                end = mid
            else:
                return mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1

# 测试
reader = ArrayReader([-1,0,3,5,9,12])
target = 9
print(Solution().search(reader, target))


