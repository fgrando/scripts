#!/usr/bin/python3

import requests as rs
CSV_TEMPLATE='https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet='


# Add your spreadsheet here (shared option - anyone with the link can read):
key = '1mwt-yufbmw5FCXKpieoEyFlG8NedZ1Ri_5dClDl7esd' # control/control sheet

csv_url = CSV_TEMPLATE.format(key)
res=rs.get(url=csv_url)

fd = open('/home/fgrando/Downloads/scripts/bitcoin_rate2/google.csv', 'wb')
fd.write(res.content)
fd.close()

