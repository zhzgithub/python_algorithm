# 装饰器
'''装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功
能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的
雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。'''
# 使用装饰器的时候需要在装饰函数(不是被装饰函数)中必须定义一个嵌套函数，不然将会引发错误“TypeError: 'NoneType' object is not callable”

# func1(foo)不是直接产生调用效果，而是返回一个与foo参数列表一致的函数,
# 将func1(foo)的返回值赋值给foo，然后，调用foo()的代码完全不用修改

# ======================================================
# 下面代码中必须定义一个嵌套函数，不然将会引发错误“TypeError: 'NoneType' object is not callable”
# def abc(func):
	# print('我要开始调用func了')
	# func()
	# print('func()调用完了')
	# print('使用该方法会比直接调用func多打印三句话')
# @abc
# def cde():
	# print('本函数是要被调用的func()函数，当做参数传给abc()')
	
# cde()	

# =============================================
# 定义一个嵌套函数，避免引发错误“TypeError: 'NoneType' object is not callable”
def abc(func):
	def wrapper():  #这个嵌套函数不能少，虽然我还不知道为什么加了嵌套函数就可以避免类型错误
		print('我要开始调用func了')
		func()
		print('func()调用完了')
		print('使用该方法会比直接调用func多打印三句话')
	return wrapper

@abc		#与cde=abc(cde)功能一样，但是这句话位置不能写在这。
def cde():
	print('本函数是要被调用的func()函数，当做参数传给abc()')
	
cde()	
# ========================================================================
'''内置的装饰器有三个，        分别是staticmethod、classmethod和property，
作用分别是把 类中定义的实例方法  变成  静态方法、类方法  和  类属性。
由于模块里可以定义函数，所以静态方法和类方法的用处并不是太多，除非你想要完全的面向对象编程。
而属性也不是不可或缺的，Java没有属性也一样活得很滋润。从我个人的Python经验来看，我没有使
用过property，使用staticmethod和classmethod的频率也非常低。
@property 把类中定义的实例方法变成类属性
'''
>>>class Parrot(object):  
	def __init__(self):  
		self._voltage = 100000

	@property  
	def voltage(self):  
		"""Get the current voltage."""  
		return self._voltage
>>>a=Parrot()
>>>a.voltage	#显示 10000。本来voltage是类中定义的函数，现在可以当成属性直接访问。
			# 如果不加上@property,那么a.voltage会输出<bound method Parrot.voltage 
			# of <__main__.Parrot object at 0x000000000357D5F8>>
			# 因为a.voltage()才会输出1000。加上括号与不加上括号是由很大区别的。加上括号是有返回值的，不加括号是啥我还说不清楚

# =====================爱看不看，看上面的已经够了===================================================================
# 知乎上的https://www.zhihu.com/question/26930016 
# import logging
# # logging是记录、日志的意思，这里logging是日志模块
# def use_logging(func):
	# logging.warn("%s is running" % func.__name__)
	# func()

# def bar():
	# print('i am bar')
	
# use_logging(bar)

# =============================================================================
# import logging
# def use_logging(func):
	# def wrapper(*args, **kwargs):
		# logging.warn("%s is running" % func.__name__)
		# return func(*args, **kwargs)
	# return wrapper

# def bar():
	# print('i am bar')

# bar = use_logging(bar)	#把函数bar()当做参数传给use_logging()，然后再把use_logging()返回值赋给bar。
				# # 这不就是把use_logging()里面的代码变成了bar里面的一部分了吗，但是并没有重复写代码
# bar()

# ==========================================================================
# import logging
# def use_logging(func):
	# def wrapper(*args, **kwargs):
		# logging.warn("%s is running" % func.__name__)
		# return func(*args)
	# return wrapper

# @use_logging
# def foo():
	# print("i am foo")

# @use_logging
# def bar():
	# print("i am bar")

# foo()
# bar()


