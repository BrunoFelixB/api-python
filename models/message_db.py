from app_module import db, ma

class Message(db.Model):
    __tablename__ = 'tbl_message'
    id = db.Column(db.Integer, primary_key = True)
    student_email = db.Column(db.String(256), nullable = False, unique = False)
    student_name = db.Column(db.String(50), nullable = False, unique = False)
    course = db.Column(db.String(256), nullable = False, unique = False)
    turma = db.Column(db.String(50), nullable = False, unique = False)
    subject = db.Column(db.String(256), nullable = False, unique = False)
    student_message = db.Column(db.String(1000), nullable = False, unique = False)
    prof_name = db.Column(db.String(50), nullable = False, unique = False)
    prof_email = db.Column(db.String(256), nullable = False, unique = False)
    message_reply = db.Column(db.String(1000), nullable = False, unique = False)
    reply_status = db.Column(db.Boolean, nullable = False, unique = False)
    reply_date = db.Column(db.DateTime, nullable = False)
    created_date = db.Column(db.DateTime, nullable = False)

class Message_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message

"""
Create Table tbl_message (
	id serial primary key,
    student_email varchar(256) not null,
	student_name varchar(50) not null,
	course varchar(256) not null,
    turma varchar(50) not null,
    subject varchar(256) not null,
    student_message varchar(1000) not null,
    prof_email varchar(256) not null,
    prof_name varchar(50) not null,
    message_reply varchar(1000) not null,
    reply_status boolean default 'false' not null,
    reply_date timestamp null,
	created_date timestamp default Now() not null
)

"""