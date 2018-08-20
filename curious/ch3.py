kk=[1,[2,3],[3,4]]
kk1=kk.copy()

good1=[]
import itertools
def fun(kk,subs,value,ind):
	print("hello")
	if len([i for i in kk if str(type(i)) == "<class 'list'>"]) == 0 or len(kk) == 0 :
		print(subs,kk,value)
	
			
		
	else:
		ind=0
		
		if len(kk) != 0:
			for ii in kk:
				if str(type(ii)) == "<class 'list'>":
					ind =kk.index(ii)
					break
			perms=itertools.permutations(ii)
		
		for perm in perms:
					
			good1=kk[ind+1:]
			subs=subs[0:ind]
			value=subs+list(perm)+good1
			fun(good1,subs,value,ind)
			
			
		
		
		
		
			

fun(kk,kk1,0,0)			
		