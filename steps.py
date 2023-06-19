### Gives the Transport Distance from a given graph.
### Written by Caroline Cox with help from Jey Raymond and Robert Bland, 06/09/2023

import numpy as np
import graphs
import mu_nu
from collections import Counter



def bin_array(vert):
    #returns the power set of all vertices
    if vert==1:
        return np.array((0,1)).reshape((2,1))
    U_l = bin_array(vert-1)
    top= np.hstack((np.zeros((U_l.shape[0],1)),U_l))
    bot= np.hstack((np.ones((U_l.shape[0],1)),U_l))
    return(np.vstack((top,bot)))


def steps(Matrix, U, mu, nu, tol=1e-10):
  #returns the number of steps given two random measures
  N_U = U
  nu_U = np.dot(N_U,nu.T)
  n=0
  counter = 0
  while not np.all(np.dot(N_U,mu.T) >= (nu_U - tol)):
    N_U = np.dot(N_U, Matrix)
    N_U[N_U > 0] = 1
    n+=1
  return n

def expected_transport_distance(M, numtrials, fname):
  U = bin_array(M.shape[0])
  counts = Counter()
  with open(fname, "w") as data:
    for number in range(numtrials):
        mu = mu_nu.get_mu(M.shape[0])
        nu = mu_nu.get_mu(M.shape[0])
        s = steps(M, U, mu, nu)
        counts[s] += 1
    for i in counts:
        data.write(str(i) + ',')
        data.write(str(counts[i]) + ' ')
        data.write('\n')
    

if __name__ == "__main__": 
  numtrials = 100
  fname = 'data/new_samples'
  for i in range(3,21):
    M = graphs.matrix(0, i)
    expected_transport_distance(M, numtrials, f'{fname}_{i}.txt') 
  
    
