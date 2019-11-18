# 给出两个整数 a 和 b , 求他们的和

def aplusb(a, b):

    # if(a == 0):return b
    # if(b == 0):return a
    # x1 = a^b
    # x2 = (a&b)<<1
    # return aplusb(x1,x2)

    if ((a&b)==0):
        return a|b
    return aplusb(a^b,(a&b)<<1)

print(aplusb(7,8))