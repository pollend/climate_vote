from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json

from app import db
from app.model.problem import Problem
from app import app
from app import socketio
import requests

from app.model.account import Account

from flask_kvsession import KVSessionExtension

import string
import math
import datetime

@socketio.on('connect', namespace='/robot')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/robot')
def test_disconnect():
    print('Client disconnected')
