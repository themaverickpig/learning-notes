## 标题标签
## 段落标签
属性：align='' 对齐方式。属性值包括 left center right
HTML标签时分等级的，HTML将所有的标签分为两种：
* 文本级标签：p span a b i u em 。文本级标签里只能放文字、图片、表单元素。（a标签里不能放a和input）
* 容器级标签：div h系列 li dt dd 。 容器级标签里可以放置任何东西

**p标签是一个文本级标签，p里面只能放文字 图片 表单元素，其他的一律不能放**

## 水平线标签`<hr/>`
属性：
* align 设定线条放置位置，可选 left right  center
* size  设定线条粗细，以像素为单位，内定为2
* width 设定线条长度，可以是绝对值（单位是像素）或相对值
* color 设定线条颜色
* noshade 不要阴影，即设定线条为平面显示，若没有这个属性则表明线条具有阴影或立体

## 换行标签`<br/>`

## `<div>`和`<span>`标签
* div标签可以把标签中的内容分割为独立的区块。必须单独占据一行
* span标签和div的作用一致，但不换行

div标签的属性：align 设置块儿的位置，属性值可以选择 left right center

### div和span的区别
`<span>`和`<div>`的唯一区别在于：span是不换行的，而div是换行的。
如果单独在网页中插入这两个元素，不会对页面产生任何的影响。这两个元素是专门为定义CSS样式而生的
div在浏览器中，默认是不会增加任何的效果的，但是语义变了，div中的所有元素是一个小区域。div标签时一个容器级标签，里面什么都能放，设置可以放div自己。
span也是表达“小区域、小跨度”的标签，但只是一个文本级的标签。就是说，span里面只能放置文字、图片、表单元素。span里面不能放p h ul dl ol div

## 内容居中标签`<center>`
此时center代表是一个标签，而不是一个属性值。只要是在这个标签里面的内容，都会居于浏览器的中间。
**不建议使用**

## 预定义(预格式化)标签`<pre>`
含义：将保留标签内部所有的空白字符（空格、换行符 ）原封不动地输出结果
**几乎用不着**

## 字体标签
特殊字符
* $nbsp 空格
* &lt 小于号
* &gt 大于号
* &amp 符号&
* &quot 双引号
* &apos 单引号
* &copy 版权©
* &trade 商标™

 | 特殊字符 | 描述 | 字符的代码 |
 | :----: | :----: | :----: |
 |  空格 | 空格符 | &nbsp |
 |  < | 小于号 | &lt |
 |  > | 大于号 | &gt |
 |  & | 和号 | &amp |
 |  ￥ | 人民币 | &yen |

### 下划线、中划线、斜体
* `<u>` 下划线标记
* `<s>`或`<del>` 中划线标记（删除线）
* `<i>`或`<em>` 斜体标记

**小图标经常用`<i>`标签**

### 上标`<sup>` 下标`<sub>`

## 超链接

1. 外部链接：链接到外部文件
```html
<a href="www.baidu.com" target="_blank"> click <a/>
```
2. 锚链接
锚链接：给超链接起一个名字，作用是在本页面或者其他页面的不同位置进行跳转。
比如：在网页底部有一个向上的箭头 ，点击箭头后回到顶部，这个就可以利用锚链接。
首先创建一个锚点，使用name属性或者id属性给那个特定的位置起个名字。
[#测试](./demo/%E9%94%9A%E9%93%BE%E6%8E%A5.html)

3. 邮件链接
```html
<a href="mailto:1062539080@qq.com">点击进入我的邮箱</a>
```
效果：点击之后，会弹出邮件窗口

超链接属性：
* href  目标URL
* title  悬停文本
* name  主要用于设置一个锚点的名称
* target  告诉浏览器用什么方式来打开目标页面 target属性有以下几个值
  * _self  在同一个网页中显示（默认值）
  * _blank  在新的窗口打开
  * _parent  在父窗口中显示
  * _top  在顶级窗口中显示

## img标签
图片标签
```html
<img src="img url" />
```
img标签的属性：
* src属性：指图片的路径，source
  在写图片的路径时，有两种写法：相对路径、绝对路径
* width（图像的宽度） height（图像的高度） 
  **如果想要保证图片等比例缩放，请只放置width和height中其中一个
* alt属性 当图片不可用（无法显示）时候，代替图片显示的内容。
* title 提示性文本。鼠标悬停时出现的文本。
* align  图片和周围文字的相对位置 可选值是 bottom（默认） center top left right 
如果想实现图文混排的效果，使用align属性取值为left right

## 列表标签
列表标签分为三种
1. 无序列表`<ul>` 无须列表中的每一项是`<li>` 
    * li不能单独存在，必须包裹在ul里面
    * ul的作用不是给文字增加小圆点，而是增加无序列表的语义
    * 属性： type 属性值可选：disc（实心圆点 默认） square（实心方点） circle（空心圆）
    *  **li里面什么都能放，甚至可以再放一个li**

2. 有序列表`<ol>` 里面的每一项是`<li>`
属性： 
  * type 属性值可以是1（阿拉伯数字 默认） a A i I 结合start属性表示从几开始

3. 定义列表`<dl>`

dl英文单词:definition list 没有属性。dl的子元素只能是dt和dd
* dt definition title 列表的标题，这个标签时必须的
* dd definition description 列表的列表项，如果不需要它，可以不加
**dt dd只能在dl里面 dl里面只能有dt dd**

## 表格标签
表格标签用table表示，一个表格table是由每行tr组成的，每行是由每个单元格td组成的。**一个表格是由行组成的（行是由列组成的）**而不是由行和列组成的。
table的属性
* border 边框 像素为单位
* style=“border-collapse：collapse” 单元格的线和表格的边框线合并（表格的两边框合并为一条）
* width 宽度 像素为单位
* height 高度 像素为单位
* bordercolor 表格的边框颜色
* align 表格的水平对齐方式。属性可以填 left right center **这个不是设置表格里内容的对齐方式，如果想设置内容的对齐方式，要对单元格标签td进行设置**
* cellpadding 单元格内容到边的距离，像素为单位。默认情况下文字是紧挨着左边的那条线的，默认情况下的值是0 
* cellspacing 单元格和单元格之间的距离（外边距）像素为单位 默认情况下的值为0
* background 背景图片 背景图片的优先级大于背景颜色
* dir 共有属性 单元格内容的排列方式。可以取值：ltr 从左到右 rtl从右到左 

`<tr>`行
属性：
* dir 共有属性
* bgcolor 设置这一行的单元格的背景色 注：无法设置这一行的背景图片
* height 一行的高度
* align=“center” 一行的内容水平居中显示 取值left center right
* valign=“center”一行的内容垂直居中 取值 top middle bottom

`<td>`单元格
属性：
* align 内容的横向对齐方式。可选值 left right center 
* valign 内容的纵向对齐方式  可选值  top middle bottom 
* width 绝对值或者相对值（%）
* height 单元格的高度
* bgcolor 设置这个单元格的背景色
* background 设置这个单元格的背景图片

`<th>`单元格
表示加粗的单元格 相当于`<td>+<b>`

#### 单元格的合并
单元格的属性：
* colspan 横向合并 colspan='2' 表示当前单元格在水平方向上要占据两个单元格的位置
* rowspan 纵向合并 rowspan=’2‘ 表示当前单元格在垂直方向上要占据两个单元格的位置

`<caption>` 表格的标题。使用时和tr标签并列
属性：align 可选值 left center right top bottom 

表格的thead标签 tbody标签 tfoot标签
这三个标签有与没有的区别：
* 1. 如果写了，那么这三个部分的代码顺序可以任意，浏览器显示的时候还是按照thead tbody tfoot的顺序依次来显示内容 如果不写的话，那么浏览器解析并显示表格内容的时候是从按照代码的从上到下的顺序来显示
* 2. 当表格非常大内容非常多的时候，如果用thead tbody tfoot标签的话，那么数据可以边获取边显示。如果不写，则必须等表格的内容全部从服务器获取完成才能显示出来

## 框架标签
如果我们希望在一个页面中显示多个页面，就得选用框架标签

### 内嵌框架
内嵌框架用iframe表示 iframe是body的子标记

## 表单标签
表单标签用form表示 用于与服务器的交互，表单就是收集用户信息的，就是让用户填写 选择的
属性：
* name 表单的名称
* id 表单的名称
* action 指定表单数据逇处理程序
* method 表单数据的提交方式 一般取值 get post 

**get提交和post提交的区别**
get方式：将表单数据，以’name=value‘形式追加到action指定的处理程序的后面，两者间用’?‘隔开，每一个表单的’name=value‘间用 & 隔开 特点：只适合提交少量信息，并且不太安全 提交的数据类型只限于ASCII字符
post方式 将表单数据直接发送（隐藏）到action指定的处理程序，post发送的数据不可见action指定的处理程序可以获取到表单数据，特点：可以提交海量信息，相对来说安全一些提交的数据格式是多样的（word excel rar img）

enctype 表单数据的编码方式（加密方式）取值可以是：application/x-www-form-urlencoded multipart/form-data  enctype只能在post方式下使用
* application/x-www-form-urlencoded 默认加密方式，除了上传文件之外的数据都可以
* multipart/form-data 上传附件时，必须使用这种编码方式 

`<input>`输入标签（文本框）用于接收用户输入
属性：
* type 可选值
  * text （默认）
  * password 密码类型
  * radio 单选按钮，名字相同的按钮作为一组进行单选（单选按钮，天生是不能互斥的，如果想互斥必须要有相同的name属性 name就是名字）
  * checkbox 多选按钮 name属性相同的按钮作为一组进行选择
  * checked 将单选按钮或多选按钮默认处于选中状态。当input标签设置为type=“radio”或者checkbox时，可以用这个属性。属性值也是checked，可以省略
  * hidden 隐藏框，在
