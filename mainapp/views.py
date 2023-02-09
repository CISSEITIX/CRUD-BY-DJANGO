
from django.shortcuts import render, HttpResponse,redirect
from django.http.response import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    item_list=Item.objects.all()
    context={'item_list': item_list}

    return render(request,'index.html',context)


################### added ##################################

def add_item(request) :
    if request.method=="POST":
       nom=request.POST['nom']
       email=request.POST['email']
       mdp=request.POST['mdp']
       item=Item(nom=nom, email=email, mdp=mdp)
       item.save()
       messages.info(request, "Added succeful!")
       return  redirect('index')
    else:
      pass

    item_list=Item.objects.all()
    context={'item_list': item_list}
    return render(request,'index.html', context)




  ############## delete ##################

def delete_item(request,myid):
      item=Item.objects.get(id=myid)
      item.delete()
      messages.info(request,"Delete succefull")
      return redirect(index)

########### Update ################

def edit_item(request,Id) :
      sel_item=Item.objects.get(id=Id)
      item_list=Item.objects.all()
      context= {'sel_item': sel_item, 'item_list' : item_list}

      return render(request,'index.html',context)

def update_item(request,Id):
      item=Item.objects.get(id=Id)
      item.nom=request.POST['nom']
      item.email=request.POST['email']
      item.mdp=request.POST['mdp']
      item.save()
      messages.info(request, "Update succeful!")
      return redirect('index')


