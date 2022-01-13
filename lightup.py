#!/usr/bin/python3
 
import pycosat
import math
 
border_puzzle=input()
n_border=int(len(border_puzzle))
n_aux=int(math.sqrt(n_border))

cnf = []

        
for j in range(0,n_aux*n_aux):
    if (border_puzzle[j]=='B' or border_puzzle[j]=='0' or border_puzzle[j]=='1' or border_puzzle[j]=='2' or border_puzzle[j]=='3' or border_puzzle[j]=='4'):
        cnf.append([-(j+1)])
 
sets=[]
little_set = []

for i in range (0,n_aux):
    j=0
    while(j<n_aux):
        if(border_puzzle[n_aux*i+j]=='W'):
            little_set = []
            while(border_puzzle[n_aux*i+j]=='W' and j<n_aux-1):
                little_set.append((n_aux*i+j)+1)
                j=j+1
            if(border_puzzle[n_aux*i+j]=='W' and j==n_aux-1):
                little_set.append((n_aux*i+j)+1)
            sets.append(little_set)
        j=j+1

little_set = []

for i in range (0,n_aux):
    j=0
    while(j<n_aux):
        if(border_puzzle[n_aux*j+i]=='W'):
            little_set = []
            while(border_puzzle[n_aux*j+i]=='W' and j<n_aux-1):
                little_set.append((n_aux*j+i)+1)
                j=j+1
            if(border_puzzle[n_aux*j+i]=='W' and j==n_aux-1):
                little_set.append((n_aux*j+i)+1)
            sets.append(little_set)
        j=j+1
 
i=0
j=0
k=0

coord = []
for i in range(0, n_aux*n_aux):
    for j in sets:
        for k in j:
            if((i+1) == int(k)):
                coord.append((i+1,j))
    
i=0
j=0
k=0

neigh = []
mini = []
for i in range(0,n_aux*n_aux):
    mini=[]
    for j in coord:
        if((i+1)==int(j[0])):
           for k in j[1]:
                mini.append(int(k))
    if mini:
        neigh.append((i+1, list(dict.fromkeys(mini))))
       
i=0
j=0
k=0

least=[]
for i in neigh:
    for j in i[1]:
        least.append(int(j))
    cnf.append(least)
    least=[]

 
i=0
j=0
k=0
x=0
y=0

mos=[]
for i in neigh:
    x=(int(i[0]))
    for j in i[1]:
        y=(int(j))
        if(x!=y):
            mos=[]
            mos.append(-x)
            mos.append(-y)
            cnf.append(mos)
 
i=0 
x1_cnf=0
x2_cnf=0
x3_cnf=0
x4_cnf=0

for j in range(0,len(border_puzzle)):
    x=border_puzzle[j]
    if (x=='0' or x=='1' or x=='2' or x=='3' or x=='4'):
        x1_cnf=i
        x2_cnf=i+n_aux+1
        x3_cnf=i+2
        x4_cnf=i-n_aux+1

        if(i%n_aux-1<0):
            x1_b='-1'
        else:
            x1_b=x1_cnf
        if(int(i/n_aux)+1>n_aux-1):
            x2_b='-1'
        else:
            x2_b=x2_cnf
        if(i%n_aux+1>n_aux-1):
            x3_b='-1'
        else:
            x3_b=x3_cnf
        if(int(i/n_aux)-1<0):
            x4_b='-1'
        else:
            x4_b=x4_cnf
         
         
        if(x=='0'):
            if (x1_b!='-1'):
                cnf.append([-x1_cnf])
            if (x2_b!='-1'):
                cnf.append([-x2_cnf])
            if (x3_b!='-1'):
                cnf.append([-x3_cnf])
            if (x4_b!='-1'):
                cnf.append([-x4_cnf])
            
        elif (x=='1'):
            if (x1_b!='-1' and x2_b!='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x2_cnf])
                cnf.append([-x1_cnf,-x3_cnf])
                cnf.append([-x1_cnf,-x4_cnf])
                cnf.append([x1_cnf,x2_cnf,x3_cnf,x4_cnf])
                cnf.append([-x2_cnf,-x3_cnf])
                cnf.append([-x2_cnf,-x4_cnf])
                cnf.append([-x3_cnf,-x4_cnf])
            elif (x1_b=='-1' and x2_b!='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x2_cnf,-x3_cnf])
                cnf.append([-x2_cnf,-x4_cnf])
                cnf.append([x2_cnf,x3_cnf,x4_cnf])
                cnf.append([-x3_cnf,-x4_cnf])
                
            elif (x1_b!='-1' and x2_b=='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x3_cnf])
                cnf.append([-x1_cnf,-x4_cnf])
                cnf.append([x1_cnf,x3_cnf,x4_cnf])
                cnf.append([-x3_cnf,-x4_cnf])
                 
            elif (x1_b!='-1' and x2_b!='-1' and x3_b=='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x2_cnf])
                cnf.append([-x1_cnf,-x4_cnf])
                cnf.append([x1_cnf,x2_cnf,x4_cnf])
                cnf.append([-x2_cnf,-x4_cnf])
                 
            elif (x1_b!='-1' and x2_b!='-1' and x3_b!='-1' and x4_b=='-1'):
                cnf.append([-x1_cnf,-x2_cnf])
                cnf.append([-x1_cnf,-x3_cnf])
                cnf.append([x1_cnf,x2_cnf,x3_cnf])
                cnf.append([-x2_cnf,-x3_cnf])
                 
            elif (x1_b=='-1' and x2_b=='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x3_cnf,-x4_cnf])
                cnf.append([x3_cnf,x4_cnf])
                 
            elif(x1_b=='-1' and x2_b!='-1' and x3_b!='-1' and x4_b=='-1'):
                cnf.append([-x2_cnf,-x3_cnf])
                cnf.append([x2_cnf,x3_cnf])
                 
            elif(x1_b!='-1' and x2_b=='-1' and x3_b=='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x4_cnf])
                cnf.append([x1_cnf,x4_cnf])
                 
            elif (x1_b!='-1' and x2_b!='-1' and x3_b=='-1' and x4_b=='-1'):
                cnf.append([-x1_cnf,-x2_cnf])
                cnf.append([x1_cnf,x2_cnf])
           

        elif (x=='2'):
            if (x1_b!='-1' and x2_b!='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x2_cnf,-x3_cnf])
                cnf.append([-x1_cnf,-x2_cnf,-x4_cnf])
                cnf.append([-x1_cnf,-x3_cnf,-x4_cnf])
                cnf.append([x1_cnf,x2_cnf,x3_cnf])
                cnf.append([x1_cnf,x2_cnf,x4_cnf])
                cnf.append([x1_cnf,x3_cnf,x4_cnf])
                cnf.append([-x2_cnf,-x3_cnf,-x4_cnf])
                cnf.append([x2_cnf,x3_cnf,x4_cnf])
                
            elif (x1_b=='-1' and x2_b!='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x2_cnf,-x3_cnf,-x4_cnf])
                cnf.append([x2_cnf,x3_cnf])
                cnf.append([x2_cnf,x4_cnf])
                cnf.append([x3_cnf,x4_cnf])
                
            elif (x1_b!='-1' and x2_b=='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x3_cnf,-x4_cnf])
                cnf.append([x1_cnf,x3_cnf])
                cnf.append([x1_cnf,x4_cnf])
                cnf.append([x3_cnf,x4_cnf])
                 
            elif (x1_b!='-1' and x2_b!='-1' and x3_b=='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x2_cnf,-x4_cnf])
                cnf.append([x1_cnf,x2_cnf])
                cnf.append([x1_cnf,x4_cnf])
                cnf.append([x2_cnf,x4_cnf])
                
            elif (x1_b!='-1' and x2_b!='-1' and x3_b!='-1' and x4_b=='-1'):
                cnf.append([-x1_cnf,-x2_cnf,-x3_cnf])
                cnf.append([x1_cnf,x2_cnf])
                cnf.append([x1_cnf,x3_cnf])
                cnf.append([x2_cnf,x3_cnf])
                
            elif (x1_b=='-1' and x2_b=='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([x3_cnf])
                cnf.append([x4_cnf])
                
            elif(x1_b=='-1' and x2_b!='-1' and x3_b!='-1' and x4_b=='-1'):
                cnf.append([x2_cnf])
                cnf.append([x3_cnf])
                
            elif(x1_b!='-1' and x2_b=='-1' and x3_b=='-1' and x4_b!='-1'):
                cnf.append([x4_cnf])
                cnf.append([x1_cnf])
               
            elif (x1_b!='-1' and x2_b!='-1' and x3_b=='-1' and x4_b=='-1'):
                cnf.append([x1_cnf])
                cnf.append([x2_cnf])
                
        elif (x=='3'):
            if (x1_b!='-1' and x2_b!='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([-x1_cnf,-x2_cnf,-x3_cnf,-x4_cnf])
                cnf.append([x1_cnf,x2_cnf])
                cnf.append([x1_cnf,x3_cnf])
                cnf.append([x1_cnf,x4_cnf])
                cnf.append([x2_cnf,x3_cnf])
                cnf.append([x2_cnf,x4_cnf])
                cnf.append([x3_cnf,x4_cnf])
            elif (x1_b=='-1' and x2_b!='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([x2_cnf])
                cnf.append([x3_cnf])
                cnf.append([x4_cnf])
            elif (x1_b!='-1' and x2_b=='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([x1_cnf])
                cnf.append([x3_cnf])
                cnf.append([x4_cnf])
            elif (x1_b!='-1' and x2_b!='-1' and x3_b=='-1' and x4_b!='-1'):
                cnf.append([x1_cnf])
                cnf.append([x2_cnf])
                cnf.append([x4_cnf])
            elif (x1_b!='-1' and x2_b!='-1' and x3_b!='-1' and x4_b=='-1'):
                cnf.append([x1_cnf])
                cnf.append([x2_cnf])
                cnf.append([x3_cnf])
            else:
                cnf.append([j+1])
                 
        elif(x=='4'):
            if (x1_b!='-1' and x2_b!='-1' and x3_b!='-1' and x4_b!='-1'):
                cnf.append([x1_cnf])
                cnf.append([x2_cnf])
                cnf.append([x3_cnf])
                cnf.append([x4_cnf])
            else:
                cnf.append([j+1])
 
    i=i+1

cell_bulb=pycosat.solve(cnf)

final =""
if (cell_bulb=='UNSAT'):
    print(0)
else:
    i=0
    for i in cell_bulb:
        if (int(i) > 0):
            final=final+"L"
        else:
            final=final+border_puzzle[cell_bulb.index(i)]
    if (len(final)<len(border_puzzle)):
        final=final+border_puzzle[len(final)::]
    print(final)
