import numpy as np

f32 = np.float32(100.98763)

#Code from jupyter notebook
def get_bits(number):
    """For a NumPy quantity, return bit representation
    
    Inputs:
    ------
    number : NumPy value
        value to convert into list of bits
        
    Returns:
    -------
    bits : list
       list of 0 and 1 values, highest to lowest significance
    """
    bytes = number.tobytes()
    bits = []
    for byte in bytes:
        bits = bits + np.flip(np.unpackbits(np.uint8(byte)), np.uint8(0)).tolist()
    return list(reversed(bits))

#convert array of bits to string for easy manipulation
bits32 = ''.join(map(str, get_bits(f32)))
print("Binary Representation of 100.98763:", bits32)

#the exponent is contained in bits 1 to 9
exponent = bits32[1:9]
print("Exponent: ", exponent)
print("Exponent integer representation: ", int(exponent, 2))
#The integer value exponent is given by 2^(e-127)
power = int(exponent, 2) - 127
print("Exponent -127: ", power)

#the mantissa is bits 9 until the end with a one added to the front
mantissa = "1"+bits32[9:]
print("Mantissa with 1 added to the front: ", mantissa)

#to convert the number into decimal, we need to split the whole and fractional parts by using the exponent to determine the position of the decimal
whole = mantissa[0:power+1]
fraction = mantissa[power+1:]
print("Adding in decimal point based on the exponent: ", whole + "." + fraction)

#while the whole number portion of the number is trivial to convert from binary to decimal, the fractional portion must be done "by hand" with a for loop
intfraction = 0
index = 1
for bit in fraction:
    intfraction += 2**(-index)*int(bit)
    index += 1
#eliminating the '0.' from the string so we can nicely concatinate it with the whole portion of the number
stringIntFrac = str(intfraction)[2:]
print("Converting the left and right sides of the deciman to base 10 integers: ", f"{int(whole,2)}.{stringIntFrac}")


