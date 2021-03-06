class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
            
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                if self.judge(nums, mid, right):
                    right = mid
                else:
                    left = mid
        return nums[left] if nums[left] < nums[right] else nums[right]
        
    def judge(self, A, mid, right):
        temp = None
        for i in A[mid:right + 1]:
            if temp is None or i == temp:
                temp = i
            else:
                return False
        return True