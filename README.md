# GAO Compliance Checker (GCC)
Currently, there is no automated method for determining the compliance of DHS AI/ML systems against GAO's AI Accountability Framework – despite the fact that GAO is already conducting audits of DHS AI/ML systems based on its Audit Procedures. This tool could be used by AI/ML system owners, DHS CTOD, and even GAO for performing preliminary compliance checks. 

## Running GCC UI
Start server from environment: `python -m flask run`
Open a browser: http://127.0.0.1:5000/gao-ai
Stop the server: `Ctrl-C`

Consult [requirements.txt](https://github.com/ethanmoscot/gao-ai/blob/main/requirements.txt) as necessary.

## <strong> If you make any changes to the code, you will need to stop and restart the server before reloading the website! </strong>