from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def track_list(request):
    # track=[]
    # track1={'id':1,'name':'python'}
    # track2={'id':2,'name':'ELearning'}
    # track.append(track1)
    # track.append(track2)
    # context={}
    # context['tracks']=track
    # return render(request,'track/track_list.html',context)
    context={}
    tracks=Track.objects.all()
    context['tracks']=tracks
    return render(request,'track/list.html',context) 

def track_update(request, id):
    return  HttpResponse(f'<h1>update track number {id}</h1>')

def track_delete(reqest, id):
    return  HttpResponse(f'<h1>delete track number {id}</h1>')

def track_details(request, id):
    # return  HttpResponse(f'<h1>details of track number {id}</h1>')
    context={'track':Track.objects.get(pk=id)}
    return render(request,'track/details.html',context)

def track_create(request):
    # return  HttpResponse(f'<h1>Account details</h1>')
    context={}
    if(request.method=='POST'):
        context={}
        if(len(request.POST['trackname'])>0 and len(request.POST['trackname'])<=50):
            trackobj=Track()
            trackobj.name=request.POST['trackname']
            trackobj.save()
            return redirect('track_list')
        else:
            context['error']='invalid'
    return render(request,'track/create.html',context)