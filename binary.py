import itertools as it

def change_bit_combination(index_list, n):
	all_one_list = list(it.repeat('1', times=n)) # create a list with all values equal to one and has length of n

	def change_bit(index, bit_list=all_one_list):
		''' 
		define a function to change the value of a certain index into 0
		'''
		bit_list[index] = '0'
	map(change_bit, index_list) # change all values of specified index into 0
	return ''.join(all_one_list)


def zbits(n, k):
	index_list_combination = list(it.combinations(range(n), k)) # create a list of index combination
	result = it.starmap(change_bit_combination, list(it.product(index_list_combination, [n]))) # generate result
	return set(result)