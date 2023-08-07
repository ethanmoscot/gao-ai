""" 
This class creates a Sequential NN model for each of the four GAO compliance frameworks, which are saved via keras.
Some recommend using a single hidden layer where the number of nodes (units) is equal to sqrt(num_input_nodes * num_output_nodes).
"""
from keras.models import Sequential
from keras.layers import Dense

class ModelGeneration:

    def generate_governance(self):
        model = Sequential([ #two hidden layers followed by output layer
                Dense(units=32, activation='relu', input_shape=(27,)), #27 inputs
                Dense(units=64, activation='relu'),
                Dense(units=1, activation='sigmoid')
            ])
        model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
        model.save("governance_model")

    '''
    def generate_data(self):
        model = Sequential([ #two hidden layers followed by output layer
                    Dense(units=32, activation='relu', input_shape=(24,)), #24 inputs
                    Dense(units=64, activation='relu'),
                    Dense(units=1, activation='sigmoid')
                ])
        model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
        model.save("data_model")
    
    def generate_performance(self):
        model = Sequential([ #two hidden layers followed by output layer
                        Dense(units=32, activation='relu', input_shape=(27,)), #27 inputs
                        Dense(units=64, activation='relu'),
                        Dense(units=1, activation='sigmoid')
                    ])
        model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
        model.save("performance_model")
    
    def generate_monitoring(self):
        model = Sequential([ #two hidden layers followed by output layer
                        Dense(units=32, activation='relu', input_shape=(15,)), #15 inputs
                        Dense(units=64, activation='relu'),
                        Dense(units=1, activation='sigmoid')
                    ])
        model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
        model.save("monitoring_model")
    '''