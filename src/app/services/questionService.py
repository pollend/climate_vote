from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json
from  sqlalchemy.sql.expression import func, select
from validate_email import validate_email
from app.model.question import Question
from app.model.response import Response

from app import db

mod = Blueprint('account', __name__, url_prefix='/api')



@mod.route("/question", methods=['GET'])
def question():
    return jsonify(Question.query.order_by(func.random()).first().serialize()),200



@mod.route("/response/<int:id>", methods=['POST'])
def response(id):
    if(Question.query.filter_by(award_id = id).first() != None):
        json = request.get_json()
        if("score" not in json ):
            return jsonify(err="score is required"), 400
        if ("email" not in json or not json["email"]):
            return jsonify(err="email is required"), 400
        score = float(json["score"])
        if(not isinstance(score , float)):
            return jsonify(err="invalid score"), 400
        if(not validate_email(json['email'])):
            return jsonify(err="invalid email"), 400
        if(score < -1 and score > 1):
                return jsonify(err = "score has to be between -1 and 1"), 400
        response = Response(request.remote_addr,id,json["email"],score)
        db.session.add(response)
        db.session.commit()
        return jsonify()
    return jsonify(err = "Unknown award"), 400