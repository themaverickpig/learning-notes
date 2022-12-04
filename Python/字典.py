'''
  tinydict1 = {'abc':123}
  tinydict2 = {'abc':123,98:23}
  print(tinydict2)
  print(type(tinydict2))
  print(len(tinydict2))
  
tinydict = {'name':'run','age':7,'class':'first'}
tinydict['age'] = 8
tinydict['school'] = 'tsinghua'
print(tinydict['age'])
print(type(tinydict['school']))
print(id(tinydict))
del tinydict
print(tinydict)

tinydict = {1:[1,2,3],2:[2,3,4]}
dict = tinydict # 直接赋值
dict2 = tinydict.copy() # 浅拷贝
dict3 = copy.deepcopy(tinydict) # 深拷贝

print(dict)
print(dict2)
print(dict3)

tinydict[1].append('hello')

print(dict)
print(dict2)
print(dict3)
print(tinydict.keys())
print(tinydict.values())


# 题目1
x = True
country_counter = {}
def add(country):
  if country in country_counter:
    country_counter[country] += 1
  else:
    country_counter[country] = 1

add('china')
add('japan')
add('china')
print(len(country_counter))


'''
import copy
confusion = {}
