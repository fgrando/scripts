#!/usr/bin/python3

import requests as rs   # to get the url
from io import StringIO # to parse the downloaded CSV
import csv              # csv parser

class ConfigClientGSHEET:
    
    def __init__(self, gsheet_key):
        """ The gsheet_key is like '1mwt-yufbmw5FCXKpieoEyFlG8NedZ1Ri_5dClDl7eog' """
        self.gsheet_key = gsheet_key
        self.data_dic = self.build_dic(key)
        

    def build_dic(self, sheet_key):
        CSV_URL_TEMPLATE='https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet='
        csv_url = CSV_URL_TEMPLATE.format(sheet_key)
        res = rs.get(url=csv_url)
        csv_text = res.content.decode('utf-8', 'ignore')

        sep = ','
        fs = StringIO(csv_text)
        reader = csv.reader(fs, delimiter=sep)

        configs = {}
        for row in reader:
            key = row[0].strip()
            value = row[1].strip()

            try:
                configs[key]=float(value)
            except:
                configs[key]=value
                pass

        print(configs)
        return configs


    def get(self, param, debug=False):
        status = False
        result = None

        try:
            result = self.data_dic[param]
            status = True

        except Exception as e:
            # it the debug is enabled, the error can be returned
            if debug:
                result = str(e)
            pass

        # allow feedback 
        if debug:
            return (status, result)

        return result

