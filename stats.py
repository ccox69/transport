### Reads in data file and returns the mean, standard deviation,
### and pdf of the stpes.
### Author Caroline Cox, 06/11/2023

import numpy as np

def get_mean_steps(pdf):
    #Returns the mean number of steps from a given data set.
    #Takes the parameter pdf, which is the probability density function. 
    avg = 0
    for i in range(len(pdf)):
        avg = i * pdf[i] + avg
    return avg   
def get_s_dev(pdf):
    #Returns the standard deviation of the steps from a given data set.
    #Takes the parameter pdf, which is the probability density function.
    return np.std(pdf)

def get_pdf(file):
    #Returns the pdf from a given data step.
    #Takes the parameter file, which is the data set. 
    data = file.readlines()
    steps= []
    for i in range(0,len(data),3):
        steps.append(int(data[i]))
    largest = max(steps)
    num_trials = len(steps)
    pdf= []
    for i in range(largest+1):
        pdf.append(steps.count(i)/num_trials)
    return pdf
  
    
if __name__ == "__main__":
    file= open('new_samples', 'r')
    pdf= get_pdf(file)
    print(pdf)
    print(get_mean_steps(pdf))
    print(get_s_dev(pdf))
    
