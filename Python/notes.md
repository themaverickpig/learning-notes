### 判断数据类型
isinstance 和 type 
* type 不会认为子类是一种父类类型
* isinstance 会认为子类是一种父类类型

Python字符串不能被改变。向一个索引位置赋值，会导致错误。
* 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
* 字符串可以用+运算连接在一起，用*运算符重复
* Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
* Python中的字符串不能改变

### list
和字符串一样，list可以被索引和截取，list被截取后返回一个包含所需元素的新列表
* list卸载方括号之间，元素用逗号隔开
* 和字符串一样，list可以被索引和切片
* list可以使用 + 操作符进行拼接
* list中的元素是可以改变的

Python的list截取可以接收第三个参数，参数作用是截取的步长：
````python
letters = ['r','u','n','o','o','b']
letters[1:4:2]
# ['u','o']
````
如果第三个参数为负数表示逆向读取
````python
#用于反转字符串
def reverseWords(input):
  #通过空格将字符串分隔符，把各个单词分隔为列表
  inputWords = input.split(" ")

  # 翻转字符串
  # 假设列表 list = [1,2,3,4],
  # list[0] = 1, list[1]=2,而 -1 表示最后一个元素 list[-1]=4(与list[3]=4 一样）
  # inputWords[-1::-1]有三个元素
  # 第一个参数 -1 表示最后一个元素
  # 第二个参数为空，表示移动到列表末尾
  # 第三个参数为步长，-1 表示逆向
  inputWords=inputWords[-1::-1]

  # 重新组合字符串
  output = ' '.join(inputWords)
  return output

if __name__ == "__main__":
  input = 'i like runoob'
  rw = reverseWords(input)
  print(rw)
````

## Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号（）里，元素之间用逗号隔开。元祖中的元素类型也可以不相同：
````python
# tuple 相关知识点
tuple = ('abcd',231,21.3,'run',201.2)
tinytuple = (123,'run')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple*2)
print(tuple + tinytuple)
````
元组与字符串类似，可以被索引且下标索引从0开始，-1为从末尾开始的位置。也可以进行截取。其实可以把字符串看作一种搞特殊的元组。
元组的元素不可改变
但是可以包含可变的对象，比如list列表。
构造包含0个或1个元素的元组比较特殊，所以有一些额外的语法规则：
````python
tup1 = ()  # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
````

String list tuple 都属于sequence（序列）
* 与字符串一样，元组的元素不能修改
* 元组也可以被索引和切片，方法一样
* 注意构造包含0或1个元素的元组的特殊语法规则 
* 元组也可以使用 + 操作符进行拼接

## Set（集合）
集合是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{ },因为{ }是用来创建一个空字典。

````python
# eg.创建集合
parame = {value01,value02,...}
# 或者
set(value)
# 相关知识点
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
````
## Dictionary(字典)
列表是有序的对象集合，字典是无序的对象集合。
**两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取的。**
字典是一种映射类型，字典{ }标识，它是一个无序的 **键(key):值(value)**的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。

## Python推导式
python推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体
Python支持各种数据结构的推导式：
* 列表list推导式
* 字典dict推导式
* 集合set推导式
* 元组tuple推导式

### 列表推导式
格式：
````python
[表达式  for 变量 in 列表]
[out_exp_res  for  out_exp  in input_list]

或者
[表达式  for 变量 in 列表 if 条件]
[out_exp_res  for  out_exp  in input_list if condition]
````
* out_exp_res:列表生成元素表达式，可以是有返回值的函数。
* for out_exp in input_list :迭代input_list将out_exp传入到out_exp_res表达式中
* if condition :条件语句，可以过滤列表中不符合条件的值

````python 

````


