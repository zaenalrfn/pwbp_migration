from flask import jsonify, request
from app import app

mahasiswa = []

@app.route('/')
def index():
    return "Hello"

@app.route('/mahasiswa', methods=['GET'])
def get_mahasiswa():
    return jsonify(mahasiswa)

@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    new_mahasiswa = request.get_json()
    mahasiswa.append(new_mahasiswa)
    return jsonify(new_mahasiswa), 201

@app.route('/mahasiswa/<int:mahasiswa_id>', methods=['GET'])
def get_mahasiswa_by_id(mahasiswa_id):
    if 0 <= mahasiswa_id < len(mahasiswa):
        return jsonify(mahasiswa[mahasiswa_id])
    else:
        return jsonify({"error": "Mahasiswa not found"}), 404

@app.route('/mahasiswa/<int:mahasiswa_id>', methods=['PUT'])
def update_mahasiswa(mahasiswa_id):
    if 0 <= mahasiswa_id < len(mahasiswa):
        updated_data = request.get_json()
        mahasiswa[mahasiswa_id] = updated_data
        return jsonify(updated_data)
    else:
        return jsonify({"error": "Mahasiswa not found"}), 404

@app.route('/mahasiswa/<int:mahasiswa_id>', methods=['DELETE'])
def delete_mahasiswa(mahasiswa_id):
    if 0 <= mahasiswa_id < len(mahasiswa):
        deleted_mahasiswa = mahasiswa.pop(mahasiswa_id)
        return jsonify(deleted_mahasiswa)
    else:
        return jsonify({"error": "Mahasiswa not found"}), 404
