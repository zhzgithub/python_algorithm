
# with的用法：当你不用该文件时，自动关闭文件，而不需要我们自己写下f.close()，因为很多时候我们会忘了写f.close()
# 这里的with用法与tensorflow里面的with用法一致，如with tf.Session() as sess:就可以不用调用Session.close()了。见tensorflow书本 P45
try:
	with open('test.txt','w') as f:
		f.write('nihai a===')
		for each_line in f:		#这句话就是在读取f的内容，但是该文件是以写入的方式打开的，所以会报错'not readable'
			print(each_line)
except OSError as reason:
	print('出错了！'+str(reason))
	
# -------------以下两个小程序都是用作对比说明-----------------------------------------------------------------------

# f=open('test.txt','a')
# f.write('nihai a===\n')
# f.close()			
# f=open('test.txt','r')
# for each_line in f:		#这句话就是在读取f的内容，要读取该文件内容就必须以只读的模式打开
        # print(each_line)

		
# # --------------------------------------------------------------------------------------------
		
# try:
	# f=open('test.txt','w')
	# f.write('nihai a===')
	# for each_line in f:		#这句话就是在读取f的内容，但是该文件是以写入的方式打开的，所以会报错'not readable'
		# print(each_line)
# except OSError as reason:
	# print('出错了！'+str(reason))
# finally:
	# f.close()
	
# # ----------------------------------------------------------------------------------------------

# 顺带介绍一下else的用法：除了if-else，else还可以与while以及for循环结合使用
# 这里以while循环为例，for循环也是这么做的
# def max_factor(num):  #该函数功能是判断一个数num的最大因数是多少,或者num是素数
	# count=num//2
	# while count>1:
		# if num%count==0:
			# print('%d最大的约数是%d'%(num,count))
			# break
		# count-=1
	# else:			#当上面的while循环执行结束，并且没有执行break语句跳出循环时，执行else语句；若是跳出了while循环，则不执行else语句
		# print('%d是素数!'%num)
# num=int(input('请输入一个数字：'))
# max_factor(num)


