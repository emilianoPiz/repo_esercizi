import timeit
def log_pot(n,k):
	# trova la k-esima potenza di n in tempo logaritmico in relazione a k
	if k==0:
		return 1
	if (k %2==0):
		h=log_pot(n,k//2)
		return h*h
	else:
		h= log_pot(n, ((k-1)//2))
		return n*h*h
print(log_pot(2,3003))
