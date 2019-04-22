import json
adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}
cdict_str = '{"username":"yansl","password":"123456"}'

def diyici():

    # a = dict(adict, **bdict)
    # print(a)
    # b = dict(bdict,**cdict_str)
    # print(b)
    # b = dict(bdict,**cdict_str)
    # print(b)
    # print(type(cdict_str))
    # a = json.loads(cdict_str)
    # print(a)
    # print(type(a))
    # print(type(bdict))
    # b = json.dumps(bdict)
    # print(b)
    # print(type(b))
    bdict[12] = 'nan'
    print(bdict)

def qwe():
    a = 'ni'
    b = 123
    c = 'hao'
    print(a +str (b)+c )
    print('a是%s b是%s c是%s'%(a,b,c))


def cheng():
    for i in  range(1,10):
        x = i+1
        for j in range(1,x):
            print('%s * %s =%s'%(i,j,i*j),end='   ')
        print('')

if __name__ == '__main__':
    # diyici()
    # qwe()
    # jishu()
    # a = 5
    # while a < 10:
    #     print(a)
    #     a += 1

     # a = 1
     # b = 0
     # while a<= 50:
     #    print(a)
     #    a+=2

    sum = 0
    for i in  range(1,51):
        if i%2 == 1:
            sum =sum+i
    print(sum)
    # cheng()