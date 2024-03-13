"""Write a function that computes the volume of a sphere
 given its radius."""

def sphereVol():
    
    vol = lambda r: (4/3) * 3.14 * pow(r, 3)
    print(vol(rad))


rad = int(input())
sphereVol()
