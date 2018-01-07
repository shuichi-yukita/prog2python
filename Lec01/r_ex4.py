'''
Created on 2018/01/07

@author: yukita
'''
def my_print(text,n):
    for i in range(n):
        print(text)

def map_mult(xs,t):
    return map(lambda x: x*t, xs)


if __name__ == '__main__':
    my_print("Hello",5)
    print(map(lambda x: x*4,[1,2,3,4]))
    print(map_mult([1,2,3,4],4))
#   print(list(map_mult([1,2,3],4)))
