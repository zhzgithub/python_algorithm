# python_algorithm       python的一些算法程序代码    

###魔法方法例如__init__()和__str__()以及__add__()等只能重写，不能自己创造个新的如__abc__(),这么做没什么意义，和普通函数没什么两样。魔法方法就是在某种情况下自动调用他，例如__add__()当使用相加的情况下自动调用，以及__init__()当实例化新对象时自动调用来初始化。    

###当程序中需要创建文件时，使用notepad++的python解释器能使程序运行，但是创建不了文件。但是使用python自带的idle.exe可以创建文件    

###在编程时，养成好习惯：属性(也即变量)名使用名词，如name,方法(也即函数)名使用动词，如print_name()

dict_key_vote.py 是关于使用字典来统计列表中的每个元素出现的次数

iteration_recursion.py 是 关于迭代和递归的相关代码，以斐波那契和汉诺塔为例子    

set_list.py            是关于集合与列表的相关操作，删除重复元素的方法，还介绍了一点增删元素的内嵌函数，以及字典
    
file_operation.py      是关于文件操作相关的，如f=open('a.txt','r'),f.write(),f.read(),f.close()等等      
    
split_operation.py     是关于分隔符的。本例讲的是文件的每行语句分隔，比如说 把一段字符串冒号前后的字符分为两个字符串或者多个字符串。本程序有问题     

pickle_operation.py    是关于把列表或者字典保存为二进制文件，来使得程序更简洁更易懂。介绍了pickle模块的用法，主要用到了文件的读取和pickle.dump()       

try_except.py          是关于异常处理的相关代码:try,except,else,finally,raise等操作     
  
with.py              是关于with的用法：使用with后可以不用调用f.close()函数来关闭文件；以及文件写入时不能读取的解释说明。最后介绍了else的丰富用法
    
object_variable.py   是关于类变量，成员变量，私有变量 相关的概念解析以及代码        

baseClass_childClass_super().py 是关于继承的代码。子类、父类、以及多重继承，以及super()方法讲解   
    
zuhe_combine.py      是关于类的组合的概念：当几个类不是同一物种，即横向关系的类，不适合使用继承，这就要用到组合。另外还讲到在类定义外部可以直接定义属性赋值，因为python的变量不需要声明。最后还讲到了关于self 绑定的概念     
        
BIF_property.py   是关于一些面向对象的内嵌函数如issubclass(),isinstance(),getattr()等，以及property的用法    

magicFunction__init__.py    是关于 魔法方法例如__init__和__del__等相关的概念及代码       

timer__str____repr____add__.py  是关于定制一个定时器，其间用到了__str__()和__repr__()以及__add__()等魔法方法，并详细做了解释

属性访问__setattr__getattr__等等以及__dict__.py    是关于属性访问的魔法方法如__setattr__()等等，还有super()方法讲解

iter_next_yield.py  是关于迭代器和生成器相关的代码。讲了iter()、next()以及__iter__()和__next__(),yield 的使用

mudule1.py		是关于 模块 和 包 相关的知识点，讲了import,from..import..,以及__name__和__main__的知识点

@decoration_@property.py和@decorator_装饰器.py是关于装饰器的知识点。主要看decoration_@property.py文件就行了，另一个文件辅助看一下。

