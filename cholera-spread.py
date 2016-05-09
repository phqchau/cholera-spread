
# coding: utf-8

# In[1]:

import math
import numpy as np, pandas as pd, seaborn as sns
from matplotlib import pyplot as plt
from ipywidgets import interact, interactive, fixed
get_ipython().magic('matplotlib inline')
import csv


# In[6]:

df = pd.read_csv('https://www.udel.edu/johnmack/frec682/cholera/pumps.txt')
dt = pd.read_csv('https://www.udel.edu/johnmack/frec682/cholera/deaths.txt')

df.plot(kind='scatter',x='X',y='Y', color='red',label='Pump locations')
dt.plot(kind='scatter',x='X',y='Y',label='Death locations')


# In[8]:

def cholera():
    with open('deaths.csv', 'rt') as f:
        reader = csv.reader(f)
        Coordlist = list(reader)
        
    CList = [[float(column) for column in row] for row in Coordlist]
    
    XYdist = []
    
    for row in CList:
        x = row[0]
        y = row[1]
        dist = math.sqrt(((x-12.5713596)**2)+((y-11.7271700)**2))
        XYdist.append(dist)
    
    distxy = [x for (y,x) in sorted(zip(XYdist,CList))]
    
    def deathcount(n=1):
        deaths = 3
        for n in np.arange(n):
            deaths = deaths + (math.sqrt(deaths))
            
            dist = distxy[:int(deaths)]
            
            x,y = zip(*dist)
            
            plt.plot(12.5713596,11.7271700,'r.')
            plt.axis([0, 20, 0, 18])
            plt.scatter(x,y)
    
    deathcount()
    
    interact(deathcount,n=(1,60))
        
cholera()


# In[ ]:



