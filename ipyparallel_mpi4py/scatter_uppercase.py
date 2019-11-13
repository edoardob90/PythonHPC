from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

A = np.zeros((size,size))
if rank==0:
    A = np.random.randn(size, size)
    print("Original array on root process\n", A)
local_a = np.zeros(size)

comm.Scatter(A, local_a, root=0)
print("Process", rank, "received", local_a)
