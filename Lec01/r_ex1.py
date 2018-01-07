'''
Created on 2018/01/06

@author: yukita
'''
def addup10():
    temp = 0
    for x in [1,2,3,4,5,6,7,8,9,10]:
        temp += x
    return temp


def addup(n):
    temp = 0
    for x in range(n+1):
        temp += x
    return temp


if __name__ == '__main__':
    print('addup10()={0}, addup(10)={1}'.format(addup10(),addup(10)))
    print('addup10()=%d, addup(10)=%d' % (addup10(), addup(10)))

