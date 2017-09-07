# 导入模块有三种方法：
# 第一种：import 模块名				例如：import abc		abc.py是存放在搜索路径下的.py文件
# 第二种：from 模块名 import func1,func2。。。。func1是函数名
		# 或者from 模块名 import *
		# 这第二种方式就可以不用在调用函数时候加上模块名，例如module.func()可以直接写成func()
# 第三种：import 模块名 as 新名字
		# 例如 import tesnsorflow as tf     import temperature as t

通常包总是一个目录，导入包的方式和模块一样，可以使用import导入包，或者from + import来导入包中
的部分模块。包目录下为首的一个文件便是 __init__.py(必须要有该文件，即使为空也行)。然后是一些模块文件和子目录，假如子目录中
也有 __init__.py 那么它就是这个包的子包了。例如numpy就是包		
可以这么导入包里面的模块：import matplotlib.pyplot as pl
		
# 模块属性__name__，它的值由Python解释器设定。如果脚本文件是作为主程序调用，__name__的值就设为__main__，
# 如果是作为模块被其他文件导入，__name__的值就是其文件名。		
# if __name__='__main__':
	# test()
# =======================================================================================
>>>import sys
>>> sys.path		#这是模块的搜索路径，要存放在这些路径下的模块或者包才可以被导入
['', 'D:\\Anaconda3\\Scripts', 'D:\\Anaconda3\\python35.zip', 'D:\\Anaconda3\\DLLs', 
	'D:\\Anaconda3\\lib', 'D:\\Anaconda3', 'D:\\Anaconda3\\lib\\site-packages',
	 'D:\\Anaconda3\\lib\\site-packages\\Sphinx-1.4.1-py3.5.egg',
	 'D:\\Anaconda3\\lib\\site-packages\\win32', 'D:\\Anaconda3\\lib\\site-packages\\win32\\lib', 
	 'D:\\Anaconda3\\lib\\site-packages\\Pythonwin', 
	 'D:\\Anaconda3\\lib\\site-packages\\setuptools-23.0.0-py3.5.egg']

通常都把包放在site-packages这个路径下，例如numpy包就存放在这个路径下，自己写的包或者模块也可以
放在这个路径下。
也可以使用sys.path.append('E:\\GitHub\\python_algorithm')把该路径添加进搜索路径。
但是重启shell之后添加的路径又没了，所以不推荐使用这种方式。
有一种方式可以把路径加入到python系统路径下，避免每次通过代码指定路径，但是我还不会用
