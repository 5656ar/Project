from flask import Flask , render_template
from sqlalchemy.ext.declarative import declarative_base 
from data_orm import Data_euro,Data_yen,Data_thai,session

from bs4 import BeautifulSoup
import requests

app  = Flask(name)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:MDDnfo15110@node38352-bunnapon.proen.app.ruk-com.cloud:11234/work'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False



### DATA for scrpaing   ####
##################################################################################
url = "https://finance.yahoo.com/currencies?.tsrc=fin-srch"
req = requests.get(url)
req.encoding = "utf-8"
soup = BeautifulSoup(req.text, "html.parser")
##################################################################################






@app.route('/')
def index():
    return render_template('Home.html')


@app.route('/Table')
def Table():

    result_euro = session.query(Data_euro.last_price, Data_yen.change, Data_yen.change_per)
    result_thai = session.query(Data_thai.last_price, Data_thai.change, Data_thai.change_per)
    result_japan = session.query(Data_thai.last_price, Data_thai.change, Data_thai.change_per)



    return print(result_euro)

@app.route('/Graph')
def Graph():
    return render_template('Graph.html')



if name == 'main':
    app.run(host='0.0.0.0' , port =80 ,debug = True)