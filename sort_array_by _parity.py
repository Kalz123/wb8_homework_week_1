''' leetcode #905
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.
You may return any answer array that satisfies this condition.

 Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

leetcode #905
'''


def sortArrayByParity(nums):
    # nums.sort(key=lambda x: x % 2)                                                  time O(NlogN), space O(N)
    # return nums

    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] % 2 > nums[r] % 2:
            nums[l], nums[r] = nums[r], nums[l]  # time O(N), space O(1)
        elif nums[l] % 2 == 0:
            l += 1
        elif nums[r] % 2 == 1:
            r -= 1
    return nums


nums = [3, 1, 2, 4]
sortArrayByParity(nums)
