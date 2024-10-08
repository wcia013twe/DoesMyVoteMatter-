import math

def calculate_efficiencygap(dem, rep):
    # Add the two parameters
    total = dem + rep
    # Calculate the threshold by halving the total
    threshold = math.ceil(total / 2)
        
    if dem > rep:
        dem_waste = dem - threshold
        rep_waste = rep
        eg = abs((rep_waste - dem_waste)) / total
    else:
        dem_waste = dem
        rep_waste = rep - threshold
        eg = abs((dem_waste - rep_waste)) / total
        
    return round(eg, 5)

def Schwartzberg(Area, Perimeter):
    c = 2 * math.pi * math.sqrt((Area / math.pi))
    score = 1 / (Perimeter / c)
    return round(score, 5)

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
    return round((4 * math.pi * area) / (perimeter ** 2), 5)

def reock(area, perimeter):
    """A district's Reock score falls within the range of [0,1] and a score closer to 1 indicates a more compact district.

    Parameters:
    area (float): Area of the district (A_D)
    perimeter (float): Perimeter of the district
    
    Returns:
    float: Reock compactness score
    """
    
    if perimeter <=0:
        raise ValueError("Perimeter must be greater than zero")
    return round(area / (math.pi * ((perimeter / (2 * math.pi)) ** 2)), 5)
