minion_ids = []

def answer(n, b):
	if n == 0:
		return 1 								 #return 1 if z == 0
	else:
		y = ''.join(sorted(n))				
		x = y[::-1]
		z = int(x,base = b) - int(y,base = b)
		lenn = len(n)
		print ('Z is ', z) 
		z = numberToBase(z, b , lenn)                   #function call to convert the number to base b
		if z in minion_ids:
			return len(minion_ids) - minion_ids.index(z)   	 #return the length of the ending cycle
		else:
			minion_ids.append(z)
			return answer(z, b)
    

# function to conver number to the base b
def numberToBase(n, b, lenn):
	if n == 0:
		return 0
	else:
		d =  []
		while n:
			d.append(n % b)
			try:
				n = n // b
			except:
				print('n is', n)
				input()

		n = ''.join(map(str,d[::-1]))
		if lenn > len(n):
			n = '0'*(lenn - len(n))+n
		return n



x = answer(214334,6)
print (x)