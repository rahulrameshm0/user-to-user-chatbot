from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Message
from django.db.models import Q
from django.contrib import messages
# Create your views here.

# @login_required
# def home(request):
#     users = User.objects.exclude(id=request.user.id)
#     return render(request, 'home.html', {'users': users})

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')  

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, 'Password does not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')
            
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'signup.html')

def sign_out(request):
    logout(request)
    return redirect('login')

def chat_user(request,username):
    other_user = get_object_or_404(User, username=username)
    current_user = request.user
    if request.method == "POST":
        content = request.POST.get('message')
        if content:
            Message.objects.create(
            sender = current_user,
            receiver = other_user,
            content = content
        )
        return redirect('chat_user', username=other_user.username)
    
    Message.objects.filter(
    sender=other_user,
    receiver=current_user,
    is_read=False
    ).update(is_read=True)
    
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user),

    ).order_by('timestamp')

    return render(request, 'chat-page.html', {'other_user': other_user, 'messages':messages})

def text_user(request):
    if request.method == "POST":
        sender = request.POST['sender']
        receiver = request.POST['receiver']

        output = Message(
         sender=sender,
         receiver=receiver,
        )
        output.save()
        return redirect('home')
    
def home(request):
    current_user = request.user
    users_data = []

    users = User.objects.exclude(id=current_user.id)

    for user in users:
        last_message = Message.objects.filter(
            Q(sender=current_user, receiver=user) |
            Q(sender=user, receiver=current_user)
        ).order_by('-timestamp').first()

        unread_count = Message.objects.filter(
            sender=user,
            receiver=current_user,
            is_read=False
        ).count()

        users_data.append({
            'username': user.username,
            'last_message': last_message.content if last_message else '',
            'unread_count':int(unread_count)
        })

    return render(request, 'home.html', {'users': users_data})