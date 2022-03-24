from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Category, About, Addwork, Blog, CommentsBlog, Contect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.contrib import messages



def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        userprofile = ''
    recentwork = Addwork.objects.all()[0 : 8]
    context = {
        'title': 'nook | Home Page',
        'userprofile': userprofile,
        'category': Category.objects.all(),
        'recentwork': recentwork,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        userprofile = ''
    count = Category.objects.all().count()
    category = Category.objects.all()
    aboutdescription = About.objects.get(pk = 1).description
    context = {
        'title': 'nook | About Page',
        'aboutdescription': aboutdescription,
        'count': count,
        'category': category,
        'userprofile': userprofile

    }
    return render(request, 'pages/about.html', context)


@login_required
def addwork(request, username):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user = user)
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST' and 'addwork' in request.POST:
        title = None
        description = None
        price = None
        category = None
        
        try:
            if request.POST['myFile'] != '':
                upload  = request.FILES['myFile']
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
                file_url = fss.url(file)
            else:
                upload = ''
        except:
            upload  = request.FILES['myFile']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            
        if 'title' in request.POST: title = request.POST['title'].strip()
        else: messages.error(request, 'Error in title field')
        
        if 'description' in request.POST: description = request.POST['description'].strip()
        else: messages.error(request, 'Error in description field')
        
        if 'price' in request.POST: price = request.POST['price']
        else: messages.error(request, 'Error in price field')
        
        if 'category' in request.POST: category = request.POST['category']
        else: messages.error(request, 'Error in category field')

        if title and description and price and category:
            if category == 'Open this select menu':
                messages.error(request, 'Please, select your category')
            else:
                if upload == '':
                    messages.error(request, 'Please, select your Image')
                else:
                    work = Addwork.objects.create(
                        title = title,
                        description = description,
                        price = price,
                        photo = upload,
                        category = Category.objects.get(name = category),
                        user = user
                    )
                    # messages.success(request, 'Work added successfully')
                    return redirect('profile', user_id = user.pk)
        else:
            messages.error(request, 'Check empty fields')
            
    categor = UserProfile.objects.get(user=user).category
    context = {
        'title': 'nook | Add Work',
        'categor': categor,
        'category': Category.objects.all(),
        'userprofile': userprofile
    }
    return render(request, 'pages/addwork.html', context)


def photodetails(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        userprofile = ''
    work = get_object_or_404(Addwork, pk = id)
    context = {
        'title': 'nook | Photo Details',
        'work': work,
        'category': Category.objects.all(),
        'userprofile': userprofile
    }
    return render(request, 'pages/photodetails.html', context)


@login_required
def editwork(request, id):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user = user)
    work = get_object_or_404(Addwork, pk = id, user = user)
    categor = UserProfile.objects.get(user=user).category
    
    oldimage = str(work.photo)
    oldi = oldimage[oldimage.index('/') + 1 : ]

    if request.method == 'POST' and 'editwork' in request.POST:
        title = None
        description = None
        price = None
        category = None
        

        
        print(request.POST)
        try:
            if request.POST['myFile'] != '':
                upload  = request.FILES['myFile']
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
                file_url = fss.url(file)
            else:
                upload = ''
        except:
            upload  = request.FILES['myFile']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            
        if 'title' in request.POST: title = request.POST['title'].strip()
        else: messages.error(request, 'Error in title field')
        
        if 'description' in request.POST: description = request.POST['description'].strip()
        else: messages.error(request, 'Error in description field')
        
        if 'price' in request.POST: price = request.POST['price']
        else: messages.error(request, 'Error in price field')
        
        if 'category' in request.POST: category = request.POST['category']
        else: messages.error(request, 'Error in category field')

        if title and description and price and category:
            if category == 'Open this select menu':
                messages.error(request, 'Please, select your category')
            else:
                if upload == '':
                    print('**********')
                    work = Addwork()
                    work.pk = id
                    work.title = title
                    work.description = description
                    work.price = price
                    work.photo = oldimage
                    work.category = Category.objects.get(name = category)
                    work.user = user
                    work.save()
                    # messages.success(request, 'Work edit successfully')
                    # messages.error(request, 'Please, select your Image')
                    return redirect('photodetails', id=work.pk)
                else:
                    work = Addwork()
                    work.pk = id
                    work.title = title
                    work.description = description
                    work.price = price
                    work.photo = upload
                    work.category = Category.objects.get(name = category)
                    work.user = user
                    work.save()
                    # messages.success(request, 'Work edit successfully')
                    return redirect('photodetails', id=work.pk)
        else:
            messages.error(request, 'Check empty fields')
            
    
    context = {
        'title': 'nook | Edit Work',
        'work': work,
        'category': Category.objects.all(),
        'userprofile': userprofile,
        'categor': categor,
        'ph': work.photo
    }
    return render(request, 'pages/editwork.html', context)


def blog(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        userprofile = ''
    allblog = Blog.objects.all()
    context = {
        'title': 'nook | Blog',
        'category': Category.objects.all(),
        'userprofile': userprofile,
        'allblog': allblog
    }
    return render(request, 'pages/blog.html', context)


def blogdetails(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        userprofile = ''
    blogdet = Blog.objects.get(pk = id)
    allcomments = CommentsBlog.objects.filter(blog = blogdet)
    context = {
        'title': 'nook | Blog Details',
        'category': Category.objects.all(),
        'blogdet': blogdet,
        'userprofile': userprofile,
        'allcomments': allcomments,
    }
    return render(request, 'pages/blogdetails.html', context)


def savecommentnotregister(request, id):
    if request.method == 'POST' and 'sendcomment' in request.POST:
        name = request.POST['name'].strip()
        email = request.POST['email']
        message = request.POST['message'].strip()
        blog = Blog.objects.get(pk = id)
        if name and email and message:
            comment = CommentsBlog.objects.create(
                name = name,
                message = message,
                email = email,
                registeruser = False,
                blog = blog
                    )
            return redirect('blogdetails', id=id)
        else:
            # messages.error(request, 'Check the entered data')
            return redirect('blogdetails', id=id)
    else:
        print('*******************')
        return redirect('blogdetails', id=id)
    
def savecommentregister(request, id):
    if request.method == 'POST' and 'sendcomment' in request.POST:
        userid = request.POST['userid']
        user = User.objects.get(pk=userid)
        name = user.first_name + ' ' + user.last_name
        email = user.email
        message = request.POST['message'].strip()
        blog = Blog.objects.get(pk = id)
        if name and message:
            comment = CommentsBlog.objects.create(
                name = name,
                message = message,
                email = email,
                registeruser = True,
                user = user,
                blog = blog
                    )
            return redirect('blogdetails', id=id)
        else:
            # messages.error(request, 'Check the entered data')
            return redirect('blogdetails', id=id)
    else:
        print('*******************')
        return redirect('blogdetails', id=id)


def category(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        userprofile = ''
    allwork = Addwork.objects.all()
    context = {
        'title': 'nook | Category',
        'userprofile': userprofile,
        'category': Category.objects.all(),
        'allwork': allwork
    }
    return render(request, 'pages/category.html', context)


def contact(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user = user)
    else:
        userprofile = ''
    if request.method == 'POST' and 'contact' in request.POST:
        name = request.POST['name'].strip()
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message'].strip()
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
            contact = Contect.objects.create(
                name = name,
                email = email,
                phone = phone,
                message = message
            )
            messages.success(request, 'Your message has been sent to technical support')
    context = {
        'title': 'nook | Contact',
        'category': Category.objects.all(),
        'userprofile': userprofile,
    }
    return render(request, 'pages/contact.html', context)


def contacthomepage(request):
    if request.method == 'POST' and 'contact' in request.POST:
        name = request.POST['name'].strip()
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message'].strip()
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
            contact = Contect.objects.create(
                name = name,
                email = email,
                phone = phone,
                message = message
            )
            messages.success(request, 'Your message has been sent to technical support')
    return redirect('index')


def photodelete(request, id):
    work = Addwork.objects.get(pk = id)
    work.delete()
    return redirect('profile', user_id = work.user.pk)

def handler404(request, exception):
    context = {
        'title': 'Page Not Found'
    }
    return render(request, 'handler/handler404.html', context, status=404)

def handler505(request):
    context = {
        'title': 'Error Server'
    }
    return render(request, 'handler/handler505.html', context, status=505)

