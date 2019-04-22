def a():
    for i in range(10):
        print(i)
        print('hello word')

def b():
    for i in range(3,10):
        print(i)

ad = ['哈',1213,'hao',3123143]

def d():
    for i in ad:
        print(i)


def d2():
    a = len(ad)
    for i in range(a):
        print(ad[i])


if __name__ == '__main__':
    # a()
    # b()
    d2()