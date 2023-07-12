import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

#df = pd.read_csv('/Users/ethanmoscot/Desktop/GAO AI/gao-ai/gao_governance.csv') #Personal file path
""" Simplified path since data in same directory. """
df = pd.read_csv('gao_governance.csv') #Personal file path

#df.head()
#df = df.values

X = df.iloc[:,1:28] #input features (GAO governance criteria)
#df.iloc[:,1:28]
Y = df['Compliance Status'].apply(lambda x: 1 if x=='Compliant' else 0)

""" Use random_state=42 if needed. """
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size = 0.3) #val_and_test is 30% of dataset
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5) #equal split for validation and test sets


#print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape) 
#(700, 27) (150, 27) (150, 27) (700,) (150,) (150,)
#training: 700 datapoints, validation and test: 150 points
#X has 150 input features, Y only has 1 (i.e., the results)

model = Sequential([ #two hidden layers followed by output layer
    Dense(units=32, activation='relu', input_shape=(27,)),
    Dense(units=64, activation='relu'),
    Dense(units=1, activation='sigmoid')
])

"""
# Some recommend using a single hidden layer where the number of nodes (units) is 
# equal to sqrt(num_input_nodes * num_output_nodes).
model = Sequential([ #one hidden layers followed by output layer
    Dense(units=6, activation='relu', input_shape=(27,)),
    Dense(units=1, activation='sigmoid')
])
"""

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
#Fit model

"""
# A rule of thumb for num_epochs is 3 times the number of input nodes (3*27=81). If the model 
# stopped improving accuracy before then, reduce num epochs. If the accuracy is still improving 
# after this, increase epochs.
"""
hist = model.fit(X_train, Y_train, batch_size=32, epochs=3, validation_split=0.1, validation_data=(X_val, Y_val))
#Evaluate on training and test data
print(model.evaluate(X_train, Y_train)[1])
print(model.evaluate(X_test, Y_test)[1])

"""
# Test predictions on the test data set.
"""
y_pred = model.predict(X_test) 
T = 0.5
y_pred_bool = y_pred >= T
print(f'----------------------\nPrediction:\n{y_pred_bool}')


"""
# Test predictions on arbitrary example data.
"""
headers = list(df.columns.values)
headers.remove('SystemName')
headers.remove('Result')
headers.remove('Compliance Status')
#print(f'headers: {headers}')

example_data = [99,	99,	99,	84,	97,
                91,	99,	86,	97,	87,	
                82,	97,	84,	81,	90,
                86,	89,	83,	88,	86,
                87,	92,	88,	90,	98,	
                99,	87]
# Don't forget to transform the data from a column to a row.
df2 = pd.DataFrame(example_data).T
#print(df2)

# Predict
y_pred = model.predict(df2) 
T = 0.5
y_pred_bool = y_pred >= T
result = 'Compliant' if y_pred >= T else 'Not Compliant'
print(f'----------------------\nExample Prediction:\n{result}')
