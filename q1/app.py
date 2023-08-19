from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    valid_numbers = []

    for url in urls:
        num = fetch_the_numbers_from_url(url)
        if num is not None:
            valid_numbers.extend(num)

    return jsonify(numbers=sorted(list(set(valid_numbers))))


def fetch_the_numbers_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "numbers" in data and isinstance(data["numbers"], list):
                return data["numbers"]
    except:
        pass
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
