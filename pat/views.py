#import os
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Report
from .forms import ReportForm
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

"""
class ReportListView(ListView):
    template_name="pat/report_list.html"
    queryset=Report.objects.all()
"""
@login_required(login_url='signin')
def index(request):
    date_spent=[]
    query_by_username=Report.objects.filter(profileLinked=request.user)
    queryset=query_by_username.order_by('date')
    date_list=sorted(set([i.date for i in queryset]))
    for j in range(len(date_list)):
        date_spent.append(sum([i.cost for i in query_by_username.filter(date=date_list[j])]))
    context={
        'object_list':queryset,
        'total':sum([i.cost for i in queryset]),
        'food':sum([i.cost for i in query_by_username.filter(tags__contains="food")]),
        'health':sum([i.cost for i in query_by_username.filter(tags__contains="health")]),
        'transport':sum([i.cost for i in query_by_username.filter(tags__contains="transport")]),
        'utilities':sum([i.cost for i in query_by_username.filter(tags__contains="utilities")]),
        'other':sum([i.cost for i in query_by_username.filter(tags__contains="other")]),
        'length':len(date_list),
        'date':zip(date_list,date_spent)
    }
    return render (request,'pat/report_list.html',context)

class ReportDetailView(DetailView):
    #if we use pk in url
    #queryset=Article.objects.all()
    template_name='pat/report_detail.html'
    def get_queryset(self):
        return Report.objects.filter(profileLinked=self.request.user)

    #if we use id in url
    #def get_object(self):
        #id_=self.kwargs.get('id')
        #return get_object_or_404(Report,id=id_)

class ReportCreateView(CreateView):
    template_name='pat/report_create.html'
    form_class=ReportForm
    queryset=Report.objects.all()
    def form_valid(self, form):
        form.instance.profileLinked = self.request.user
        return super().form_valid(form)

class ReportUpdateView(UpdateView):
    template_name='pat/report_create.html'
    form_class=ReportForm
    def get_queryset(self):
        return Report.objects.filter(profileLinked=self.request.user)
    # we use pk instead of id
    def form_valid(self,form):
        return super().form_valid(form)

class ReportDeleteView(DeleteView):
    template_name='pat/report_delete.html'
    """
    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Report,id=id_)
    """
    def get_queryset(self):
        return Report.objects.filter(profileLinked=self.request.user)
    def get_success_url(self):
       return reverse('list')
def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully, signin now')
            return redirect('signin')
    else:
        form=UserForm()
    return render(request,'pat/register.html',{'form':form})
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f"You are now logged in as {username}")
            #return render (request,'pat/signin.html')
            return redirect('signin')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('signin')
    return render (request,'pat/signin.html')
def signout(request):
    logout(request)
    return redirect('signin')

def weather(request):
    context={'WEATHER_APIKEY':settings.WEATHER_APIKEY,'CURRENCY_APIKEY':settings.CURRENCY_APIKEY}
    return render (request,'pat/weather.html',context)