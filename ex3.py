#Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.	
#Examples	
#"()"              =>  true	
#")(()))"          =>  false	
#"("               =>  false	
#"(())((()())())"  =>  true	
#	
#	
## print(valid_parentheses("hi(hi)("))	
## print(valid_parentheses("hi(hi)()()()"))	

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
print (parentheses('(((((()))))))))))(('))