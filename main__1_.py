 
import webbrowser

from flask import Flask, app, render_template, redirect , request ,url_for
from flask.helpers import url_for
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.config['Mysql_Host']='localhost'
app.config['Mysql_user']='root'
app.config['Mysql_password']=''
app.config['Mysql_database']='sky_travel_booking_portal'

mysql = MySQL(app)

print ("1")

@app.route('/')
def home():
    webbrowser.open('index.html')
    return render_template('hello2.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/read')
def read():
    cur = mysql.connection.cursor()
    cur.execute( "SELECT * FROM bus_timetable ")
    fetchdata = cur.fetchall()
    print(fetchdata)
    cur.close()
    render_template('bus.html',data =fetchdata )
    print("tmam")
    webbrowser.open("bus.html")
    return redirect(url_for('bus'))
    
