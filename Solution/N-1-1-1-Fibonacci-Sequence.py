# there's still one problem
# the loop is infinty..

def mygold(n):
	x = 1
	while n >= 1:
		x = 1 + 1 / x
		n -= 1				
		# print ("x= %d", x)
	return x

def myfibo(n):
	golden = mygold(100)  # call function once and save the value for later use
	# a = (golden ** n+1 - (1 - golden ** n+1)  # problem brackets a**b+1 and a**(b+1) are not same
	a = golden ** (n+1) - (1 - golden) ** (n+1)
	b = 2 * golden - 1
	return a/b	



def main():
	print("golden number ", mygold(1000))

	for i in range(11):
		print(myfibo(i))
		pass

if __name__=="__main__":
	main()

	
	
	
