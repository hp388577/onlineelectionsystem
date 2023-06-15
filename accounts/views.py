from django.shortcuts import render
from User_Login.models import UserProfile
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib import auth
import random
import string
from Candidate_Login.models import Participant,Candidate

tokenglobal=''
def participantRegister(request):
    as_candidate=True
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        if not validate_email(email):
            messages.info(request,'Email is not valid.')
            as_candidate=True
            return render(request,'registeration.html',{'as_candidate':as_candidate});
        elif Participant.objects.filter(email=email).exists():
        
            messages.info(request,'email already exist.')
            return render(request,'registeration.html',{'as_candidate':as_candidate});
        area=request.POST['area']
        documents_image=request.FILES.get('documents_image')
        participant=Participant()

        participant.name = (first_name + " " + last_name)
        participant.email = email
        participant.area_name = area
        participant.is_verified = False
        participant.documents_image=documents_image
        token=participant.token=''.join(random.choices(string.ascii_lowercase, k=8))
        participant.save()
        messages.info(request,{' your token is  ' :token  }  )

        return render(request,'index.html');
    return render(request,'registeration.html');


from django.views.decorators.csrf import csrf_exempt



@csrf_exempt

def validateToken(request):
    as_candidate=True
    if request.method=='POST':
        token=request.POST['validateToken']
        tokenglobal=token
        participant=Participant.objects.all()
        if Participant.objects.filter(token=token):
            participant=Participant.objects.filter(token=token)
            for p in participant:
                if p.is_registered==True:
                    messages.info(request,'Your Registeration is already done')
                    return render(request,'registeration.html',{'as_candidate':as_candidate});
                if p.is_verified==True:
                    messages.info(request,'Your Document is verified please register and provide more details and get your usr id and password')
                    return render(request,'registeration.html',{'as_candidate': as_candidate , 'is_verified':p.is_verified});
                elif p.is_rejected==True:
                    messages.info(request,'Your Document is rejected by authority try again if wish to participate in election')
                    return render(request,'registeration.html',{'as_candidate':as_candidate});
                else:
                    messages.info(request,'Your Document is not verified yet please try again after few time')
                    return render(request,'registeration.html',{'as_candidate':as_candidate});
        else:
            messages.info(request,'Invalid Token.')
            return render(request,'registeration.html',{'as_candidate':as_candidate})
    else:
        messages.info(request,'Please Provide Token.')
        return render(request,'registeration.html',{'as_candidate':as_candidate});

def registration_as_candidate(request):
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        if not validate_email(email):
            messages.info(request,'Email is not valid.')
            as_candidate=True
            return render(request,'registeration.html',{'as_candidate':as_candidate});
        else:
            user = create_random_user()
            if User.objects.filter(username=user[0]).exists():
                messages.info(request,'username already exist.')
                return render(request,'registeration.html',{'as_candidate':as_candidate});
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exist.')
                return render(request,'registeration.html',{'as_candidate':as_candidate});

            usercreate = User.objects.create_user(username=user[0], password=user[1], is_staff=True,first_name=first_name,last_name=last_name,email=email)
            
            documents_image=request.FILES.get('documents_image')
            symbol_image=request.FILES.get('symbol_image')
            
            area=request.POST['area']
            profile = Candidate()
            profile.user = usercreate
            profile.email = email
            profile.area_name = area
            profile.total_votes=0
            profile.documents_image=documents_image
            profile.symbol_image=symbol_image
            profile.save()
            auth.login(request,usercreate)
            messages.info(request,{' your username is  ' :" "+  user[0] +" " ,  '  youur password is ' :  user[1]  }  )
            participant=Participant.objects.all()
            participant=Participant.objects.filter(token=tokenglobal)
            for p in participant:
                p.is_registered=True
            
            return render(request,'index.html')
        
    else:
        as_candidate=True
        return render(request,'registeration.html',{'as_candidate':as_candidate});

def registration_as_voter(request):
    as_candidate=False
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        if not validate_email(email):
            messages.info(request,'Email is not valid.')
            return render(request,'registeration.html',{'as_candidate':as_candidate});
        else:
            
            user = create_random_user()
            if User.objects.filter(username=user[0]).exists():
                messages.info(request,'username already exist.')
                return render(request,'registeration.html',{'as_candidate':as_candidate});
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exist.')
                return render(request,'registeration.html',{'as_candidate':as_candidate});

            usercreate = User.objects.create_user(username=user[0], password=user[1], is_staff=False,first_name=first_name,last_name=last_name,email=email)
            
            area=request.POST['area']
            profile = UserProfile()
            profile.user = usercreate
            profile.name = (first_name + " " + last_name)

            profile.email = email
            profile.area = area
            profile.eligible_to_vote = False
            profile.save()
            messages.info(request,{' your username is  ' :" "+  user[0] +" " ,  '  youur password is ' :  user[1]  }  )
            auth.login(request,usercreate)

            return render(request,'index.html')
    else:
        
        return render(request,'registeration.html',{'as_candidate':as_candidate});

def logout(request):
    auth.logout(request)
    return render(request,'choose.html')

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
def login(request):
    return render(request,'choose.html')




def generate_random_password(length=8):
    # Define the characters to choose from when generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def create_random_user():
    # Generate a random username
    username = ''.join(random.choices(string.ascii_lowercase, k=8))

    # Generate a random password
    password = generate_random_password()

    # Create the Django User instance with the generated username and password
    

    return username,password

# Create your views here.

def registration(request):
    registration=True
    return render(request,'choose.html',{'Registration':registration});

def home(request):
    return render(request,'index.html')