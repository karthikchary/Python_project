def factorial(n):
	for x in range(n-1,0,-1):
		n = n*x
	if n == 0: return 1
	if n < 0 : return False
	return n
  
factorial(5)