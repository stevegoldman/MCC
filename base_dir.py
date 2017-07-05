#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:33:46 2017

@author: Steve
"""

import os

def get_base_dir():
    if os.name=='posix':
        return '/users/Steve/MCC/MCC/data/'
    
    else:
        return 'c:\\Users\\sgoldman\\MCC\\data\\'