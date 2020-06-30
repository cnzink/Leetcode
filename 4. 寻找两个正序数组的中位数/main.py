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

# 垃圾方法，归并
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         i , j , nums3 = 0 ,0 ,[]
#         while(i<len(nums1) or j<len(nums2)):
#             if j == len(nums2):
#                 nums3.append(nums1[i])
#                 i = i + 1
#             elif i == len(nums1):
#                 nums3.append(nums2[j])
#                 j = j + 1
#             elif nums1[i] <= nums2[j]:
#                 nums3.append(nums1[i])
#                 i = i+1
#             elif nums1[i] > nums2[j]:
#                 nums3.append(nums2[j])
#                 j = j+1
#             else:
#                 break
#         if len(nums3)%2 == 0:
#             return (nums3[int(len(nums3)/2-1)]+nums3[int(len(nums3)/2)])/2
#         else:
#             return nums3[int(len(nums3)/2)]

# 垃圾方法2，不归并
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m = len(nums1)
#         n = len(nums2)
#         total_length = m + n
#         def get_k(k):
#             index1,index2 = 0,0
#             while True:
#                 if index1 == m:
#                    return nums2[index2+k-1]
#                 if index2 == n:
#                     return nums1[index1+k-1]
#                 if k ==1 :
#                     return min(nums1[index1],nums2[index2])
#                 newindex1 = min(index1+k//2-1,m-1)
#                 newindex2 = min(index2+k//2-1,n-1)
#                 pivot1 = nums1[newindex1]
#                 pivot2 = nums2[newindex2]
#                 if pivot1 <= pivot2:
#                     k -= newindex1 - index1 +1
#                     index1 = newindex1 + 1
#                 else:
#                     k -= newindex2 - index2 +1
#                     index2 = newindex2 +1
#         if total_length %2 == 1:
#             return get_k((total_length+1)//2)
#         else:
#             return (get_k(total_length//2)+get_k(total_length//2+1))/2

# 聪明办法，划分数组
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        infinty = 2**40 #代表无穷大
        m ,n = len(nums1),len(nums2)
        left ,right,ansi = 0,m,-1
        while left <= right:
            i = (left+right)//2
            j = (m+n+1)//2-i
            nums_im1 = -infinty if i==0 else nums1[i-1]
            nums_i = infinty if i == m else nums1[i]
            nums_jm1 = -infinty if j == 0 else nums2[j - 1]
            nums_j = -infinty if j == n else nums2[j]
            if nums_im1 <= nums_j:
                # ansi = i
                median1,median2 = max(nums_im1,nums_jm1),min(nums_i,nums_j)
                left = i+1
            else:
                right = i-1
        return (median1+median2)/2 if(m+n)%2 ==0 else median1

if __name__ == '__main__':
    A =Solution()
    print(A.findMedianSortedArrays([1,2,3,6],[1,3,4,5,8]))