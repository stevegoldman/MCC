#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:12:29 2017

@author: Steve
"""



import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


class ItemSelector(BaseEstimator, TransformerMixin):
# Author: Matt Terry <matt.terry@gmail.com>
#
# License: BSD 3 clause
    """For data grouped by feature, select subset of data at a provided key.

    The data is expected to be stored in a 2D data structure, where the first
    index is over features and the second is over samples.  i.e.

    >> len(data[key]) == n_samples

    Please note that this is the opposite convention to scikit-learn feature
    matrixes (where the first index corresponds to sample).

    ItemSelector only requires that the collection implement getitem
    (data[key]).  Examples include: a dict of lists, 2D numpy array, Pandas
    DataFrame, numpy record array, etc.

    >> data = {'a': [1, 5, 2, 5, 2, 8],
               'b': [9, 4, 1, 4, 1, 3]}
    >> ds = ItemSelector(key='a')
    >> data['a'] == ds.transform(data)

    ItemSelector is not designed to handle data grouped by sample.  (e.g. a
    list of dicts).  If your data is structured this way, consider a
    transformer along the lines of `sklearn.feature_extraction.DictVectorizer`.

    Parameters
    ----------
    key : hashable, required
        The key corresponding to the desired value in a mappable.
    """
    def __init__(self, key):
        self.key = key

    def fit(self, x, y=None):
        return self

    def transform(self, data_dict):
        return data_dict[self.key]


class EPAText(BaseEstimator, TransformerMixin):
    """Vectorize EPA codes, replace empty list with NONE"""

    
    def __init__(self):
        self.code_vec=CountVectorizer()

    
    def fit(self, epaCodes, y=None):
        ecs=[]
        for ec in epaCodes:
            if ec is np.nan:
                ecs.append('NONE')
            else:
                ecs.append(ec)
        self.code_vec.fit(ecs)            
        return self

    def transform(self, epaCodes):
        ecs=[]
        for ec in epaCodes:
            if ec is np.nan:
                ecs.append('NONE')
            else:
                ecs.append(ec)
        
        return self.code_vec.transform(ecs)