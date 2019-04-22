def app():
    for i in  range(5):
        print(i)
        if i ==2:
            break

def ads():
    for i in  range(4):
        print(i)
        if i ==2:
            continue
        print('第%s'%i)


if __name__ == '__main__':
    a = 5
    while a<10 :
        print(a)
        a+=1
    # ads()
