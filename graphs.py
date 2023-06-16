###Gives three different types of graphs as dictionaries when given a number of vertiecs
###Author: Caroline Cox, 06/09/2023
import numpy as np

def line(vert):
  #returns a line graph given the parameter vert, representing the number of vertices  
  line_graph= {}
  for i in range(1,vert+1):
    if i == 1:
      line_graph["1"] = str(2)
    elif i == vert:
        line_graph[str(vert)] = str(vert-1)
    else:
        line_graph[str(i)] = str(i-1), str(i+1)
  Transitions=set()
  nums=len(line_graph)+1
  for i in line_graph:
    Transitions.add((int(i),int(i)))
    for j in line_graph[i]:
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

def circle(vert):
  #returns a circle graph given the parameter vert, representing the number of vertices    
  circle_graph= {}
  for i in range(1,vert+1):
    if i == 1:
      circle_graph[str(i)] = str(i+1), str(vert)
    elif i == vert:
        circle_graph[str(vert)] = str(vert-1), str(1)
    else:
        circle_graph[str(i)] = str(i-1), str(i+1)
  Transitions=set()
  nums=len(circle_graph)+1
  for i in circle_graph:
    Transitions.add((int(i),int(i)))
    for j in circle_graph[i]:
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

def prism(vert):
    #returns a prism graph given the parameter vert, representing the number of vertices  
    prism_graph = {}
    for i in range(1, vert//2 +1):
      if i == 1:
        prism_graph[str(i)] = str(i+1), str(vert//2), str(vert//2 +1)
      elif i == vert//2:
        prism_graph[str(i)] = str(vert//2-1), str(1), str(vert)
      else:
        prism_graph[str(i)] = str(i-1), str(i+1), str (vert//2 + i)
    for i in range(vert//2+1, vert+1):
      if i == vert//2+1:
          prism_graph[str(i)] = str(i+1), str(i - vert//2), str(vert)
      elif i == vert:
          prism_graph[str(i)] = str(vert-1), str(vert//2 +1), str(i - vert//2)
      else:
          prism_graph[str(i)] = str(i-1), str(i+1), str (i- vert//2)
    Transitions=set()
    nums=len(prism_graph)+1
    for i in prism_graph:
      Transitions.add((int(i),int(i)))
      for j in prism_graph[i]:
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



def grid(vert1, vert2):
    line_1 = line(vert1)
    line_2 = line(vert2)
    grid = np.kron(line_2, np.identity(vert1, dtype=int)) + np.kron(np.identity(vert2, dtype=int), line_1)
    grid[grid>0]=1
    return grid

def matrix(types, verts):
  if types == 0:
    return line(verts)
  if types == 1:
    return circle(verts)
  if types == 2:
    return prism(verts)
  if types == 3:
    return grid(verts, verts)

