#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:16:10 2018

@author: afonya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file ='/home/afonya/eghajlati adatsorok/eghajlati_adatsor_Debrecen1901-2010/havi_adatok/DE_M_ta.txt'

monthdata_avgtemp = pd.read_csv(file, sep=';')

monthdata_avgtemp['year']= [str(x)[:4] for x in monthdata_avgtemp['#datum']]
monthdata_avgtemp['month']= [str(x)[5:] for x in monthdata_avgtemp['#datum']]                 
monthdata_avgtemp['year']=monthdata_avgtemp['year'].astype('int64')
monthdata_avgtemp['month']=monthdata_avgtemp['month'].astype('int64')

month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December' ]

fig=plt.figure(figsize=(8,6))

p=[]

for i in range(0,12):
    b = month[i] 
    a = monthdata_avgtemp[monthdata_avgtemp.month==i+1]
    
    name=fig.add_subplot(4, 3, i+1)
    name.set_title(b)
    name.plot(a.year, a.m_ta, 'o')
    z1 = np.polyfit(a.year, a.m_ta, 1)
    p1 = np.poly1d(z1)
    plt.plot(a.year,p1(a.year))
    
    p.append(p1[1])
    i+=1
    
plt.tight_layout()    
plt.show()

for i in range(0,12):
    print(month[i],p[i])