# python推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体
# Python支持各种数据结构的推导式：
'''
# 列表推导式
names = ['bob','tom','alice','jerry','wendy','smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)
# 计算30以内可以被3整除的整数：
multiples = [ i for i in range(30) if i % 3 ==0]
print(multiples)

# 字典推导式
listdemo = ['google','tencent','facebook']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict) # {'google': 6, 'tencent': 7, 'facebook': 8}
# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {x: x**2 for x in (2,4,6)}
print(dic)

#计算数字1,2，3的平方数
setnew = { i**2 for i in (1,2,3)}
print(setnew)
# 判断不是abc的字母并输出
a = {x for x in 'abcdhasjhduiqhasca' if x not in 'abc'}
print(a)


# 生成一个包含数字1到9的元组：
a = (x for x in range(1,10))
print(tuple(a))
'''

# 字符串运算符
# print(r'\n')
# str = '[demo]'
# print(str.center(40,'#'))
# str = 'abcdefgacbef'
# str2 = 'abc'
# print(str.count('a'))
# print(str.count(str2))
# print(len(str))
# print(max(str))
# print(str.replace('a','A',1))

str = 'i love you so much!'
strList = str.split( )
# print(strList)
strList.append('happy')
del strList[2]
print(strList)
