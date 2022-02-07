import uuid
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail
from account.models import Profile
from django.contrib.auth.models import User
from dashboard.models import Member
# from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator




from django.conf import settings

# Create your views here.


def home(request):
    return redirect(login)

def homepage(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request,'account/home.html')

def dashboard(request):
    if(request.user.is_authenticated == False):
        return redirect('/login')
    print(request.user.id)
    filled_forms = Member.objects.filter(ritwik = request.user.id)
    # print(filled_forms)
    # context = {'members':filled_forms}
    paginator = Paginator(filled_forms,3)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    return render(request,'dashboard/dashboard.html',{'page_obj': page_obj})

def login(request):
        if request.user.is_authenticated:
            return redirect('/dashboard')

        if request.method == 'POST':
            username = request.POST.get('username')
            password= request.POST.get('password')

            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('/login')
            
            
            profile_obj = Profile.objects.filter(user = user_obj ).first()

            if not profile_obj.is_verified:
                messages.success(request, 'Profile is not verified check your mail.')
                return redirect('/login')

            user = authenticate(request, username = username , password = password)
            print(user)
            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('/login')
            else:
                auth_login(request,user)
                return redirect('/dashboard')

        return render(request , 'account/login.html')

def register(request):
        if request.user.is_authenticated:
            return redirect('/dashboard')
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            if(pass1 != pass2):
                messages.error(request,"Passwords didn't Matched")
                return redirect('/register')

            try:
                if User.objects.filter(username = username).first():
                    messages.error(request,"Username is already taken.")
                    return redirect('/register')

                if User.objects.filter(email = email).first():
                    messages.error(request, 'Email is already taken.')
                    return redirect('/register')
                
                user_obj = User(username = username , email = email)
                user_obj.set_password(pass1)
                user_obj.save()
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
                profile_obj.save()
                print("Sending Mail")
                send_mail_after_registration(email , auth_token)
                return redirect('/token')

            except Exception as e:
                print(e)

        return render(request , 'account/register.html')
    

def logout(request):
    auth_logout(request)
    return redirect('/login')


def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )  
    print("Mail Sent!")  

def error_page(request):
    return  render(request , 'account/error.html')    

def success(request):
    return render(request , 'account/success.html')


def token_send(request):
    return render(request , 'account/token_send.html')


def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/success')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def forget_password(request):

    if request.method == "POST":
        credential = request.POST.get('credential')
        print(len(credential))
        credential = credential.strip() 
        print(len(credential))
        print(credential)
        user = User.objects.filter(username = credential).first()
        if user is None:
            user = User.objects.filter(email__exact = credential).first()    ## Filter can return empty set so not throw error but get throw
            print("email not found")
        if user is None:
            print("Invalid Credential Register")
            messages.error(request, 'User Not Found.')
            return redirect("/forget_password")    
        else:
            print(user)
            auth_token = str(uuid.uuid4())
            email = user.email
            profile_obj = Profile.objects.get(user = user)
            profile_obj.auth_token = auth_token
            profile_obj.save()
            print("Sending Mail")
            send_mail_to_resetpass(email , auth_token)  
            print(profile_obj,auth_token,email) 
            return redirect('/token') 


    return render(request,'account/forgot_pass.html')       


def change_password(request , auth_token):
    print("Hii")

    account = Profile.objects.filter(auth_token=auth_token).first()
    if account is not None:
        if request.method == "POST":
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            if(pass1 == pass2):
                print("Passwords are same")
                # user = account.user
                print(account,account.user)
                user = account.user
                user.set_password(pass1)
                user.save()
                # Token Will Expire After One Click
                auth_token = str(uuid.uuid4())
                account.auth_token = auth_token
                account.save()
                print("Password Changed")
                return redirect('/login')
            else:
                messages.error(request,"Passwords didn't matched.")
                print(auth_token)
                return redirect(f'/resetpassword/{auth_token}')    
        else:
            return render(request,'account/change_password.html')
    else:
        print("Error")
        return redirect("/error")    

    

def send_mail_to_resetpass(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to reset your account password http://127.0.0.1:8000/resetpassword/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )  
    print("Mail Sent!")  

