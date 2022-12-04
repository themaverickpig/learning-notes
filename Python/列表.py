list = ['facebook','taobao','tencent','alibaba','alibaba','net','JD']
# print(list[0])
# print(list[-1])
# print(list[1:3])
# list.append('JD')
# print(list)
# del list[-1]
# print(list)
# print(len(list))
# print('alibaba'  in list)
# for x in [1,2,3]:
#   print(x,end=' ')
print(list)
print(max(list))
print(min(list))
print(list.count('alibaba'))
print(list.index('alibaba')) #返回第一个索引值
list.insert(2,'JD')
print(list)
a = list.pop(1)
print(list)
print(a)
list.reverse()
print(list)