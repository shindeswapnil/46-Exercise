#Implement the higher order functions map(), filter() and reduce().
#(They are built-in but writing them yourself may be a good exercise.)

#-------------------map()--------------------
def my_map(fun,seq):
	res=[]
	for val in seq:
		res.append(fun(val))
	return res
#--------------------------------------------

#-------------------filter()-----------------
def my_filter(fun,seq):
	if isinstance(seq,tuple):
		res=()
	elif isinstance(seq,str):
		res=""
	else:
		res=[]
	for val in seq:
		if fun(val):
			if isinstance(seq,tuple):
				res+=(val,)
			elif isinstance(seq,str):
				res+=val
			else:
				res.append(val)
	return res	
#--------------------------------------------

#-------------------reduce()-----------------
def my_reduce(fun,seq,init=None):
	if init:
		res=init
	else:
		res=seq[0]
	if init:
		for val in seq:
			res=fun(res,val)
	else:
		for val in seq[1:]:
			res=fun(res,val)
	return res
#--------------------------------------------

print(my_map(lambda x:x*x,[1,2,3,4]))
print(my_filter(lambda x: x.endswith('in'), ('shirin', 'co.in', 'mail', 'lg')))
print(my_reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 5))
