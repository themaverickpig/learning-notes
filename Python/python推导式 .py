# python推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体
# Python支持各种数据结构的推导式：

names = ['bob','tom','alice','jerry','wendy','smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)