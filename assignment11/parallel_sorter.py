import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

step_size = 100/float(size)

if rank == 0:
	n_integer = input("How many integers: ")
	try:
		n_integer = int(n_integer)
	except ValueError:
		print('You typed a non-integer value. Set default value to be 100.')
		n_integer = 100
	random_int_list = np.random.randint(low=0, high=100, size=n_integer)
	print('Process 0 initialized array: {}'.format(random_int_list))	
	temp_list =[]
	for i in range(size):
		subset = random_int_list[np.where((random_int_list >= i * step_size) & (random_int_list < (i+1) * step_size))[0]]
		temp_list.append(subset)
	random_int_list = temp_list
else:
	random_int_list = np.zeros(1, dtype=int)

data = comm.scatter(random_int_list, root=0)
print('Process {} received array {}'.format(rank, data))

data = np.sort(data)

data_collected = comm.gather(data, root=0)

if rank == 0:
	data_collected = np.concatenate(data_collected)
	print('Process 0 gathered sorted array: {}'.format(data_collected))