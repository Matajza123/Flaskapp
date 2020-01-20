import datetime
from datetime import time
import secrets
import os
from PIL import Image
from flask import request
from flaskapp import app, db
from flask_sqlalchemy import BaseQuery
from flaskapp.models import User, Ban_list
from flask_login import current_user

now = datetime.datetime.now()
now_date = now.strftime("%d-%m-%Y")
now_time = now.strftime("%H:%M:%S")

def log(e, loc, id0):
    try:
        log_text = []
        log_text.append(e)
        log_text.append(loc)
        log_text.append(now_date)
        log_text.append(now_time)
        log_text.append(id0)

        with open("flaskapp/logs/log.txt", "a+") as output:
            output.writelines(str(log_text))
            output.writelines("\n")

    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)

def bugs(name, id0, text):
    try:
        bug_text = []
        bug_text.append(name)
        bug_text.append(id0)
        bug_text.append(text)
        bug_text.append(now_date)
        bug_text.append(now_time)

        with open("flaskapp/logs/bugs.txt", "a+") as output:
            output.writelines(str(bug_text))
            output.writelines("\n")

    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)

def ban_user(id0, time):
    try:
        ban = Ban_list(user_id=id0, time=time)
        db.session.add(ban)
        db.session.commit()

    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)

def check_ban_list():
    try:
        len_ban_list = len(Ban_list.query.order_by(Ban_list.ban_id).all()) + 1

        for x in range(1, len_ban_list):
            ban_list = Ban_list.query.filter_by(ban_id=x).first()
            if not ban_list == None:
                print(ban_list)
                ban_list_name = ban_list.user_id
                ban_list_time = ban_list.time

                if not ban_list_time == "Infinite":
                    ban_list_time = int(ban_list_time) - 1
                    if ban_list_time == 0:
                        db.session.delete(ban_list)
                        db.session.commit()
                    else:
                        db.session.delete(ban_list)
                        Ban = Ban_list(ban_id = x, user_id=ban_list_name, time=ban_list_time)

                        db.session.add(Ban)
                        db.session.commit()

                    ban_list = Ban_list.query.filter_by(ban_id=x).first()    

    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id) 
        
def save_picture(form_picture):
    try:
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(form_picture.filename)
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

        output_size = (1920, 1080)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)

        return picture_fn
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)