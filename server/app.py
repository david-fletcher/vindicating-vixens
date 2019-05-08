from flask import Flask, jsonify, g, request
from flask_cors import CORS
import os, os.path

import db

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'src/assets/')

# database connection teardown
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# vixen CRUD
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

@app.route('/vixens/<vid>', methods=['GET'])
def get_vixen(vid):
    result = db.query_db('select * from vixens where id = ?', (vid), one=True)
    if result:
        paragraphs = result['long_desc'].split("\n")
        return jsonify({
            'id': result['id'],
            'name': result['name'],
            'short_desc': result['short_desc'],
            'paragraphs': paragraphs,
            'image': result['image']
        })
    else:
        return 'vixen not found', 404

@app.route('/vixens', methods=['POST'])
def create_vixen():
    data = request.get_json(silent=True)
    args = (data.get('name'), data.get('short_desc'), data.get('long_desc'), data.get('image'))
    result = db.update_db('insert into vixens (name, short_desc, long_desc, image) values (?, ?, ?, ?)', args)
    return jsonify({'id': result})

@app.route('/vixens/<vid>', methods=['PATCH'])
def update_vixen(vid):
    data = request.get_json(silent=True)
    args = (data.get('name'), data.get('short_desc'), data.get('long_desc'), data.get('image'), vid)
    result = db.update_db('update vixens set name = ?, short_desc = ?, long_desc = ?, image = ? where id = ?', args)
    return jsonify({'id': result})

@app.route('/vixens/<vid>', methods=['DELETE'])
def delete_vixen(vid):
    args = (vid)
    result = db.update_db('delete from vixens where id = ?', args)
    return jsonify({'id': result})

# image CRUD
@app.route('/images', methods=['GET'])
def get_images():
    images = []
    reserved = []
    result = db.query_db('select image from vixens')
    for r in result:
        reserved.append(r['image'])

    for root, dirs, files in os.walk(IMAGE_DIR):
        for fname in files:
            if fname in reserved:
                images.append({
                    'image': fname,
                    'allowed': False
                })
            else:
                images.append({
                    'image': fname,
                    'allowed': True
                })

    return jsonify(images)

@app.route('/images', methods=['POST'])
def save_image():
    if request.files:
        if request.files['file']:
            image = request.files['file']
        else:
            return 'no image selected', 422
    else:
        return 'no files received', 422

    IMAGE_PATH = os.path.join(IMAGE_DIR, image.filename)
    if not file_exists(image.filename, IMAGE_DIR):
        image.save(IMAGE_PATH)
    else:
        return 'image already exists', 422
    return jsonify(image.filename)

@app.route('/images/<filename>', methods=['DELETE'])
def delete_image(filename):
    if(filename):
        IMAGE_PATH = os.path.join(IMAGE_DIR, filename)

        if file_exists(filename, IMAGE_DIR):
            os.remove(IMAGE_PATH)
        else:
            return 'file not found', 404

    return jsonify({ 'message': 'deleted'})


def file_exists(filename, dir):
    file_exists = False
    for root, dirs, files in os.walk(dir):
        for fname in files:
            if(fname == filename):
                file_exists = True
                break
    return file_exists

if __name__ == '__main__':
    app.run(host='0.0.0.0')
