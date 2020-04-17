#!/usr/bin/python3

import xmlrpc.client

class ConfigClientXMLRPC:
    
    def __init__(self, server_url):
        """ The server_url should be like 'http://localhost:8000/' """
        self.proxy = xmlrpc.client.ServerProxy(server_url)

    def get(self,param, debug=False):
        status = False
        result = None

        try:
            result = self.proxy.query_dic(param)
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
