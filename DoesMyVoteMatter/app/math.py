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

def Schwartzberg(Perimeter, Area):
    c = 2 * math.pi * math.sqrt((Area / math.pi))
    score = 1 / (Perimeter / c)
    return score
