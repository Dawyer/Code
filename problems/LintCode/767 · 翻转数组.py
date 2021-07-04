"""
第58天
原地翻转给出的数组 nums
"""

class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # 1.使用reverse()方法将列表元素反向排列
        # nums.reverse()
        # return nums

        # 2.从列表开头遍历到中间，将列表首位的元素调换
        n = len(nums)
        for i in range(n // 2 + 1):
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.reverseArray([1,2,5,3,6,5,3,8]))