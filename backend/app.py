from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def generate_segitiga(data):
    response = ""
    for i, i_char in enumerate(data):
        for j, j_char in enumerate(range(i+1)):
            response += i_char if j == 0 else "0"
        response += '<br />'
    return response

def generate_ganjil(data):
    response = ""
    for i in range(int(data) + 1):
        if i % 2 != 0: 
            response += str(i) + " "
    return response

def is_prima(num):
    for i in range(2, num):
        if (num % i ==0):
            return False
    return True

def generate_prima(data):
    response = ""
    for i in range(int(data) + 1):
        if i > 1:
            if is_prima(i):
                response += str(i) + " "
    return response

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/api")
def process():
    type = request.json['type']
    data = request.json['data']

    if data == None or data == '': 
        return jsonify(
            status=False,
            message="Input angka tidak boleh kosong",
            data = None
        ), 500

    if re.search("^[0-9]*$", data) == None:
        return jsonify(
            status=False,
            message="Input hanya boleh angka",
            data = None
        ), 500

    response = ''
    if type == 'segitiga':
        response = generate_segitiga(data)
    elif type == 'ganjil':
        response = generate_ganjil(data)
    elif type == 'prima':
        response = generate_prima(data)
    else: 
        return jsonify(
            status=False,
            message="Tipe generate tidak ditemukan",
            data = None
        ), 500

    return jsonify(
            status=True,
            message="Success",
            data = response
        )