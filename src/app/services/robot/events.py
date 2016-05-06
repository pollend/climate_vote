from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json

from app import db
from app.model.problem import Problem
from app import app
from app import socketio
import requests
import Queue

from app.model.account import Account

from flask_kvsession import KVSessionExtension

import string
import math
import datetime

users = []
active_user = -1;

def send_updated_player_list()
 out =[]
 for key, value in users.iteritems():
  out.append(value)
 emit("client_list",jsonify(out),namespace='/robot')

@socketio.on('connect', namespace='/robot')
def connect():
 users[requests.sid] = "temp"
 send_updated_player_list()
 emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/robot')
def disconnect():
 users.remove(requests.sid)
 send_updated_player_list()
 print('Client disconnected')
