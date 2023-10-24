from flask import jsonify
import pymysql
from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sys'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql =MySQL(app)
mysql.init_app(app)



@app.route('/user')
def user():
    try:

            conn= mysql.connect()
            cur=conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("select * from emp")
           
            rows=cur.fetchall()
            resp =jsonify(rows)
            resp.status_code=200
            return resp
       

    except Exception as e:
        print(e)
    finally :
        cur.close()
        conn.close()
       

@app.errorhandler(500)
def not_found(error=None):
    message ={
        'status' :500,
        'message' :'Record not found:'
        }
    resp.jsonify(message)
    resp.status_code=404
    return resp

if __name__  == "__main__":
 app.run()