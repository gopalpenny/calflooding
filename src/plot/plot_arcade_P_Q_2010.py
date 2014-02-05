
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


dformat = '../../data/format/'
dformat = 'data/format/'
fname = 'arcade_Q_11447360_2008_2013_format.csv'

arcade_Q = pd.read_csv(dformat + fname)

arcade_Q_dt = datetime(arcade_Q[['yr','mo','day','hr','min','sec']])

arcade_Q_dt = datetime(arcade_Q['yr'],arcade_Q['mo',arcade_Q['day'],arcade_Q['hr'],arcade_Q['min'],['sec'])


arcae_Q_dt = arcade_Q.integer[['yr','mo','day','hr','min','sec']]

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)

arcae_Q_dt[1:4]

plt.plot()

year = 



arcade_Q2 = pd.DataFrame(arcade_Q)

print arcade_Q2[1:4]

abc = arcade_Q['yr']
abc[1] = 200