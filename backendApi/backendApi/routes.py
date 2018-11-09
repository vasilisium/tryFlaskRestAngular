from flask import request, flash, jsonify, redirect, url_for, Response
from flask import render_template, render_template_string
from flask import send_from_directory

import os
from backendApi import app, mongo
from backendApi.data import getTable, getRecodr, insert_update, getQeryConditions, deleteRecord
from config import Config

def getRequestParametr(request, key):
    param = None
    if key in request.args:
        param = request.args[key]
        try:
            param = int(param)
        except Exception:
            pass
    return param


@app.route('/')
def index():
    # resp = jsonify({'result': 'hellow world!!!'})
    return render_template('index.html')

@app.route('/id/<id>')
def record(id):
    rec = getRecodr(id)
    return rec