# This script cleans the CIMIS data contained in CIMIS131_2008_2013.csv

import numpy as np
import pandas as pd
from datetime import datetime

# import the data
filepath_in = '../../data/orig/'
filename_in = 'CIMIS131_2008_2013.csv'
data_in = pd.read_csv(filepath_in + filename_in)

# store the data in pd.Series
yr = data_in['Year']
mo = data_in['Month']
day = data_in['Day']
hr = data_in['Hour']
minute = data_in['Minute']
second = data_in['Sec']

# create a list of dates
dates = []
for i in data_in.index:
    dates.append(datetime(yr[i],mo[i],day[i],hr[i],minute[i],second[i]))

# create an output timeseries, with the dates as the index
data_out = data_in.Precip_in
data_out.index = dates

# output the data to a csv file
filename_out = 'arcade_P_CIMIS_2008_2013_inches.csv'
filepath_out = '../../data/format/'
data_out.to_csv(filepath_out + filename_out)

