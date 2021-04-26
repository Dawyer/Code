# 第12天
#
# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
# 传送带上的第 i 个包裹的重量为 weights[i]。
# 每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

# 二分法解决
def shipWithinDays(weights, D: int) -> int:
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        day, cur = 1, 0
        for weight in weights:  # 累加的和大于mid的话，天数加1，累加计0
            if cur+weight > mid:
                day += 1
                cur = 0
            cur += weight
        if day <= D:
            right = mid
        else:
            left = mid + 1
    return left

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(shipWithinDays([3,2,2,4,1,4], 3))
print(shipWithinDays([1,2,3,1,1], 4))