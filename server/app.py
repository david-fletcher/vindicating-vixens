from flask import Flask, jsonify, g
from flask_cors import CORS

import db

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# database connection teardown
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/pong', methods=['GET'])
def pong_ping():
    return jsonify('ping!')

@app.route('/vixens', methods=['GET'])
def get_vixens():
    results = db.query_db('select * from vixens')
    vixens = []
    for v in results:
        vixens.append({
            'id': v['id'],
            'name': v['name'],
            'short_desc': v['short_desc'],
            'long_desc': v['long_desc'],
            'image': v['image']
        })
    return jsonify(vixens)

if __name__ == '__main__':
    app.run()