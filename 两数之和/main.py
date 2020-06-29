# encoding:utf-8
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 暴力循环法，时间复杂度O(n*n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target and i != j:
#                     return [i, j]
#                 j = j + 1
#             i = i + 1

# 首尾递进法，时间复杂度O(nlogn)//排序花费
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         id = sorted(range(len(nums)),key=lambda k:nums[k],reverse=False)
#         head = 0
#         end = len(nums) -1
#         while head < end:
#             if nums[id[head]] + nums[id[end]] < target:
#                 head = head+1
#             elif nums[id[head]] + nums[id[end]] == target:
#                 return [id[head],id[end]]
#             elif nums[id[head]] + nums[id[end]] > target:
#                 end = end-1

# 字典法，时间复杂度O(n)
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap = {}
    #     for index,num in enumerate(nums):
    #         another_num = target - num
    #         if another_num in hashmap:
    #             return [hashmap[another_num],index]
    #         hashmap[num] = index
    #     return None
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,num in enumerate(nums):
            try:
                return [hashmap[target - num],index]
            except:
                hashmap[num] = index
        return None



if __name__ == '__main__':
    A = Solution()
    print(A.twoSum(nums=[15, 11, 7, 2], target=9))
