# Binary Search (二分查找)

## 基本概念
二分查找是一种在有序数组中查找特定元素的算法。时间复杂度为 O(log n)，空间复杂度为 O(1)。
Search 的区间是什么？
怎么确定 target？

## 使用场景
1. 有序数组中的查找
2. 旋转数组中的查找
3. 在有序矩阵中查找
4. 查找峰值元素
5. 查找缺失值
6. 查找重复值
7. 查找范围

## 模板代码
### 模板1：标准二分查找
```python
[start end]
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
```
[start end）
### 模板2：查找左边界
```python
def binary_search_left(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
            
    return left
```
[start end)
### 模板3：查找右边界
```python
def binary_search_right(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
            
    return left - 1
```
range 从 第二个 到倒数第二个
def search(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
    if nums[mid] < target:
        start = mid
    elif nums[mid] > target:
        end = mid
    else:
        return mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1


## 常见题型
1. 查找目标值
   - 704. Binary Search
   - 33. Search in Rotated Sorted Array
   - 81. Search in Rotated Sorted Array II

2. 查找边界
   - 34. Find First and Last Position of Element in Sorted Array
   - 35. Search Insert Position

3. 查找峰值
   - 162. Find Peak Element
   - 852. Peak Index in a Mountain Array

4. 查找缺失值
   - 268. Missing Number
   - 287. Find the Duplicate Number

5. 在矩阵中查找
   - 74. Search a 2D Matrix
   - 240. Search a 2D Matrix II

## 解题技巧
1. 确定搜索区间
   - 左闭右闭 [left, right]
   - 左闭右开 [left, right)

2. 确定循环条件
   - while left <= right (all range)
   - while left < right  (excluding right)

3. 确定中间值计算
   - mid = left + (right - left) // 2  # 防止整数溢出

4. 确定更新条件
   - left = mid + 1
   - right = mid - 1
   - right = mid

5. 处理边界情况
   - 空数组
   - 单元素数组
   - 目标值不存在

## 注意事项
1. 数组必须是有序的
2. 注意整数溢出问题
3. 注意边界条件的处理
4. 注意循环终止条件
5. 注意返回值的选择

## 时间复杂度分析
- 时间复杂度：O(log n)
- 空间复杂度：O(1)

## 常见错误
1. 死循环
2. 边界条件处理不当
3. 返回值错误
4. 整数溢出
5. 区间更新错误


