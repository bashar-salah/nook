from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from pages.models import Category, Addwork
from django.core.files.storage import FileSystemStorage
import json
import requests
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from pages.models import Category
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST' and 'signup' in request.POST:
            firstname = None
            lastname = None
            username = None
            email = None
            phone = None
            password1 = None
            password2 = None
            category = None
            # upload  = None
            
            # Save Image
            # try:
            #     if request.POST['myFile'] != '':
            #         upload  = request.FILES['myFile']
            #         fss = FileSystemStorage()
            #         file = fss.save(upload.name, upload)
            #         file_url = fss.url(file)
            #     else:
            #         upload = ''
            # except:
            #     upload  = request.FILES['myFile']
            #     fss = FileSystemStorage()
            #     file = fss.save(upload.name, upload)
            #     file_url = fss.url(file)
            
            if 'firstname' in request.POST: firstname = request.POST['firstname'].strip()
            else: messages.error(request, 'Error in first name field')
            
            if 'lastname' in request.POST: lastname = request.POST['lastname'].strip()
            else: messages.error(request, 'Error in last name field')
            
            if 'username' in request.POST: username = request.POST['username'].strip()
            else: messages.error(request, 'Error in username field')
            
            if 'email' in request.POST: email = request.POST['email']
            else: messages.error(request, 'Error in email field')
            
            if 'phone' in request.POST: phone = request.POST['phone']
            else: messages.error(request, 'Error in phone field')
            
            if 'password1' in request.POST: password1 = request.POST['password1']
            else: messages.error(request, 'Error in password field')
            
            if 'password2' in request.POST: password2 = request.POST['password2']
            else: messages.error(request, 'Error in confirm password field')
            
            if 'category' in request.POST: category =  request.POST['category']
            else: messages.error(request, 'Error in category field')
            

            if firstname and lastname and username and email and phone and password1 and password2 and category:
                if category == 'Choose your artistic talent':
                    messages.error(request, 'Please, select your category')
                else:
                    print(request.POST)
                    if User.objects.filter(username = username).exists():
                        messages.error(request, 'This username is taken')   
                    else:
                        uservalid = True
                        for a in username:
                            if a.isalnum() or a == '@' or a == '/' or a == '.' or a == '+' or a == '-' or a == '_':
                                uservalid = True
                            else:
                                uservalid = False
                        if uservalid == False:
                            messages.error(request, 'Enter a valid username')
                        else:
                            if User.objects.filter(email = email).exists():
                                messages.error(request, 'This email is taken')
                            else:
                                num = True
                                for a in phone:
                                    if a.isspace():
                                        num = False
                                        break
                                    else:
                                        try:
                                            if type(int(a)) == int:
                                                pass
                                        except:
                                            num = False
                                            break
                                if num != True:
                                    messages.error(request, 'The phone number may not contain a special character or symbol or space')
                                else:
                                    if password1 != password2:
                                        messages.error(request, 'Password and confirmation password do not match')
                                    else:
                                        if len(password1) < 8:
                                            messages.error(request, 'The password is short')
                                        else:
                                            cate = Category.objects.get(pk = int(category))
                                            user = User.objects.create_user(
                                                    first_name = firstname,
                                                    last_name = lastname,
                                                    email = email,
                                                    username = username,
                                                    password = password1)
                                            userProfile = UserProfile.objects.create(
                                                phone = phone,
                                                type_account = request.POST['type_account'],
                                                category = cate,
                                                user = user,
                                            )
                                            # messages.success(request, 'Your account is created')
                                            firstname = ''
                                            lastname = ''
                                            username = ''
                                            email = ''
                                            phone = ''
                                            auth_login(request, user)
                                            return redirect('index')
            else:
                messages.error(request, 'Check empty fields')

            context = {
                'title': 'Sign Up',
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'email': email,
                'phone': phone,
                'category': Category.objects.all(),
            }
            return render(request, 'account/signin.html', context)
        else:
            context = {
                'title': 'nook | Sign Up',
                'category': Category.objects.all(),
            }
            return render(request, 'account/signin.html', context)


def signinfacebook(request):
    # get auth code from redirect url
    code = request.GET.get('code')
    # Generate user token
    request_user_token = requests.get("https://graph.facebook.com/oauth/access_token?code="+code+"&fields=id,name,first_name,last_name&client_secret=b45e28547eddbf8d8586b80e788e63c0&client_id=722789235370191&redirect_uri=http://localhost:8000/account/signinfacebook")
    # Convert from binry to string then Json
    user_token = json.loads(request_user_token.content.decode("utf-8"))['access_token'] 
    # Get user profile using access token
    profile = requests.get("https://graph.facebook.com/me?fields=id,name,first_name,last_name,picture&access_token=" + user_token)
    # Convert from binry to string then Json
    profile = json.loads(profile.content.decode("utf-8"))
    
    
    id = str(profile['id'])
    firstname = profile['first_name']
    lastname = profile['last_name']
    # email = profile['email']
    username = profile['first_name'] + id[-1]   
    password = profile['id']
    
    if not User.objects.filter(username = username).exists():
        user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            # email = email,
            username = username,
            password = password
            )
        userProfile = UserProfile.objects.create(
            type_account = 'facebook login',
            user = user,
        )
        auth_login(request, user)
        # messages.success(request, 'Your account is created, Hello ' + username)
    else:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
    # return redirect('signin')
    return redirect('index')


def signingoogle(request):
    # get auth code from redirect url
    auth_code = request.GET.get('code')
    # Get user access token using POST method
    url = 'https://oauth2.googleapis.com/token'
    data = {
    'code' : auth_code,
    'client_id' : '542085961146-v77a1spko4fusekchd9mkqd6uhubsul9.apps.googleusercontent.com',
    'client_secret' : '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',
    'redirect_uri' : 'http://localhost:8000/account/signingoogle',
    'grant_type' : 'authorization_code'
    }
    headers = {'content-type': 'application/json'}
    request_user_token = requests.post(url, data=json.dumps(data), headers=headers)
    user_token = json.loads(request_user_token.content.decode("utf-8"))['access_token'] 
    # Get user profile using access token
    profile = requests.get("https://www.googleapis.com/oauth2/v3/userinfo?access_token=" + user_token)
    # Convert from binry to string then Json
    profile = json.loads(profile.content.decode("utf-8"))
    
    firstname = profile['given_name']
    lastname = profile['family_name']
    email = profile['email']
    username = profile['given_name'] + '2021'   
    password = profile['sub']
    if not User.objects.filter(email = email).exists():
        user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            email = email,
            username = username,
            password = password
            )
        userProfile = UserProfile.objects.create(
            type_account = 'google login',
            user = user,
        )
        # messages.success(request, 'Your account is created, Hello ' + username)
        auth_login(request, user)
    else:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            # messages.success(request, 'Success login, Hello '+ username)
        else:
            messages.error(request, 'There is already an account with the same email    ')
    # return redirect('signin')
    return redirect('index')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST' and 'signin' in request.POST:
            emailuser = request.POST['emailuser']
            password = request.POST['password']
            if '@' in emailuser:
                if User.objects.filter(email = emailuser).exists():
                    username = User.objects.get(email=emailuser).username
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        if 'remembercheck' not in request.POST:
                            request.session.set_expiry(0)
                        auth_login(request, user)
                        if request.GET.get('next', None):
                            return HttpResponseRedirect(request.GET['next'])
                        # messages.success(request, 'Success login, Hello '+ username)
                        return redirect('index')
                    else:
                        messages.error(request, 'Please check the data entered')
                else:
                    messages.error(request,'Please check the data entered')
            else:
                if User.objects.filter(username = emailuser).exists():
                    user = authenticate(request, username=emailuser, password=password)
                    if user is not None:
                        if 'remembercheck' not in request.POST:
                            request.session.set_expiry(0)
                        auth_login(request, user)
                        if request.GET.get('next', None):
                            return HttpResponseRedirect(request.GET['next'])
                        # messages.success(request, 'Success login, Hello '+ username)
                        return redirect('index')
                    else:
                        messages.error(request, 'Please check the data entered')
                else:
                    
                    
                    messages.error(request, 'Please check the data entered')
        context = {
            'title': 'nook | Sign In',
            'category': Category.objects.all(),
        }
        return render(request, 'account/signin.html', context)


def profile(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        user = User.objects.get(pk = user_id)
        userprofile = UserProfile.objects.get(user = user)
    works = Addwork.objects.filter(user = user)
    print(works)
    context = {
        'title': 'nook | Profile',
        'category': Category.objects.all(),
        'user': user,
        'userprofile': userprofile,
        'works': works
    }
    return render(request, 'account/profile.html', context)


@login_required
def editprofile(request, user_id):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user = user)
    if request.method == 'POST' and 'saveedie' in request.POST:
        firstname = request.POST['firstname'].strip()
        lastname = request.POST['lastname'].strip()
        username = request.POST['username'].strip()
        email = request.POST['email']
        phone = request.POST['phone']
        oldpassword = None
        password1 = None
        password2 = None
        # oldpassword = request.POST['oldpassword']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']
        
        if firstname and lastname and username and email and phone:
            if User.objects.filter(username = username).exists():
                if request.user.username == username:
                    num = True
                    for a in phone:
                        if a.isspace():
                            num = False
                            break
                        else:
                            try:
                                if type(int(a)) == int:
                                    pass
                            except:
                                num = False
                                break
                    if num != True:
                        messages.error(request, 'Enter a valid phone')
                    else:
                        request.user.first_name = firstname
                        request.user.last_name = lastname
                        request.user.email = email
                        userprofile.phone = phone
                        request.user.save()
                        userprofile.save()
                else:
                    messages.error(request, 'This username is taken')
            else:
                uservalid = True
                for a in username:
                    if a.isalnum() or a == '@' or a == '/' or a == '.' or a == '+' or a == '-' or a == '_':
                        uservalid = True
                    else:
                        uservalid = False
                        break
                if uservalid == False:
                    messages.error(request, 'Enter a valid username')
                else:
                    num = True
                    for a in phone:
                        if a.isspace():
                            num = False
                            break
                        else:
                            try:
                                if type(int(a)) == int:
                                    pass
                            except:
                                num = False
                                break
                    if num != True:
                        messages.error(request, 'Enter a valid phone')
                    else:
                        request.user.first_name = firstname
                        request.user.last_name = lastname
                        request.user.username = username
                        request.user.email = email
                        userprofile.phone = phone
                        request.user.save()
                        userprofile.save()
                    # messages.success(request, 'Update data successflly')
                    
        if oldpassword != None and password1 != None and password2 != None:
            oldpassword = request.POST['oldpassword']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            check = user.check_password(oldpassword)
            if check == True:
                if password1 == password2:
                    user.set_password(password1)
                    user.save()
                    messages.success(request, 'Password Change Successfully')
                else:
                    messages.error(request, 'The confirmation password you entered does not match')
            else:
                messages.error(request, 'The old password you entered is wrong')
    context = {
        'tltle': 'nook | Edit Profile',
        'userprofile': userprofile,
        'category': Category.objects.all(),
    }
    return render(request, 'account/editprofile.html', context)