#!/usr/bin/python

'''
Program to transform Palo Alto firewall blocklist 
Removes data that has not been normalized
Removes duplicate IP Addresses and duplicate line entries
Purges old IP entries from the blocklist
'''

__author__    = 'Donald Whitfield'
__copyright__ = '(c) Skyline Technology Solutions'
__email__     = 'donald.whitfield@maryland.gov'
__satus__     = 'Production Version'

import numpy as np
import pandas as pd
from datetime import date
import datetime

blocklist = pd.read_csv("blocklist.txt", sep='\s+', header = None)

pd.set_option("display.max_rows", None, "display.max_columns", None) 
pd.set_option('display.width', None, 'display.max_colwidth', None)

blocklist.columns = ['IPADDR', 'INCIDENT', 'DATE']
blocklist.dropna(how='any', thresh=None, inplace=True)

cleaned = blocklist.drop_duplicates().drop_duplicates(subset='IPADDR')
np.savetxt('ip_blocklist.txt', cleaned.values, fmt='%s')

cleaned_rows = cleaned.shape[0]
print(cleaned_rows, " Rows of Data Printed", "\n")

print(cleaned)


### Filter by DATE ###
### Note: Not implementing at this time

### cleaned['DATE'] = pd.to_datetime(cleaned['DATE'])
### cleaned[cleaned['DATE'] < pd.Timestamp(date(2020,12,1))]
