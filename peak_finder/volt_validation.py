#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:30:31 2019

@author: dmhedges
"""

from full_processing import get_dataframe
import pandas as pd

spon1 = '00_Nac1p_3.tdms'
spon2 = '00_Nac1p_9_spons.tdms'
spon3 = '00_Nac1p_10.tdms'
spon4 = '00_Nac1p_11.tdms'
spon5 = '01_Nac1p_1uMCoc_1.tdms'
spon6 = '01_Nac1p_1uMCoc_4.tdms'

spons = [spon1, spon2, spon3, spon4, spon5, spon6]

appended_data = []

for i in spons:
    df = get_dataframe(i)
    #print(df.head())
    appended_data.append(df)
    
    
appended_df = pd.concat(appended_data, axis=0)
print(appended_df.count())


