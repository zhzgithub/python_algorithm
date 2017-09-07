# --------迭代器----------------------------------------------------------------
# ----for循环就是利用的迭代器---------------------------
>>>links={'鱼C工作室':'www.fishc.com',\
		'鱼C论坛':'www.bbs.fishc.com',\
		'你好啊':'www.google.com'}
>>>for each in links:
	print('%s->%s'%(each,links[each]))	#这里each是键，links[each]是键each对应的值

# --------------------------------------------------------------------------------------
# 对于迭代操作，Python提供了两个BIF，即 iter(),next()
>>>string='fishc'
>>>it=iter(string)
>>>next(it)			#输出 'f'
>>>next(it)			#输出 'i'

# --------------------------------------------------------------------------
>>>string='fishc'
>>>it=iter(string)
>>>while True:
	try:
		each=next(it)
	except StopIteration:	#当迭代完所有元素之后再继续next(it)，会报错，加上这个异常处理就直接停止迭代了
		break
	print(each)

# ----------------迭代器的魔法方法--------------------------------------------------------------------
# 迭代器的魔法方法__iter__()，__next__()
>>>class Fibs:
	def __init__(self):
		self.a=0
		self.b=1
	
	def __iter__(self):			#迭代器的魔法方法__iter__(),一般只用来返回self。重点是__next__()
		return self
	def __next__(self):			#重写魔法方法__next__()。魔法方法就是在某种情况下自动调用他
		self.a, self.b=self.b, self.a+self.b
		return self.a
>>>fibs=Fibs()
>>>for each in fibs:	#这里的for循环就是在调用__iter__()和__next__()魔法方法
	if each<30:
		print(each)
	else:			#有if最好就写上else,本例如果不写上下面的else语句，程序会一直
					#运行下去，只是不打印结果在屏幕上而已
		break
# =====================================================================================
#对上面的代码改进一下，或者说另一种写法
>>>class Fibs:
	def __init__(self,n=10):
		self.a=0
		self.b=1
		self.n=n
	def __iter__(self):			#迭代器的魔法方法__iter__(),一般只用来返回self。重点是__next__()
		return self
	def __next__(self):			#重写魔法方法__next__()。魔法方法就是在某种情况下自动调用他
		self.a, self.b=self.b, self.a+self.b
		if self.a>self.n:		#加上这个异常处理当self.a>self.n时就直接停止迭代了，不必再迭代后面的了
			raise StopIteration
		return self.a
>>>fibs=Fibs()
>>>for each in fibs:	#这里的for循环就是在调用__iter__()和__next__()魔法方法	
		print(each)
	

# ============生成器=================================================
# 生成器是一个特殊的迭代器
>>>def  Mygen():		# 注意这里不是在class定义类了，而是def定义函数
		print('生成器被执行！')
		yield 20  	# 即返回20并暂停该函数,暂停在yield这个位置，下一次执行就从该句下面一句话开始执行
		yield 23
	
>>>myGen=Mygen()
>>>next(myGen)		# 生成器是一个特殊的迭代器.该句会打印出20
>>>next(myGen)		# 该句会打印出23

# ------------------------------------------------------------------------
# 使用生成器的yield来写斐波那契数列
>>>def fib():		#斐波那契数列
	a=0
	b=1
	while True:
		a,b=b,a+b
		yield a 
		
>>>for each in fib():
	if each >100:
		break 
	print(each,end=' ')