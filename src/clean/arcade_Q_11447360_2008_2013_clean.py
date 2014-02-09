# This script formats the USGS Streamflow data from Arcade Creek in:
# 11447360_2008_2013.txt, converts it to csv with only the datetime and 
# streamflow discharge. The output file is arcade_Q_11447360_2008_2013.csv 

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt

filepath_in = '../../data/orig/11447360_2008_2013.txt'
filepath_out = '../../data/format/arcade_Q_11447360_2008_2013.csv'
na_val = 'alldataisgood'

data_in = pd.read_table(filepath_in, sep='\t',skiprows=26,header=0,na_values=na_val) #read in data
data_in.columns=['agency_cd','site_no','datetime_orig','tz_cd','discharge_cfs','cd'] #set the columns

# create datetime vector of dates
dates = pd.to_datetime(data_in.datetime_orig)

# generate output data
data = {'dates':dates,'discharge_cfs':data_in.discharge_cfs}
data_format = pd.DataFrame(data)

#data_format = data_in['discharge_cfs'] #create output DataFrame
#data_format.index = pd.to_datetime(data_in['datetime_orig']) #convert dates to datetime and sets it as index


# output the pandas timeseries data to csv
data_format.to_csv(filepath_out,index=False) #write data to csv

