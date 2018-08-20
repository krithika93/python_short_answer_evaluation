kk=[1,[2,3],[3,4]]
kk1=kk.copy()

good1=[]
import itertools
def fun(kk,subs,perm,value,old):
	print("hello")
	print(subs,"subs")
	if len([i for i in kk if str(type(i)) == "<class 'list'>"]) == 0 or len(kk) == 0 :
			
			print(value,"value","\n",kk,"kk\n")
			return kk
		
	else:
		ind=0
		print(kk,"else",subs)
		print(subs,kk[0])
		if len(kk) != 0:
			for ii in kk:
				if str(type(ii)) == "<class 'list'>":
					ind =kk.index(ii)
					break
			perms=itertools.permutations(ii)
		good1=kk[ind+1:]
		
			

		for perm in perms:
			subs=subs[0:old]+list(perm)	
			good=fun(good1,subs,perm,value,ind)
			
				
			
			print(good,perm,subs,perm,kk)
			if good  == None:
				good=[]
			value=subs+list(perm)+good
			
			print(value,"value")

fun(kk,kk1,0,0,0)			
		