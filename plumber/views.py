from django.shortcuts import render

# Create your views here.
import pymysql


class DbConnect:

    def connect(self):
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="minorproject"
        )
        return mydb


# Create your views here.

def page1(request):
    mydb = DbConnect().connect()
    mycursor = mydb.cursor()
    sql = """select aadhar_num from plumber_plumber"""
    mycursor.execute(sql)
    record = mycursor.fetchall()
    li = []
    main = []

    for i in record:
        sql = """select * from labour_maindata where aadhar_num=%s"""
        mycursor.execute(sql, i)
        data = mycursor.fetchall()
        li.append(data)

    for i in range(len(li)):
        for j in range(len(li[0])):
            main.append(li[i][j])

    dict = {'main': main}
    return render(request, 'plumber/plumber_list.html',{'dict':dict})
