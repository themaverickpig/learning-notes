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
字典类型也有一些内置的函数，例如clear()  keys()  values()等
* 字典是一种映射类型，它的元素是键值对
* 字典的关键字必须为不可变类型，且不能重复
* 创建空字典使用 **{}**

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
names = ['bob','tom','alice','jerry','wendy','smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)

# 计算30以内可以被3整除的整数：
multiples = [ i for i in range(30) if i % 3 ==0]
print(multiples)
````
### 字典推导式
```` python
{ key_expr : value_expr for value in collection}
或
{ key_expr : value_expr  for value in collection if condition}

# 字典推导式
listdemo = ['google','tencent','facebook']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict) # {'google': 6, 'tencent': 7, 'facebook': 8}
# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {x: x**2 for x in (2,4,6)}
print(dic)
````

### 集合推导式
````python
{expression for item in sequence }
或
{expression for item in sequence if conditional}

#计算数字1,2，3的平方数
setnew = { i**2 for i in (1,2,3)}
print(setnew)
# 判断不是abc的字母并输出
a = {x for x in 'abcdhasjhduiqhasca' if x not in 'abc'}
print(a)
````

### 元组推导式（生成器表达式）
元组推导式可以利用range区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
````python
(expression for item in sequence )
或
(expression for item in sequence if conditional )

# 生成一个包含数字1到9的元组：
a = (x for x in range(1,10))
print(tuple(a))
````

## 数据类型转换
需要对数据内置的类型进行转换，数据类型的转换，一般情况下你只需要将数据类型作为函数名即可。
数据类型转换可以分为两种：
* 隐式类型转换-自动完成 - 较低数据类型（整数）转换为较高数据类型（浮点数）以避免数据丢失
* 显式类型转换-需要使用类型函数来转换

## 运算符
### 赋值运算符
* +=  加法赋值运算符  c += a  => c = c + a
* -=  减法赋值运算符  c -= a  => c = c - a
* *=  乘法赋值运算符  c *= a  => c = c * a
* /=  除法赋值运算符  c /= a  => c = c / a 
* %=  取模赋值运算符  c %= a  => c = c % a
* **=  幂赋值运算符   c **= a => c = c ** a
* //= 取整除赋值运算符 c //= a  => c = c // a
* :=  海象运算符  可以在表达式内部为变量赋值 

### 位运算符
* & 按位与运算符：参与运算的两个值，如果两个相应位都为1，则该位的结果为1，否则为0
* | 按位或运算符：只要对应的两个二进位有一个为1是，结果位就为1
* ^ 按异或运算符：当两对应的二进位相异时，结果为1
* ~ 按位取反运算符：对数据的每个二进制位取反，即把1变为0，把0变为1.**~x类似于-x-1**
* << 左移动运算符：运算数的各二进位全部左移若干位，由“<<”右边的数指定移动的位数，高位丢弃，低位补0
* \>>  右移动运算符：把“>>”左边的运算数的各二进位全部右移若干位，“>>”右边的数指定移动的位数

### 逻辑运算符
and or not 
### 成员运算符
in     not in

### 身份运算符
* is 判断两个标识符是不是引用自一个对象  x is y 类似于 id() 如果引用的是同一个对象则返回true，否则返回false
* is not 判断两个标识符是不是引用自不同对象
注： id()函数用于获取对象内存地址


## number
数字数据类型用于存储数值。数据类型是不允许改变的，这就意味着如果改变数字数据类型的值，将重新分配内存空间
Python 支持三种不同的数据类型：
* 整型 int 没有限制大小  bool是整型的子类型
* 浮点型 float 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2=2.5x10x10=250）
* 复数 complex 复数由实数部分和虚数部分构成，可以用a+bj或者complex(a,b)表示，ab都是浮点型

## 字符串
f-string  
````python
var1  = 'hello world!'
var2  = 'python'
print(var1[0])
print(var1[1:5])
print('hello %s' %var2)
````

## 列表
序列是Python中最基本的数据结构，序列中的每个值都有对应的位置值，称之为索引，第一个索引是0，第二个索引是1。
Python有6个序列的内置类型，最常见的是列表和元组。
列表都可以进行的操作包括索引，切片，加，乘，检查成员。
Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

* append()

## 元组
元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号(),列表使用方括号[]。
**元组的不可变指的是元组所指向的内存中的内容不可变 对于重新赋值的元组，绑定到了新的对象，不是修改了原来对象**

## 字典
字典是可变容器模型，且可存储任意类型对象
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
````python
d = {key1 : value1, key2 : value2, key3 : value3 }
````
* 键必须是唯一的，但值则不必唯一
* 值可以取任何数据类型，但键必须是不可变的，如字符串、数字
* 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住(前一个值会被删除)
* 键必须不可变，所以可以用数字、字符串或元组充当，用列表就不行

### 深拷贝 浅拷贝


## 集合
集合是一个无序的不重复元素序列。
可以使用大括号{ }或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{ },因为{ }是用来创建一个空字典。


