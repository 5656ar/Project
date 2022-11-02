import time
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker
import psycopg2
from bs4 import BeautifulSoup
import requests

engine = sqlalchemy.create_engine('postgresql://webadmin:MDDnfo15110@node38352-bunnapon.proen.app.ruk-com.cloud:11234/work')
Base = declarative_base()



##################################################################################
url = "https://finance.yahoo.com/currencies?.tsrc=fin-srch"
req = requests.get(url)
req.encoding = "utf-8"
soup = BeautifulSoup(req.text, "html.parser")
##################################################################################

class Data_euro(Base):
    __tablename__ = "euro"
    id = Column(Integer, primary_key=True)
    last_price = Column(String, nullable=False)
    change = Column(String, nullable=False)
    change_per = Column(String, nullable=False)

class Data_yen(Base):
    __tablename__ = "yen"
    id = Column(Integer, primary_key=True)
    last_price = Column(String, nullable=False)
    change = Column(String, nullable=False)
    change_per = Column(String, nullable=False)

class Data_thai(Base):
    __tablename__ = "thai"
    id = Column(Integer, primary_key=True)
    last_price = Column(String, nullable=False)
    change = Column(String, nullable=False)
    change_per = Column(String, nullable=False)




Base.metadata.create_all(engine)

euro_list = []
yen_list = []
thai_list = []

courses_euro = soup.find_all('fin-streamer',{'data-symbol':'EURUSD=X'})
for i in courses_euro:
    
    euro_list.append(i.string)
        

courses_yen = soup.find_all('fin-streamer',{'data-symbol':'JPY=X'})
for i in courses_yen:
    yen_list.append(i.string)

courses_thai = soup.find_all('fin-streamer',{'data-symbol':'THB=X'})
for i in courses_thai:
    thai_list.append(i.string)



Session = sessionmaker(bind=engine)
session = Session()



commit_data = Data_euro(last_price = euro_list[0], change = euro_list[1], change_per = euro_list [2])
commit_data1 = Data_yen(last_price = yen_list[0], change = yen_list[1], change_per = yen_list [2])
commit_data2 = Data_thai(last_price = thai_list[0], change = thai_list[1], change_per = thai_list [2])



connection= psycopg2.connect(user ='webadmin',
                                password ='MDDnfo15110',
                                host = 'node38352-bunnapon.proen.app.ruk-com.cloud', 
                                port = '11234',
                                database ='work')

Cursor = connection.cursor()
Cursor2 = connection.cursor()
Cursor3 = connection.cursor()

select_data = "SELECT last_price, change, change_per FROM euro"
select_data_2 = "SELECT last_price, change, change_per FROM thai"
select_data_3 = "SELECT last_price, change, change_per FROM yen"
        
Cursor.execute(select_data)
Cursor2.execute(select_data_2)
Cursor3.execute(select_data_3)

all_cur = Cursor.fetchall()
all_cur2 = Cursor2.fetchall()
all_cur3 = Cursor3.fetchall()

list_thai_check = []

all_money = []

for i in all_cur2:
    for z in i:
        list_thai_check.append(z)

# if list_thai_check[0] == thai_list[0]:
#     print('same data')
# else:
#     session.add(commit_data)
#     session.add(commit_data1)
#     session.add(commit_data2)
#     session.commit()
print(list_thai_check)

print(thai_list[0])


