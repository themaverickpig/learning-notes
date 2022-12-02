'''
a = 123.2
b = 'string'
print(type(a),type(b))
print(isinstance(a,int),isinstance(b,str))


# list相关知识点
list = ['abc',1234,22123,314231,'run',12.43]
list2 = ['list2',2]
print(list)
list[2] = 'list1'
print(list)



# 反转字符串
def reverseWords(input):
  inputWords = input.split(" ")
  inputWords = inputWords[-1::-1]
  output = ' '.join(inputWords)
  return output

if __name__ == "__main__":
  input = 'i like you'
  rw = reverseWords(input)
  print(rw)


# tuple 相关知识点
tuple = ('abcd',231,21.3,'run',201.2)
tinytuple = (123,'run')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple*2)
print(tuple + tinytuple)

# Set集合相关知识点
sites = {'google','taobao','ali','tencent','facebook','zhihu','baidu','taobao'}
print(sites) # 输出集合，重复的元素被自动去掉
if 'taobao' in sites:
  print('taobao inside')
else:
  print('taobao outside')

a = set('abcdefg')
b = set('abcxyzabc')
print(a)
print(a-b) # a 和 b 的差集 a中有 b中没有的元素
print(a | b) # a 和 b 的并集 a b 中有的所有不重复的元素合集
print(a & b) # a 和 b 的交集 a b 中重复的元素的合集
print(a ^ b) # a 和 b 中不同时存在的元素
'''

# Dictionary 相关知识点操作
dict = {}
dict['one'] = '1 - 教程'
dict[2] = '2 - 工具'
dict2 = {'name':'教程','code':2,'site':'www.baidu.com'}
print(dict['one'])
print(dict[2])
print(dict2)
print(dict2.keys())
print(dict2.values())

