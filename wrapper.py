from governance_class import GovernanceModel
from data_class import DataModel
from performance_class import PerformanceModel
from monitoring_class import MonitoringModel

def get_overall_compliance(results):
    # Add new neural network here? Or, just calculate average?
    # For now, calculate average. If avg>69.9, return 'Compliant'
    avg = sum(results) / len(results)
    if avg >= 80:
        return 'Compliant'
    else:
        return 'Not Compliant'


def main():    
    # Instantiate all model classes
    governance_model = GovernanceModel()
    data_model = DataModel()
    perforamnce_model = PerformanceModel()
    monitoring_model = MonitoringModel()
    
    # Run prediction on each model
    
    governance_data = [86,	83,	82,	80,	90,	87,	83,	90,	87,	80,	98,	86,	87,	80,	87,	96,	86,	99,	84,	98,	84,	
            97,	92,	86,	87,	97,	98]
    """
    governance_data = [99,	99,	99,	85,	97, 91,	99,	86,	97,	87,	
                82,	97,	94,	91,	90, 86,	89,	83,	88,	86,
                87,	92,	88,	90,	98,	99,	87]"""
    governance_result = governance_model.predict(governance_data)
    print(f'governance_result: {governance_result}')
    
    # Just set these for now
    data_result = 92
    performance_result = 90
    monitoring_result = 90
    
    models_results = []
    
    models_results.append(governance_result)
    models_results.append(data_result)
    models_results.append(performance_result)
    models_results.append(monitoring_result)
    print(f'models_results: {models_results}')

    result = get_overall_compliance(models_results)
    print(f'result: {result}')


if __name__ == "__main__":
    main()