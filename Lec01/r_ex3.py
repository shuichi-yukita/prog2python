'''
Created on 2018/01/06

@author: yukita
'''
from pip.utils.logging import indent_log

# recursive definition
def has_negative(xs):
#    print(xs)
    if xs == []:
        return False
    elif xs[0]<0:
        return True
    else:
        return has_negative(xs[1:])

# imperative alternative
def has_negative2(xs):
    for i in range(len(xs)):
        if (xs[i]<0):
            return True
        else:
            continue
    return False

# definition with local recursive function
def find_negative(xs):
    def it(i,ixs):
        if ixs == []:
            return -1
        elif ixs[0]<0:
            return i
        else:
            return it(i+1,ixs[1:])
    return it(0,xs)

# imperative alternative
def find_negative2(xs):
    for i in range(len(xs)):
        if xs[i]<0:
            return i
        else:
            continue
    return -1

if __name__ == '__main__':
    print('has_negative')
    print(has_negative([]))
    print(has_negative([1,2,3]))
    print(has_negative([3,-1,2]))
    print('has_negative2')
    print(has_negative2([]))
    print(has_negative2([1,2,3]))
    print(has_negative2([3,-1,2]))
    print('find_negative')
    print(find_negative([]))
    print(find_negative([1,2,3]))
    print(find_negative([3,-1,2]))
    print('find_negative2')
    print(find_negative2([]))
    print(find_negative2([1,2,3]))
    print(find_negative2([3,-1,2]))

