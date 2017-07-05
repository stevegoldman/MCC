# -*- coding: utf-8 -*-
"""
Created on Sat Jul 01 13:10:12 2017

@author: sgoldman

"""
import base_dir as bd
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
from collections import defaultdict


base_dir=bd.get_base_dir()


def load_raw_profile_data():
    df_raw_profiles=pd.read_csv(base_dir+'Profile_Data_6-29-2017.txt',sep='|')
    return df_raw_profiles

def get_labeled_profiles(df):
    df_lab=df
    for bad_lab in ('    ','LIL ','W002'):
        df_lab=df_lab.loc[~(df_lab['Matl Category Code']==bad_lab)]
    df_lab=df_lab.loc[~(df_lab['Matl Category Code'].isnull())]
    return df_lab

def make_train_test_data(df):
    
    X=df#['Composition']
    y=np.c_[df['Matl Category Code']].reshape((-1,))
    #y=np.array([x[:2]for x in y])
    X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=0.2,
                                                    random_state=42)
    
    return {'X_train':X_train,
            'y_train':y_train,
            'X_test':X_test,
            'y_test':y_test}    
    
