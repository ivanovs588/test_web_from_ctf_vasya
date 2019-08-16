from flask import Flask, render_template ,request, redirect
import sqlite3


app= Flask(__name__)


task_amount_simple=4
task_amount_symmetry=2



@app.route("/")
def mainpage():
    return render_template("mainpage.html")
    
    
@app.route("/task/simple/1", methods=['GET', 'POST'])
def task_1():
    task_num=1
    conn = sqlite3.connect("answers.db")
    cursor = conn.cursor()
    cursor.execute(f"select ans from Answers where id= {task_num}")
    correct_answer=cursor.fetchall()[0][0]
    
    return render_template("simple/task_1.html",answer=correct_answer,tn=task_num,task_am=task_amount_simple)
@app.route("/task/simple/2", methods=['GET', 'POST'])
def task_2():
    task_num=2
    conn = sqlite3.connect("answers.db")
    cursor = conn.cursor()
    cursor.execute(f"select ans from Answers where id= {task_num}")
    correct_answer=cursor.fetchall()[0][0]
    
    return render_template("simple/task_2.html",answer=correct_answer,tn=task_num,task_am=task_amount_simple)
@app.route("/task/simple/3", methods=['GET', 'POST'])
def task_3():
    task_num=3
    conn = sqlite3.connect("answers.db")
    cursor = conn.cursor()
    cursor.execute(f"select ans from Answers where id= {task_num}")
    correct_answer=cursor.fetchall()[0][0]
    
    return render_template("simple/task_3.html",answer=correct_answer,tn=task_num,task_am=task_amount_simple)

@app.route("/task/simple/4", methods=['GET', 'POST'])
def task_4():
    task_num=4
    conn = sqlite3.connect("answers.db")
    cursor = conn.cursor()
    cursor.execute(f"select ans from Answers where id= {task_num}")
    correct_answer=cursor.fetchall()[0][0]
    
    return render_template("simple/task_4.html",answer=correct_answer,tn=task_num,task_am=task_amount_simple)



@app.route("/task/symmetry/1", methods=['GET', 'POST'])
def sym_task_1():
    task_num=1
    conn = sqlite3.connect("answers.db")
    cursor = conn.cursor()
    cursor.execute(f"select ans from Answers_symmetry where id= {task_num}")
    correct_answer=cursor.fetchall()[0][0]
    
    return render_template("symmetry/task_1.html",answer=correct_answer,tn=task_num,task_am=task_amount_symmetry)


@app.route("/task/symmetry/2", methods=['GET', 'POST'])
def sym_task_2():
    task_num=2
    conn = sqlite3.connect("answers.db")
    cursor = conn.cursor()
    cursor.execute(f"select ans from Answers_symmetry where id= {task_num}")
    correct_answer=cursor.fetchall()[0][0]
    
    return render_template("symmetry/task_2.html",answer=correct_answer,tn=task_num,task_am=task_amount_symmetry)

@app.route("/task/asymmetry/1", methods=['GET', 'POST'])
def asymmetry_task_1():
    task_num=1
    return render_template("asymmetry/task_1.html",tn=task_num,task_am=task_amount_simple)


#app.run(host="127.0.0.1",port = 5001)
