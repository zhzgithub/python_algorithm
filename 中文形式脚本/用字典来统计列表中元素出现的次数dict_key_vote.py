# 使用字典来统计列表中的每个元素出现的次数，列表元素可以有重复的，但是字典中不会有重复的关键字
# 即 把列表中的元素作为字典中的键，把列表中的每个元素的重复次数求出来作为键值
neighbors=[2,2,2,0,1,2,0,1,2,0,0,1]
def a(neighbors):
	classvotes={}	#创建一个空字典
	for x in range(len(neighbors)):
		response=neighbors[x]
		if response in classvotes:		#如果某键0或1或2在字典classvotes里，则把对应键值加1，否则键值赋为1
			classvotes[response]+=1		#这里response作为classvotes的键，键有0,1,2；classvotes[response]就是键值
		else:
			classvotes[response]=1
	return classvotes
print(a(neighbors))

			