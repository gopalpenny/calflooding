# This script formats the USGS Streamflow data from Arcade Creek in:
# 11447360_2008_2013.txt, converts it to csv with only the datetime and 
# streamflow discharge. The output file is arcade_Q_11447360_2008_2013.csv 

import numpy as np
import pandas as pd
from datetime import datetime

filepath_in = '../../data/orig/11447360_2008_2013.txt'
filepath_out = '../../data/format/arcade_Q_11447360_2008_2013.csv'

data_in = pd.read_table(filepath_in, sep='\t',skiprows=26,header=0) #read in data
data_in.columns=['agency_cd','site_no','datetime_orig','tz_cd','discharge_cfs','cd'] #set the columns
data_in['datet'] = pd.to_datetime(data_in['datetime_orig']) #convert dates to datetime
data_format = data_in[['datet','discharge_cfs']] #create output DataFrame
data_format.to_csv(filepath_out) #write data to csv
