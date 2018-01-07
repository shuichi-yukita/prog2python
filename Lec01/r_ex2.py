'''
Created on 2018/01/06

@author: yukita
'''

from itertools import repeat

def mysum(xs):
    acc = 0
    for x in xs:
        acc += x
    return acc

def myproduct(xs):
    acc = 1
    for x in xs:
        acc *= x
    return acc

if __name__ == '__main__':
    print 'mysum([1..10])={0}'.format(mysum(range(11)))
    print 'myproduct([2 repeated 10 times]={0}'.\
            format(myproduct(repeat(2,10)))
