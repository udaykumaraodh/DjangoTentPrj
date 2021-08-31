from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def offWork(request):
    with connection.cursor() as cursor:
        cursor.execute('''Insert into office_tenant_officedetails(empdet_id,work) values(3,'operationsManager') ''')
        connection.commit()


        cursor.execute('Select * from office_tenant_officedetails')

        ds=cursor.fetchall()
    return HttpResponse(ds)



def ofUpd(request):
    with connection.cursor() as cursor:
        cursor.execute('''update office_tenant_officedetails set work='Project manger' where id=3 ''')
        connection.commit()


        cursor.execute('Select * from office_tenant_officedetails')

        ds=cursor.fetchall()
    return HttpResponse(ds)


def ofDel(request):
    with connection.cursor() as cursor:
        cursor.execute('''delete from  office_tenant_officedetails  where id=3 ''')
        connection.commit()


        cursor.execute('Select * from office_tenant_officedetails')

        ds=cursor.fetchall()
    return HttpResponse(ds)







