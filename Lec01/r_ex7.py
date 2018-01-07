'''
Created on 2018/01/07

@author: yukita
'''

command = {"forward":200}
inst_list = [{"forward":200}, {"left":90}, {"forward":200} ]


if __name__ == '__main__':
    print("command:{}".format(command))
    for command in inst_list:
        print("command:{}".format(command))
