
# 怎样删除列表list1中重复的元素？

# method—1  
# 使用 for循环，并且使用 not in ,append 等。如果在意列表中元素的顺序，就用此方法
list1=[1,3,2,5,3,1,6,5,2,'B','b','a','A']
temp=[]
for each in list1:
	if each not in temp:
		temp.append(each)
new_list=temp
print(new_list)

# method-2   
# 使用集合set    如果在意列表中元素的顺序，集合会出问题，因为集合是无序的,顺序每次都会随机
list1=[1,3,2,5,3,1,6,5,2,'B','b','a','A']
set1=set(list1)
new_list2=list(set1)
print(new_list2)





### 列表的添加/删除元素方法:  append,remove,del,pop


### 集合的添加/删除元素方法:add,remove,pop         frozenset关键字是的集合不可修改  如：set=frozenset((1,2,3))
set1={1,2,4,3}
set1.add(5)		#添加元素
print(set1)
set1.remove(4)	#删除元素
print(set1)
set1.pop()		#弹出/删除集合中最前面的元素
print(set1)

# 字典的添加/删除元素方法 pop
#pop(key)