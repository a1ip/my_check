from fractions import Fraction 
def divide_pie(shares):
    # Number of all drones
    drones = sum(abs(drone) for drone in shares)
    pie = 1
    for share in shares:
        pie -= (Fraction(share, drones) if
                share > 0 else
                Fraction(- share, drones) * pie)
    return pie.numerator, pie.denominator


test = (-1,-1,-1)
print(divide_pie(test))
        
    
