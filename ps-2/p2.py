import numpy as np

#Code to find the smallest number I can add to one and not get one
f32 = np.float32(1)
while 1:
    f32 = f32/10
    if(f32+1 == 1):
        print("Smallest f32 that can be added to 1:", f32)
        break

#Smallest f64 that can be added to one
f64 = np.float64(1)
while 1:
    f64 = f64/10
    if(f64+1 == 1):
        print("Smallest f64 that can be added to 1:",f64)
        break

#Smallest f32 before underflow
f32 = np.float32(1)
while f32/10 != 0:
    f32 = f32/10
print("float32 underflow", f32)

#smallest f64 before underflow
f64 = np.float64(1)
while f64/10 != 0:
    f64 = f64/10
print("float64 underflow", f64)


#largest f32 before overflow
f32 = np.float32(1)
while 1:
    if f32*10 == np.inf:
        print("Max f32 before overflow:", f32)
        break
    f32=f32*10

#largest f64 before overflow
f64 = np.float64(1)
while 1:
    if f64*10 == np.inf:
        print("Max f64 before overflow:", f64)
        break
    f64=f64*10
