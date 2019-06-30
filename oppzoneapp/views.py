from django.shortcuts import render
from dataProcessing import dataToTable,getTable1,getTable2

# Create your views here.
from django.http import HttpResponse
# from dataProcessing import getData


def index(request):
    return HttpResponse("Testing")

def getSomeData(request,tableName):
    if tableName=='5year':
        table = getTable2()
    if tableName=='1year':
        table=getTable1()
    table= dataToTable(["CensusTractNumber","tract","countyName","stateName","Population","MHI","HomeValue","Unemployment","Poverty","Bachelors","stateCode","countyCode","tract"],table)
    return HttpResponse("<html><body><h2><a href='/table/1year'>1 year</a>      <a href='/table/5year'>5 year</a></h2><h1>"+tableName+"</h1>"+table+"</body></html>")
