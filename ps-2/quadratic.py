import numpy as np


#Functions for Parts a & b
def a_quadratic(a, b, c):
    d = np.sqrt(b**2 - 4*a*c)
    return ((-b + d)/(2*a), (-b - d)/(2*a))


def b_quadratic(a, b, c):
    d = np.sqrt(b**2 - 4*a*c)
    return (2*c /(-b - d), 2*c / (-b + d))

#Function for part c
def quadratic(a, b, c):
    d = np.sqrt(b**2 - 4*a*c)

    #If b<0 use part a for the plus solution and part b for the minus solution
    if(b<0):
        plus = (-b + d)/(2*a)
        minus = (2*c/(-b + d))
        return(plus, minus)

    #Tho opposite for b>0
    else:
        plus = (2*c/(-b - d))
        minus = (-b - d)/(2*a)
        return(plus, minus)

if __name__ == "__main__":
    print("Method From Part a", a_quadratic(0.001, 1000, 0.001))

    print("Method From Part b", b_quadratic(0.001, 1000, 0.001))

    print("Function for part c")
    print("a=0.001, b=1000, c=0.001", quadratic(0.001, 1000, 0.001))
    print("a=0.001, b=-1000, c=0.001", quadratic(0.001, -1000, 0.001))
