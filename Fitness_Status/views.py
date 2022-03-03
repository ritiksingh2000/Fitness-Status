from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from.forms import AddArticle
from django.views.generic import UpdateView
from django.views.generic import TemplateView


# HOME
def Home(request):
    return render(request, 'home.html')


def videos(request):
    category = VideoCategory.objects.all()
    video = Healthtube.objects.all()
    return render(request, 'healthtube.html', {'video': video, 'category':category})


def Contactus(request):
    return render(request, 'contactus.html')


def bmi(request):
    val1 = float(request.POST['height'])
    val2 = float(request.POST['weight'])
    val3 = float(request.POST['age'])
    val4 = str(request.POST['sex'])
    res = int(val2 / (val1 / 100) ** 2)

    if res <= 18.4:
        health = ' - UNDER-WEIGHT'
    elif res <= 25:
        health = ' - NORMAL'
    elif res <= 35:
        health = ' - OVER-WEIGHT'
    elif res > 35:
        health = ' - OBESE'

    messages.info(request, 'Your BMI is ')
    messages.info(request, res)
    messages.info(request, health)
    return redirect('/')


def subs(request):
    email = request.POST.get('email')

    if Subs.objects.filter(email=email).exists():
        messages.info(request,'Email Alreday Exists.')
        return redirect( '/')

    else:
        sub = Subs(email=email)
        sub.save()

        messages.info(request,'Welcome To Fitness Status')
        return redirect( '/')


def contact(request):
    name = request.POST.get('nam')
    email = request.POST.get('email')
    mesg = request.POST.get('message')
    subject = request.POST.get('subject')

    mesg= UserMessage(Name=name,Email=email,Message=mesg,Subject=subject)
    mesg.save()
    messages.info(request, "Message Sent Successfully. You Will Recieve A Reply Soon On Your Email.") 
    return redirect('contactus')


def Calorie(request):
    val1 = str(request.POST['gender'])
    val2 = str(request.POST['age'])
    val3 = str(request.POST['lifestyle'])

    if val1 == 'Male' and val2 == '4-8' and val3 == 'Sedentary':
        cal = '1400'
    elif val1 == 'Male' and val2 == '9-13' and val3 == 'Sedentary':
        cal = '1800'
    elif val1 == 'Male' and val2 == '14-18' and val3 == 'Sedentary':
        cal = '2200'
    elif val1 == 'Male' and val2 == '19-30' and val3 == 'Sedentary':
        cal = '2400'
    elif val1 == 'Male' and val2 == '31-50' and val3 == 'Sedentary':
        cal = '2200'
    elif val1 == 'Male' and val2 == 'Above 51' and val3 == 'Sedentary':
        cal = '2000'

    elif val1 == 'Male' and val2 == '4-8' and val3 == 'Moderately Active':
        cal = '1400-1600'
    elif val1 == 'Male' and val2 == '9-13' and val3 == 'Moderately Active':
        cal = '1800-2200'
    elif val1 == 'Male' and val2 == '14-18' and val3 == 'Moderately Active':
        cal = '2400-2800'
    elif val1 == 'Male' and val2 == '19-30' and val3 == 'Moderately Active':
        cal = '2600-2800'
    elif val1 == 'Male' and val2 == '31-50' and val3 == 'Moderately Active':
        cal = '2400-2600'
    elif val1 == 'Male' and val2 == 'Above 51' and val3 == 'Moderately Active':
        cal = '2200-2400'

    elif val1 == 'Male' and val2 == '4-8' and val3 == 'Active':
        cal = '1600-2000'
    elif val1 == 'Male' and val2 == '9-13' and val3 == 'Active':
        cal = '2000-2600'
    elif val1 == 'Male' and val2 == '14-18' and val3 == 'Active':
        cal = '2800-3200'
    elif val1 == 'Male' and val2 == '19-30' and val3 == 'Active':
        cal = '3200-3600'
    elif val1 == 'Male' and val2 == '31-50' and val3 == 'Active':
        cal = '2800-3000'
    elif val1 == 'Male' and val2 == 'Above 51' and val3 == 'Active':
        cal = '2400-2800'

    elif val1 == 'Female' and val2 == '4-8' and val3 == 'Sedentary':
        cal = '1200'
    elif val1 == 'Female' and val2 == '9-13' and val3 == 'Sedentary':
        cal = '1600'
    elif val1 == 'Female' and val2 == '14-18' and val3 == 'Sedentary':
        cal = '1800'
    elif val1 == 'Female' and val2 == '19-30' and val3 == 'Sedentary':
        cal = '2000'
    elif val1 == 'Female' and val2 == '31-50' and val3 == 'Sedentary':
        cal = '1800'
    elif val1 == 'Female' and val2 == 'Above 51' and val3 == 'Sedentary':
        cal = '1600'

    elif val1 == 'Female' and val2 == '4-8' and val3 == 'Moderately Active':
        cal = '1400-1600'
    elif val1 == 'Female' and val2 == '9-13' and val3 == 'Moderately Active':
        cal = '1600-2000'
    elif val1 == 'Female' and val2 == '14-18' and val3 == 'Moderately Active':
        cal = '2000'
    elif val1 == 'Female' and val2 == '19-30' and val3 == 'Moderately Active':
        cal = '2000-2200'
    elif val1 == 'Female' and val2 == '31-50' and val3 == 'Moderately Active':
        cal = '2000'
    elif val1 == 'Female' and val2 == 'Above 51' and val3 == 'Moderately Active':
        cal = '1800'

    elif val1 == 'Female' and val2 == '4-8' and val3 == 'Active':
        cal = '1400-1800'
    elif val1 == 'Female' and val2 == '9-13' and val3 == 'Active':
        cal = '1800-2200'
    elif val1 == 'Female' and val2 == '14-18' and val3 == 'Active':
        cal = '2400'
    elif val1 == 'Female' and val2 == '19-30' and val3 == 'Active':
        cal = '2600'
    elif val1 == 'Female' and val2 == '31-50' and val3 == 'Active':
        cal = '2200-2600'
    elif val1 == 'Female' and val2 == 'Above 51' and val3 == 'Active':
        cal = '1800-2200'
    
    messages.info(request,"Your Calorie Requirement For")
    messages.info(request, (val1, val2, val3) )
    messages.info(request, " is ",cal )
    messages.info(request, cal )

    return redirect('/')

def ShareVideo(request):
    ChannelName = request.POST.get('c_name')
    ChannelLink = request.POST.get('c_link')
    VideoName = request.POST.get('v_name')
    VideoLink = request.POST.get('v_link')
    category = request.POST.get('category')
    AddedBy = request.POST.get('by')

    sharevid = VideoSuggestion(Channel_Name = ChannelName,
                            Channel_Link = ChannelLink,
                            Video_Name = VideoName,
                            Video_Link = VideoLink,
                            Category = category,
                            Added_By = AddedBy,
                        )
    sharevid.save()

    messages.info(request,"Thanks For Sharing. We will add the video if the content is valid.")
    return redirect('profile')

def DeleteBlog(request, id):
    blog = Article.objects.get(id=id)
    blog.delete()

    message = "Blog Successfully Deleted."
    return render(request, 'profile.html', {"message":message})


# ARTICLES
def Blog(request):
    category = Categories.objects.all()
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles, 'category':category})


def Blogpage(request, id):
    articlepage = Article.objects.get(id=id)
    articles = Article.objects.all()
    return render(request, 'blogpage.html', {'articlepg': articlepage,'articles': articles})


def Profile(request):
    userarticles = Article.objects.all()
    catgry = Categories.objects.all()
    vcatgry = VideoCategory.objects.all()
    shared = VideoSuggestion.objects.all()

    useremail = request.user.email
    username = request.user.username
    form_class1 = AddArticle(initial={'author_email':useremail, 'author':username})
    if request.method == 'POST':
        
        form_class1 = AddArticle(request.POST, request.FILES)
        if form_class1.is_valid():
            user_pr = form_class1.save(commit=False)
            user_pr.display_picture = request.FILES['thumbnail']
            user_pr.save()  
            messages.info(request, "Blog Added Successfully")

        return redirect("profile")      


    
    
    context = {"form1": form_class1, "shared":shared, "userarticles":userarticles, "catgry":catgry, "vcatgry":vcatgry}

    return render(request, 'profile.html',context)


def CreateCategory(request):
    category = request.POST.get('category')
    newcategory = Categories(category=category)
    newcategory.save()

    messages.info(request, "Category Created Successfully")
    return redirect('profile')


# ACCOUNTS 
def signup(request):
    return render(request, 'signup.html')


def regestration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Taken')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Alredy Exists.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password1, email=email)
                user.save()
        else:
            messages.info(request, "Password Does'nt Match")
            return redirect('signup')

    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Email Or Paasword Didn't Match")
            return redirect('/')

    else:
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')
