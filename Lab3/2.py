"""Read in a Fahrenheit temperature. Calculate and display the 
equivalent centigrade temperature. The following formula is used 
for the conversion:"""

def farToCel():
     cel = (5/9) * (far - 32)
     print(int(cel))

far = int(input())
farToCel()