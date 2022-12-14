from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def cms_index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)
