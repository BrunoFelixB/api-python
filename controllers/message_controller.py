from flask import request, jsonify
from sqlalchemy import true
from app_module import create_app, db
from models.message_db import Message, Message_Schema
from datetime import datetime

app = create_app()
app.app_context().push()

message_schema = Message_Schema()
messages_schema = Message_Schema(many=True)

def index():
    ''' Método para consultar todas não lidas as mensagens do banco de dados'''
    messages = Message.query.filter_by(reply_status = False).order_by(Message.created_date).all()
    return jsonify(messages_schema.dump(messages)), 200

def answered():
    ''' Método para consultar todas as mensagens respondidas do banco de dados'''
    messages = Message.query.filter_by(reply_status = True).order_by(Message.created_date).all()
    return jsonify(messages_schema.dump(messages)), 200

def create():
    ''' Método para criar uma mensagem '''
    if request.is_json:
        req = request.get_json()

        message = Message(student_name = req['student_name'], student_email = req['student_email'], subject = req['subject'], student_message = req['student_message'], course = req['course'], turma = req['turma'] , message_reply = '', prof_name = '', prof_email = '', created_date = datetime.now(), reply_status = False )

        db.session.add(message)
        db.session.commit()

    return jsonify({ "message": "mensagem enviada com sucesso"}), 201

def read(id):
    ''' Método para ler uma mensagem pelo id '''
    message = Message.query.filter_by(id = id).first()
    return message_schema.jsonify(message), 200

def update(id):
    ''' Método para atualizar uma mensagem no banco de dados '''
    if request.is_json:
        message_req = request.get_json()

        message = Message.query.filter_by(id = id).first()

        if not message_req['subject'] is None:
            message.subject = message_req['subject']

        if not message_req['student_message'] is None:
            message.student_message = message_req['student_message']

        db.session.commit()

    return jsonify({ "message": "mensagem atualizada com sucesso"}), 201


def reply(id):
    '''Método para enviar a resposta'''
    if request.is_json:
        message_req = request.get_json()

        message = Message.query.filter_by(id = id).first()

        if not message_req['message_reply'] is None:
            message.message_reply = message_req['message_reply']
            message.reply_status = True
            message.reply_date = datetime.now()

        if not message_req['prof_email'] is None:
            message.prof_email = message_req['prof_email']
        
        if not message_req['prof_name'] is None:
            message.prof_name = message_req['prof_name']

        db.session.commit()

    return jsonify({ "message": "resposta enviada com sucesso"}), 201

def delete(id):
    ''' Método para deletar uma mensagem do banco de dados '''
    message = Message.query.filter_by(id = id).first()
    
    if message:
        db.session.delete(message)
        db.session.commit()

        return jsonify({ "message": "mensagem deletada com sucesso"}), 200

    else:
        return jsonify({ "message": "mensagem não encontrada"}), 500 

