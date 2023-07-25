""" 
This file generates the test dataset that is submitted via the UI. This 
dataset includes system names and data for all four principles related to
each system. This dataset does not include compliance results for any 
system. The dataset is written to /data/predict_data.csv.
"""

import random
import pandas as pd


def generate_result(j):
    if j>=50 and j<=100:
        return 1
    else:
        return 0
    
    
def generate_value(j):
    if j==3 or j==7:
        # Create all compliant values
        return random.randint(0, 100)
    else:
        return random.randint(0, 100)
    """
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
    """

# Generate governance values
governance_values = []
for j in range(0, 10):
    #for i in range(0, 10):
    dict = {}
    dict['SystemName'] = 'System_' + str(j)
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
    dict['2.1.1'] = generate_value(j)
    dict['2.1.2'] = generate_value(j) 
    dict['2.1.3'] = generate_value(j) 
    dict['2.2.1'] = generate_value(j) 
    dict['2.2.2'] = generate_value(j)
    dict['2.2.3'] = generate_value(j) 
    dict['2.3.1'] = generate_value(j)
    dict['2.3.2'] = generate_value(j) 
    dict['2.3.3'] = generate_value(j) 
    dict['2.4.1'] = generate_value(j) 
    dict['2.4.2'] = generate_value(j) 
    dict['2.4.3'] = generate_value(j) 
    dict['2.5.1'] = generate_value(j) 
    dict['2.5.2'] = generate_value(j) 
    dict['2.5.3'] = generate_value(j) 
    dict['2.6.1'] = generate_value(j)
    dict['2.6.2'] = generate_value(j) 
    dict['2.6.3'] = generate_value(j) 
    dict['2.7.1'] = generate_value(j) 
    dict['2.7.2'] = generate_value(j) 
    dict['2.7.3'] = generate_value(j) 
    dict['2.8.1'] = generate_value(j) 
    dict['2.8.2'] = generate_value(j) 
    dict['2.8.3'] = generate_value(j) 
    dict['3.1.1'] = generate_value(j)  
    dict['3.1.2'] = generate_value(j)  
    dict['3.1.3'] = generate_value(j)  
    dict['3.2.1'] = generate_value(j)  
    dict['3.2.2'] = generate_value(j)  
    dict['3.2.3'] = generate_value(j)  
    dict['3.3.1'] = generate_value(j) 
    dict['3.3.2'] = generate_value(j)  
    dict['3.3.3'] = generate_value(j)  
    dict['3.4.1'] = generate_value(j)  
    dict['3.4.2'] = generate_value(j)  
    dict['3.4.3'] = generate_value(j)  
    dict['3.5.1'] = generate_value(j)  
    dict['3.5.2'] = generate_value(j)  
    dict['3.5.3'] = generate_value(j)  
    dict['3.6.1'] = generate_value(j) 
    dict['3.6.2'] = generate_value(j)  
    dict['3.6.3'] = generate_value(j)  
    dict['3.7.1'] = generate_value(j)  
    dict['3.7.2'] = generate_value(j)  
    dict['3.7.3'] = generate_value(j)  
    dict['3.8.1'] = generate_value(j)  
    dict['3.8.2'] = generate_value(j)  
    dict['3.8.3'] = generate_value(j)  
    dict['3.9.1'] = generate_value(j) 
    dict['3.9.2'] = generate_value(j)  
    dict['3.9.3'] = generate_value(j)         
    dict['4.1.1'] = generate_value(j)  
    dict['4.1.2'] = generate_value(j) 
    dict['4.1.3'] = generate_value(j)  
    dict['4.2.1'] = generate_value(j)  
    dict['4.2.2'] = generate_value(j)  
    dict['4.2.3'] = generate_value(j)  
    dict['4.3.1'] = generate_value(j) 
    dict['4.3.2'] = generate_value(j)  
    dict['4.3.3'] = generate_value(j)  
    dict['4.4.1'] = generate_value(j)  
    dict['4.4.2'] = generate_value(j)  
    dict['4.4.3'] = generate_value(j)  
    dict['4.5.1'] = generate_value(j)  
    dict['4.5.2'] = generate_value(j)  
    dict['4.5.3'] = generate_value(j)  
    governance_values.append(dict)
        
governance_df = pd.DataFrame(governance_values)
print('Writing data/demo_data.csv')
governance_df.to_csv('data/demo_data.csv', index=False)
print('Done')


