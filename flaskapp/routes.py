import datetime
from datetime import time
import time
import os
from PIL import Image
from flaskapp import app, db, bcrypt, cache
from flask import render_template, url_for, flash, redirect, request, Response
from flask_sqlalchemy import BaseQuery
from flask_login import login_user, current_user, logout_user, login_required

from flaskapp.forms import RegistrationForm, LoginForm, MngForm
from flaskapp.models import User, Post, Info, Photo, Ban_list
from flaskapp.callendar import events, update_event, update_event_admin, get_desc, get_id, add_events, admin_free_events, admin_events, multi_add_events, awaiting_events, last_events
from flaskapp.functions import log, bugs, ban_user, check_ban_list, save_picture
from flaskapp.error_handlers import bad_request, forbidden, page_not_found, method_not_allowed, server_error

now = datetime.datetime.now()
now_date = now.strftime("%d-%m-%Y")
now_date2 = now.strftime("%Y-%m-%d")

now_date_days = now.strftime("%d")
now_date_months = now.strftime("%m")
now_date_years = now.strftime("%Y")

now_time = now.strftime("%H:%M:%S")
now_hour = now.strftime("%H")
now_min = now.strftime("%M")

#Daty używane w rezerwacji 
date_now = datetime.date.today()
date_1 = date_now + datetime.timedelta(days=1)
date_2 = date_now + datetime.timedelta(days=2)
date_3 = date_now + datetime.timedelta(days=3)
date_4 = date_now + datetime.timedelta(days=4)
date_5 = date_now + datetime.timedelta(days=5)
date_6 = date_now + datetime.timedelta(days=6)

isascii = lambda s: len(s) == len(s.encode())

if now_hour == "8" and now_min == "00":
    check_ban_list()

@app.route("/home")
def home():
    return redirect(url_for('rezerwacja'))

@app.route("/lokalizacja")
def lokalizacja():
    try:
        return render_template('lokalizacja.html')
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

#Rezerwacja start
@app.route('/')
@app.route("/rezerwacja", methods=['GET', 'POST'])
@cache.cached()
@login_required
def rezerwacja():
    try:
        day12 = False
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja2')
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, now1=date_now, next=next1)
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))
        
@app.route("/rezerwacja2", methods=['GET', 'POST'])
@cache.cached()
@login_required
def rezerwacja2():
    try:
        day12 = 1
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja3')
        previous = url_for('rezerwacja')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, now1=date_1, next=next1, previous=previous, previous1=previous1)
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja3", methods=['GET', 'POST'])
@login_required
@cache.cached()
def rezerwacja3():
    try:
        day12 = 2
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja4')
        previous = url_for('rezerwacja2')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, now1=date_2, next=next1, previous=previous, previous1=previous1)
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja4", methods=['GET', 'POST'])
@login_required
@cache.cached()
def rezerwacja4():
    try:
        day12 = 3
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja5')
        previous = url_for('rezerwacja3')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, now1=date_3, next=next1, previous=previous, previous1=previous1)
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja5", methods=['GET', 'POST'])
@login_required
@cache.cached()
def rezerwacja5():
    try:
        day12 = 4
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja6')
        previous = url_for('rezerwacja4')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, now1=date_4, next=next1, previous=previous, previous1=previous1)
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja6", methods=['GET', 'POST'])
@login_required
@cache.cached()
def rezerwacja6():
    try:
        day12 = 5
        summary, start1, list1 = events(day12)
        list_len = list1
        next1 = url_for('rezerwacja7')
        previous = url_for('rezerwacja5')
        previous1 = True
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, now1=date_5, next=next1, previous=previous, previous1=previous1)
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/rezerwacja7", methods=['GET', 'POST'])
@login_required
@cache.cached()
def rezerwacja7():
    try:
        day12 = 6
        summary, start1, list1 = events(day12)
        list_len = list1
        previous = url_for('rezerwacja6')
        previous1 = True
        next1 = False
        return render_template('rezerwacja.html', start=start1, summary=summary, list_len=list_len, now1=date_6, next=next1, previous=previous, previous1=previous1)
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/confirm1", methods=['GET', 'POST'])
@login_required
def confirm1():
    try:
        start_date_confirm = request.form.get("test1")
        if len(start_date_confirm) == 0:
            flash('Nie wybrano terminu', 'danger')
            return redirect(url_for('rezerwacja'))

        if isascii(start_date_confirm) == False:
            flash('Podano nieprawidłowe znaki', 'danger')
            return redirect(url_for('rezerwacja'))

        date = get_id(start_date_confirm)
        if not date == True:
            print("Not False")
            flash('Termin jest już zajęty', 'danger')
            return redirect(url_for('rezerwacja'))
        else:
            print("Not True")

        len_ban_list = len(Ban_list.query.order_by(Ban_list.ban_id).all()) + 1
        for x in range(1, len_ban_list):
            ban_list = Ban_list.query.filter_by(ban_id=x).first()
            if current_user.id == ban_list.user_id:
                if ban_list.time == "Infinite":
                    flash('Masz dożywotnio zablokowany dostęp do strony', 'danger')
                    return redirect(url_for('rezerwacja'))
                else:
                    time = date_now + datetime.timedelta(days=int(ban_list.time))
                    flash('Masz zablokowany dostęp do strony do dnia: '+str(time), 'danger')
                    return redirect(url_for('rezerwacja'))
        letter1 = []
        
        for letter in start_date_confirm:
            letter1.append(letter)

        for x in range(len(letter1)-10):
            letter1.pop(-1)

        letter1 = "".join(letter1)

        format = "%Y-%m-%d"
        try:
            letter1 = now.strptime(letter1, format)
        except:
            flash('Nie poprawny format', 'danger')
            return redirect(url_for('rezerwacja'))

        letter1_days = letter1.strftime("%d")
        letter1_months = letter1.strftime("%m")
        letter1_years = letter1.strftime("%Y")
        
        if int(now_date_years) <= int(letter1_years):#TODO fix blisko nowego roku błąd ponieważ niepoprawna data 
            if int(now_date_months) <= int(letter1_months):
                if int(now_date_days) <= int(letter1_days):
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
        log(e, request.path, current_user.id)
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
        log(e, request.path, False)
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
        log(e, request.path, False)
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
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    try:
        logout_user()
        return redirect(url_for('home'))

    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
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

            return render_template('admin.html', title='admin', start_admin=start_admin, summary_admin=summary_admin, list_len_admin=list_len_admin, 
                                start_user=start_user, summary_user=summary_user, list_len_user=list_len_user,
                                start_awaiting=start_awaiting, summary_awaiting=summary_awaiting, list_len_awaiting=list_len_awaiting, now1=now_date)
        
        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
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
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/add2", methods=['GET', 'POST'])
@login_required
def add2():#TODO fix gdy bezpośrednio przechodzisz to add2 błąd odświeżenie naprawia
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

            a = multi_add_events(start_date, start_time1, end_time1, len1)
            if a == False:
                flash('Wystąpił błąd', 'danger')
            else:
                flash('Poprawnie dodano wydarzenia', 'info')
                return redirect(url_for('admin'))
        
        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
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
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))


@app.route("/confirm_admin2", methods=['GET', 'POST'])#HEHE
@login_required
def confirm_admin2():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            start_date_confirm = request.form['test1']
            start_time, desc = get_desc(start_date_confirm)

            id0 = get_id(start_date_confirm)
            desc0 = User.query.filter_by(id=id0).first()

            return render_template('confirm_admin2.html',start_date_confirm=start_time, desc_awaiting=desc0, id0=id0)
        
        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
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
            start_date_confirm = request.form['start_date']
            update_event_admin(start_date_confirm)

            flash('Zatwierdzono Wydarzenia', 'info')
            return redirect(url_for('admin'))
        
        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))


@app.route("/del", methods=['GET', 'POST'])
@login_required
def delete():
    try:
        return render_template('del_warning.html')
    
    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
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
            if wyb == "TAK":
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

                db.session.delete(user)

                db.session.commit()
                flash('Pomyślnie usunięto konto', 'info')
                return redirect(url_for('login'))
            else:
                flash('Konto nie zostało usunięte', 'danger')
                return redirect(url_for('home'))

    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
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
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/rejestr2", methods=['GET', 'POST'])
@login_required
def rejestr2(): #TODO fix gdy bezpośrednio przechodzisz to rejestr2 błąd poprostu refresh naprawia
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            id1 = request.form['wyb1']

            check_user = User.query.filter_by(id=id1).first()
            if check_user == None:
                flash('Użytkiwnik nie istnieje, podaj poprawne ID', 'danger')
                return redirect(url_for('rejestr'))
                
            if len(id1) == 0:
                flash('Podaj ID', 'danger')
                return redirect(url_for('rejestr'))

            check = Post.query.filter_by(post_user_id=id1).first()
            if check == None:
                user1 = User.query.filter_by(id=id1).first()
                post = Post(author=user1, created=now_date)
                db.session.add(post)
                db.session.commit()

            form = MngForm()
            form.id0 = id1
            user1 = User.query.filter_by(id=id1).first()
            info = Info.query.filter_by(info_id=id1).first()

            post1 = []
            posts = Post.query.filter_by(post_user_id=id1).all()
            for post in posts:
                post1.append(post)
            
            post1.reverse()
            post2 = post1.pop(0)

            choroba = post2.choroba
            objawy = post2.objawa
            notes = post2.notes
            visit_nr = post2.visit_nr + 1

            return render_template('rejestr2.html',id0 = id1, user1=user1, form=form, choroba=choroba, objawy=objawy, visit_nr=visit_nr, notes=notes)
        
        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
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
            post1 = []
            user1 = User.query.filter_by(id=id1).first()
            posts = Post.query.filter_by(post_user_id=id1).all()
            post_len = len(posts)
            for post in posts:
                post1.append(post)
            id0 = id1
            
            post1.reverse()
            return render_template('rejestr2_more.html', post=post1, post_len=post_len)

        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))


@app.route("/rejestr3", methods=['POST'])
@login_required
def rejestr3():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            form = MngForm()
            ID = request.form['id0']
            author = User.query.filter_by(id=str(ID)).first()
            post = Post.query.filter_by(post_id=str(ID)).first()
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
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/photos/<int:id0>", methods=['GET', 'POST']) #TODO change photo scale
@login_required
def photos(id0):
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            ID = id0
            photo0 = []
            dates = []
            photos1 = []

            photos0 = Photo.query.filter_by(photo_user_id=ID).all()
            photo_len = len(photos0)

            for x in range(len(photos0)):
                photo11 = photos0[x]
                link = url_for('static', filename='profile_pics/' + str(photo11.photo))
                
                photos1.append(link)
                dates.append(str(photo11.created))

            photos1.reverse()
            dates.reverse()
            return render_template('photos.html', photo=photos1, date=dates, photo_len=photo_len)

        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
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

            users = User.query.order_by(User.id).all()
            avr_age = []
            for user in users:
                avr_age.append(user.age)

            avr_nr = 0
            avr_nr0 = len(avr_age)
            for x in range(len(avr_age)):
                avr_nr += int(avr_age.pop(0))
            avr_nr = avr_nr/avr_nr0

            return render_template('stats.html', last_7=last_7, last_30=last_30, last_90=last_90, user_count=user_count_nr, avr_age=avr_nr)

        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/bug", methods=['GET', 'POST'])
@login_required
def bug():
    return render_template('bug.html')

@app.route("/bug_confirm", methods=['GET', 'POST'])
@login_required
def bug_confirm():
    try:
        text = request.form['bug1']
        bugs(current_user.username, current_user.id, text)
        flash("Poprawnie zgłoszono błąd", "info")
        return redirect(url_for('home'))

    except Exception as e:
        print("Error at ", e)
        log(e, request.path, current_user.id)
        return render_template('error_page.html', error = type(e))

@app.route("/ban", methods=['GET', 'POST'])
@login_required
def ban():
    admin = User.query.filter_by(role='1').first()
    if admin == current_user:
        try:
            user = User.query.order_by(User.username).all()
            user_len = len(user)
            return render_template('ban.html', user=user, user_len=user_len)
        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))
    else:
        flash('Nie masz uprawnien', 'danger')
        return redirect(url_for('home'))

@app.route("/ban_confirm", methods=['GET', 'POST'])
@login_required
def ban_confirm():
    user_id = request.form['ban1']
    time = request.form['time']

    if time == "1": time = "1"
    if time == "7": time = "7"
    if time == "30": time = "30"
    if time == "Na zawsze": time = "Infinite"

    if user_id == "1":
        flash("Nie można zablokować admina", "danger")
        return redirect(url_for('admin'))

    ban_list = Ban_list.query.filter_by(user_id = user_id).first()
    if not ban_list == None:
        flash('Użytkownik ma już zablokowany dostęp', 'danger')
        return redirect(url_for('admin'))
    else:
        try:
            ban_user(user_id, time)
            flash('Poprawnie zablokowano dostęp', 'info')
            return redirect(url_for('admin'))

        except Exception as e:
            print("Error at ", e)
            log(e, request.path, current_user.id)
            return render_template('error_page.html', error = type(e))

@app.route("/test", methods=['GET', 'POST'])
@login_required
def test():
     return render_template('test.html')