# #Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # Calculate mid index

            if nums[mid] == target:  # Target found
                return mid
            elif nums[mid] < target:  # Target is in the right half
                left = mid + 1
            else:  # Target is in the left half
                right = mid - 1

        return -1  # Target not found