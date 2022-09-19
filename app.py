from flask import Flask, render_template, request, redirect, session
from socket import gethostname
from time import strptime, localtime, strftime, sleep
import threading
from binarysearchtree import BinarySearchTree
from account import Account
from heaps import MaxHeap

app = Flask(__name__)
app.secret_key = "test"

accounts = BinarySearchTree()

def load():
    try:
        input_file = open("database.txt", 'r')

    except FileNotFoundError:
        file = open("database.txt", 'w')
        file.close()

    else:
        for line in input_file:
            info = line.strip().split(';\t')
            temp_account = Account(info[0], info[1])
            info.pop(0)
            info.pop(0)
            for a in info:
                a = a.split(',\t')
                temp_account.add_task(a[0], a[1], a[2], int(a[3]), a[4])
            accounts.add(temp_account)

        input_file.close()

def store():
    while True:
        try:
            accounts.traversal(accounts.pre_order)

        except RuntimeError:
            pass
    
        sleep(60)
            

########## Home
@app.route('/', methods=["GET", "POST"])
def home():
    if request.form.get("submit") == 'login':
        return redirect('/login/True')

    elif request.form.get("submit") == 'about':
        return redirect('/about')

    elif request.form.get("submit") == 'signup':
        return redirect('/signup/True')

    else:
        return render_template("home.html")

########## About
@app.route('/about', methods=["GET", "POST"])
def about():
    if request.form.get("submit") == "back":
        return redirect('/')

    else:
        return render_template('about.html')

########## Signup
@app.route('/signup/<state>', methods=['GET', 'POST'])
def signup(state):
    return render_template('signup.html', state=state)

@app.route('/signup/confirmation', methods=['GET', 'POST'])
def signup_confirmation():
    if request.form.get("submit") == "back":
        return redirect('/')
    try:
        if request.form.get("username") == '' or request.form.get("pswd") == '' or '\\' in request.form.get("username") or '\\' in request.form.get("pswd"):
            return redirect('/signup/False1')
        
        accounts.search(request.form.get("username"))

    except RuntimeError:
        session["user_account"] = request.form.get("username")
        accounts.add(Account(request.form.get("username"), request.form.get("pswd")))
        return redirect(f'/page')

    else:
        return redirect('/signup/False2')

########## Login
@app.route('/login/<state>', methods=['GET', 'POST'])
def login(state):
    return render_template('login.html', state=state)

@app.route('/login/confirmation', methods=['GET', 'POST'])
def login_confirmation():
    if request.form.get("submit") == "back":
        return redirect('/')
    try:
         user_account = accounts.search(request.form.get("username"))
         session["user_account"] = request.form.get("username")

    except RuntimeError:
        return redirect('/login/False1')
    
    else:
        if request.form.get("pswd") == user_account.get_password():
            return redirect('/page')

        else:
            return redirect('/login/False2')

########## Page
@app.route('/page', methods=['GET', 'POST'])
def page():
    if "user_account" not in session:
        return redirect('/login/True')

    if request.form.get("submit") == "add":
        return redirect(f"/form/addtask")

    if request.form.get("submit") == "logout":
        session.pop("user_account")
        return redirect('/')

    if request.form.get("submit") == "edit":
        return redirect('/form/edittask')
    
    try:
        current_task = accounts.search(session["user_account"]).get_task()
        
    except RuntimeError:
        return render_template("task.html", task = "Nothing", state="False")

    else:
        return render_template("task.html", task = current_task, state="True")
    

@app.route('/form/addtask', methods=['GET', 'POST'])
def addtask():
    if request.form.get("submit") == "back":
        return redirect('/page')
    elif request.form.get("submit") == "Submit":
        try:
            strptime(request.form.get("due_date"), "%m/%d/%Y")
        except:
            return render_template('task_form_add.html', state1 = "False", state2 = "True")

        try:
            if not (1 <= int(request.form.get("weight")) <= 100):
                raise RuntimeError

        except:
            return render_template('task_form_add.html', state1 = "True", state2 = "False")

        accounts.search(session["user_account"]).add_task(request.form.get("title").replace("\\", ''), request.form.get("info").replace("\\", ''), request.form.get("due_date"), int(request.form.get("weight")))

        return redirect(f'/page')

    else:
        return render_template('task_form_add.html', state1 = "True", state2 = "True")

@app.route('/form/edittask', methods=['GET', 'POST'])
def edittask():
    user_account = accounts.search(session['user_account'])

    if request.form.get("submit") == "delete" and request.form.get("index") is not None:
        tasks = user_account.get_tasks()
        tasks.pop(int(request.form.get("index")))
        temp = MaxHeap()

        for task in tasks:
            temp.add(task)

        user_account.set_tasks(temp)
        return redirect('/form/edittask')

    if request.form.get("submit") == "edit" and request.form.get("index") is not None:
        session["index"] = int(request.form.get("index"))
        return render_template("task_form_edit_page.html", task=user_account.get_tasks()[session["index"]], state1="True", state2="True")

    if request.form.get("submit") == "back":
        return redirect('/page')

    if request.form.get("submit2") == "back":
        return redirect('/form/edittask')

    if request.form.get("submit2") == "Submit":
        try:
            strptime(request.form.get("due_date"), "%m/%d/%Y")
        except:
            return render_template('task_form_edit_page.html', task=user_account.get_tasks()[session["index"]], state1 = "False", state2 = "True")

        try:
            if not (1 <= int(request.form.get("weight")) <= 100):
                raise RuntimeError

        except:
            return render_template('task_form_edit_page.html', task=user_account.get_tasks()[session["index"]], state1 = "True", state2 = "False")

        task = user_account.get_tasks()[session["index"]]
        task.set_title(request.form.get("title"))
        task.set_info(request.form.get("info"))
        task.set_due_date(request.form.get("due_date"))
        task.set_weight(int(request.form.get("weight")))

        tasks = user_account.get_tasks()

        temp = MaxHeap()

        for task in tasks:
            temp.add(task)

        user_account.set_tasks(temp)

        session.pop("index")

    temp = list(enumerate(user_account.get_tasks().copy()))
    temp.sort(key=lambda y: y[1])

    return render_template('task_form_edit.html', tasks=temp)

if __name__ == '__main__':
    x = threading.Thread(target=store)
    x.start()
    load()
    app.run(host='0.0.0.0')
