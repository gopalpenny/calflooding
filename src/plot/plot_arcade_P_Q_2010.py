# This script imports formatted P and Q data for arcade creek from 2008 - 2013, and plots the data in a series of subplots (1 subplot for each year, Oct - March). The resulting figure is saved in the /data/fig directory)

# import python extensions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# data directory and filenames
dirformat = '../../data/format/'
Q_filename = 'arcade_Q_11447360_2008_2013.csv'
P_filename = 'arcade_P_CIMIS_2008_2013.csv'

# import data
arcade_Q = pd.read_csv(dirformat + Q_filename)
arcade_P = pd.read_csv(dirformat + P_filename)

# convert data to pd.TimeSeries
Q = pd.Series(arcade_Q['discharge_cfs'])
Q.index = pd.to_datetime(arcade_Q['dates'])
P = pd.Series(arcade_P['precip_mm'])
P.index = pd.to_datetime(arcade_P['dates'])

# create dates Series, index DataFrames to dates
Qdates = pd.to_datetime(arcade_Q.dates)
Pdates = pd.to_datetime(arcade_P.dates)
arcade_Q.index = pd.to_datetime(arcade_Q.dates)
arcade_P.index = pd.to_datetime(arcade_P.dates)

# create series for each year, Oct-March
# create date series for each year to match data
# Note: I was unable to plot by indexing while plotting the figure. Tried a variety of methods, and this appeared to be the only way to get both series on the same subplot with different y axes
P2008 = arcade_P[datetime(2008,10,10):datetime(2009,4,1)]
Q2008 = arcade_Q[datetime(2008,10,10):datetime(2009,4,1)]
Pdates2008 = pd.to_datetime(P2008.dates)
Qdates2008 = pd.to_datetime(Q2008.dates)

P2009 = arcade_P[datetime(2009,10,10):datetime(2010,4,1)]
Q2009 = arcade_Q[datetime(2009,10,10):datetime(2010,4,1)]
Pdates2009 = pd.to_datetime(P2009.dates)
Qdates2009 = pd.to_datetime(Q2009.dates)

P2010 = arcade_P[datetime(2010,10,10):datetime(2011,4,1)]
Q2010 = arcade_Q[datetime(2010,10,10):datetime(2011,4,1)]
Pdates2010 = pd.to_datetime(P2010.dates)
Qdates2010 = pd.to_datetime(Q2010.dates)

P2011 = arcade_P[datetime(2011,10,10):datetime(2012,4,1)]
Q2011 = arcade_Q[datetime(2011,10,10):datetime(2012,4,1)]
Pdates2011 = pd.to_datetime(P2011.dates)
Qdates2011 = pd.to_datetime(Q2011.dates)

P2012 = arcade_P[datetime(2012,10,10):datetime(2013,4,1)]
Q2012 = arcade_Q[datetime(2012,10,10):datetime(2013,4,1)]
Pdates2012 = pd.to_datetime(P2012.dates)
Qdates2012 = pd.to_datetime(Q2012.dates)

# make figure and all subplots
f1 = plt.figure()
ax2008a = f1.add_subplot(5,1,1)
ax2008b = ax2008a.twinx()
ax2008a.plot(Pdates2008,P2008.precip_mm)
ax2008b.plot(Qdates2008,Q2008.discharge_cfs,'g')
ax2008a.set_ylabel('Precip, mm', color = 'b')
ax2008b.set_ylabel('Streamflow, cfs',color = 'g')

ax2009a = f1.add_subplot(5,1,2)
ax2009b = ax2009a.twinx()
ax2009a.plot(Pdates2009,P2009.precip_mm)
ax2009b.plot(Qdates2009,Q2009.discharge_cfs,'g')
ax2009a.set_ylabel('Precip, mm', color = 'b')
ax2009b.set_ylabel('Streamflow, cfs',color = 'g')


ax2010a = f1.add_subplot(5,1,3)
ax2010b = ax2010a.twinx()
ax2010a.plot(Pdates2010,P2010.precip_mm)
ax2010b.plot(Qdates2010,Q2010.discharge_cfs,'g')
ax2010a.set_ylabel('Precip, mm', color = 'b')
ax2010b.set_ylabel('Streamflow, cfs',color = 'g')


ax2011a = f1.add_subplot(5,1,4)
ax2011b = ax2011a.twinx()
ax2011a.plot(Pdates2011,P2011.precip_mm)
ax2011b.plot(Qdates2011,Q2011.discharge_cfs,'g')
ax2011a.set_ylabel('Precip, mm', color = 'b')
ax2011b.set_ylabel('Streamflow, cfs',color = 'g')


ax2012a = f1.add_subplot(5,1,5)
ax2012b = ax2012a.twinx()
ax2012a.plot(Pdates2012,P2012.precip_mm)
ax2012b.plot(Qdates2012,Q2012.discharge_cfs,'g')
ax2012a.set_ylabel('Precip, mm', color = 'b')
ax2012b.set_ylabel('Streamflow, cfs',color = 'g')

f1.suptitle('Precipitation (CIMIS 131) and Streamflow (USGS) for Arcade Cr',size=24)

# plt.show()

# Save the plot to file
plt.tight_layout()
out_filename = 'arcade_P_Q'
out_dir = '../../results/fig/'
f1.set_size_inches(30,20)
f1.savefig(out_dir + out_filename + '.jpg')
