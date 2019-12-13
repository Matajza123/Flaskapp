from mechanize import Browser
from random import randint
import time
br = Browser()
br.set_handle_robots(False)
jeden = ["Admin Admin", "Admin@gmail.com", "jeden jeden", "jeden@gmail.com", "dwa dwa", "dwa@gmail.com", "trzy trzy", "trzy@gmail.com"]

for x in range(4):
    tel = randint(000000000,999999999)

    br.open("http://127.0.0.1:5000/register")

    br.select_form(nr = 0)
    br.form['username'] = jeden.pop(0)
    br.form['email'] = jeden.pop(0)
    br.form['tel_nr'] = str(tel)
    br.form['age'] = "21"
    br.form['password'] = '123'
    br.form['confirm_password'] = '123'

    br.submit()
    time.sleep(7)
