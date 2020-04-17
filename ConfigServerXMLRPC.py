#!/usr/bin/python3

from xmlrpc.server import SimpleXMLRPCServer # the server
import json # to load the configs

configserver_file_path = 'configserver.json'

fd = open(configserver_file_path, 'r')
data_dic = json.load(fd)

def query_dic(key):
    return data_dic[key]

server = SimpleXMLRPCServer(('localhost', data_dic['configserver']['port']))
print('configserver settings:', data_dic['configserver'])

server.register_function(query_dic, 'query_dic')
server.serve_forever()