""" 
This file generates the test dataset that is submitted via the UI. This 
dataset includes system names and data for all four principles related to
each system. This dataset does not include compliance results for any 
system. The dataset is written to /data/predict_data.csv.
"""

import random
import pandas as pd
    
    
def generate_values(row_num, num_cols):
    values = []
    for i in range(0, num_cols):
        if row_num % 2 == 0:
            # NOTE: that the average needed to be compliant is >= 70.
            #print(f'row_num: {row_num}')
            r = random.randint(50, 100)
            values.append(r)
        else:
            r = random.randint(0, 100)
            values.append(r)
    
    avg = sum(values) / len(values)
    compliant = 1 if avg >= 70 else 0
    return values, avg, compliant


n = 10

# Generate governance values
row_values = []
for i in range(0, n):
    dict = {}
    dict['SystemName'] = 'System-' + str(i)
    values, avg, compliant = generate_values(i, 93)
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
    
    dict['2.1.1'] = values[27]
    dict['2.1.2'] = values[28] 
    dict['2.1.3'] = values[29]
    dict['2.2.1'] = values[30] 
    dict['2.2.2'] = values[31]
    dict['2.2.3'] = values[32] 
    dict['2.3.1'] = values[33]
    dict['2.3.2'] = values[34] 
    dict['2.3.3'] = values[35]
    dict['2.4.1'] = values[36]
    dict['2.4.2'] = values[37] 
    dict['2.4.3'] = values[38]
    dict['2.5.1'] = values[39] 
    dict['2.5.2'] = values[40] 
    dict['2.5.3'] = values[41] 
    dict['2.6.1'] = values[42]
    dict['2.6.2'] = values[43] 
    dict['2.6.3'] = values[44] 
    dict['2.7.1'] = values[45] 
    dict['2.7.2'] = values[46] 
    dict['2.7.3'] = values[47]
    dict['2.8.1'] = values[48] 
    dict['2.8.2'] = values[49] 
    dict['2.8.3'] = values[50] 
    
    dict['3.1.1'] = values[51]  
    dict['3.1.2'] = values[52]  
    dict['3.1.3'] = values[53]  
    dict['3.2.1'] = values[54]  
    dict['3.2.2'] = values[55]  
    dict['3.2.3'] = values[56]  
    dict['3.3.1'] = values[57] 
    dict['3.3.2'] = values[58]  
    dict['3.3.3'] = values[59]  
    dict['3.4.1'] = values[60]  
    dict['3.4.2'] = values[61]  
    dict['3.4.3'] = values[62]  
    dict['3.5.1'] = values[63]  
    dict['3.5.2'] = values[64]  
    dict['3.5.3'] = values[65]  
    dict['3.6.1'] = values[66] 
    dict['3.6.2'] = values[67]  
    dict['3.6.3'] = values[68]  
    dict['3.7.1'] = values[69]  
    dict['3.7.2'] = values[70]  
    dict['3.7.3'] = values[71]  
    dict['3.8.1'] = values[72]  
    dict['3.8.2'] = values[73]  
    dict['3.8.3'] = values[74]  
    dict['3.9.1'] = values[75] 
    dict['3.9.2'] = values[76]  
    dict['3.9.3'] = values[77] 
    
    dict['4.1.1'] = values[78] 
    dict['4.1.2'] = values[79] 
    dict['4.1.3'] = values[80] 
    dict['4.2.1'] = values[81]  
    dict['4.2.2'] = values[82]  
    dict['4.2.3'] = values[83]  
    dict['4.3.1'] = values[84] 
    dict['4.3.2'] = values[85]  
    dict['4.3.3'] = values[86]  
    dict['4.4.1'] = values[87]  
    dict['4.4.2'] = values[88] 
    dict['4.4.3'] = values[89]  
    dict['4.5.1'] = values[90]  
    dict['4.5.2'] = values[91]  
    dict['4.5.3'] = values[92] 
    
    row_values.append(dict)
        
df = pd.DataFrame(row_values)
print(f'Writing data/demo_data.csv')
df.to_csv('data/demo_data.csv', index=False)



print('Done')

