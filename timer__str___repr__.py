'''

>>>class A():
	def __str__(self):			#重写魔法方法__str__()
		return '小甲鱼真牛'
>>>a=A()
>>>a    	#输出<__main__.A object at 0x00000000035D3518>
>>>print(a)	#输出'小甲鱼真牛'。当需要打印字符串时候，就自动调用__str__()方法了，把__str__的返回值打印出来，直接调用a就会出现上一行结果

# -------------------------------------------------------------------------------
# 只要直接调用实例对象，就会执行__repr__()的魔法方法
class A():
	def __repr__(self):			#重写魔法方法__repr__()
		return '小甲鱼真牛'
		
>>>a=A()
>>>a    	#输出'小甲鱼真牛'-------只要直接调用实例对象，就会执行__repr__()的魔法方法
>>>print(a)	#输出'小甲鱼真牛'
'''
# -----------111111111111111111111111111111111111111111111111111111111111111111111111111-----------------------
# 例1
>>>import time as t
>>>class Mytimer():
	def start(self):
		self.start=t.localtime()
		print("计时开始...")
	
	def stop(self):
		self.stop=t.localtime()
		self._calc()
		print('计时结束！')
	
	def _calc(self):		#内部方法，以单下划线开始
		self.lasted=[]		#lasted[]是把时间间隔存储进去，年月日时分秒间隔分别存储进去，索引0到5分别表示年月日时分秒的间隔
		self.prompt='总共运行了'			#prompt:提示
		for index in range(6):	#这里的6表示localtime()返回值的六个索引，localtime()返回一个元组，前六个对应索引分别为年月日时分秒
								# 例如localtime的返回值索引[0]表示年,[1]表示月。
			self.lasted.append(self.stop[index]-self.start[index])
			self.prompt+=(str(self.lasted[index])+"/")
		
		print(self.prompt)
		
>>>t1=Mytimer()
>>>t1.start()		#输出'计时开始...'
>>>t1.stop()		#输出'总共运行了。。。。计时结束！'
	
# -----------------222222222222222222222222222222222222222222222222222222222222222-------------------------------------
# ------------使用__str__和__repr__改变一下----------------------------------------------------------------------------
# 例2
>>>import time as t
>>>class Mytimer():
	# def __str__(self):
		# return self.prompt
	# __repr__=__str__
	def __repr__(self):
		return self.prompt
	
	def start(self):
		self.start=t.localtime()
		print("计时开始...")
	
	def stop(self):
		self.stop=t.localtime()
		self._calc()
		print('计时结束！')
	
	def _calc(self):		#内部方法，以单下划线开始
		self.lasted=[]		#lasted[]是把时间间隔存储进去，年月日时分秒间隔分别存储进去，索引0到5分别表示年月日时分秒的间隔
		self.prompt='总共运行了'			#prompt:提示
		for index in range(6):	#这里的6表示localtime()返回值的六个索引，localtime()返回一个元组，前六个对应索引分别为年月日时分秒
								# 例如localtime的返回值索引[0]表示年,[1]表示月。
			self.lasted.append(self.stop[index]-self.start[index])
			self.prompt+=(str(self.lasted[index])+"/")
		
>>>t1=Mytimer()
>>>t1.start()		#输出'计时开始...'
>>>t1.stop()		#输出'计时结束！'
>>>t1 				#输出'总共运行了。/。/。。'


# ---------------33333333333333333333333333333333333333333333333333333333333333333333333-----------------------------------

# --------使用__init__()魔法方法来改进上述程序----------------------------------------------	
# --------有个问题：start(),stop()方法的属性start,stop与方法名重名，很容易出现调用的问题，应该尽量避免方法名与属性名重名-------
# 例3
>>>import time as t
>>>class Mytimer():
	def __init__(self):
		self.uint=['年','月','天','小时','分钟','秒']
		self.prompt='未开始计时'
		self.lasted=[]		#lasted[]是把时间间隔存储进去，年月日时分秒间隔分别存储进去，索引0到5分别表示年月日时分秒的间隔
		self.begin=0
		self.end=0
	
	# def __str__(self):
		# return self.prompt
	# __repr__=__str__
	def __repr__(self):
		return self.prompt			#当直接调用实例对象时返回self.prompt值。如果没调用start(),则prompt值为初始化值'未开始计时'
									#如果调用了start()之后再调用实例对象，则prompt被赋值为 '提示：请先调用stop()停止计时'。
									#如果调用了start()和stop()后，再调用实例对象，则prompt被stop()里面调用_cal()函数里面更新赋值了。
									#也就是说，只要直接调用实例对象，就会执行__repr__()的魔法方法
		
	def start(self):
		self.begin=t.localtime()
		self.prompt='提示：请先调用stop()停止计时'		#这句话是当没有调用stop()就直接调用实例对象t1时。这句话与__repr__()对应
												# __repr__()作用当直接调用实例对象时，会输出返回值self.prompt。要搞清楚这句话是赋值，
												# 并不是打印语句，但是在命令行中输出了这句话，是因为直接调用实例对象，会返回
												# self.prompt值，即打印在命令行上了
		print("计时开始...")
	
	def stop(self):
		if not self.begin:
			print('提示：请先调用start()开始计时')
		else:
			self.end=t.localtime()
			self._calc()
			print('计时结束！')
	
	def _calc(self):		#内部方法，以单下划线开始
		self.lasted=[]		#lasted[]是把时间间隔存储进去，年月日时分秒间隔分别存储进去，索引0到5分别表示年月日时分秒的间隔
		self.prompt='总共运行了'			#prompt:提示
		for index in range(6):	#这里的6表示localtime()返回值的六个索引，localtime()返回一个元组，前六个对应索引分别为年月日时分秒
								# 例如localtime的返回值索引[0]表示年,[1]表示月。
			self.lasted.append(self.end[index]-self.begin[index])
			if self.lasted[index]:	#当它不为0时执行下面语句，为0时，不执行。即若年或月或日或时分相减后为0，则不显示年或月或日时分
				self.prompt+=(str(self.lasted[index])+self.uint[index])
		
>>>t1=Mytimer()
>>>t1.start()		#输出'计时开始...'
>>>t1.stop()		#输出'计时结束！'
>>>t1 				#输出'总共运行了.......'	

# --------44444444444444444444444444444444444444444444444444444444444444444444444444444444444------------------------------------

# ------------两个实例化对象相加----即重写魔法方法__add__()--------------------------------
# __add__()魔法方法对应两个实例对象如t1、t2相加，如t1+t2就会调用__add__()方法了
# 例4------------本程序的不足之处：比如2017/9/5/11:12:30-2017/9/5/10:20:30会得到0/0/0/1/-8/0,出现了负数
>>>import time as t
>>>class Mytimer():
	def __init__(self):
		self.uint=['年','月','天','小时','分钟','秒']
		self.prompt='未开始计时'
		self.lasted=[]	#lasted[]是把时间间隔存储进去，年月日时分秒间隔分别存储进去，索引0到5分别表示年月日时分秒的间隔
		self.begin=0
		self.end=0
	
	# def __str__(self):
		# return self.prompt
	# __repr__=__str__
	def __repr__(self):
		return self.prompt			#当直接调用实例对象时返回self.prompt值。如果没调用start(),则prompt值为初始化值'未开始计时'
									#如果调用了start()之后再调用实例对象，则prompt被赋值为 '提示：请先调用stop()停止计时'。
									#如果调用了start()和stop()后，再调用实例对象，则prompt被stop()里面调用_cal()函数里面更新赋值了。
									#也就是说，只要直接调用实例对象，就会执行__repr__()的魔法方法
									
	def __add__(self,other):	#当两个实例对象相加时,如a+b就直接调用了__add__()魔法方法
		prompt1="总共运行了"	#这里prompt1是局部变量，不加self.，小甲鱼用了prompt我怕混淆，所以改为了prompt1
		result=[]		#result[]是把两个实例对象的年月日时分秒 间隔 分别相加后存储进去，0到5索引对应不同的间隔相加后的结果
						#注意：是间隔相加，不是本地时间相加，不会出现年份2017+2017相加的情况，年份相减为0即使年份间隔。注意是时间间隔
		for index in range(6):	
			result.append(self.lasted[index]+other.lasted[index])
			if result[index]:	
				prompt1+=(str(result[index])+self.uint[index])
		return prompt1
		
	def start(self):
		self.begin=t.localtime()
		self.prompt='提示：请先调用stop()停止计时'		#这句话是当没有调用stop()就直接调用实例对象t1时。这句话与__repr__()对应
												# __repr__()作用当直接调用实例对象时，会输出返回值self.prompt。要搞清楚这句话是赋值，
												# 并不是打印语句，但是在命令行中输出了这句话，是因为直接调用实例对象，会返回
												# self.prompt值，即打印在命令行上了
		print("计时开始...")
	
	def stop(self):
		if not self.begin:
			print('提示：请先调用start()开始计时')
		else:
			self.end=t.localtime()
			self._calc()
			print('计时结束！')
	
	def _calc(self):		#内部方法，以单下划线开始
		self.lasted=[]		#lasted[]是把时间间隔存储进去，年月日时分秒间隔分别存储进去，索引0到5分别表示年月日时分秒的间隔
		self.prompt='总共运行了'			#prompt:提示
		for index in range(6):	#这里的6表示localtime()返回值的六个索引，localtime()返回一个元组，前六个对应索引分别为年月日时分秒
								# 例如localtime的返回值索引[0]表示年,[1]表示月。
			self.lasted.append(self.end[index]-self.begin[index])
			if self.lasted[index]:	#当它不为0时执行下面语句，为0时，不执行。即若年或月或日或时分相减后为0，则不显示年或月或日时分
				self.prompt+=(str(self.lasted[index])+self.uint[index])
		
>>>t1=Mytimer()
>>>t1.start()		#输出'计时开始...'
>>>t1.stop()		#输出'计时结束！'
>>>t1 				#输出'总共运行了.......'	