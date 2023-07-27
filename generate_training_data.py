""" 
This file generates training/test/validation datasets for each of the four GAO compliance areas. 
These datasets are specifically developed to reflect an even distribution of the data. The 
four datasets are written to /data as CSV files.
"""

import random
import pandas as pd
    
    
def generate_values(row_num, num_cols):
    values = []
    for i in range(0, num_cols):
        if row_num % 5 == 0:
            #print(f'row_num: {row_num}')
            r = random.randint(70, 100)
            values.append(r)
        else:
            r = random.randint(0, 100)
            values.append(r)
    
    avg = sum(values) / len(values)
    compliant = 1 if avg >= 70 else 0
    return values, avg, compliant


n = 100000

# Generate governance values
governance_values = []
for i in range(0, n):
    dict = {}
    dict['SystemName'] = 'System-' + str(i)
    values, avg, compliant = generate_values(i, 27)
    dict['1.1.1'] = values[0]
    dict['1.1.2'] = values[1]
    dict['1.1.3'] = values[2]
    dict['1.2.1'] = values[3]
    dict['1.2.2'] = values[4]
    dict['1.2.3'] = values[5]
    dict['1.3.1'] = values[6]
    dict['1.3.2'] = values[7]
    dict['1.3.3'] = values[8]
    dict['1.4.1'] = values[9]
    dict['1.4.2'] = values[10]
    dict['1.4.3'] = values[11]
    dict['1.5.1'] = values[12]
    dict['1.5.2'] = values[13]
    dict['1.5.3'] = values[14]
    dict['1.6.1'] = values[15]
    dict['1.6.2'] = values[16]
    dict['1.6.3'] = values[17]
    dict['1.7.1'] = values[18]
    dict['1.7.2'] = values[19]
    dict['1.7.3'] = values[20]
    dict['1.8.1'] = values[21]
    dict['1.8.2'] = values[22]
    dict['1.8.3'] = values[23]
    dict['1.9.1'] = values[24]
    dict['1.9.2'] = values[25]
    dict['1.9.3'] = values[26]
    
    dict['Result'] = compliant
    governance_values.append(dict)
        
governance_df = pd.DataFrame(governance_values)
print(f'Writing data/governance_training.csv')
governance_df.to_csv('data/governance_training.csv', index=False)


# Generate data values
data_values = []
for i in range(0, n):
    dict = {}
    dict['SystemName'] = 'System-' + str(i)
    values, avg, compliant = generate_values(i, 24)
    dict['2.1.1'] = values[0]
    dict['2.1.2'] = values[1] 
    dict['2.1.3'] = values[2]
    dict['2.2.1'] = values[3] 
    dict['2.2.2'] = values[4]
    dict['2.2.3'] = values[5] 
    dict['2.3.1'] = values[6]
    dict['2.3.2'] = values[7] 
    dict['2.3.3'] = values[8]
    dict['2.4.1'] = values[9]
    dict['2.4.2'] = values[10] 
    dict['2.4.3'] = values[11]
    dict['2.5.1'] = values[12] 
    dict['2.5.2'] = values[13] 
    dict['2.5.3'] = values[14] 
    dict['2.6.1'] = values[15]
    dict['2.6.2'] = values[16] 
    dict['2.6.3'] = values[17] 
    dict['2.7.1'] = values[18] 
    dict['2.7.2'] = values[19] 
    dict['2.7.3'] = values[20]
    dict['2.8.1'] = values[21] 
    dict['2.8.2'] = values[22] 
    dict['2.8.3'] = values[23] 
    dict['Result'] = compliant
    data_values.append(dict)
        
data_df = pd.DataFrame(data_values)
print(f'Writing data/data_training.csv')
data_df.to_csv('data/data_training.csv', index=False)


# Generate performance values
performance_values = []
for i in range(0, n):
        dict = {}
        dict['SystemName'] = 'System-' + str(i)
        values, avg, compliant = generate_values(i, 27)
        dict['3.1.1'] = values[0]  
        dict['3.1.2'] = values[1]  
        dict['3.1.3'] = values[2]  
        dict['3.2.1'] = values[3]  
        dict['3.2.2'] = values[4]  
        dict['3.2.3'] = values[5]  
        dict['3.3.1'] = values[6] 
        dict['3.3.2'] = values[7]  
        dict['3.3.3'] = values[8]  
        dict['3.4.1'] = values[9]  
        dict['3.4.2'] = values[10]  
        dict['3.4.3'] = values[11]  
        dict['3.5.1'] = values[12]  
        dict['3.5.2'] = values[13]  
        dict['3.5.3'] = values[14]  
        dict['3.6.1'] = values[15] 
        dict['3.6.2'] = values[16]  
        dict['3.6.3'] = values[17]  
        dict['3.7.1'] = values[18]  
        dict['3.7.2'] = values[19]  
        dict['3.7.3'] = values[20]  
        dict['3.8.1'] = values[21]  
        dict['3.8.2'] = values[22]  
        dict['3.8.3'] = values[23]  
        dict['3.9.1'] = values[24] 
        dict['3.9.2'] = values[25]  
        dict['3.9.3'] = values[26]  
        dict['Result'] = compliant
        performance_values.append(dict)
        
performance_df = pd.DataFrame(performance_values)
print(f'Writing data/performance_training.csv')
performance_df.to_csv('data/performance_training.csv', index=False)


# Generate monitoring values
monitor_values = []
for i in range(0, n):
        dict = {}
        dict['SystemName'] = 'System-' + str(i)
        values, avg, compliant = generate_values(i, 15)
        dict['4.1.1'] = values[0] 
        dict['4.1.2'] = values[1] 
        dict['4.1.3'] = values[2] 
        dict['4.2.1'] = values[3]  
        dict['4.2.2'] = values[4]  
        dict['4.2.3'] = values[5]  
        dict['4.3.1'] = values[6] 
        dict['4.3.2'] = values[7]  
        dict['4.3.3'] = values[8]  
        dict['4.4.1'] = values[9]  
        dict['4.4.2'] = values[10] 
        dict['4.4.3'] = values[11]  
        dict['4.5.1'] = values[12]  
        dict['4.5.2'] = values[13]  
        dict['4.5.3'] = values[14]  
        dict['Result'] = compliant 
        monitor_values.append(dict)
        
monitor_df = pd.DataFrame(monitor_values)
print(f'Writing data/monitor_training.csv')
monitor_df.to_csv('data/monitor_training.csv', index=False)

print('Done')

