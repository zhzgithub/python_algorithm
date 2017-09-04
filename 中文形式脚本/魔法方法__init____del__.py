# 魔法方法:魔法方法总是被双下划线包围，例如__init__
# 魔法方法是面向对象的python的一切，如果不知道魔法方法，说明你还没认识到面向对象的Python的强大
# __init__()初始化函数只能返回'None',不能有别的返回类型。比如说在__init__()后面return 1或者a+b都不对。不能有返回值
class Rectangle:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		
	def getPeri(self):		#获取周长
		return (self.x+self.y)*2
	
	def getArea(self):		#获取面积
		return self.x*self.y

rect=Rectangle(3,4)
print(rect.getPeri())
print(rect.getArea())

# ----------------------------------------------------------------------------
# __new__(cls[,...])方法需要一个实例对象作为返回值
# -----------------我没搞懂这个__new__在做啥-----------------见小甲鱼第41讲----------------------------
>>>class CapStr(str):
	def _new__(cls,string):		
		string=string.upper()
		return str.__new__(cls,string)
>>>a=CapStr('i love pandas!')

# -----------------------------------------------------------------------------------
>>>class A():
	def __init__(self):
		print('我是__init__方法，我被调用了！')
	def __del__(self):
		print('我是__del__方法，我被调用了！')
>>>a=A()	#输出'我是__init__方法，我被调用了'
>>>b=a
>>>del b    #没输出
>>>del b	#输出'我是__del__方法，我被调用了！'    直到关于对象实例的所有都del(删除，释放)时候，才会调用__del__方法