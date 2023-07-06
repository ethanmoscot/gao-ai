import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

df = pd.read_csv('/Users/ethanmoscot/Desktop/GAO AI/gao-ai/gao_dataset_063023.csv') #Personal file path
#df.head()
#df = df.values

X = df.iloc[:,2:95] #input features (GAO criteria)
Y = df.iloc[:,95] #predict (Result column)

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
#X_scale

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size = 0.3) #val_and_test is 30% of dataset
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5) #equal split for validation and test sets

#print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape) 
#(700, 92) (150, 92) (150, 92) (700,) (150,) (150,)
#training: 700 datapoints, validation and test: 150 points
#X has 92 input features, Y only has 1

#Convert to arrays for Keras
X_train = np.asarray(X_train).astype('float32')
Y_train = np.asarray(Y_train).astype('float32')
X_val = np.asarray(X_val).astype('float32')
Y_val = np.asarray(Y_val).astype('float32')
X_test = np.asarray(X_test).astype('float32')
Y_test = np.asarray(Y_test).astype('float32')


model = Sequential([ #two hidden layers followed by output layer
    Dense(units=16, activation='relu', input_shape=(93,)),
    Dense(units=16, activation='relu'),
    Dense(units=1, activation='sigmoid')
])

#model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])

model.fit(X_train, Y_train, batch_size=16, epochs=40, validation_data=(X_val, Y_val))
model.evaluate(X_test, Y_test)[1]