# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:24:30 2019

@author: dmhedges
"""


from scipy.signal import argrelmax
from preprocessing import read_tdms


def find_peaks_x(color_plot):
    '''
    This function reads in the result of read_tdms and returns the coordinates for the peaks in an x and y array.
    
    The peaks are for each 1d, x-array for the colorplot.
    '''
    peak_x = []
    peak_y = []
    for idx,i in enumerate(color_plot[:]):
        peaks = argrelmax(i, order=8)[0]
        
        for j in peaks:
            peak_x.append(j)
            peak_y.append(idx)
    return peak_x,peak_y


def find_peaks_y(color_plot):
    '''
    This function reads in the result of read_tdms and returns the coordinates for the peaks in an x and y array.
    
    The peaks are for each 1d, y-array for the colorplot.
    '''
    peak_x = []
    peak_y = []
    for idx,i in enumerate(color_plot.T[:]):
        peaks = argrelmax(i, order=8)[0]
        
        for j in peaks:
            peak_y.append(j)
            peak_x.append(idx)
    return peak_x,peak_y


def find_peaks(color_plot):
    '''
    This function takes in a tdms file and calucates the peaks for each 1d array in both the x and y directions.
    The function returns the coordinates for the peaks that are common to both the previous x and y arrays.
    '''
    
    # Get data in
    #color_plot = read_tdms(filename)
    
    # Get coordinates of x-direction peaks
    x3,y3 = find_peaks_x(color_plot)

    # Get coordinates of y-direction peaks
    x5,y5 = find_peaks_y(color_plot)

    # Get intersection of x and y peaks
    x_peak_arrays = list(zip(x3,y3))
    y_peak_arrays = list(zip(x5,y5))
    intersect = set(x_peak_arrays).intersection(set(y_peak_arrays))

    x_final = []
    y_final = []
    for i in intersect:
        x_final.append(i[0])
        y_final.append(i[1])
        
    return x_final,y_final
