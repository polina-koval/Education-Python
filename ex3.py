def parentheses(a):
	counter1=0
	counter2=0
	for i in range(len(a)):
	    if a[i]=='(':
	        counter1+=1
	    if a[i]==')':
	        counter2+=1
	    if counter2>counter1:
	        break
	return counter1==counter2 