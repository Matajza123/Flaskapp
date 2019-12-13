import datetime
from datetime import time
import secrets
import time
import os
from PIL import Image
from flaskapp import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from flaskapp.forms import RegistrationForm, LoginForm, MngForm
from flaskapp.models import User, Post, Info, Photo, Stats
from flask_sqlalchemy import BaseQuery
from flask_login import login_user, current_user, logout_user, login_required
from flaskapp.callendar import events, update_event, update_event_admin, get_desc, add_events, admin_free_events, admin_events, multi_add_events, awaiting_events, last_events

now = datetime.datetime.now()
now_date = now.strftime("%d-%m-%Y")
now_date2 = now.strftime("%Y-%m-%d")

now_date_days = now.strftime("%d")
now_date_months = now.strftime("%m")
now_date_years = now.strftime("%Y")

now_time = now.strftime("%H:%M:%S")
now_hour = now.strftime("%H")

#Daty używane w rezerwacji 
date_now = datetime.date.today()
date_1 = date_now + datetime.timedelta(days=1)
date_2 = date_now + datetime.timedelta(days=2)
date_3 = date_now + datetime.timedelta(days=3)
date_4 = date_now + datetime.timedelta(days=4)
date_5 = date_now + datetime.timedelta(days=5)
date_6 = date_now + datetime.timedelta(days=6)

def log(e, loc):
    log_text = []
    log_text.append(e)
    log_text.append(loc)
    log_text.append(now_date)
    log_text.append(now_time)
    log_text.append(current_user.id)

    with open("flaskapp/logs/log.txt", "a+") as output:
        output.writelines(str(log_text))
        output.writelines("\n")

def bugs(name, text):
    bug_text = []
    bug_text.append(name)
    bug_text.append(text)
    bug_text.append(now_date)
    bug_text.append(now_time)

    with open("flaskapp/logs/bugs.txt", "a+") as output:
        output.writelines(str(log_text))
        output.writelines("\n")

@app.route("/home")
def home():
    return redirect(url_for('rezerwacja'))

@app.route("/lokalizacja")
def lokalizacja():
    try:
        return render_template('lokalizacja12.html')
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

#Rezerwacja start
@app.route('/')
@app.route("/rezerwacja", methods=['GET', 'POST'])
@login_required
def rezerwacja():
    try:
        day12 = False
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja2')
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, list1=events(day12), now1=date_now, next=next1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))
        
@app.route("/rezerwacja2", methods=['GET', 'POST'])
@login_required
def rezerwacja2():
    try:
        day12 = 1
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja3')
        previous = url_for('rezerwacja')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, list1=events(day12), now1=date_1, next=next1, previous=previous, previous1=previous1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja3", methods=['GET', 'POST'])
@login_required
def rezerwacja3():
    try:
        day12 = 2
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja4')
        previous = url_for('rezerwacja2')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, list1=events(day12), now1=date_2, next=next1, previous=previous, previous1=previous1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja4", methods=['GET', 'POST'])
@login_required
def rezerwacja4():
    try:
        day12 = 3
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja5')
        previous = url_for('rezerwacja3')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, list1=events(day12), now1=date_3, next=next1, previous=previous, previous1=previous1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja5", methods=['GET', 'POST'])
@login_required
def rezerwacja5():
    try:
        day12 = 4
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja6')
        previous = url_for('rezerwacja4')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, list1=events(day12), now1=date_4, next=next1, previous=previous, previous1=previous1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja6", methods=['GET', 'POST'])
@login_required
def rezerwacja6():
    try:
        day12 = 5
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja7')
        previous = url_for('rezerwacja5')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, list1=events(day12), now1=date_5, next=next1, previous=previous, previous1=previous1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja7", methods=['GET', 'POST'])
@login_required
def rezerwacja7():
    try:
        day12 = 6
        summary, start1, list1 = events(day12)
        list_len = list1
        previous = url_for('rezerwacja6')
        previous1 = True
        next1 = False
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, list1=events(day12), now1=date_6, next=next1, previous=previous, previous1=previous1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/confirm1", methods=['GET', 'POST'])
@login_required
def confirm1():
    try:
        start_date_confirm = request.form.get("test1")
        if len(start_date_confirm) == 0:
            flash('Nie wybrano terminu', 'danger')
            return redirect(url_for('rezerwacja'))

        letter1 = []
        print(start_date_confirm)
        for letter in start_date_confirm:
            letter1.append(letter)

        for x in range(len(letter1)-10):
            letter1.pop(-1)

        print("".join(letter1))
        letter1 = "".join(letter1)

        format = "%Y-%m-%d"
        letter1 = now.strptime(letter1, format)

        letter1_days = letter1.strftime("%d")
        letter1_months = letter1.strftime("%m")
        letter1_years = letter1.strftime("%Y")
        
        if int(now_date_years) <= int(letter1_years):
            print(int(now_date_years), int(letter1_years))

            if int(now_date_months) <= int(letter1_months):
                print(int(now_date_months), int(letter1_months))

                if int(now_date_days) <= int(letter1_days):
                    print(int(now_date_days), int(letter1_days))

                    update_event(start_date_confirm)
                else:
                    flash('Wybierz poprawną datę', 'danger')
                    return redirect(url_for('rezerwacja'))
            else:
                flash('Wybierz poprawną datę', 'danger')
                return redirect(url_for('rezerwacja'))
        else:
            flash('Wybierz poprawną datę', 'danger')
            return redirect(url_for('rezerwacja'))


            
        flash('Poprawnie zarezerwowano termin. Proszę poczekać na potwierdzenie które otrzymasz drogą telefoniczną, może to portwać do kilku godzin.', 'info')
        return redirect(url_for('rezerwacja'))
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))
#Rezerwacja end


@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Logowanie się nie powiodło. Sprawdź email lub hasło', 'danger')
        return render_template('login.html', title='Login', form=form)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/register", methods=['GET', 'POST'])
def register():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('home'))

        form = RegistrationForm()
        if form.validate_on_submit():
            if str(form.tel_nr.data).isdigit()==True:
                tel = User.query.filter_by(tel_nr=form.tel_nr.data).first()
                if tel == None: 
                    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                    user = User(username=form.username.data, email=form.email.data,tel_nr=form.tel_nr.data, age=form.age.data, password=hashed_password)
                
                    db.session.add(user)
                    db.session.commit()

                    user1 = User.query.filter_by(username=form.username.data).first()
                    info = Info(author=user1, created=now_date)
                    db.session.add(info)
                    db.session.commit()

                    flash('Towje konto zostało stworzone!', 'success')
                    return redirect(url_for('login'))
                else:
                    flash("Numer telefonu jest już zajęty", "danger")
                    return redirect(url_for('register'))

            else:
                flash("Numer telefonu nie może zawierać znaków", "danger")
                return redirect(url_for('register'))

        return render_template('register.html', title='Rejestracja', form=form)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    try:
        name = current_user.username
        email = current_user.email
        tel = current_user.tel_nr
        age = current_user.age

        return render_template('account.html', title='Account', name=name, email=email, tel=tel, age=age,)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    try:
        logout_user()
        return redirect(url_for('home'))
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))   

#admin routes
@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            summary_admin, start_admin, list_admin, desc_admin = admin_events() # zatwierdzone 
            list_len_admin = list_admin

            summary_awaiting, start_awaiting, list_awaiting, desc_awaiting = awaiting_events() # oczekujące potwierdzenia
            list_len_awaiting = list_awaiting

            summary_user, start_user, list_user = admin_free_events() # wolne terminy
            list_len_user = list_user

            return render_template('admin.html', title='admin', start_admin=start_admin, summary_admin=summary_admin, list_len_admin=list_len_admin, desc_admin=desc_admin, 
                                start_user=start_user, summary_user=summary_user, list_len_user=list_len_user,
                                start_awaiting=start_awaiting, summary_awaiting=summary_awaiting, list_len_awaiting=list_len_awaiting,desc_awaiting=desc_awaiting, now1=now_date)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
@login_required
def add():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            len12 = int(24) - int(now_hour)
            now_date1 = []
            for x in range(7): 
                target = datetime.date.today() + datetime.timedelta(days=int(x))
                now_date1.append(target)

            return render_template('add.html', title='add', list1=admin_events(), now1=now, now_date1=now_date1)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/add2", methods=['GET', 'POST'])
@login_required
def add2():#TODO fix gdy bezpośrednio przechodzisz to add2 błąd
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            result = request.form
            start_date = request.form['start_date'] 
            start_time1 = request.form['start_time'] 
            end_time1 = request.form['end_time']
            len1 = request.form['lenght']

            if len(start_date) == 0:
                flash('Nie podałeś daty', 'danger')
                return redirect(url_for('add'))
            if len(start_time1) == 0:
                flash('Nie podałeś godziny', 'danger')
                return redirect(url_for('add'))
            if len(end_time1) == 0:
                flash('Nie podałeś godziny zakończenia', 'danger')
                return redirect(url_for('add'))
            if len(len1) == 0:
                flash('Nie podałeś długości wydarzenia', 'danger')
                return redirect(url_for('add'))


            multi_add_events(start_date, start_time1, end_time1, len1)
            flash('Poprawnie dodano wydarzenia', 'info')
            return redirect(url_for('admin'))
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/confirm_admin", methods=['GET', 'POST'])
@login_required
def confirm_admin():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            summary, start1, list2, desc1 = awaiting_events()
            list_len_confirm_admin = list2

            return render_template('confirm_admin.html',summary=summary, start1=start1, list_len_confirm_admin=list_len_confirm_admin, desc1=desc1)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))


buffer = []
@app.route("/confirm_admin2", methods=['GET', 'POST'])
@login_required
def confirm_admin2():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            start_date_confirm = request.form['test1']
            start_time, desc = get_desc(start_date_confirm)
            buffer.append(start_date_confirm)

            return render_template('confirm_admin2.html',start_date_confirm=start_time, desc_awaiting=desc)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))
@app.route("/confirm_admin3", methods=['GET', 'POST'])
@login_required
def confirm_admin3():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            start_date_confirm = buffer

            update_event_admin(start_date_confirm)

            buffer.clear()
            flash('Poprawnie Zatwierdzono Wydarzenia', 'info')
            return redirect(url_for('admin'))
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))


@app.route("/del", methods=['GET', 'POST'])
@login_required
def delete():
    try:
        delete_txt = ["Tak", "Nie"]
        return render_template('del_warning.html', list1=delete_txt)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/del_confirmed", methods=['GET', 'POST'])
@login_required
def delete_confirmed():
    try:
        wyb = request.form['wyb1'] 
        admin = User.query.filter_by(role='1').first()
        if admin == current_user:
            flash('Nie można usunąć admina', 'danger')
            return redirect(url_for('account'))
        else:
            if wyb == "Tak":
                user = current_user
                post = Post.query.filter_by(post_id=current_user.id).first()
                if post:
                    db.session.delete(post)
                
                info = Info.query.filter_by(info_id=current_user.id).first()
                if info:
                    db.session.delete(info)
                            
                photo = Photo.query.filter_by(photo_id=current_user.id).first()
                if photo:
                    db.session.delete(photo)

                stats = Stats.query.filter_by(stats_id=current_user.id).first()
                if stats:
                    db.session.delete(stats)

                db.session.delete(user)

                db.session.commit()
                flash('Pomyślnie usunięto konto', 'info')
                return redirect(url_for('login'))
            else:
                flash('Konto nie zostało usunięte', 'info')
                return redirect(url_for('home'))
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

idbuffer1 = []

@app.route("/rejestr", methods=['GET', 'POST'])
@login_required
def rejestr():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            user = User.query.order_by(User.username).all()
            len_user = len(user)
            idbuffer1.clear()
            return render_template('rejestr.html', len_user=len_user, name=user)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/rejestr2", methods=['GET', 'POST'])
@login_required
def rejestr2(): #TODO fix gdy bezpośrednio przechodzisz to rejestr2 błąd
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            id1 = request.form['wyb1']

            check_user = User.query.filter_by(id=id1).first()
            if check_user == None:
                flash('Użytkiwnik nie istnieje, podaj poprawne ID', 'danger')
                return redirect(url_for('rejestr'))

            if len(idbuffer1) == 0:
                for x in range(10):
                    idbuffer1.append(id1)

            if not idbuffer1[0] == id1:
                idbuffer1.clear()
                idbuffer1.append(id1)
                
            if len(id1) == 0:
                flash('Podaj ID', 'danger')
                return redirect(url_for('rejestr'))

            check = Post.query.filter_by(post_user_id=id1).first()
            if check == None:
                user1 = User.query.filter_by(id=id1).first()
                post = Post(author=user1, created=now_date)
                db.session.add(post)
                db.session.commit()

            check1 = Photo.query.filter_by(photo_user_id=id1).first()
            if check1 == None:
                user1 = User.query.filter_by(id=id1).first()
                photo = Photo(author=user1)
                db.session.add(photo)
                db.session.commit()

            form = MngForm()
            user1 = User.query.filter_by(id=id1).first()
            info = Info.query.filter_by(info_id=id1).first()

            post = Post.query.filter_by(post_user_id=id1).all()
            post_len = len(post)
            post1 = []
            for x in range(post_len):
                post1.append(post.pop(0))
            
            post1.reverse()
            post2 = post1.pop(0)

            choroba = post2.choroba
            objawy = post2.objawa
            notes = post2.notes
            visit_nr = post2.visit_nr + 1

            return render_template('rejestr2.html', user1=user1, form=form, choroba=choroba, objawy=objawy, visit_nr=visit_nr, notes=notes)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/rejestr2_more", methods=['GET', 'POST'])
@login_required
def rejestr2_more():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            id1 = str(idbuffer1[0])
            user1 = User.query.filter_by(id=id1).first()
            post = Post.query.filter_by(post_user_id=id1).all()
            post_len = len(post)
            post1 = []
            for x in range(post_len):
                post1.append(post.pop(0))
            
            post1.reverse()

            return render_template('rejestr2_more.html', post=post1, post_len=post_len)

        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/photos", methods=['GET', 'POST'])
@login_required
def photos():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            author = User.query.filter_by(id=str(idbuffer1[0])).first()
            photo_name = Photo.query.filter_by(photo_user_id=author.id).all()
            photo_len = len(photo_name)

            print(len(photo_name))
            print(photo_name)
            if len(photo_name) == 1:
                photo_len = 0

            post1 = []
            test = []
            for x in range(photo_len):
                post1.append(photo_name.pop(0))
            
            post1.reverse()
            for x in range(photo_len):
                post2 = post1.pop(0)
                photo1 = url_for('static', filename='profile_pics/' + str(post2.photo))
                test.append(photo1)
            return render_template('photos.html', photo=test, photo_len=photo_len)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

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
        log(e, request.path)
        return render_template('error_page.html', error = type(e))

@app.route("/rejestr3", methods=['GET', 'POST'])
@login_required
def rejestr3():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            form = MngForm()
            
            author = User.query.filter_by(id=str(idbuffer1[0])).first()
            post = Post.query.filter_by(post_id=str(idbuffer1[0])).first()
            if post:
                post_choroba = post.choroba
                post_objawa = post.objawa
                post_notes = post.notes
                post_visit_nr = post.visit_nr

                visit_nr1 = post_visit_nr + 1
            else:
                visit_nr1 = 0

            
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                author.image_file = picture_file
                photo1 = Photo(author=author, photo=author.image_file, created=now_date)
                db.session.add(photo1)
            
            post = Post(choroba=form.choroba.data, objawa=form.objawa.data, notes=form.notes.data, created=now_date, visit_nr=visit_nr1, author=author)
            db.session.add(post)
            db.session.commit()

            flash('Poprawnie zaaktualizowano dane pacjęta', 'info')
            return redirect(url_for('admin'))

        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/stats", methods=['GET', 'POST'])
@login_required
def stats():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            last_7 = last_events(date=7)
            last_30 = last_events(date=30)
            last_90 = last_events(date=90)

            user_count_nr = User.query.order_by(User.id).all()
            user_count_nr = len(user_count_nr)

            stats1 = Stats.query.order_by(Stats.stats_id).all()
            stats_len = len(stats1)
            post1 = []
            test = []
            test1 = []
            stats1.reverse()
            for x in range(stats_len):
                post1.append(stats1.pop(0))
                user13 = post1.pop(0)
                user14 = user13.user_count
                user13 = user13.date
                test.append(user13)
                test1.append(user14)
            dates = test
            user_nr = test1

            return render_template('stats.html', last_7=last_7, last_30=last_30, last_90=last_90, user_count=user_count_nr, stats_len=stats_len, dates=dates, user_nr=user_nr)

        except Exception as e:
            print("Error at ", e)
            log(e, request.path)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

def user_count():
    try:
        stats1 = Stats.query.filter_by(date=now_date).first()
        if stats1 == None:
            user_count = User.query.order_by(User.id).all()
            user_count = len(user_count)
            stats = Stats(date=str(now_date), user_count=str(user_count))
            db.session.add(stats)
            db.session.commit()
    except Exception as e:
        print("Error at ", e)
        log(e, request.path)
        return render_template('error_page.html', error = type(e))


@app.route("/stats", methods=['GET', 'POST'])
@login_required
def bug():
    pass