from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import *
from .forms import *
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout 
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import EmailMessage

# Create your views here.
@login_required(login_url="accounts:login")
def home(request):
    if Post:
        posts = Post.objects.all()
    return render(request, "home.html",{'posts':posts})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username, password=password).exists:
            messages.error(request, "Uername or password Already exists")
            return redirect("accounts:signup")
        
        user = User.objects.create_user(username, password)
        user.save()
        messages.success(request, "User SignIN Successfully")
        return redirect("accounts:login")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request, "User login Successfully")
            return redirect("accounts:home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("accounts:login")
    return render(request, "login.html")

@login_required(login_url="accounts:login")
def logout(request):
    auth_logout(request)
    return redirect("accounts:login")

@login_required(login_url="accounts:login")
def create_post(request):
    if request.method == "POST":
       form = PostForm(request.POST, request.FILES)
       if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "create post succefully")
            return redirect("accounts:home")
       else:
           return HttpResponse(form.errors)
    else:
        form = PostForm()
    return render(request, "post.html", {'form':form})


@login_required(login_url="accounts:login")
def delete_post(request, id):
    # post = get_object_or_404(Post, id=id, user=request.user)
    if request.method == "POST":
        post = Post.objects.get(id=id)
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect('accounts:home')
    else:
        return render(request, "delete.html")
    
    
@login_required(login_url="accounts:login")
def update_post(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request,"Update post SuccessFully")
            return redirect("accounts:home")
    else:
        form = PostForm(instance=post)
    return render(request, "update.html",{'form':form})


@login_required(login_url="accounts:login")
# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Save the form data
#             contact = form.save()

#             # Subject and message
#             subject = f"Contact Form Submission by {contact.first_name} {contact.last_name}"
#             message = f"""
#                 Name: {contact.first_name} {contact.last_name}
#                 Email: {contact.username}
#                 Address: {contact.address}
#                 Mobile: {contact.mobile}
#                 City: {contact.city}
#                 State: {contact.state}
#                 Agreed to Terms: {"Yes" if contact.agreed_to_terms else "No"}
#             """

#             # Send email using EmailMessage
#             email = EmailMessage(
#                 subject,
#                 message,
#                 'no-reply@yourdomain.com',  # Sender email
#                 ['admin@example.com'],  # Recipient email
#                 reply_to=[contact.username],  # User's email for reply-to
#             )
#             email.send()

#             return redirect("accounts:home")
#     else:
#         form = ContactForm()
#     return render(request, "contact_form.html", {"form": form})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form data save karein
            contact = form.save()

            # Email details
            subject = f"New Contact Form Submission by {contact.first_name} {contact.last_name}"
            message = f"""
                You have received a new contact form submission:

                Name: {contact.first_name} {contact.last_name}
                Username: {contact.username}
                Address: {contact.address}
                Mobile: {contact.mobile}
                City: {contact.city}
                State: {contact.state}
            """
            from_email = 'sainikm719@gmail.com'  # Replace with your sender email

            # Dynamic recipient from contact model
            recipient_list = ['admin@example.com', contact.email]

            # Send the email
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request,"Email Send Successfully Submitted")
            return redirect("accounts:home")
    else:
        form = ContactForm()
    return render(request, "contact_form.html", {"form": form})

