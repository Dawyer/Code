

def fun1(fun):
    def fun2(*args,**kwargs):
        print('start')
        return_fun = fun(*args,**kwargs)
        print('end')
        return return_fun
    return fun2


@fun1
def fun(arg1):
    print('开始')
    print(arg1)
    print('结束')
    return '完成'


fun([1,2,3])