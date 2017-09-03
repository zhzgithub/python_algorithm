
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


