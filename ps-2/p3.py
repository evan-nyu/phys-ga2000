import numpy as np
import time #I was having trouble getting timeit to run on my computer without crashing, so I used unix time instead

#Size of grid
L = 100 

#Function to get V(i, j, k) -- Using the where parameter of np.divide to deal with /0 case
def V(i, j, k):
    return np.divide((-1)**(i+j+k), np.sqrt((i**2) + (j**2) + (k**2)), where=((i**2 + j**2 + k**2) != 0))

#For Loop Method
loop_start = time.time()
#create sum variable
sum = 0.0
#loop throught all coordinates
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            #get the V of the specified coordinates
            sum += V(i, j, k)

print("For Loop Madelung Constant:", sum)
loop_end = time.time()
print("Time Taken (s)", loop_end - loop_start)


#Meshgrid Method
mesh_start = time.time()

#Create a meshgrid of LxLxL
xs, ys, zs = np.meshgrid(np.arange(-L, L+1, dtype=np.float32), np.arange(-L, L+1, dtype=np.float32), np.arange(-L, L+1, dtype=np.float32))
#Apply V(i,j,k) to all points in the meshgrid
print("Meshgrid Madelung:", np.sum(V(xs, ys, zs)))
mesh_end = time.time()

print("Time Taken (s)", mesh_end - mesh_start)

#print out time difference
print(f"Meshgrid method is {(loop_end - loop_start) / (mesh_end - mesh_start)}x faster than for loop method")
