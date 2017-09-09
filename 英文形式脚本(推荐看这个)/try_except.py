
# 只要try里面的语句出现一个错误，该语句后面的语句就都不会执行了，直接跳到执行该语句对应的except语句

try:
	sum=1+'1'
	f=open('test.txt')
	print(f.read())
	f.close()
except OSError as reason:			# 该语句也可以不加as reason,reason变量名随便取都行。# 该异常对应于f=open('test.txt')语句
	print('文件出错了！\n出错的原因是：'+str(reason))	
# except TypeError as reason:
	# print('类型出错了！\n出错的原因是：'+str(reason))
except TypeError :			# 该异常对应于sum=1+'1'语句
	print('类型出错了！')
# 也可以把几个异常以元组形式合并起来
# except (OSError,TypeError):
	# print('出错了')
	
else:	# 当前面的异常都没有出现时候，如果加上else，那么就直接执行else语句。感觉else一般都用不到
	print('没有异常')
	
finally:		# 加上finally语句就是说，无论如何，最后都得把finally语句执行
	print('你猜猜看有没有异常呢')
	# 小甲鱼给的例子是建议把f.close()语句写到这里来，因为当出现对文件写入操作后，一旦出现异常，就不会执行f.close()语句了，
	# 不关闭文件那么最终写入的语句只在缓存中，不会保存在文件中。把f.close()语句写在这里，无论如何都会被执行，就解决了这种情况


	
# raise的作用是引出异常。感觉raise 没有什么作用	
# raise	# 单独执行这一个单词，就会出现traceback的异常
# 1/0	# 单独执行这一句看看
# raise ZeroDivisionError	# 单独执行这一句看看
raise ZeroDivisionError('除数为0的异常')