#!/usr/bin/env python
# coding: utf-8

# In[11]:


def pageRank(inputFile):
    print("\n************************ For "+ inputFile+" ************************")
    outputFile=open('output_'+ inputFile,"w")
    
    inputFile=open(inputFile,"r")
    nodes=int(inputFile.readline()) # no of vertices
    graph=np.zeros((nodes,nodes)) # initialize the graph with all zeros

    
    while True:
    #creating the graph matrix from the input 
            line = inputFile.readline()
            if line=="":
                    break
            
            line=line.split()   
            x=int(line[0])
            y=int(line[1])
            graph[y][x]=1
            
    
    
    inputFile.close()

    print("\nNumber of nodes:",nodes)

    print("\nWeb graph:\n",graph)

    M=np.zeros((nodes,nodes))  # Calculate M matrix
    outLink=np.sum(graph, axis=0)
    print("\noutLink: ", outLink)

    for i in range(nodes):
        for j in range(nodes):
            if(graph[i][j] == 1):
                    M[i][j] = 1/outLink[j]

    print("\nM:\n",M)

    r=np.ones(nodes)
    r=r/nodes
    

    print ( "\nExecuting Power Iteration\n")
    
    print("Iteration  0", "\t-> ", np.around(r, decimals=5))
 
    for i in range(99) :
        
        prev_r = r.copy()    
        
        r = np.dot(M,r)
        
        print("Iteration ",i+1, "\t-> ", np.around(r, decimals=5))

        diff = abs(prev_r-r)/prev_r  
        print ("Difference ", "\t-> ", diff)
        
        if(all(i <= 0.05 for i in diff)):
            break



    for i in range(len(r)):

        string ="< "+str(i)+", "+str(round(r[i], 5))+" >\n"
        outputFile.write(string)

    outputFile.close()
    


# In[12]:


import numpy as np

inputFiles = ["test1.txt", "test2.txt", "test3.txt", "test4.txt"]


for inputFile in inputFiles:
    pageRank(inputFile)
    


# In[ ]:





# In[ ]:




