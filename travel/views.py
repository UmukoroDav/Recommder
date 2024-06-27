from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages
from .form import Signupform, EditUser
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            messages.success(request, 'Your Registration was  successfully. Pls Log in!.')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong with your registration. Please try again.')
    else:
        form = Signupform() 

    context = {
        'form': form,
    }

    return render(request, 'register/register.html', context)

def edit_profile(request):
    user = request.user
    form = EditUser(instance=user)

    if request.method == 'POST':
        form = EditUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'This user has been updated Successfully')
            return redirect('index')
        
    context = {
        'form':form,
    }
    return render(request, 'edit-profile.html', context)

def applogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You have been Logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Email and Password')
            return redirect('login')
    return render(request, 'register/login.html')

def indexlogout(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('index')


def index(request):
    blo = Destination.objects.all()[0:1]
    pot = Post.objects.all()[0:3]
    about = About.objects.all()

    context = {
        'pot':pot,
        'blo':blo,
        'about':about,
    }
    return render(request, 'home/index.html', context)

@login_required(login_url='login')
def package(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    post = Post.objects.filter(Q(topic__name__icontains=q))
    topic = TourismCartegory.objects.all()


    context = {
        'post':post,
        'topic':topic,
    }
    return render(request, 'package/packages.html', context)

@login_required(login_url='login')
def packagedetails(request, pk):
    pots = Post.objects.get(id=pk)

    context = {
        'pots':pots,
    }
    return render(request, 'package/package-details.html', context)

@login_required(login_url='login')
def blogdetails(request, pk): 
    blo = get_object_or_404(Destination, pk=pk)
    comments = Comments.objects.filter(bloo=blo)
    comment_count = comments.count()
    uer = request.user

    if request.method == 'POST':
        message = request.POST.get('message')
        if not message:
            messages.error(request, 'Please fill in all the fields.')            
            return redirect('blogdetails', pk=pk)
        
        comment = Comments(message=message, bloo=blo, user=uer)
        comment.save()                                                                              
        messages.success(request, 'Your message has been sent successfully')
        return redirect('blogdetails', pk=pk)
    
    context = {
        'blo': blo,
        'comments': comments,
        'comment_count': comment_count,
    }

    return render(request, 'blog/blog-details.html', context)





@login_required(login_url='login')
def blog(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    blog = Destination.objects.filter(Q(country_namw__icontains=q)).order_by('-created')
    bl = Destination.objects.all()[0:3]
    comment = blog.count()


    context = {
        'blog':blog,
        'bl':bl,
        'comment':comment,
    }
    return render(request, 'blog/blog.html', context)

def about(request):
    aboutm = About.objects.all()

    context = {
        'aboutm':aboutm,
    }
    return render(request, 'home/about.html', context)


@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        email_subject = f'Mew Message from {name}'
        email_body = f'You have recieved a new message from {name}\n\n Subject : {subject}\n\n Email : {email}\n\n Message : {message}'


        send_mail(
            email_subject,
            email_body,
            'rafua.k.kenneth@gmail.com',
            ['rafua.k.kenneth@gmail.com'],
            fail_silently=False,
        )

    messages.success(request, 'Your Email Have Been Successfully Sent!')
    return redirect('contact')
    

    return render(request, 'contact.html')

