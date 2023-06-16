import numpy as np
from numpy import linalg as LA

def get_mu(vert):
     #returns a random measure
     measure = np.random.random(vert)
     measure = measure/measure.sum()
     return measure
    

    
