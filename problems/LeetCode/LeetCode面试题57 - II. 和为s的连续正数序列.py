# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
# 示例 1：
#
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：
#
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
# 限制：
#
# 1 <= target <= 10^5

def findContinuousSequence(target: int):
    list=[]
    if target == 1:
        return [1]
    for min_num in range(1,target):
        sum=0
        temp=min_num
        temp_list=[]
        while sum <= target:
            if sum == target:
                list.append((temp_list))
                break
            sum=sum+temp
            temp_list.append(temp)
            temp += 1
    return list
print(findContinuousSequence(1))
