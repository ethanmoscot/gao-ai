""" 
This file generates datasets for each of the four GAO compliance areas. 
These datasets are specifically developed to reflect an even distribution of the data.
"""

import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

governance_headers = ['SystemName', '1.1.1', '1.1.2', '1.1.3', '1.2.1', '1.2.2', '1.2.3', '1.3.1',
                    '1.3.2', '1.3.3', '1.4.1', '1.4.2', '1.4.3', '1.5.1', '1.5.2', '1.5.3', '1.6.1',
                    '1.6.2', '1.6.3', '1.7.1', '1.7.2', '1.7.3', '1.8.1', '1.8.2', '1.8.3', '1.9.1',
                    '1.9.2', '1.9.3', 'Result']
data_headers = ['SystemName', '2.1.1', '2.1.2', '2.1.3', '2.2.1', '2.2.2', '2.2.3', '2.3.1',
                    '2.3.2', '2.3.3', '2.4.1', '2.4.2', '2.4.3', '2.5.1', '2.5.2', '2.5.3', '2.6.1',
                    '2.6.2', '2.6.3', '2.7.1', '2.7.2', '2.7.3', '2.8.1', '2.8.2', '2.8.3', 'Result']

performance_headers = ['SystemName', '3.1.1', '3.1.2', '3.1.3', '3.2.1', '3.2.2', '3.2.3', '3.3.1',
                       '3.3.2', '3.3.3', '3.4.1', '3.4.2', '3.4.3', '3.5.1', '3.5.2', '3.5.3', '3.6.1',
                       '3.6.2', '3.6.3', '3.7.1', '3.7.2', '3.7.3', '3.8.1', '3.8.2', '3.8.3', '3.9.1',
                       '3.9.2', '3.9.3', 'Result']

monitoring_headers = ['SystemName', '4.1.1', '4.1.2', '4.1.3', '4.2.1', '4.2.2', '4.2.3', '4.3.1',
                      '4.3.2', '4.3.3', '4.4.1', '4.4.2', '4.4.3', '4.5.1', '4.5.2', '4.5.3', 'Result']


def generate_result(j):
    if j>=70 and j<=100:
        return 1
    else:
        return 0
    
    
def generate_value(j):
    if j>=0 and j<=9:
        return random.randint(0, 9)
    elif j>=10 and j<=19:
        return random.randint(10, 19)
    elif j>=20 and j<=29:
        return random.randint(20, 29)
    elif j>=30 and j<=39:
        return random.randint(30, 39)
    elif j>=40 and j<=49:
        return random.randint(40, 49)
    elif j>=50 and j<=59:
        return random.randint(50, 59)
    elif j>=60 and j<=69:
        return random.randint(60, 69)
    elif j>=70 and j<=79:
        return random.randint(70, 79)
    elif j>=80 and j<=89:
        return random.randint(80, 89)
    elif j>=90 and j<=100:
        return random.randint(90, 100)
    

# Generate governance values
governance_values = []
for j in range(0, 100):
    print(f'j: {j}')
    for i in range(0, 10):
        dict = {}
        dict['SystemName'] = 'System-' + str(j) + '_' + str(i)
        dict['1.1.1'] = generate_value(j)
        dict['1.1.2'] = generate_value(j)
        dict['1.1.3'] = generate_value(j)
        dict['1.2.1'] = generate_value(j)
        dict['1.2.2'] = generate_value(j)
        dict['1.2.3'] = generate_value(j)
        dict['1.3.1'] = generate_value(j)
        dict['1.3.2'] = generate_value(j)
        dict['1.3.3'] = generate_value(j)
        dict['1.4.1'] = generate_value(j)
        dict['1.4.2'] = generate_value(j)
        dict['1.4.3'] = generate_value(j)
        dict['1.5.1'] = generate_value(j)
        dict['1.5.2'] = generate_value(j)
        dict['1.5.3'] = generate_value(j)
        dict['1.6.1'] = generate_value(j)
        dict['1.6.2'] = generate_value(j)
        dict['1.6.3'] = generate_value(j)
        dict['1.7.1'] = generate_value(j)
        dict['1.7.2'] = generate_value(j)
        dict['1.7.3'] = generate_value(j)
        dict['1.8.1'] = generate_value(j)
        dict['1.8.2'] = generate_value(j)
        dict['1.8.3'] = generate_value(j)
        dict['1.9.1'] = generate_value(j)
        dict['1.9.2'] = generate_value(j)
        dict['1.9.3'] = generate_value(j)
        dict['Result'] = generate_result(j)
        governance_values.append(dict)
        
governance_df = pd.DataFrame(governance_values)
governance_df.to_csv('governance_training_2.csv')


# Generate data values


# Generate performance values


# Generate monitoring values


