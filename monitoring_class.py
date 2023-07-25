import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

class MonitoringModel:

    def __init__(self):
        # During initialization, train the model
        self.df = pd.read_csv('data/monitor_training.csv')

        X = self.df.iloc[:,1:16] #input features (GAO monitoring criteria)
        print(X)
        Y = self.df['Result'] # Results column

        done = False
        while not done:
            
            """ Use random_state=42 if needed. """
            X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size = 0.3) #val_and_test is 30% of dataset
            X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5) #equal split for validation and test sets

            # Some recommend using a single hidden layer where the number of nodes (units) is 
            # equal to sqrt(num_input_nodes * num_output_nodes).
            self.model = Sequential([ #two hidden layers followed by output layer
                Dense(units=32, activation='relu', input_shape=(15,)),
                Dense(units=64, activation='relu'),
                Dense(units=1, activation='sigmoid')
            ])
            self.model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')

            """
            A rule of thumb for num_epochs is 3 times the number of input nodes. If the model 
            stops improving accuracy, then reduce num epochs. If the accuracy is still improving 
            # after this, increase epochs.
            """
            # Use verbose=0 to hide epoch values
            hist = self.model.fit(X_train, Y_train, verbose=0, batch_size=32, epochs=81, validation_split=0.1, validation_data=(X_val, Y_val))
            #print(hist.history.keys())
            accuracy_list = hist.history['accuracy']
            #print(f"Accuracy: {accuracy_list}")
            if accuracy_list[-1] > 0.80:
                done = True
            
        accuracy_list = hist.history['accuracy']

        plt.plot(hist.history['accuracy'])
        plt.plot(hist.history['val_accuracy'])
        plt.title('Monitoring Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')
        plt.savefig('monitoring_accuracy.png', bbox_inches='tight')
        plt.clf()
        print(f"DONE Monitoring Accuracy: {accuracy_list[-1]}")


    def predict(self, data):
        # data contains 16 input values

        # Test predictions on arbitrary example data
        headers = list(self.df.columns.values)
        headers.remove('SystemName')
        #headers.remove('Result')
        #headers.remove('Compliance Status')
        #print(f'headers: {headers}')

        # Transpose the data from a column to a row.
        df2 = pd.DataFrame(data).T
        #print(df2)

        # Predict
        print(f'\n*******************************************')
        y_pred = self.model.predict(df2) 
        print(f'y_pred: {y_pred}')
        T = 0.5
        y_pred_bool = y_pred >= T
        result = 1 if y_pred >= T else 0
        print(f'----------------------\nMonitoring Prediction:\n{result}')
        return int(y_pred * 100)

    
# This file can be called directly using: python monitoring_class.py
if __name__ == "__main__":
    monitoring_model = MonitoringModel()
    
    """
    For testing, use values '0..9', '10..19', ..., '70..79', '80..89', '90..100'
    Values 70..100 should result in 1; otherwise, result is 0
    """
    #example_data = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
    #                90, 91, 92, 93, 94, 95]
    #monitoring_model.predict(example_data)