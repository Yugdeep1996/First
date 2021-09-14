from flask import Flask, request, jsonify  
import pandas as pd
import time
from path import workbook_path

print('Loading data...')
# global variables declared.
bank_data = []
Statistics = []
bank_leaderboard_data = []

# storing xlsx data in memory.
# reading xlsx Sheet1 data.
workbook1 = pd.read_excel(workbook_path, sheet_name = 'Sheet1')
workbook1.head()
# extracting xlsx Sheet1 data. 
for i in range(0, len(workbook1)):
    bank_data.append({
        "BANK": workbook1['BANK'][i],
        "IFSC": workbook1['IFSC'][i],
        "MICR": workbook1['MICR CODE'][i],
        "CODE": workbook1['BRANCH'][i],
        "BRANCH": workbook1['ADDRESS'][i],
        "ADDRESS": workbook1['STD CODE'][i],
        "STD_CODE": workbook1['CONTACT'][i],
        "CITY": workbook1['CITY'][i],
        "DISTRICT": workbook1['DISTRICT'][i],
        "STATE": workbook1['STATE'][i],
    })

# reading xlsx Pivot Table_Sheet1_1 data.
workbook2 = pd.read_excel(workbook_path, sheet_name = 'Pivot Table_Sheet1_1')
workbook2.head()
# extracting xlsx Pivot Table_Sheet1_1 data. 
for i in range(1, len(workbook2)):
    bank_leaderboard_data.append({
        workbook2['BANK'][i]: str(workbook2['Count - BANK'][i]),
    })


app = Flask(__name__)  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def Search_ifsc_viewset():     
    return jsonify({'MESSAGE': 'Welcome user'})

@app.route("/ifsc_search")
def Search_ifsc_viewset():
    '''
    The function for searched ifsc with timestamp.

    Parameters:
        ifsc_code (String): The ifsc code to be searched.
    
    Returns:
        results: A list which contains the ifsc bank data.
    '''
    
    # requested parameter.
    if request.args.get('ifsc_code'):
        # storing ifsc code matched results
        results = [data for data in bank_data if data['IFSC'] == request.args.get('ifsc_code')]
        if results:
            # storing ifsc code with timestamp for statistics results.
            Statistics.append({request.args.get('ifsc_code'): str(time.time())})
            return jsonify(results)
        else: 
            return jsonify({'MESSAGE': 'NO RESULTS FOUND'})
    else: 
        return jsonify({'MESSAGE': 'ifsc_code parameter required'})

@app.route("/bank_leader_board", methods=['GET', 'POST'])
def bank_leader_board_viewset():
    '''
    The function for bank leader board data.

    Parameters:
        sortorder (String): The sorting order ASC/DESC,
        fetchcount (String): The counts to be fetched.
    
    Returns:
        results: A list which contains the bank leader board data.
    '''

    if bank_leaderboard_data:
        results = []
        if int(request.args.get('fetchcount')) <= len(bank_leaderboard_data):
            if request.args.get('sortorder') == 'ASC':
                # if sortorder is ASC then get results in ascending order.
                for i in range(0, int(request.args.get('fetchcount'))):
                    results.append(bank_leaderboard_data[i])   
            else:
                # if sortorder is DESC then get results in descending order.
                for i in reversed(range(int(request.args.get('fetchcount')))):
                    results.append(bank_leaderboard_data[i])
            return jsonify(results)        
        else:
            if request.args.get('sortorder') == 'ASC':
                # if sortorder is ASC then get results in ascending order.
                for i in range(0, len(bank_leaderboard_data)):
                    results.append(bank_leaderboard_data[i])   
            else:
                # if sortorder is DESC then get results in descending order.
                for i in reversed(range(len(bank_leaderboard_data))):
                    results.append(bank_leaderboard_data[i]) 
            return jsonify(results, {'MESSAGE': 'ONLY '+str(len(bank_leaderboard_data))+' RESULTS'})
    else: 
        return jsonify({'MESSAGE': 'NO RESULTS'})


@app.route("/stats")
def statistics_viewset():
    '''
    The function for searched ifsc code with timestamp statistics data.

    Parameters:
        sortorder (String): The sorting order ASC/DESC,
        fetchcount (String): The counts to be fetched.
    
    Returns:
        results: A list which contains the ifsc statistics data.
    '''

    if Statistics:
        if request.args.get('fetchcount')=='ALL':
            # returning all ifsc statistics data.
            if request.args.get('sortorder') == 'DESC':
                Statistics.reverse()
            return jsonify(Statistics)
        else:
            results = []
            if int(request.args.get('fetchcount')) <= len(Statistics):
                # if sortorder is DESC then get results in descending order.
                if request.args.get('sortorder') == 'DESC':
                    for i in reversed(range(int(request.args.get('fetchcount')))):
                        results.append(Statistics[i])   
                else:
                    # if sortorder is ASC then get results in ascending order.
                    for i in range(0, int(request.args.get('fetchcount'))):
                        results.append(Statistics[i])
                return jsonify(results)        
            else: 
                # if sortorder is DESC then get results in descending order.
                if request.args.get('sortorder') == 'DESC':
                    for i in reversed(range(len(Statistics))):
                        results.append(Statistics[i])   
                else:
                    # if sortorder is ASC then get results in ascending order.
                    for i in range(0, len(Statistics)):
                        results.append(Statistics[i])
                return jsonify(results, {'MESSAGE': 'ONLY '+str(len(Statistics))+' RESULTS'})
    else: 
        return jsonify({'MESSAGE': 'NO RESULTS'})


if __name__ == '__main__':  
    app.run(debug = False)