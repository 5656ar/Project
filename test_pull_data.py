import psycopg2

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

list_euro = []
list_thai = []
list_japan = []

all_money = []

for i in all_cur:
    print(all_cur)
    print(i)
    for z in i:
        list_euro.append(z)

all_money.append(list_euro[0])
    
for i in all_cur2:
    print(i)
    for z in i:
        list_thai.append(z)
    
all_money.append(list_thai[0])

for i in all_cur3:
    print(i)
    for z in i:
        list_japan.append(z)
    
all_money.append(list_japan[0])

print(all_money)
        


