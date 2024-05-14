import random
import requests
s = 'more is different'
# print(s[3:90:2])
# print('m' in s)
# print('test'.join(['1','2','3']))
# print(s.split(' '))   #以 为间隔符返回列表
s_str = list(s)         #将字符串转化为列表
# print(s_1)

ls1 = [1,2,3]
ls2 = [5,6]
ls = ls1 + ls2          #splice the list
ls.insert(4,9)
                        #Insert element at specified position
ls.append(4)            #在末尾添加
# print(ls)
ls.pop(3)               #pop(i)删除第i-1个，pop()默认删除最后一个
# print(ls)

#删除列表元素
#方法一
# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)     # 删除值为 3 的元素
# print(my_list)        # 输出 [1, 2, 4, 5]

#方法二
# my_list = [1, 2, 3, 4, 5]
# del my_list[2]        # 删除索引为 2 的元素（值为 3）
# print(my_list)        # print [1, 2, 4, 5]

#方法三
# my_list = [1, 2, 3, 4, 5]
# my_list = [x for x in my_list if x >= 3]
# print(my_list)        # print [3, 4, 5]

ls.reverse()            #reverse
# print(ls)
ls.sort()               #Sort from small to large
# print(ls)
ls.sort(reverse = True) #Sort from large to small
# print(ls)
s_str.sort(key = len)   #Sort by keyword by string length
ls.extend('python')     #将可迭代对象(iterable)添加到列表末尾
ls = [i for i in ls if isinstance(i,str) != True]
                        #delete the string variable in ls
# print(ls)

tup = tuple(ls)         #convert a list into a tuple
# print(tup)
# print(sum(ls))        #find the sum of list,tuple

gather = set()          #Create empty set
dict = {}               #creat empty dict
dict.update({'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5})
                        #add key value pairs to a dict
dict['f'] = 6           #add key value pairs to a dict
# print(dict)

#print(abs(-654))        #Find the absolute value
#print(abs(3+4j))        #Find the modulus of a complex number
#print(round(3.14159265,4))
                        #Round to 3.14159265，Keep n decimal places
num1 = 3.14159265
# print(f"x是{num1:.2f}")

#判断素数
def isprime(num):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

#区分continue和break
num2 = random.random()         #Generate decimals in [0.0,1.0)
num3 = random.randint(3,13)
                                #Generate integers in [a,b]
# if __name__ == "__main__":    #当前模块被其他模块调用时判断是否执行if __name__ == "__main__"下的语句

class people():
    def __init__(self,name,age,sex,hobby):#__init__函数在创建对象时自动调用
        self.name = name
        self.age = age
        self.sex = sex
        self.hobby = hobby
        print('调用了__init__函数')
    def self_introduction(self,string):
        print(string)
cxk = people('鸡',18,'female',['sing','jump','rap','basketball'])
# cxk.self_introduction(s)        #调用了self_introduction函数
# print(cxk.name)
class College_Students(people):
    def __init__(self,name,age,sex,hobby,major1):
        people.__init__(self, name, age, sex, hobby)
                                #调用了people类的__init__()函数给名字、年龄、性别、爱好赋值
        self.major = major1

f1 = open(r'1.txt','r',encoding='utf-8')
f1_read = f1.read()
f1.seek(0)                      #将指针重新设置到开头
f1_readlines = f1.readlines()
f1.seek(0)
f1_readline1 = f1.readline()
f1_readline2 = f1.readline()
f1_readline3 = f1.readline(2)
f1.close()                      #open后务必close
# print(f1_read)
# print(f1_readlines)
# print(f1_readline1)
# print(f1_readline2)
# print(f1_readline3)
# with open('scores.txt','r',encoding='utf-8') as scores_file,open('scores_english.txt','r',encoding='utf-8') as scores_english_file,open('scores_all.txt','w',encoding='utf-8') as scores_all_file,open('scores_all_lines.txt','w',encoding='utf-8') as scores_all_lines_file:
#     scores_readlines = scores_file.readlines()
#     scores_english_readlines = scores_english_file.readlines()
#     write_lines = []
#     print(type(scores_readlines))
#     print(scores_readlines)
#     print(list(zip(scores_readlines,scores_english_readlines)))
#     for scores_line,scores_english_line in zip(scores_readlines,scores_english_readlines):
#         scores_line = scores_line.strip()
#         scores_english_line = scores_english_line.strip()
#         print(scores_line)
#         print(scores_english_line)
#         scores_english_line = scores_english_line.split(',')
#         print(scores_english_line)
#         merged_line = scores_line + ',' + scores_english_line[-1] + '\n'
#         print(merged_line)
#         scores_all_file.write(merged_line)
#         write_lines.append(merged_line)
#     scores_all_lines_file.writelines(write_lines)

