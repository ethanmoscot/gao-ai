from flask import Flask, Response, render_template, request, jsonify
from werkzeug.utils import secure_filename
import traceback
from flask import send_file
from wrapper_class import WrapperClass
import pandas as pd
import json

app = Flask(__name__)

# Load the NN models now
wrapper = WrapperClass()  

# ------------------------------------ Globals ------------------------------------ 

df = None

# ------------------------------------ Functions ------------------------------------ 

@app.route('/gao-ai', endpoint='gao_ai')
def gao_ai():
    return render_template('gao-ai.html')
        

@app.route('/uploader', methods = ['GET', 'POST'], endpoint='upload_file')
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        global df
        df = pd.read_csv(f)
        #f.save(secure_filename(f.filename))
        wrapper.load_df(df)
        num_rows, num_cols, status = wrapper.validate()
        system_results = wrapper.predict()

        return render_template('dynamic_update.html', title='Bootstrap Table',
                            filename=f.filename, num_rows=num_rows, num_cols=num_cols, status=status,
                            system_results=system_results)
    else:
        return render_template('dynamic_update.html', title='Bootstrap Table',
                            filename=f.filename, num_rows=0, num_cols=0, status='Error with data.',
                            system_results=None)

    
@app.route('/get_data', methods=['GET'], endpoint='get_system_data')
def get_system_data():
    try:
        # IMPORTANT! HTML row number is 1 greater than data row number
        row_id = request.args.get('row_id')
        row_id = int(row_id) - 1
        print(f'Got row: {row_id}')
        # Get the governance data for row row_id
        global df
        governance_list = []
        governance_series = df.iloc[row_id, 1:28]
        #print(f'governance_df: {governance_series}')
        for index, value in governance_series.items():
            dict={}
            dict['Section'] = index
            dict['Score'] = int(value*100)
            governance_list.append(dict)

        data_list = []
        data_series = df.iloc[row_id, 25:52]
        for index, value in data_series.items():
            dict={}
            dict['Section'] = index
            dict['Score'] = int(value*100)
            data_list.append(dict)
        
        performance_list = []
        performance_series = df.iloc[row_id, 52:79]
        for index, value in performance_series.items():
            dict={}
            dict['Section'] = index
            dict['Score'] = int(value*100)
            performance_list.append(dict)        
        
        monitoring_list = []
        monitoring_series = df.iloc[row_id, 79:94]
        for index, value in monitoring_series.items():
            dict={}
            dict['Section'] = index
            dict['Score'] = int(value*100)
            monitoring_list.append(dict)  
                    
        dict={}
        dict['GovernanceData'] = governance_list
        dict['DataData'] = data_list
        dict['PerformanceData'] = performance_list
        dict['MonitoringData'] = monitoring_list
        
        all_data_json = json.dumps(dict)
        print(all_data_json)
        
        response = Response(status=200)
        response.set_data(all_data_json)
        response.headers.add("Access-Control-Allow-Origin", "*")        
    
        #json_str = json.dumps(dict)
        #print(json_str)
        #json_str = json_str.replace('\\','')
        
        """GET in server"""
        #response = jsonify(message=json_str)

        # IMPORANT! Add the following otherwise it will be blocked by 
        # CORS policy. Enable Access-Control-Allow-Origin
        #response.headers.add("Access-Control-Allow-Origin", "*")        
        return response
    except:
        traceback.print_exc()
    

if __name__ == '__main__':
    app.run( host='localhost', port='5000', debug=True)

