from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from track.models import *
from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def trainee_list(request):
    # trainee=[]
    # trainee1={'id':1,'name':'stephania ehab','email':'stephania@gmail.com','age':23,'address':'El-Fayoum','trackID':1}
    # trainee2={'id':2,'name':'veronia ehab','email':'veronia@gmail.com','age':20,'address':'El-Fayoum','trackID':2}
    # trainee.append(trainee1)
    # trainee.append(trainee2)
    # context={}
    # context['trainees']=trainee
    # return render(request,'trainee/list.html',context)
    context={}
    trainees=Trainee.objects.all()
    context['trainees']=trainees
    return render(request,'trainee/list.html',context)


def trainee_update(request, id):
    # # context = {}
    # context = {"id": id}
    # return render(request, "trainee/update.html", context)
    context={}
    context['tracks']=Track.objects.all()
    context['trainee']=Trainee.objects.get(pk=id)
    if(request.method=='POST'):
        if(len(request.POST['traineename'])>0 and len(request.POST['traineename'])<=100):
            Trainee.objects.filter(pk=id).update(name=request.POST['traineename'],
                                          image=request.POST['traineeimage'],
                                          email=request.POST['traineeemail'],
                                          age=request.POST['traineeage'],
                                          phone=request.POST['traineephone'],
                                          trackobj=Track.objects.get(pk=request.POST['traineetrackid']))
            return redirect('trainee_list')
        else:
            context['error']='invalid'
    return render(request,'trainee/update.html',context)

def trainee_delete(request, id):
    context = {}
    try:
        Trainee.objects.filter(pk=id).delete()
        context['msg']='trainee deleted'
        return  redirect('trainee_list')
    except:
        import sys
        context['error'] =sys.exc_info()[1]
    return render(request,'trainee/delete.html',context)
   

def trainee_details(request, id):
    # context = {}
    context={'trainee':Trainee.objects.get(pk=id)}
    return render(request,'trainee/details.html',context)

def trainee_create(request):
    context={}
    context['tracks']=Track.objects.all()
    if(request.method=='POST'):
        context={}
        if(len(request.POST['traineename'])>0 and len(request.POST['traineename'])<=100):
            traineeobj=Trainee()
            traineeobj.name=request.POST['traineename']
            traineeobj.email=request.POST['traineeemail']
            traineeobj.age=request.POST['traineeage']
            traineeobj.phone=request.POST['traineephone']
            traineeobj.trackobj=Track.objects.get(pk=request.POST['traineetrackid'])
            traineeobj.save()
        else:
            context['error']='invalid'

    return render(request, "trainee/create.html")

def trainee_create_form(request):
    context={}
    form=NewTrainee()
    context['form']=form
    if(request.method=='POST'):
        form=NewTrainee(request.POST)
        if(form.is_valid()):
          Trainee.create(form.cleaned_data['name'],
                        form.cleaned_data['image'],
                        form.cleaned_data['email'],
                        form.cleaned_data['age'],
                        form.cleaned_data['phone'],
                        form.cleaned_data['track'])
        else:
            context['error']=form.errors
    return render(request,'trainee/createform.html',context)

def trainee_create_formmodel(request):
    form=NewtraineeModel()
    context={'form':form}
    if(request.method=='POST'):
        form = NewtraineeModel(request.POST,request.FILES)
        if (form.is_valid()):
            form.save(commit=True)
    return render(request, 'trainee/createformmodel.html', context)