#import os
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# django's class based generic views are imported here
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
#User model is imported here
from django.contrib.auth import get_user_model
User = get_user_model()

"""
class ReportListView(ListView):
    template_name="pat/report_list.html"
    queryset=Report.objects.all()
"""

#this index function query through our database model and render
# category wise and datewise money spent to our home page
@login_required(login_url='signin')
def index(request):
    date_spent=[]
    #query all our report model orderd by date associated with the current user
    query_by_username=Report.objects.filter(profileLinked=request.user)
    queryset=query_by_username.order_by('date')
    # unique dates of our report models activity is stored in date_list
    date_list=sorted(set([i.date for i in queryset]))
    #for every date, total cost spent is stored in the list date_spent
    for j in range(len(date_list)):
        date_spent.append(sum([i.cost for i in query_by_username.filter(date=date_list[j])]))

    #context dictionary is used to pass to html template along with different 
    # key value pair generated from querying report model
    context={
        'object_list':queryset,
        #total money spent by a user
        'total':sum([i.cost for i in queryset]),
        #total money spent on food is stored as food key in context dictionery
        'food':sum([i.cost for i in query_by_username.filter(tags__contains="food")]),
        'health':sum([i.cost for i in query_by_username.filter(tags__contains="health")]),
        'transport':sum([i.cost for i in query_by_username.filter(tags__contains="transport")]),
        'utilities':sum([i.cost for i in query_by_username.filter(tags__contains="utilities")]),
        'other':sum([i.cost for i in query_by_username.filter(tags__contains="other")]),
        'length':len(date_list),
        # date_list and date_spent list is passed together using zip function
        'date':zip(date_list,date_spent)
    }
    return render (request,'pat/report_list.html',context)
#class based reportdetailview  used to query a particular row of 
#Report model by its pk coloumn and render its details to html templates
class ReportDetailView(DetailView):
    template_name='pat/report_detail.html'
    def get_queryset(self):
        return Report.objects.filter(profileLinked=self.request.user)

    #if we use id in url
    """
    def get_object(self):
        #id_=self.kwargs.get('id')
        #return get_object_or_404(Report,id=id_)
        
    """
# this classbased view is used to create new instance of Report model using
#  a django default modelform
class ReportCreateView(CreateView):
    template_name='pat/report_create.html'
    form_class=ReportForm
    queryset=Report.objects.all()
    def form_valid(self, form):
        form.instance.profileLinked = self.request.user
        return super().form_valid(form)

#this classbased view is used to update an exsisting instance of Report model,
#  first querying with primary key
class ReportUpdateView(UpdateView):
    template_name='pat/report_create.html'
    form_class=ReportForm
    def get_queryset(self):
        return Report.objects.filter(profileLinked=self.request.user)
    # we use pk instead of id
    def form_valid(self,form):
        return super().form_valid(form)

#this classbased view uses pk to get a instance and then later 
# deletes it and redirects to main page
class ReportDeleteView(DeleteView):
    template_name='pat/report_delete.html'
    #if we use id
    """
    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Report,id=id_)
    """
    def get_queryset(self):
        return Report.objects.filter(profileLinked=self.request.user)
    def get_success_url(self):
       return reverse('list')
#this function registers new user
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
#this function is for signin new user to application and redirects to home page
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f"You are now logged in as {username}")
            return redirect('signin')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('signin')
    return render (request,'pat/signin.html')
#this function signout already logged in user,if no user is curently logged in it will throw warning message
def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have succesfully logged out")
        return redirect('signin')
    messages.warning(request,"You are already logged out")
    return redirect('signin')
#this function rendes weather page
def weather(request):
    context={'WEATHER_APIKEY':settings.WEATHER_APIKEY,'CURRENCY_APIKEY':settings.CURRENCY_APIKEY}
    return render (request,'pat/weather.html',context)