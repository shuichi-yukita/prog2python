'''
Created on 2018/01/07

@author: yukita
'''

x="1:2:3:4"
values=map(int,x.split(':'))

def double(xs):
    result = []
    for k in xs:
        result.append(k*2)
    return result

if __name__ == '__main__':
    print(values)
    values.append(5)
    print(values)
    print(double(range(1,5)))
