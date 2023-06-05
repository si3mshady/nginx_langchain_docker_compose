from flask import request, Flask
import socket


app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'You got served by container {socket.gethostname()}'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')