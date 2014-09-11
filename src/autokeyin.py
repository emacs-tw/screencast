#!/bin/env python

import sys
import os
import time
import config

def transform(string):
    if "\"" in string:
        return ['type'] + ['\"' + char + '\"' for char in string.replace('\"', '')]
    else:
        wdict = {'M-':'Alt+',
                 'C-':'Ctrl+',
                 'S-':'Shift+'}
        for key in wdict:
            string = string.replace(key, wdict[key])
        return ['key'] + string.split(' ')

with open(sys.argv[1], 'r') as command:
    os.system('mkdir ' + sys.argv[2])
    for index,line in enumerate(command):
        key = transform(line.replace('\n', ''))
        func = key[0]
        operate = key[1:]
        print(key)
        for single in operate:
            os.system("xdotool " + func + " " + single)
            time.sleep(config.pause)
        os.system('scrot ' + sys.argv[2] + '/' + 
                  'screen_' + str(index) + '00.png')
