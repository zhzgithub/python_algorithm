# 继承的作用是继承父类的方法或者属性，并且增加或者修改父类的方法或者属性，使得子类更具体化。
# 例如鱼有基本属性：鳞片、尾巴。基本方法：在水中游。子类鲨鱼继承父类的属性和方法后，可以增加属性：体积；增加方法：吃小鱼。
# 子类中定义的方法或属性与父类中的同名，则会自动覆盖父类中对应的方法或者属性

class Fish:
	def __init__(self):
		self.x=20
	def move(self):
		self.x-=1
		print('父类中的x=',self.x)
		
	
# class Shark(Fish):		#子类继承父类就这么写，把父类写在括号里面
	# def __init__(self):
		# self.y=100
		
# fish=Shark()
# fish.move()				# 这句话会报错，因为子类重写了父类的__init__()方法，因此子类不再有属性x。但是子类还是有move方法

	
class Shark(Fish):		#子类继承父类就这么写，把父类写在括号里面
	def __init__(self):
		# 方法1		调用未绑定的父类方法  当多重继承时这种方式就繁琐了，需要把每个父类依次调用出来
		# Fish.__init__(self)			#由于这里是调用函数，所以后面不需要加冒号':',这里的self是shark的实例对象，并不是父类Fish的实例对象
		
		# 方法2    super方法		当多重继承时super方法优势就体现出来了，不需要把每个父类一次调用出来
		super().__init__()			#这里的括号里面不需要加self
		self.y=100
		print('子类特有的y=',self.y)
		
fish=Shark()
fish.move()


# -------------------------------------------------------------------------
# 多重继承方式	class ClassName(BaseClass1,BaseClass2,BaseClass3):

