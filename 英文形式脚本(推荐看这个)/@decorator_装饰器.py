import time
	
# def deco123(func):
	# startTime=time.time()
	# func()
	# endTime=time.time()
	# msecs=(endTime-startTime)*1000
	# print('->elapsed time:%f ms'%msecs)
	
# def myfunc():
	# print('start myfunc')
	# time.sleep(6)
	# print('end myfunc')

# deco123(myfunc)
# # myfunc()

##-----------------------------------------------------------------------------------
# def deco123(func):
	# def wrapper():
		# startTime=time.time()
		# func()
		# endTime=time.time()
		# msecs=(endTime-startTime)*1000
		# print('->elapsed time:%f ms'%msecs)
	# return wrapper

# def myfunc():
	# print('start myfunc')
	# time.sleep(6)
	# print('end myfunc')

# print("myfunc is:"+myfunc.__name__)
# myfunc=deco123(myfunc)
# print('myfunc is:',myfunc.__name__)
# print()
# myfunc()


####---------------------------------------------------------------------------------
def deco123(func):
	def wrapper():
		startTime=time.time()
		func()
		endTime=time.time()
		msecs=(endTime-startTime)*1000
		print('->elapsed time:%f ms'%msecs)
	return wrapper

@deco123		##等价于 myfunc=deco123(myfunc)，但是不能把 myfunc=deco123(myfunc)写在这一行
#即 使得装饰器下面定义的函数作为deco123函数的输入参数，然后再把deco123()赋给下面的函数
def myfunc():
	print('start myfunc')
	time.sleep(1)
	print('end myfunc')

print("myfunc is:"+myfunc.__name__)
print()
myfunc()


##--------------------------------------------------------------------------------------
# def deco123(func):
	# def wrapper(a,b):
		# startTime=time.time()
		# func(a,b)
		# endTime=time.time()
		# msecs=(endTime-startTime)*1000
		# print('->elapsed time:%f ms'%msecs)
	# return wrapper

# @deco123	
# def addFunc(a,b):
	# print('start addFunc')
	# time.sleep(1)
	# print('result is %d'%(a+b))
	# print('end addFunc')
	
# addFunc(3,8)


###---------------------------------------------------------------------------------------------------
# def deco123(arg=True):
	# if arg:
		# def _deco123(func):
			# def wrapper(*args,**kwargs):
				# startTime=time.time()
				# func(*args,**kwargs)
				# endTime=time.time()
				# msecs=(endTime-startTime)*1000
				# print('->elapsed time:%f ms'%msecs)
			# return wrapper
	# else:
		# def _deco123(func):
			# return func
	# return _deco123

# @deco123(False)
# def myFunc():
	# print('start myFunc')
	# time.sleep(1)
	# print('end myFunc')
	
# @deco123(True)	
# def addFunc(a,b):
	# print('start addFunc')
	# time.sleep(1)
	# print('result is %d'%(a+b))
	# print('end addFunc')

# print('myFunc is ',myFunc.__name__)	
# myFunc()
# print ()
# print('addFunc is ',addFunc.__name__)
# addFunc(3,8)





















