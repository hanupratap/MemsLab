#Third-Party Imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
import random
from django.contrib.auth.models import User


from memslab.forms import UserRegisterForm, ProfilePic, LoginForm
from memslab.models import Employee, Employee_details, \
    Employee_details_topic, Project, Project_type, project_image

def IndexView(request):

    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        return render(request, 'memslab/index.html', {'employee_logggedin': None, \
                'employees':Employee.objects.all(), 'projects': Project.objects.all()})
    return render(request, 'memslab/index.html', {'employee_logggedin': emp,  \
        'employees':Employee.objects.all(), 'projects': Project.objects.all()})

def detail(request):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    return render(request, 'memslab/detail.html',{'employees': \
        Employee.objects.all(), 'employee_logggedin': emp})
@login_required
def profile(request):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    employee = Employee.objects.get(user=request.user)
    employees = Employee.objects.all()
    emp_det = Employee_details.objects.all()
    for employee in employees:
        if employee.user.username == request.user.username:
            for det in emp_det:
                if det.user.username == request.user.username:
                    empdet = Employee_details.objects.filter(user=employee.user)
                    employee1 = employee

    if request.method == "POST":
        form = ProfilePic(request.POST or None, request.FILES or None)
        if form.is_valid():
            employee.emp_pic = request.FILES['emp_pic']
            employee.save()
            return HttpResponse('Done')
    else:
        form = ProfilePic()
    return render(request, 'memslab/profile.html', {'employee': employee1, \
        'empdet':empdet, 'employee_logggedin': employee, 'change_pic': form })


def show_profile(request, username):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    employees = Employee.objects.all()
    emp_det = Employee_details.objects.all()
    empdet = [] 
    for det in emp_det: 
        if det.topic not in empdet:
            empdet.append(det)
    for employee in employees:
        if employee.user.username == username:
            for det in emp_det:
                if det.user.username == username:
                    return render(request, 'memslab/profile.html', {'employee': employee, \
                        'employee_logggedin': emp, 'empdet':empdet})
            return render(request, 'memslab/profile.html', {'employee': employee, \
                    'employee_logggedin': emp, 'empdet':None})
    return HttpResponse("ERROR")

def show_projects(request, project_name):
    bg_images = (   'https://images.unsplash.com/photo-1517420704952-d9f39e95b43e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=nicolas-thomas-540353-unsplash.jpg',
                    'https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=chad-kirchoff-202730-unsplash.jpg',
                    'https://images.unsplash.com/photo-1525207106105-b340f7384b30?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=conor-luddy-650741-unsplash.jpg',
                    'https://www.nist.gov/file/461891/download?token=hjzRlLCc',
                    'https://images.unsplash.com/photo-1473831818960-c89731aabc3e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=randall-bruder-136626-unsplash.jpg',
                    'https://images.unsplash.com/photo-1473831818960-c89731aabc3e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=randall-bruder-136626-unsplash.jpg',
                    'https://images.pexels.com/photos/1837605/pexels-photo-1837605.jpeg?cs=srgb&dl=architectural-design-architecture-background-1837605.jpg&fm=jpg',
                    'https://images.unsplash.com/photo-1473831818960-c89731aabc3e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=randall-bruder-13662',
                    'https://www.allaboutcircuits.com/uploads/thumbnails/MEMS_close_post_actuator.jpg',
                    'http://4.bp.blogspot.com/_O9KFUaJsTaE/TNmpQGsMYMI/AAAAAAAAACc/EsFk0OtiPEw/s1600/Sandia+friction+device.jpg',
                    'https://cdn.dnaindia.com/sites/default/files/styles/full/public/2016/11/29/524004-quadrotor-board-electric-circuit-wiki-commons.jpg'
                )

    bg = random.choices(bg_images)
    proj = Project.objects.get(name=project_name)
   
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


def prof_cat(request, det_id):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    det = Employee_details.objects.get(id=det_id)
    employee = Employee.objects.get(user=det.user)
    empdet = Employee_details.objects.filter(user=employee.user)
    return render(request, "memslab/category.html", {'det':det, \
        'employee_logggedin':emp,'employee':employee,'empdet':empdet})
