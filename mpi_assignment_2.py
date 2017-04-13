import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

init_value = np.zeros(1, dtype=np.int)

if rank == 0:
	input_temp = input("Process 0 needs an input integer between [0, 100]: ") # ask user to input an integer
	try:
		input_temp = int(input_temp) # check if user input an integer
	except ValueError:
		print("Process 0 received a non-integer value, set its default value to be 0.")
		input_temp = 0 # change the value to be 0 if user input a non-integer value
	if input_temp < 0 or input_temp > 100: # check if user input an integer in resonable range
		print("Process 0 received a value out of range, set its default value to be 0.")
		input_temp = 0 # change the value to 0 if user input a value out of range

	init_value[0] = input_temp
	print("Process {} received value: {}".format(rank, init_value[0]))
	req_send = comm.Isend(init_value, dest=rank+1) # Process 0 send the original value
	req_send.Wait()
	print("Process {} sent value: {}".format(rank, init_value[0]))
	
else:
	req_recv = comm.Irecv(init_value, source=rank-1) # Process i+1 receives value from previous Process 
	req_recv.Wait()
	print("Process {} received value: {}".format(rank, init_value[0]))
	init_value *= rank # Process i+1 multiplies input value with i+1
	try: # Process i+1 sends value to next Process except the last Process 
		req_send = comm.Isend(init_value, dest=rank+1)
		req_send.Wait()
		print("Process {} sent value: {}".format(rank, init_value[0]))
	except Exception as ex:
		print("Process {} is the terminal process.".format(rank)) # The last Process terminates the script
