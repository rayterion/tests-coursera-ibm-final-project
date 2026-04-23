import flask

app = flask.Flask(__name__)

def host_app(port):
    raise NotImplementedError("Not implemented")

def shutdown_app():
    raise NotImplementedError("Not implemented")

@app.route("/")
def getHome():
    return "The server is healthy"