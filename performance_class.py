import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

class PerformanceModel:

    def __init__(self):
        # During initialization, train the model
        self.df = pd.read_csv('gao_performance.csv')

        X = self.df.iloc[:,1:29] #input features (GAO performance criteria)
        Y = self.df['Compliance Status'].apply(lambda x: 1 if x=='Compliant' else 0)

        """ Use random_state=42 if needed. """
        X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size = 0.3) #val_and_test is 30% of dataset
        X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5) #equal split for validation and test sets

        # Some recommend using a single hidden layer where the number of nodes (units) is 
        # equal to sqrt(num_input_nodes * num_output_nodes).
        self.model = Sequential([ #two hidden layers followed by output layer
            Dense(units=32, activation='relu', input_shape=(28,)),
            Dense(units=64, activation='relu'),
            Dense(units=1, activation='sigmoid')
        ])

        self.model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')

        """
        # A rule of thumb for num_epochs is 3 times the number of input nodes (3*28=84). If the model 
        # stopped improving accuracy before then, reduce num epochs. If the accuracy is still improving 
        # after this, increase epochs.
        """
        hist = self.model.fit(X_train, Y_train, batch_size=32, epochs=3, validation_split=0.1, validation_data=(X_val, Y_val))
        #Evaluate on training and test data
        #print(self.model.evaluate(X_train, Y_train)[1])
        #print(self.model.evaluate(X_test, Y_test)[1])
        print('PerformanceModel ready.')


    def predict(self, data):
        """
        # Test predictions on arbitrary example data.
        """
        headers = list(self.df.columns.values)
        headers.remove('SystemName')
        headers.remove('Result')
        headers.remove('Compliance Status')
        #print(f'headers: {headers}')

        #28 sample inputs
        example_data = [99,	99,	99,	84,	97,
                        91,	99,	86,	97,	87,	
                        82,	97,	84,	81,	90,
                        86,	89,	83,	88,	86,
                        87,	92,	88,	90,	98,	
                        99,	87, 84]
        # Don't forget to transpose the data from a column to a row.
        df2 = pd.DataFrame(data).T
        #print(df2)

        # Predict
        y_pred = self.model.predict(df2) 
        print(f'y_pred: {y_pred}')
        T = 0.5
        y_pred_bool = y_pred >= T
        result = 'Compliant' if y_pred >= T else 'Not Compliant'
        print(f'----------------------\nExample Prediction:\n{result}')
        return int(y_pred * 100)