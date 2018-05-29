from django.shortcuts import render
from django.http import HttpResponse
# from firstapp.models import AccessRecord,Topic,Webpage
from firstapp.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

# from . import forms
# from forms import FormName
# Create your views here.
# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = { 'access_records' : webpages_list}
#     # mydict = {'insertme':"hi i am from views"}
#     return render(request,'firstapp/index.html',context=date_dict)
# def form_name_view(request):
#     form=forms.FormName()
#     if request.method == 'POST':
#         form=forms.FormName(request.POST)
#         if form.is_valid():
#             print("name"+form.cleaned_data['name'])
#             print("Email"+form.cleaned_data['email'])
#             print("text"+form.cleaned_data['text'])
#     return render(request,'firstapp/form_name.html',{'form':form})
def index(request):
    return render(request,'firstapp/index.html')
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered == True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'firstapp/registration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")
        else:
            print("suspicious user")
            print("username:{} and password:{}".format(username,password))
            return HttpResponse("invalid user credentials")
    else:
        return render(request,'firstapp/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
