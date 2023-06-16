### Gives the Transport Distance from a given graph.
### Written by Caroline Cox with help from Jey Raymond and Robert Bland, 06/09/2023

import numpy as np
import graphs
import mu_nu


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

def expected_transport_distance(types, verts):
  M = graphs.matrix(0, 10)
  U = bin_array(M.shape[0])
  with open("new_samples", "w") as data:
    for number in range(10):
        mu = mu_nu.get_mu(M.shape[0])
        nu = mu_nu.get_mu(M.shape[0])
        data.write(str(steps(M, U, mu, nu)))
        data.write("\n")
        for j in range(M.shape[0]):
            if j == M.shape[0] -1:
                data.write(str(mu[j]) )
            else:     
                data.write(str(mu[j])+ "," )
        data.write("\n")
        for j in range(M.shape[0]):
            if j == M.shape[0] -1:
                data.write(str(nu[j]))
            else:     
                data.write(str(nu[j])+ "," )
        data.write("\n")

if __name__ == "__main__": 
  expected_transport_distance(1, 5) 
  
    
