# -*- coding: utf-8 -*-
"""
This code calculates price for European Call option  Using Monte Carlo method
Underlying is stock

@author: AmirMoradibaad
"""


import math
import numpy as np

#adding parameters
r=0.01; sigma=0.4; S_0=1; #market parameters
K=1; T=1; #contract parameters
nSim=1000000; #discretization parameter


#Simulates the stock dynamic S_T
s_t = [1 for x in range(nSim)]

rnd = np.random.standard_normal(nSim)

for i in range(nSim):
    s_t[i] = S_0 * (math.exp((r- 0.5*sigma**2)*T + sigma*math.sqrt(T)*rnd[i]))
    s_t[i] = math.exp(-r*T) *  max(s_t[i] - K , 0) 
    
    
price = sum(s_t)/nSim

