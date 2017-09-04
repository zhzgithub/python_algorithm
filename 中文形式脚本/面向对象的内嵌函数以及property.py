# 关于类的一些BIF(内嵌函数)
object是所有类的基类(父类)，即所有类都是object的子类
如果instance1是class2的实例化对象，class2是class1的子类，那么instance1也是class1的实例化对象
issubclass(子类,父类)		#返回True,False
isinstance(实例对象,类)		#检测一个实例对象是不是属于某个类的，这个位置也可以是由类构成的元组(class1,class2,...)
hasattr(对象,'属性')			  #检测该对象中是否有某属性，属性名需要打上引号
getattr(对象,'属性'[,default])	  #返回对象指定的属性值，如果指定的属性不存在，并且设置了default,则打印出default参数。
								  #中括号代表可选项。写的时候是这样 getattr(对象,'属性','您所访问的属性不存在(即default)')
setattr(对象,'属性',value)		  #与getattr()对应,即设定对象的属性值，若属性不存在，则创建它
delattr(对象,'属性')			  #与setattr()相反，删除对象的属性，若是属性不存在，就抛出异常

property(fget=None,fset=None,fdel=None,doc=None)#通过属性来设置属性，设置一个属性，这个属性的作用是去设置已经定义好的属性
		fget:获取属性的方法      fset是设置属性的方法    fdel是删除属性的方法
		
>>>class A():
	def __init__(self,size=10):
		self.size=size
	
	def getsize(self):
		return self.size
	def setsize(self,value):
		self.value=value
	def delsize(self):
		del self.size
	x=property(getsize,setsize,delsize)

>>>a=A()
>>>a.getsize()		#输出10
>>>a.x 				#输出10，调用getsize方法
>>>a.x=1000			#调用setsize方法，设置属性值
>>>a.size			#输出10
>>>del a.size		#这句话把a.size删除了，即A()中再也没有属性 size。
