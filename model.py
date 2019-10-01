#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:47:38 2019

@author: Zhongjiu Lu
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

### multi-label classification problem

# 1. read the file into working directory without a header row
train = pd.read_csv("train.csv", header=None)
test = pd.read_csv("test.csv", header=None)

# 2. data preparation
# train features and response feature
Y_train = train.iloc[ :, 294:300].values.tolist()
X_train = train.iloc[ :, :294].values
test = test.values

# reshape the array into image format, assume to be 21*14, and grey background

row = 21
col = 14
X_train_reshape = X_train.reshape(train.shape[0], row, col, 1)
test_reshape = test.reshape(test.shape[0], row, col, 1)

# train & test split
X_train, X_val, y_train, y_val = train_test_split(X_train_reshape, 
                                                    Y_train,
                                                  # 10% of the test set
                                                    test_size=0.1,
                                                  # seed to ensure reproduction
                                                    random_state=42
                                                   )


