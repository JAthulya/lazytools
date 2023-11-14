from flask import Flask, request, render_template, jsonify
import requests 

app = Flask(__name__)
proxy_url = 'http://127.0.0.1'
proxy_port = '8080'

# Construct the full proxy URL
full_proxy_url = f'{proxy_url}:{proxy_port}'

# Define the proxy dictionary
proxies = {
    'http': full_proxy_url,
    'https': full_proxy_url,
}

@app.route('/process_data', methods=['GET'])
def process_data():
    # Get the values of the variables from the query parameters
    variable1 = request.args.get('param1')
    variable2 = request.args.get('param2')
    #proxies={'http':'localhost:8080'}


    # Return a response (optional)
    data = {'employeeId': variable1, 'password': variable2}

    #response = requests.post('http://127.0.0.1:8000', json=data)
    # Send a POST request to http://127.0.0.1:8000
    try:
        response = requests.post('http://127.0.0.1:8000', json=data, verify=False, proxies=proxies)
        return jsonify({'status_code': response.status_code, 'response_text': response.text})
    except requests.RequestException as e:
        return jsonify({'error': f'Request error: {str(e)}'}), 500
    


if __name__ == '__main__':
    app.run(debug=True, port=5001)