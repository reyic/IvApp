
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Enterprise, Calification
from .forms import create_enterprise_form, create_calification_form

# Create your views here.

def index(request):
	list_enterprise=Enterprise.objects.order_by('name')
	context={'list_enterprise':list_enterprise}
	return render(request,'Aplicacion/index.html',context)

def create_enterprise(request):
	linea=None
	if request.method=="POST":
		form=create_enterprise_form(request.POST)
		if form.is_valid():
			form.save(commit=True)
			linea='Enterprise was created'
		else:
			form=create_enterprise_form()

		context={'form':form,'linea':linea}
		return render(request,'Aplicacion/create_enterprise.html',context)

def create_calification(request):
	linea=None
	if request.method=="POST":
		form=create_calification_form(request.POST)
		if form.is_valid():
			form.save(commit=True)
			linea='Calification was created'
	else:
		form=create_calification_form()
	context={'form':form,'linea':linea}
	return render(request,'Aplicacion/create_calification.html',context)

def delete_enterprise(request):
	linea=None
	list_enterprise=None
	
	if request.method="POST":
		try:
			x=Enterprise.objects.get(k=request.POST['enterprise'])
		except(KeyError,Enterprise.DoesNotExist):
			linea='Enterprise not select'
		else:
			x.delete()
			linea='Delete Enterprise'
	else:
		list_enterprise=Enterprise.objects.order_by('name')
	context={'enterprise_list':list_enterprise,'linea':linea}
	return render(request, 'Aplicacion/delete_enterprise.html',context)

def delete_calification(request,enterprise_id):
	linea=None
	list_calification=None
	enterprise=Enterprise.objects.get(k=enterprise_id)
	if request.method=="POST":
		try: 
			y=Calification.objects.get(k=request.POST['calification'])
		except(KeyError,Enterprise.DoesNotExist):
			linea="Not Select Calification"
		else:
			y.delete()
			linea="Delete calification"
	else:
		list_calification=Enterprise.calification_set.all()
	context={'list_calification':list_calification,'linea':linea}
	return render(request,'Aplicacion/delete_enterprise.html',context)

def show_calification(request,enterprise_id):
	enterprise=Enterprise.objects.get(k=enterprise_id)
	list_calif=Enterprise.calification_set.all()
	context={'list_calification':list_calification,'enterprise':Enterprise}
	return render(request,'Aplicacion/show_calification.html,context')



