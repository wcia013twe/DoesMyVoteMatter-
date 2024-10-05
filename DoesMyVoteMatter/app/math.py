import math

def calculate_efficiencygap(dem, rep):
    # Add the two parameters
    total = dem + rep
    # Calculate the threshold by halving the total
    threshold = math.ceil(total / 2)
        
    if dem > rep:
        dem_waste = dem - threshold
        rep_waste = rep
        eg = (rep_waste - dem_waste) / total
    else:
        dem_waste = dem
        rep_waste = rep - threshold
        eg = (dem_waste - rep_waste) / total
        
    return round(eg, 10)

<<<<<<< HEAD
import math

def polsby_Popper(area,perimeter):
    """A district's Polsby Popper(PP) score falls within the range of [0,1] and a score closer to 1 indicates a more compact district.
    
    Parameters:
    area (float): Area of the district (A_D)
    perimeter (float): Perimeter of the district
    
    Returns:
    float: PP compactness score
    """
    
    if perimeter <=0:
        raise ValueError("Perimeter must be greater than zero")
    return(4 * math.pi * area) / (perimeter ** 2)

=======
def Schwartzberg(Perimeter, Area):
    c = 2 * math.pi * math.sqrt((Area / math.pi))
    score = 1 / (Perimeter / c)
    return score
>>>>>>> f2a1f1e76a60ac3104f113858ddcecfc292260c0
