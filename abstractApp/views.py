from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,get_object_or_404
from .models import Product,Order,History,Client,Admin
from django.utils import timezone
from datetime import datetime,timedelta
from django.views.decorators.csrf import csrf_protect



import os


import json

import time
@csrf_protect
# Create your views here.
def index(request):
    all_products=Product.objects.all()
    a=Users.objects.all()
    userid=0
    for i in a:
        userid=i.id
    x=userid+1
    if request.session.get('valid', None) == True and time.time() <= request.session['timeout']:
            
        t0= time.time() 
        request.session['timeout'] = t0 + 60*10
        if request.session['valid'] == True:
            return render(request,'abstractApp/index.html',{'all_products': all_products})
        else:
            return render(request,'abstractApp/login1.html',{'u':x})
    else:
        return logout(request)
def smugglers(request):
    hondo = {'name':'Hondo','lastname': 'Ohnaka', 'id':1}
    han = {'name':'Han','lastname':'Solo','id':2}
    smugglers = [hondo,han]
    data = json.dumps(smugglers)
    return HttpResponse(data)

def details(request,id):
    species = 'Human'
    if id == '1':
        species = 'Weequay'
    return HttpResponse(species)
def product(request):
    
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    p="";
    for key,value in data.items():
        p=value
    
    product1=Product.objects.filter(product_type=p)
    
    items = []
    for value in product1:
        items.append({'id':value.id,'name':value.product_name,'price':str(value.product_price),'type':value.product_type})
    
    data1 = json.dumps(items);
    return HttpResponse(data1)


def login(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    
    i=Client.objects.filter(id=data['id']).filter(password=data['password'])
    ii=[];
    for value in i:
        ii.append(value.id)
    if not ii:
        i=Admin.objects.filter(id=data['id']).filter(password=data['password'])
        for value in i:
            ii.append(value.id)
        if not ii:
            ii="false"
        else:
            ii="admin"
    else:
        ii="client"
    return HttpResponse(ii)
def register(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=Client()
    
    a.username=data['username']
    a.password=data['password']
    a.homeadd=data['homeadd']
    a.save()
    a=Client.objects.all()
    newid=0;
    for value in a:
        newid=value.id
    return HttpResponse(json.dumps(newid))
    
def id(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=Client.objects.all()
    newid=0;
    for value in a:
        newid=value.id
    return HttpResponse(json.dumps(newid))

def get(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=Order.objects.filter(clientid=data['userid'])
    b=[]
    for value in a:
        d=Product.objects.filter(id=value.product_id);
        for val in d:

            b.append({'id':value.id,'productname':val.product_name,'quantity':value.quantity,'price':str(val.product_price),'date': str(value.date),'time':str(value.time)})
    return HttpResponse(json.dumps(b))
def showhistory(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=History.objects.filter(clientid=data['userid'])
    b=[]
    c=0;
    pn=""
    pp=""
    for value in a:
        c+=1
        dd=Product.objects.filter(id=value.product_id)
        
        for vall in dd:
            pn=vall.product_name
            pp=str(vall.product_price)
        b.append({'re':c,'id':value.id,'productname':pn,'quantity':value.quantity,'price':pp,'date': str(value.date),'time':str(value.time)})
    return HttpResponse(json.dumps(b))
def getall(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=Order.objects.all()
    b=[]
    for value in a:
        c=Client.objects.filter(id=value.clientid)
        client=""
        for v in c:
            client=v.username
        d=Product.objects.filter(id=value.product_id)
        for val in d:

            b.append({'id':value.id,'clientid':value.clientid,'clientname':client,'productname':val.product_name,'quantity':value.quantity,'price':str(val.product_price),'date': str(value.date),'time':str(value.time)})
    return HttpResponse(json.dumps(b))
def removeorder(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    Order.objects.filter(id=data['id']).delete()
    return HttpResponse('removed')
def deletep(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    Product.objects.filter(id=data['id']).delete()
    return HttpResponse('removed')
def getallhistory(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=History.objects.all()
    b=[]
    co=0
    for value in a:
        c=Client.objects.filter(id=value.clientid)
        client=""
        co+=1
        for v in c:
            client=v.username
        d=Product.objects.filter(id=value.product_id)
        for val in d:
            
            b.append({'re':co,'id':value.id,'clientid':value.clientid,'clientname':client,'productname':val.product_name,'quantity':value.quantity,'price':str(val.product_price),'date': str(value.date),'time':str(value.time)})
    return HttpResponse(json.dumps(b))
def showp(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=Product.objects.filter(product_type=data['type'])
    b=[]
    for v in a:
        b.append({'id':v.id,'productname':v.product_name,'price':str(v.product_price)})
    return HttpResponse(json.dumps(b))
def addproduct1(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}

    a=Product()
    
    a.product_name=data['name']
    a.product_price=data['price']
    a.product_type=data['type']
    a.save()
    return HttpResponse(json.dumps(1))

def deliverorder(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    date = time.strftime("%Y-%m-%d")
    time1= time.strftime("%H:%M %p")
    a=Order.objects.filter(id=data['id'])
    for value in a:
        b=History()
        b.clientid=value.clientid
        b.product_id=value.product_id
        b.quantity=value.quantity
        b.date=date
        b.time=time1
        b.save()
    Order.objects.filter(id=data['id']).delete()
    return HttpResponse('delivered')
def order(request):
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    a=Order()
    b=Product.objects.filter(id=data['id'])
    time1= time.strftime("%H:%M %p")
    a.product_id=data['id']
    a.quantity=data['quantity']
    a.clientid=data['userid']
    a.date=data['date']
    a.time=time1
    a.save()

    return HttpResponse('order successful')




def save(request):
    
    data = json.loads(request.body.decode("utf-8")) if (request.body.decode('utf-8')) else {}
    date = time.strftime("%d/%m/%Y")
    time1= time.strftime("%H:%M:%S")
    it = []
    for key, value in data.items():
        it.append(value)
    
    for i in it:
        


        for x in i:
            product_id= Product.objects.filter(product_name=x['name'])
            i=0
            for n in product_id:
                i=n.id

            a=Sold()
            a.product_name=x['name']
            a.productid_id=i
            a.product_quantity=x['quantity']
            a.product_price=x['price']
            a.product_total=x['total']
            a.date_ordered=date
            a.time=time1
            a.payment=''
            a.change=''
            a.user_id=x['id']
            a.transtype=x['transtype']
            a.save()
            b=Payment()
            b.user_id=request.session['userid']
            b.product_pay=''
            b.time=time1
            b.product_change=''
            b.save()
    return HttpResponse(data)
