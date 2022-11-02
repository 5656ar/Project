from unittest import result
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:MDDnfo15110@node38352-bunnapon.proen.app.ruk-com.cloud:11234/work'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False

@app.route('/')
def hello():
    
    connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '11234',
                                database ='work')

    Cursor = connection.cursor()

    select_data = "SELECT last_price, change,  FROM euro"
    
    Cursor.execute(select_data)

    all_cur = Cursor.fetchall()    

    return render_template('chart.html', all_cur=all_cur)

if __name__ =="__main__":
    app.run(debug=True)

