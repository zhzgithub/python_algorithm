
# 为了把特别大的字典或者列表等不留在程序中，而是将他们做成二进制保存为文件，到时候直接将该文件导入程序中就使得程序比较简洁了
# 本操作会用到pickle(泡菜的意思)模块
# 关于f=open('a.txt','wt')的 f，我不知道怎么描述。以下的pick_file就是这里的f

# 例子1   只是演示作用
import pickle
my_list=[123,456,789,[3,3,4],'aaa','bbb']	# 这里只是示例，所以不用写这么大，能懂原理就行
pickle_file=open('my_list.txt','wb')		# 这里创建一个 my_list.txt文件。可以创建任何格式的文件，不一定非得是txt文件，后缀名随便取
											#必须是'wb',打开文件既要写入模式也要是二进制。如果以文本模式't'会报错
											
											 
pickle.dump(my_list,pickle_file)			# dump是倾倒的意思，这句话意思是把my_list列表倒进pickle_file中
pickle_file.close()							#本段话执行结束后就会生成一个my_list.txt的二进制文件。
									# 但是如果用notepad++运行不会生成的my_list.txt的二进制文件，但是会运行成功，用idle.exe就会生成了
# ---------------------------------------------------------------
# 上面的那部分代码是生成二进制文件，下面的代码就是程序：
# 即 假如已经把字典或者列表生成为二进制文件了，直接运行下面的程序就可以了，不需要再输入列表和字典了
# 需要添加什么功能直接在print语句后面添加就行了
pickle_file=open('my_list.txt','rb')
my_list2=pickle.load(pickle_file)			# pickle.load()把二进制的文件加载进my_list2中，这里的my_list2是列表
print(my_list2)


# 例子2
# 如果不使用以上方式 那么如下
# my_list=[123,456,789,[3,3,4],'aaa','bbb']   #假设这里的列表或字典有1000个元素，是不是要占用很多行，很碍眼，要换列表时候还得重新写上去
# print(my_list)