import flask

app = flask.Flask(__name__)

@app.route('/')
def running():
    return 'Hello World!'

@app.route('/hello', methods=['POST'])
def hello():
    message = flask.request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello  |' + name + '|'
    }
    return flask.jsonify(response)