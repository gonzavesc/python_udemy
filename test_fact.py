def facto(x):
	result = x
	if x == 1:
		return 1
	else:
		result = x * facto(x-1)
		return result
print(facto(3))
