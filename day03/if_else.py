def if_demo():
    a = 1 > 2
    if a:
        print('zhen')
    else:
        print('jia')

def ifel_demo():
    a = 10
    if a == 1:
        print('a是1')
    elif a == 2:
        print('a是2')
    elif a == 3:
        print('a是3')
    elif a == 4:
        print('a是4')
    elif a == 5:
        print('a是5')
    else:
        print('a是%s'%a)
    print('if结束')








if __name__ == '__main__':
    ifel_demo()
