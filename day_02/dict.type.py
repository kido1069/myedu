import  json


adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}
cdict_str = '{"username":"yansl","password":"123456"}'

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

def dict_add1():
    adict['sex'] = '男'
    print(adict)
# dumps字典转字符串
def dict2str():
    print(type(adict))
    adict_str = json.dumps(adict)
    print(adict_str)
    print(type(adict_str))
# loads字符串转字典
def str2dict():
    print(type(cdict_str))
    cdict = json.loads(cdict_str)
    print(cdict)
    print(type(cdict))
if __name__ == '__main__':
    # ads()
    # dict_n()
    # dict_ni()
    # dict_add1()
    # dict2str()
    # str2dict()