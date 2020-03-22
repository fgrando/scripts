#!/usr/bin/python
#
# create the logger: https://docs.python.org/3/howto/logging-cookbook.html
#

# Logging levels:
# - CRITICAL
# - ERROR
# - WARNING
# - INFO
# - DEBUG
# - NOTSET


import logging

class Log():
    def __init__(self, name, file_name=None, format_str=None, level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        
        if format_str == None:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        else:
            formatter = logging.Formatter(format_str)

        self.logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
            
        self.logger.info("Log started with name: '{}' file: '{}' level: '{}'".format(name, file_name, level))

        if file_name is None:
            fh = logging.FileHandler(name+'.log')
        else:
            fh = logging.FileHandler(file_name)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)
     

    def get(self):
        return self.logger



if __name__ == '__main__':
    log = Log("example").get()
    log.debug("This is a Debug")    
    log.info("This is a Info")
    log.warning("This is an Warning")
    log.error("This is an Error")
    log.critical("This is an Critical")

    log2 = Log("example2", "example2_log", "%(name)s - %(levelname)s - %(message)s", logging.WARNING).get()
    log2.debug("This is a Debug")    
    log2.info("This is a Info")
    log2.warning("This is an Warning")
    log2.error("This is an Error")
    log2.critical("This is an Critical")
    
