from flask import Flask, make_response, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    resp = make_response(render_template("index.html"))
    resp.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    resp.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    resp.headers['Cross-Origin-Resource-Policy'] = 'cross-origin'
    return resp


app.run(host='0.0.0.0', port=8080)
