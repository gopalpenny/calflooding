
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


dirformat = '../../data/format/'
Q_filename = 'arcade_Q_11447360_2008_2013.csv'
P_filename = 'arcade_P_CIMIS_2008_2013.csv'

arcade_Q = pd.read_csv(dirformat + Q_filename)
arcade_P = pd.read_csv(dirformat + P_filename)

Qdates = pd.to_datetime(arcade_Q.dates)
Pdates = pd.to_datetime(arcade_P.dates)

#arcade_P_in = pd.read_csv(dirformat + P_filename, index_col=0, names=['dates','precip_in'], header=None)

f1 = plt.figure()
ax1 = f1.add_subplot(2,1,1)
ax1.plot(Pdates,arcade_P.precip_mm)
ax1.plot(Qdates,arcade_Q.discharge_cfs)

out_filename = 'arcade_P_Q'
out_dir = '../../results/fig/'
f1.set_size_inches(20,8)
f1.savefig(out_dir + out_filename + '.jpg')
