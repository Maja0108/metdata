#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:09:18 2018

@author: afonya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


monthdata_avgtemp = pd.read_csv('/home/afonya/eghajlati adatsorok/eghajlati_adatsor_Debrecen1901-2010/havi_adatok/DE_M_ta.txt', sep=';')

monthdata_avgtemp['year']= [str(x)[:4] for x in monthdata_avgtemp['#datum']]
monthdata_avgtemp['month']= [str(x)[5:] for x in monthdata_avgtemp['#datum']]                 
monthdata_avgtemp['year']=monthdata_avgtemp['year'].astype('int64')
monthdata_avgtemp['month']=monthdata_avgtemp['month'].astype('int64')
                 
#plt.plot(monthdata_avgtemp.month, monthdata_avgtemp.m_ta, 'o')

#monthdata_avgtemp.boxplot(column='m_ta', by='month')

#monthdata_avgtemp.boxplot(column='m_ta', by='year')

Jan= monthdata_avgtemp[monthdata_avgtemp.month==1]
Febr= monthdata_avgtemp[monthdata_avgtemp.month==2]
March= monthdata_avgtemp[monthdata_avgtemp.month==3]
April= monthdata_avgtemp[monthdata_avgtemp.month==4]
May= monthdata_avgtemp[monthdata_avgtemp.month==5]
June= monthdata_avgtemp[monthdata_avgtemp.month==6]
July= monthdata_avgtemp[monthdata_avgtemp.month==7]
Aug= monthdata_avgtemp[monthdata_avgtemp.month==8]
Sept= monthdata_avgtemp[monthdata_avgtemp.month==9]
Oct= monthdata_avgtemp[monthdata_avgtemp.month==10]
Nov= monthdata_avgtemp[monthdata_avgtemp.month==11]
Dec= monthdata_avgtemp[monthdata_avgtemp.month==12]



fig=plt.figure(figsize=(8,6))

sub1=fig.add_subplot(431)
sub1.set_title('January') 
sub1.plot(Jan.year, Jan.m_ta, 'o')
z1 = np.polyfit(Jan['year'], Jan.m_ta, 1)
p1 = np.poly1d(z1)
plt.plot(Jan['year'],p1(Jan['year']))

sub2=fig.add_subplot(432)
sub2.set_title('February') 
sub2.plot(Febr.year, Febr.m_ta, 'o')
z2 = np.polyfit(Febr['year'], Febr.m_ta, 1)
p2 = np.poly1d(z2)
plt.plot(Febr['year'],p2(Febr['year']))

sub3=fig.add_subplot(433)
sub3.set_title('March') 
sub3.plot(March.year, March.m_ta,'o')
z3 = np.polyfit(March['year'], March.m_ta, 1)
p3 = np.poly1d(z3)
plt.plot(March['year'],p3(March['year']))

sub4=fig.add_subplot(434)
sub4.set_title('April') 
sub4.plot(April.year, April.m_ta, 'o')
z4 = np.polyfit(April['year'], April.m_ta, 1)
p4 = np.poly1d(z4)
plt.plot(April['year'],p4(April['year']))

sub5=fig.add_subplot(435)
sub5.set_title('May') 
sub5.plot(May.year, May.m_ta, 'o')
z5 = np.polyfit(May['year'], May.m_ta, 1)
p5 = np.poly1d(z5)
plt.plot(Jan['year'],p5(Jan['year']))

sub6=fig.add_subplot(436)
sub6.set_title('June') 
sub6.plot(June.year, June.m_ta, 'o')
z6 = np.polyfit(June['year'], June.m_ta, 1)
p6 = np.poly1d(z6)
plt.plot(June['year'],p6(June['year']))

sub7=fig.add_subplot(437)
sub7.set_title('July') 
sub7.plot(July.year, July.m_ta, 'o')
z7 = np.polyfit(July['year'], July.m_ta, 1)
p7 = np.poly1d(z7)
plt.plot(July['year'],p7(July['year']))

sub8=fig.add_subplot(438)
sub8.set_title('August') 
sub8.plot(Aug.year, Aug.m_ta, 'o')
z8 = np.polyfit(Aug['year'], Aug.m_ta, 1)
p8 = np.poly1d(z8)
plt.plot(Aug['year'],p8(Aug['year']))

sub9=fig.add_subplot(439)
sub9.set_title('September') 
sub9.plot(Sept.year, Sept.m_ta, 'o')
z9 = np.polyfit(Sept['year'], Sept.m_ta, 1)
p9 = np.poly1d(z9)
plt.plot(Sept['year'],p9(Sept['year']))

sub10=fig.add_subplot(4,3,10)
sub10.set_title('October') 
sub10.plot(Oct.year, Oct.m_ta, 'o')
z10 = np.polyfit(Oct['year'], Oct.m_ta, 1)
p10 = np.poly1d(z10)
plt.plot(Oct['year'],p10(Oct['year']))

sub11=fig.add_subplot(4,3,11)
sub11.set_title('November') 
sub11.plot(Nov.year, Nov.m_ta, 'o')
z11 = np.polyfit(Nov['year'], Nov.m_ta, 1)
p11 = np.poly1d(z11)
plt.plot(Nov['year'],p11(Nov['year']))

sub12=fig.add_subplot(4,3,12)
sub12.set_title('December') 
sub12.plot(Dec.year, Dec.m_ta, 'o')
z12 = np.polyfit(Dec['year'], Dec.m_ta, 1)
p12 = np.poly1d(z12)
plt.plot(Dec['year'],p12(Dec['year']))

plt.tight_layout()
plt.show()

print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)