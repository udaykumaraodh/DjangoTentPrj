from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
def empDetails(request):
    with connection.cursor() as cursor:
        cursor.execute('''Insert into employee_shared_empdetails(empno,ename,salary) values(103,'harish',30000.0) ''')
        connection.commit()


        cursor.execute('Select * from employee_shared_empdetails')

        ds=cursor.fetchall()
    return HttpResponse(ds)

def empUpd(request):
    with connection.cursor() as cursor:
        cursor.execute('''update employee_shared_empdetails set salary=salary+10000 where empno=103 ''')
        connection.commit()


        cursor.execute('Select * from employee_shared_empdetails')

        ds=cursor.fetchall()
    return HttpResponse(ds)


def empDel(request):
    with connection.cursor() as cursor:
        cursor.execute('''delete from employee_shared_empdetails  where id=3 ''')
        connection.commit()


        cursor.execute('Select * from employee_shared_empdetails')

        ds=cursor.fetchall()
    return HttpResponse(ds)



    

# Create your views here.
