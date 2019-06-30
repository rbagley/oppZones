import mysql.connector
import sys

def convertToObject(data):
    obj=DataPoint(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12])
    return obj

def dataToTable(headers,rows):
    table = "<table><tr>"
    for h in headers:
        table=table+"<th>"+h+"</th>"
    table=table+"</tr>"
    for row in rows:
        table=table+"<tr>"
        for cell in row:
            table=table+"<td>"+str(cell)+"</td>"
        table=table+"</tr>"
    table=table+"</table>"
    return table


class DataPoint:
  def __init__(self, CTN,tractName,countyName,stateName,population, MHI,homeValue, unemployment,poverty,bachelors,state,county,tract):
    self.CTN = CTN
    self.tractName = tractName
    self.countyName= countyName
    self.stateName=stateName
    self.population=population
    self.MHI=MHI
    self.homeValue = homeValue
    self.unemployment = unemployment
    self.poverty = poverty
    self.bachelors = bachelors
    self.state = state
    self.county = county
    self.tract = tract

def getTable1():
    arr = mySQL("SELECT CensusTractNumber,tract,countyName,stateName,Population,MHI,HomeValue,Unemployment,Poverty,Bachelors,stateCode,countyCode,tract FROM oppzone_schema.merged")
    # print(arr)
    sys.stdout.flush()
    return arr
    #     a = convertToObject(a)
def getTable2():
    arr = mySQL("SELECT CensusTractNumber,tractName,countyName,stateName,population,MHI,homeValue,unemployment,poverty,bachelors,state,county,tract FROM oppzone_schema.merged2 WHERE state=1")
    # print(arr)
    return arr

def getData(table,state):
    sqlCommand="SELECT CensusTractNumber,tractName,countyName,stateName,population,MHI,homeValue,unemployment,poverty,bachelors,state,county,tract FROM oppzone_schema."+table
    if state:
        newstr=" WHERE state="+str(state)
        sqlCommand+=newstr
    arr=mySQL(sqlCommand)
    return arr;

def mySQL(command):
        cnx = mysql.connector.connect(user='root', password='4AngryZebras!',
                                      host='127.0.0.1',
                                      database='oppzone_schema', auth_plugin='mysql_native_password')
        cursor=cnx.cursor(buffered = True)
        cursor.execute(command)
        # print(cursor)
        arr=[]
        for a in cursor:
            arr.append(a)
        print(arr)
        return arr
        cursor.close()
        cnx.close()

if sys.argv[1]:
    tableName="merged"
    if sys.argv[1]=='5':
        tableName+="2"
    table=getData(tableName,None);
    for a in table:
        a = convertToObject(a)
        print(a)
    sys.stdout.write(str(table));
