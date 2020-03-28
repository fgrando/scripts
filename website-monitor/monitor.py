#!/usr/bin/python3

import json                                 # parse the config file
from urllib.request import urlopen, Request # request the website page
import re                                   # parse the webpage with regular expressions
import time                                 # do the sleep for refresh interval
from log import *                           # logging mechanism
from EmailSender import *                   # email client

# Monitoring configs
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
email_settings = 'settings.json'
website = 'https://www.horariodebrasilia.org/'
refresh_interval_seconds = 60
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def parse(txt):
    regex_to_get_hour = "(?<=\<p id\=\"relogio\"\>)[\d]+\:[\d]+\:[\d]+(?=\</p\>)"
    findings = re.findall(regex_to_get_hour, txt.decode(
        'utf-8', errors='ignore'), re.DOTALL)
    if len(findings) > 0:
        # the first finding is enough for this example
        return findings[0]

    return None


# load configurations
fd = open(email_settings, 'r')
configs = json.load(fd)

# create the logger and sender
log = Log("monitor").get()
sender = EmailSender(configs['smtp'], configs['port'],
                     configs['email'], configs['password'], log)


previous = None
while True:
    fake_browser_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=website, headers=fake_browser_headers)
    contents = urlopen(req).read()

    result = parse(contents)

    msg = "Time now [{}]".format(result)
    subject = "WEBSITE MONITOR"

    if result != previous:
        log.info("Data changed: [{}]".format(result))
        ok = sender.send(configs['recipients'], subject, msg)
        if not ok:
            log.error("Failed to send email to [{}]".format(
                configs['recipients']))
        else:
            log.info("Email sent.")

    # update the memory...
    previous = result

    # be nice and sleep
    time.sleep(refresh_interval_seconds)
