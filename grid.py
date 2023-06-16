import numpy as np

def get_grid1(vert, width, leng):
  #returns a grid graph given the parameters vert, representing the number
  #of vertices and width, the width of the graph
  nodes = np.arange(1, vert+1)
  n = np.split(nodes, width)
  newlist= []
  for i in n:
      newlist.append(i.tolist())
  grid={}
  print(n)
  print(newlist)
  for i in newlist:
    for j in i:
      if newlist.index(i)== 0:
        if i.index(j)==0:
          grid[str(j)]= str(j+1), str(j+leng)
        elif i.index(j) == leng-1:
          grid[str(j)]= str(j-1), str(j+leng)
        else:
          grid[str(j)]= str(j-1), str(j+leng), str(j+1)
      elif newlist.index(i)== width-1:
        if i.index(j)==0:
          grid[str(j)]= str(j+1), str(j-leng)
        elif i.index(j)== leng-1:
          grid[str(j)]= str(j-1), str(j-leng)
        else:
          grid[str(j)]= str(j-1), str(j-leng), str(j+1)
      else:
        if i.index(j)==0:
          grid[str(j)]= str(j+1), str(j+leng), str(j-leng)
        elif i.index(j)== leng-1:
          grid[str(j)]= str(j-1), str(j+leng), str(j-leng)
        else:
          grid[str(j)]= str(j-1), str(j+leng), str(j+1), str(j-leng)
  return grid

def get_circle(vert):
  #returns a circle graph given the parameter vert, representing the number of vertices    
  circle_graph= {}
  for i in range(1,vert+1):
    if i == 1:
      circle_graph[str(i)] = str(i+1), str(vert)
    elif i == vert:
        circle_graph[str(vert)] = str(vert-1), str(1)
    else:
        circle_graph[str(i)] = str(i-1), str(i+1)
  return circle_graph

def get_line(vert):
  #returns a line graph given the parameter vert, representing the number of vertices  
  line_graph= {}
  for i in range(1,vert+1):
    if i == 1:
      line_graph["1"] = str(2)
    elif i == vert:
        line_graph[str(vert)] = str(vert-1)
    else:
        line_graph[str(i)] = str(i-1), str(i+1)
  return line_graph

def get_adjacency_matrix(graph):
  #returns a matrix of 0s and 1s which tells us which vertices are connected
  Transitions=set()
  nums=len(graph)+1
  vert= len(graph)
  for i in graph:
    Transitions.add((int(i),int(i)))
    for j in graph[i]:
      Transitions.add((int(i), int(j)))
  Matrix=[]
  for i in range(1,nums):
    row=[]
    for j in range(1,nums):
      if (i,j) in Transitions:
        row.append(1)
      else:
        row.append(0)
    Matrix.append(row)

  return np.array(Matrix)
def get_grid2(vert1, vert2):
    graph_1 = get_line(vert1)
    M = get_adjacency_matrix(graph_1)
    graph_2 = get_line(vert2)
    N = get_adjacency_matrix(graph_2)
    grid = np.kron(M, np.identity(vert2, dtype=int)) + np.kron(np.identity(vert1, dtype=int), N)
    return grid

def bin_array(vert):
    #returns the power set of all vertices
    if vert==1:
        return np.array((0,1)).reshape((2,1))
    U_l = bin_array(vert-1)
    top= np.hstack((np.zeros((U_l.shape[0],1)),U_l))
    bot= np.hstack((np.ones((U_l.shape[0],1)),U_l))
    return(np.vstack((top,bot)))

def get_mu(vert):
     #returns a random measure
     measure = np.random.random(vert)
     measure = measure/measure.sum()
     return measure

if __name__ == "__main__":
    M = get_grid2(3,3)
    print(M)
    U=bin_array(M.shape[0])
    print(get_mu(M.shape[0]))
   
    
