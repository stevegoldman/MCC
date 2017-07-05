# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 13:36:17 2017

@author: sgoldman
"""
import base_dir as bd
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
from collections import defaultdict


base_dir=bd.get_base_dir()

rec_splits=[0,40,80,87,138,178,218]


def get_composition_records():

    lines=[]
    with open(base_dir+'Profile_Composition_6-29-2017.txt','r') as f:
        for line in f.readlines():
            fields=[]
            for idx in range(len(rec_splits)-1):
                fields.append(line[rec_splits[idx]:rec_splits[idx+1]].strip())
            fields.append(line[rec_splits[-1]:].strip())
            lines.append(fields[:])
    return lines        