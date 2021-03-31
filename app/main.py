from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(hello="world")


@app.route('/nama/<name>')
def name(name):
    return jsonify(hello=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# sources
# https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/