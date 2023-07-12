import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

df = pd.read_csv('/Users/ethanmoscot/Desktop/GAO AI/gao-ai/gao_monitoring.csv') #Personal file path
#df.head()
#df = df.values

X = df.iloc[:,1:17] #input features (GAO monitoring criteria)
Y = df['Compliance Status'].apply(lambda x: 1 if x=='Compliant' else 0)

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size = 0.3) #val_and_test is 30% of dataset
#random_state = 42
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5) #equal split for validation and test sets

#print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape) 
#(700, 16) (150, 16) (150, 16) (700,) (150,) (150,)
#training: 700 datapoints, validation and test: 150 points
#X has 150 input features, Y only has 1 (i.e., the results)

model = Sequential([ #hidden layer followed by output layer
    Dense(units=6, activation='relu', input_shape=(16,)),
    Dense(units=1, activation='sigmoid')
])

#Fit model
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
#num_epochs = 3 * 16 (input nodes)
hist = model.fit(X_train, Y_train, batch_size=32, epochs=48, validation_split=0.1, validation_data=(X_val, Y_val))
#Evaluate on training and test data
print(model.evaluate(X_train, Y_train)[1])
print(model.evaluate(X_test, Y_test)[1])

"""
y_pred = model.predict(X_test)
T = 0.5
y_pred_bool = y_pred >= T
print(Y_pred_bool)

#Test case for compliant example
headers = list(df.columns.values)
headers.remove('SystemName')
headers.remove('Result')
headers.remove('Compliance Status')
print(f'headers: {headers}')
"""