import logging
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/')
def get_ctftime_teams():
    url = request.args.get('url')
    if not url:
        error_message = "Error: No URL provided"
        logging.error(error_message)
        return error_message

    headers = {
        "User-Agent": "curl/7.64.1",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        logging.info("Request successful")
        return jsonify(response.json())
    else:
        error_message = f"Error: {response.status_code}\n{response.text}"
        logging.error(error_message)
        return error_message

if __name__ == '__main__':
    app.run(host='0.0.0.0')
