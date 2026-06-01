from flask import Flask, request

app = Flask(__name__)


VALID_KEYS = {"r_ij511_vip", "key123", "godzilla"}

@app.route('/api/check', methods=['GET'])
def check_key():
    user_key = request.args.get('key')
    if user_key in VALID_KEYS:
        return "Valid"
    else:
        return "Invalid"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
