import pandas as pd
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# processed_data_file = ""
# csv 만들고 pkl 

X = data[['pm25_concentration']]     
# 2 훈련
Y = data['pm25_concentration']


