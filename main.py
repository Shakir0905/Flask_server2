from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    message = request.args.get('message', 'Hello')
    return f'{name}! {message}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
