#Third-Party Imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
import random
from django.contrib.auth.models import User


from memslab.forms import UserRegisterForm, ProfilePic, LoginForm
from memslab.models import Employee, Employeedetails, \
    Employee_details_topic, Project, Project_type, project_image

def IndexView(request):
    superuser = User.objects.filter(is_superuser=True)
    super_employee = Employee.objects.filter(user=superuser)
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        return render(request, 'memslab/index.html', {'employee_logggedin': None, \
                'employees':Employee.objects.all(), 'projects': Project.objects.all(), 'superuser_emails':superuser.values_list('email')[0][0]})
    return render(request, 'memslab/index.html', {'employee_logggedin': emp,  \
        'employees':Employee.objects.all(), 'projects': Project.objects.all(), 'superuser_emails':User.objects.filter(is_superuser=True).values_list('email')[0][0]})

def detail(request):

    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    return render(request, 'memslab/detail.html',{'employees': \
        Employee.objects.all(), 'employee_logggedin': emp, 'superuser_emails':User.objects.filter(is_superuser=True).values_list('email')[0][0]})

@login_required
def profile(request):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
        emp_det = Employeedetails.objects.filter(user=emp.user)
    else:
        emp = None
        emp_det = None
    categ = []
    for e in emp_det:
        if e.topic in categ:
            pass
        else:
            categ.append(e.topic)
    if request.method == "POST":
        form = ProfilePic(request.POST or None, request.FILES or None)
        if form.is_valid():
            emp.emp_pic = request.FILES['emp_pic']
            emp.save()
            return render(request, 'memslab/profile.html', {'employee': emp, \
            'empdet':categ, 'employee_logggedin': emp, 'change_pic': form})
    else:
        form = ProfilePic()
    return render(request, 'memslab/profile.html', {'employee': emp, \
        'empdet':categ, 'employee_logggedin': emp, 'change_pic': form})


def show_profile(request, username):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    categ = []
    prof = User.objects.get(username=username)
    employee = Employee.objects.get(user=prof)
    authr = Project.objects.filter(Person1=prof)
    authr1 = Project.objects.filter(Person2=prof)
    authr2 = Project.objects.filter(Person3=prof)
    authr3 = Project.objects.filter(Person4=prof)
    authr4 = Project.objects.filter(Person5=prof)
    projs = len(authr)+len(authr1)+len(authr2)+len(authr3)+len(authr4)
    emp_det = Employeedetails.objects.filter(user=prof)
    for e in emp_det:
        if e.topic in categ:
            pass
        else:
            categ.append(e.topic)
    if request.method == "POST":
        form = ProfilePic(request.POST or None, request.FILES or None)
        if form.is_valid():
            emp.emp_pic = request.FILES['emp_pic']
            emp.save()
            return render(request, 'memslab/profile.html', {'employee': employee, \
            'empdet':categ, 'employee_logggedin': emp, 'change_pic': form,'projs':projs})
    else:
        form = ProfilePic()
    return render(request, 'memslab/profile.html', {'employee': employee, \
                'employee_logggedin': emp, 'empdet':categ,'change_pic': form})



def show_projects(request, project_id):
    bg_images = ('https://images.unsplash.com/photo-1517420704952-d9f39e95b43e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=nicolas-thomas-540353-unsplash.jpg',
                'https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=chad-kirchoff-202730-unsplash.jpg',
                'https://images.unsplash.com/photo-1525207106105-b340f7384b30?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=conor-luddy-650741-unsplash.jpg',
                'https://www.nist.gov/file/461891/download?token=hjzRlLCc',
                'https://images.unsplash.com/photo-1473831818960-c89731aabc3e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=randall-bruder-136626-unsplash.jpg',
                'https://images.unsplash.com/photo-1473831818960-c89731aabc3e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=randall-bruder-136626-unsplash.jpg',
                'https://images.pexels.com/photos/1837605/pexels-photo-1837605.jpeg?cs=srgb&dl=architectural-design-architecture-background-1837605.jpg&fm=jpg',
                'https://images.unsplash.com/photo-1473831818960-c89731aabc3e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=randall-bruder-13662',
                'https://www.allaboutcircuits.com/uploads/thumbnails/MEMS_close_post_actuator.jpg',
                'http://4.bp.blogspot.com/_O9KFUaJsTaE/TNmpQGsMYMI/AAAAAAAAACc/EsFk0OtiPEw/s1600/Sandia+friction+device.jpg',
                'https://cdn.dnaindia.com/sites/default/files/styles/full/public/2016/11/29/524004-quadrotor-board-electric-circuit-wiki-commons.jpg')

    bg = random.choices(bg_images)
    proj = Project.objects.get(id=project_id)
   
    try:
        image_object = project_image.objects.filter(project=proj)
    except Exception as e:
        pass
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user = request.user)
        return render(request, 'memslab/project.html', {'employee_logggedin': emp, \
            'project': proj, 'images':image_object, 'employees':Employee.objects.all(),'background':bg[0],})
    else:
        return render(request, 'memslab/project.html', {'project': proj, 'employee_logggedin':None,\
             'employees':Employee.objects.all(),'background':bg[0], 'images':image_object,})

def About(request):
    emp = Employee.objects.filter(designation="HOD")
    return render(request, 'memslab/About.html', {'HOD':emp})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            messages.success(request, 'Successfully Created')
            return redirect('{%url "memslab:index"%}')
    else:
        form = UserRegisterForm()
    return render(request, 'memslab/register.html', \
        {'form': form, 'employees': Employee.objects.all(), 'projects': Project.objects.all()})

def login(request):
    login1 = LoginForm()  
    return render(request, "login.html", {'form':login1})


def prof_cat(request, username, top):

    
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    if request.method == "POST":
        form = ProfilePic(request.POST or None, request.FILES or None)
        if form.is_valid():
            emp.emp_pic = request.FILES['emp_pic']
            emp.save()
            return render(request, 'memslab/profile.html')
    else:
        form = ProfilePic()
    categ = []
    topics = []

    user = User.objects.get(username=username)
    employee = Employee.objects.get(user=user)
    emp_det = Employeedetails.objects.filter(topic__topic=top)
    for e0 in emp_det:
        if e0.user == user:
            topics.append(e0)        
        else:
            pass
    empdet = Employeedetails.objects.filter(user=user)
    for e in empdet:
        if e.topic in categ:
            pass
        else:
            categ.append(e.topic)

    return render(request, "memslab/category.html", {'employee_logggedin':emp, 'topics':topics, 'employee':employee,'empdet':categ,'change_pic': form})
