from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import sqlite3
import time
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html',title='欢迎使用HM收作业系统')

@app.route('/view')
def view():
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	cursor = c.execute("SELECT STUNUM, NAME, CLASS, GRADE  from STUDENT")

	return render_template('view.html', entries=cursor)

@app.route('/student')

def student():
    return render_template('student.html')

@app.route('/instu', methods=['GET','POST'])
def instu():
    if request.method=='POST':
        stunum=request.form['stunum']
        name=request.form['name']
        stuclass=request.form['stuclass']
        grade=request.form['grade']
        rfid=request.form['rfid']
    else:
        stunum=request.args['stunum']
        name=request.args['name']
        stuclass=request.args['stuclass']
        grade=request.args['grade']
        rfid=request.args['rfid']
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("INSERT INTO STUDENT (STUNUM,NAME,CLASS,GRADE,RFID) VALUES (:stuname,:name,:stuclass,:grade,:rfid)",{'stuname':stunum,'name':name,'stuclass':stuclass,'grade':grade,'rfid':rfid});
    conn.commit()
    print ("插入成功")
    conn.close()
    return render_template('student.html')

@app.route('/check',methods=['GET','POST'])
def check():
  # global time
  if request.method=='POST':
  	  rfidnum=request.form['rfidnum']
  	  subject = request.form['subject']
  	  comnun =  request.form['comnum']
  conn = sqlite3.connect('test.db')
  c = conn.cursor()
  # cursor=c.execute("SELECT STUNUM,NAME,CLASS,GRADE FROM STUDENT WHERE RFID=:rfid",{'rfid':rfid})
  # for row in cursor:
  #   print(row[0])
  #   print(row[1])
  #   print(row[2])
  #   print(row[3])
  c.execute("INSERT INTO COMSTU (RFID,SUB,COMNUM,TIME) VALUES (:rfidnum,:subject,:comnum,:time)",{'rfidnum':rfidnum,'subject':subject,'comnum':comnum,'time':time})
  conn.commit()
  print('插入成功')
  conn.close()
  return render_template('check.html')

if __name__ == '__main__':
    app.run(debug=True)
