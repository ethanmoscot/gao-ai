import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten

df = pd.read_csv('/Users/ethanmoscot/Desktop/GAO AI/gao-ai/gao_dataset_063023.csv') #File path
#df.head()
data = df.values
#data

X = data[:,2:94] #input features (GAO criteria)
Y = data[:,95] #predict (Result column)

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
#X_scale

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size = 0.3) #70/30 split
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5)

#Convert numPy array to tensor
X_train = np.asarray(X_train).astype(np.float32)
Y_train = np.asarray(Y_train).astype(np.float32)

#print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape) 
#(700, 92) (150, 92) (150, 92) (700,) (150,) (150,)


model = Sequential([ #two hidden layers followed by output layer
    #Flatten(input_shape=(None, 92)),
    Dense(units=4, activation='relu'),
    Dense(units=4, activation='relu'),
    Dense(units=1, activation='sigmoid')
])

#TODO: confirm metrics
#model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

#model.fit(X_train, Y_train, batch_size=32, epochs=50, validation_data=(X_val, Y_val))
#model.evaluate(X_test, Y_test)[1]