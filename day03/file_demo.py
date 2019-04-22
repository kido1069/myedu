

if __name__ == '__main__':
    text_io = open('test','w+')
    text_io.write('你')

    text_io = open('test.text', 'a+')
    text_io.write('呵呵呵呵呵呵')
    text_io = open('test.text', 'r')
    readlines = text_io.readlines()
    print(readlines[2])
