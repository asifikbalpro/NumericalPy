# there's still one problem
# the loop is infinty..

def mygold(n):
	x = 1
	while n >= 1:
		x = 1 + 1 / x
		n -= 1				
		print ("x= %d", x)
	return x

def myfibo(n):
	a = (mygold(100) ** n+1 - (1 - mygold(100) ** n+1)
	b = 2 * mygold(100) - 1
	return a/b	


mygold(1000)
for i in range(11):
	print(myfibo(i))