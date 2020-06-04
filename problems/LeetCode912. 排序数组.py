# 给你一个整数数组 nums，请你将该数组升序排列。
#
#  
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]

def sortArray(nums):
    merge_sort(nums,0,len(nums)-1)
    return nums

def merge_sort(nums,l,r):
    if l == r:
        return
    mid = (l+r) // 2
    merge_sort(nums,l,mid)
    merge_sort(nums,mid+1,r)
    tmp=[]
    i,j = l,mid+1
    while i <= mid or j <= r:
        if i > mid or (j <= r and nums[j] < nums[i]):
            tmp.append(nums[j])
            j += 1
        else:
            tmp.append(nums[i])
            i += 1
    nums[l:r+1] = tmp

print(sortArray([5,2,3,1]))
print(sortArray([5,1,1,2,0,0]))