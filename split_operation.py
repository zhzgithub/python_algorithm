f=open('E:\\GitHub\\python_algorithm\\split.txt')

boy=[]
girl=[]
count=1

# print(f.readline())
# print(f.readline().split(',',1))
# (a,b)=f.readline().split(',',1)
# print(a,b)
# print(b)
for each_line in f:
	if each_line[:6] !='=======':	#如果该行的前六个字符不是'======'，那么该段对话没结束
		(a,b)=each_line.split(':',1)
		(role,line_spoken)=each_line.split(':',1)	#每行以冒号':'为分隔符分隔字符串，1表示分隔1个子字符串,即分成了两个字符串
		
		if role=='Jack':
			boy.append(line_spoken)
		if role=='Rose':
			girl.append(line_spoken)
	else:							#如果该行的前六个字符是'======'，那么该段对话结束
		#文件的分别保存操作
		file_name_boy ='boy_'+str(count)+'.txt'
		file_name_girl='girl_'+str(count)+'.txt'
		
		boy_file =open(file_name_boy,'w')
		girl_file=open(file_name_girl,'w')
		
		boy_file.writelines(boy)
		girl_file.writelines(girl)
		
		boy_file.close()
		girl_file.close()

		boy=[]
		girl=[]
		count+=1

f.close()