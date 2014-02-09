# This script cleans the CIMIS data contained in CIMIS131_2008_2013.csv

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt

# import the data
filepath_in = '../../data/orig/'
filename_in = 'CIMIS131_2008_2013.csv'
na_val = -9999
data_in = pd.read_csv(filepath_in + filename_in,na_values=na_val)

# calculate precip_mm units
precip_mm = data_in.Precip_in * 25.4

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
data = {'dates':dates,'precip_in':data_in.Precip_in, 'precip_mm':precip_mm} # creat dict with data
data_out = pd.DataFrame(data)

# data_out = data_in.Precip_in #old version of data frame
# data_out.index = dates

# output the data to a csv file
filename_out = 'arcade_P_CIMIS_2008_2013'
filepath_out = '../../data/format/'
data_out.to_csv(filepath_out + filename_out + '.csv',index=0)

# f1 = plt.figure()
#ax1 = f1.add_subplot(1,1,1)
#ax1.plot(dates,data_out.precip_mm)

#f1.set_size_inches(300,10)
#f1.savefig(filepath_out + filename_out + '.jpg')
