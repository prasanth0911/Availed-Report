from django.shortcuts import render
from .models import Unknown,Pwc
from django.http import HttpResponse
import psycopg2 
from django.http import JsonResponse
from datetime import date
# Create your views here.

#date picker
def date(request):
    return render(request,'Date.html')

#display total shutdown data in home page
def home(request):
    month=request.GET.get('month')
    year=request.GET.get('year')
    data=Unknown.objects.raw('select * from calc_pwc where extract(year from startdate)=%s and extract(month from startdate)=%s order by startdate asc',[year,month])
    return render(request,'Home.html', {'items' : data,'month' : month, 'year' : year})

#Availed shutdowns
def availed(request):
    month=request.GET.get('month')
    year=request.GET.get('year')
    for i in Unknown.objects.raw('select * from calc_unknown  where shutid !=0 and extract(year from startdate)=%s and extract(month from startdate)=%s',[year,month]):
        Pwc.objects.filter(shutid = i.shutid).update(availed=True,outageid=i.outageid)
    data=Pwc.objects.raw('select * from calc_pwc where availed=True and extract(year from startdate)=%s and extract(month from startdate)=%s',[year,month])
    return render(request,'Availed.html', {'items':data, 'month' : month, 'year' : year})

#Unknown shutdowns
def  unknown(request):
    option=request.GET.get('option')
    x=request.GET.get('shutid')
    y=request.GET.get('outageid')
    month=request.GET.get('month')
    year=request.GET.get('year')
    if (option == "accept"):
        Pwc.objects.filter(shutid=x).update(outageid=y, availed=True)
        Unknown.objects.filter(outageid=y).update(shutid=x)
    if (option == "reject"):
        Pwc.objects.filter(shutid=x).update(availed=False)
    data1=Pwc.objects.raw('select * from calc_pwc where availed is null and extract(year from startdate)=%s and extract(month from startdate)=%s order by startdate asc',[year,month])
    data2=Unknown.objects.raw('select * from calc_unknown where shutid=0 and extract(year from startdate)=%s and extract(month from startdate)=%s',[year, month])
    return render(request,'Unknown.html', {'items1':data1,'items2':data2, 'month' : month, 'year' : year})







