adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}

def ads():
    print(adict['username'])
    print(bdict['password'])
    adict.pop('password')
    print(adict)

def dict_n():
    adict["username"] = 'wwd'
    print(adict)

def dict_ni():
    adict.update(bdict)
    print(adict)


if __name__ == '__main__':
    # ads()
    # dict_n()
    dict_ni()