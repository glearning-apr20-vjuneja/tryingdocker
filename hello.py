from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask says hello world with version 1'

@app.route('/test')
def test():
    return 'Testing some hidden functionality'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)