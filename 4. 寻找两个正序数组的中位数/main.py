# encoding:utf-8
"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 垃圾方法
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i , j , nums3 = 0 ,0 ,[]
        while(i<len(nums1) or j<len(nums2)):
            if j == len(nums2):
                nums3.append(nums1[i])
                i = i + 1
            elif i == len(nums1):
                nums3.append(nums2[j])
                j = j + 1
            elif nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i = i+1
            elif nums1[i] > nums2[j]:
                nums3.append(nums2[j])
                j = j+1
            else:
                break
        if len(nums3)%2 == 0:
            return (nums3[int(len(nums3)/2-1)]+nums3[int(len(nums3)/2)])/2
        else:
            return nums3[int(len(nums3)/2)]

if __name__ == '__main__':
    A =Solution()
    print(A.findMedianSortedArrays([0,0 ],[0,0]))