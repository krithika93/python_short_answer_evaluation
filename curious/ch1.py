kk=[1,[2,3],[3,4]]
good1=[]
import itertools
def fun(kk,good1,value):
	print("hello")
	if len([i for i in kk if str(type(i)) == "<class 'list'>"]) == 0 or len(kk) == 0 :
			
			print(value,"value","\n",kk,"kk\n")
			return
			
		
	else:
		ind=0
		print(kk,"else")
		if len(kk) != 0:
			for ii in kk:
				if str(type(ii)) == "<class 'list'>":
					ind =kk.index(ii)
					break
			perms=itertools.permutations(ii)
		
		for perm in perms:						
			
			value=kk[0:ind]+list(perm)+good1
			good1=good1[ind+1:]
			fun(kk,good1,value)
			if good1  == None:
				good=[]
			print(good1,perm,kk)
			
			print(value,"value")

fun(kk,[],0)			
		