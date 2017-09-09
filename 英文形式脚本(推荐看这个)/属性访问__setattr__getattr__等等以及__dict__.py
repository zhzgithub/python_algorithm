# 对象有一个特殊属性__dict__,其作用是以字典的形式显示出当前对象的所有属性及其对应值
# 魔法方法的属性访问.以下魔法方法和内嵌函数getattr(),setattr(),delattr()不要记混淆了。
# 下面的是魔法方法，可以被重写，而内嵌函数直接调用使用就行了
__getattr__(self,name)   		定义当用户试图获取一个不存在的属性的行为时的行为
__getattribute__(self,name)		定义当该类的属性被访问时的行为
__setattr__(self,name,value)	定义当该类的属性被设置时的行为
__delattr__(self,name)			定义当一个属性被删除时的行为


# ------------------对比一下"BIF_property.py"的property()方法-----------------------------
>>>class Rectangle:
	def __init__(self,width=0,height=0):
		self.width=width
		self.height=height
	
	def __setattr__(self,name,value):		#只要一涉及到对象属性赋值，就会自动调用该魔法方法
		if name=='square':					#这里要求是如果name是'square',那么把他的长宽都设置为value,即正方形
			self.width=value
			self.height=value
		else:
			# self.name=value     #这样写会无限递归出错，因为在__setattr__()里面又有对象的属性赋值，就又要调用__setattr__()即调
								  #用自己而无限递归
			# 方法1：使用__dict__
			# self.__dict__[name]=value
			
			# 方法2：使用super()方法调用它的基类的__setattr__()去获得
			super().__setattr__(name,value)		#这里super()会调用Rectangle类的基类即object类的__setattr__()，这个是系统写好的，不是我们重写的
			
	def getArea(self):
		return self.width*self.height
		
>>>r=Rectangle(5,6)
>>>r.getArea()
>>>r.square=10
>>>r.width
>>>r.__dict__