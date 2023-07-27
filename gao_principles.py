import pandas as pd
from governance_class import GovernanceModel
from data_class import DataModel
from performance_class import PerformanceModel
from monitoring_class import MonitoringModel

class Principles:

    def __init__(self):
        # Instantiate all model classes
        self.governance_model = GovernanceModel()
        self.data_model = DataModel()
        self.performance_model = PerformanceModel()
        self.monitoring_model = MonitoringModel()
        print('NN models loaded')

        
    def load_df(self, df):
        self.df = df
        print(self.df)
        

    def validate(self):
        # Check number of row/columns
        num_cols = len(self.df. columns)
        num_rows = len(self.df.index)
        return num_rows, num_cols, 'File is valid.'
    
    
    def get_overall_compliance(self, results):
        # Get the average probability that the system is compliant.
        # Add new neural network here? Or, just calculate average?
        # For now, calculate average. If avg>=70, return 'Compliant'
        add = sum(results)
        print(f'sum: {add}')
        
        avg = sum(results) / len(results)
        #print(f'results: {results}')
        #print(f'avg: {avg}')
        if avg >= 0.80:
            return 'Compliant'
        else:
            return 'Not Compliant'
        
    
    def predict(self):
        print('In predict')
        systems = []
        for i, j in self.df.iterrows():
            # j[0] = System name
            # J[1..28] = params
            system_name = j[0]
            print(f'row: {i}, system: {system_name}')
            
            # ----- Governance -----
            print(f'\n*******************************************')
            governance_data = j[1:28]
            governance_data = [int(a) for a in governance_data]
            print(f'governance_data:\n {governance_data}')
            avg = sum(governance_data) / len(governance_data)
            print(f'avg:\n {avg}')
            governance_result = self.governance_model.predict(governance_data)
            print(f'governance_result: {governance_result}')
            
            # ----- Data -----
            print(f'\n*******************************************')
            data_data = j[28:52]
            data_data = [int(a) for a in data_data]
            print(f'data_data:\n {data_data}')
            avg = sum(data_data) / len(data_data)
            print(f'avg:\n {avg}')
            data_result = self.data_model.predict(data_data)
            print(f'data_result: {data_result}')

            # ----- Performance -----
            print(f'\n*******************************************')
            performance_data = j[52:79]
            performance_data = [int(a) for a in performance_data]
            print(f'performance_data:\n {performance_data}')
            avg = sum(performance_data) / len(performance_data)
            print(f'avg:\n {avg}')
            performance_result = self.performance_model.predict(performance_data)
            print(f'performance_result: {performance_result}')
            
            # ----- Monitoring -----
            print(f'\n*******************************************')
            monitoring_data = j[79:94]
            monitoring_data = [int(a) for a in monitoring_data]
            print(f'monitoring_data:\n {monitoring_data}')
            avg = sum(monitoring_data) / len(monitoring_data)
            print(f'avg:\n {avg}')
            monitoring_result = self.monitoring_model.predict(monitoring_data)
            print(f'monitoring_result: {monitoring_result}')
            
            models_results = []
            
            models_results.append(governance_result)
            models_results.append(data_result)
            models_results.append(performance_result)
            models_results.append(monitoring_result)
            print('-----------------------------')
            print(f'models_results: {models_results}')

            result = self.get_overall_compliance(models_results)
            print(f'\nRESULT: {result}')
            dict = {}
            dict['SystemName'] = system_name
            dict['Governance'] = governance_result
            dict['Data'] = data_result
            dict['Performance'] = performance_result
            dict['Monitoring'] = monitoring_result
            dict['Compliance'] = result
            systems.append(dict)
        return systems
        
    def run_governance(self):
        print()
        
        
    def run_data(self):
        print()
        
        
    def run_performance(self):
        print()
        
        
    def run_monitoring(self):
        print()
        
        
 
   


