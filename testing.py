import mysql.connector
from apiCalls import getTractInfo

# def testing1():
    # print("TESTING")
cnx = mysql.connector.connect(user='root', password='4AngryZebras!',
                              host='127.0.0.1',
                              database='oppzone_schema', auth_plugin='mysql_native_password')
cursor=cnx.cursor(buffered = True)
qozs=[]
insert = ("INSERT INTO oppzone_schema.merged2 "
            "(CensusTractNumber,TractType,ACSDataSource,tractName,countyName,stateName,population,MHI,homeValue,unemployment,poverty,bachelors,state,county,tract) "
            "VALUES( %(CensusTractNumber)s, %(TractType)s, %(ACSDataSource)s, %(tractName)s, %(countyName)s, %(stateName)s, %(population)s, %(MHI)s, %(homeValue)s, %(unemployment)s, %(poverty)s, %(bachelors)s, %(state)s, %(county)s, %(tract)s)  "
            "ON DUPLICATE KEY UPDATE  CensusTractNumber=%(CensusTractNumber)s")

cursor.execute("SELECT * FROM oppzone_schema.qoz")

x=0

for n in cursor:
    if (n[3]<=56 and n[3]>51) or n[3]==72:
        qozs.append(n)
for m in qozs:
# for m in cursor:
    print(m)
    info=getTractInfo(m[0][5:],m[0][0:2],m[0][2:5])
    if info is None:
        x+=1;
        print(x)
        continue
    print(info[1])
    data={
        'CensusTractNumber': m[0],
        'TractType': m[1],
        'ACSDataSource': m[2],
        'tractName':info[1][0],
        'countyName': m[7],
        'stateName': m[6],
        'population': int(info[1][1]),
        'MHI':int(info[1][2]),
        'homeValue':int(info[1][3]),
        'unemployment':float(info[1][4]),
        'poverty':float(info[1][5]),
        'bachelors':float(info[1][6]),
        'state': int(m[3]),
        'county': int(m[4]),
        'tract': int(m[5])
    }
    cursor.execute(insert, data)
    cnx.commit();
    # cursor.execute("INSERT INTO oppzone_schema.merged2 ('CensusTractNumber','TractType','ACSDataSource','tractName','countyName','stateName','population','MHI','homeValue','unemployment','poverty','bachelors','state','county','tract') VALUES ("+str(m[0])+","+str(m[1])+","+str(m[2])+","+str(info[1][0])+","+str(m[7])+","+str(m[6])+","+info[1][1]+","+str(info[1][2])+","+str(info[1][3])+","+str(info[1][4])+","+str(info[1][5])+","+str(info[1][6])+","+str(m[3])+","+str(m[4])+","+str(m[5])+" )")
print(x)
