import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential, load_model
from keras.layers import Dense
from tensorflow import keras

class GovernanceModel:

    def generate_governance(self):
        #Some recommend using a single hidden layer where the number of nodes (units) is equal to sqrt(num_input_nodes * num_output_nodes).
        model = Sequential([ #two hidden layers followed by output layer
                Dense(units=32, activation='relu', input_shape=(27,)), #27 inputs
                Dense(units=64, activation='relu'),
                Dense(units=1, activation='sigmoid')
            ])
        model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
        model.save("governance_model")

    def __init__(self):
        print('Training governance model...')
        # During initialization, train the model
        self.df = pd.read_csv('data/governance_training.csv')
        X = self.df.iloc[:,1:28] # input features (GAO governance criteria)
        print(X)
        Y = self.df['Result'] # Results column

        self.generate_governance()
        loaded_model = keras.models.load_model("governance_model")

        done = False
        while not done:
            
            """ Use random_state=42 if needed. """
            X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size = 0.3) #val_and_test is 30% of dataset
            X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5) #equal split for validation and test sets

            """
            A rule of thumb for num_epochs is 3 times the number of input nodes. If the model 
            stops improving accuracy, then reduce num epochs. If the accuracy is still improving 
            after this, increase epochs.
            """
            print("Fit model on training data:")
            # verbose=0 hides individual epoch values, validation_split=0.1 reserves 10% of training data for validation
            hist = loaded_model.fit(X_train, Y_train, verbose='0', batch_size=32, epochs=20, validation_split=0.1, validation_data=(X_val, Y_val)) # type: ignore

            print("Evaluate model on test data:")
            results = loaded_model.evaluate(X_test, Y_test, batch_size=128) # type: ignore
            print("Test loss, test accuracy:", results)

            '''
            Retrieve list of accuracy history during training, returning the final value only if it exceeds 80%
            '''
            #print(hist.history.keys())
            accuracy_list = hist.history['accuracy']
            if accuracy_list[-1] > 0.80:
                done = True
        accuracy_list = hist.history['accuracy'] # type: ignore
        
        # Plot model accuracy
        plt.plot(hist.history['accuracy']) # type: ignore
        plt.plot(hist.history['val_accuracy']) # type: ignore
        plt.title('Governance Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')
        plt.savefig('governance_accuracy.png', bbox_inches='tight')
        plt.clf()
        print(f"FINAL GOVERNANCE ACCURACY: {accuracy_list[-1]}")


    def predict(self, data):
        # data contains 27 input values

        # Transpose the data from a column to a row.
        df2 = pd.DataFrame(data).T
        #print(df2)

        # Get the the predicted probability that the input data is compliant.
        y_pred = self.model.predict(df2) # type: ignore
        val = '%.5f'%(y_pred[0][0])
        print(f'prob compliant: {val}')
        return float(val)
    
    
# This file can be called directly using: python governance_class.py
if __name__ == "__main__":
    governance_model = GovernanceModel()
    
    """
    For testing, use values '0..9', '10..19', ..., '70..79', '80..89', '90..100'
    Values 70..100 should result in 1; otherwise, result is 0
    """
    #example_data = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
    #                90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
    #                90, 91, 92, 93, 94, 95, 96]
    #governance_model.predict(example_data)