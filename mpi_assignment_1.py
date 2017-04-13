from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank() # get the rank for this process

if rank%2 == 0: # check if this rank is even
        print("Hello from process {}".format(rank))

if rank%2 == 1: # check if this rank is odd
        print("Goodbye from process {}".format(rank))