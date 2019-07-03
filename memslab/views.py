#Third-Party Imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
import random
from django.contrib.auth.models import User
from django.forms import inlineformset_factory, modelformset_factory


from memslab.forms import UserRegisterForm, ProfilePic, LoginForm, topic
from memslab.models import Employee, Employeedetails, \
    Employee_details_topic, Project, Project_type, project_image

def get_coordinator():
    return Employee.objects.filter(coordinator=True)[0]

def IndexView(request):
    superuser = User.objects.filter(is_superuser=True)
    super_employee = Employee.objects.filter(user=superuser)
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        return render(request, 'memslab/index.html', {'employee_logggedin': None, \
                'employees':Employee.objects.all(), 'projects': Project.objects.all(), 'coordinator':get_coordinator})
    return render(request, 'memslab/index.html', {'employee_logggedin': emp,  \
        'employees':Employee.objects.all(), 'projects': Project.objects.all(),'coordinator':get_coordinator})

def detail(request):

    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
    return render(request, 'memslab/detail.html',{'employees': \
        Employee.objects.all(), 'employee_logggedin': emp,'coordinator':get_coordinator})

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
        'empdet':categ, 'employee_logggedin': emp, 'change_pic': form, 'coordinator':get_coordinator})


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
            'empdet':categ, 'employee_logggedin': emp, 'change_pic': form,'projs':projs, 'coordinator':get_coordinator})
    else:
        form = ProfilePic()
    return render(request, 'memslab/profile.html', {'employee': employee, \
                'employee_logggedin': emp, 'empdet':categ,'change_pic': form, 'coordinator':get_coordinator})



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
                'https://calce.umd.edu/sites/calce.umd.edu/files/chris-ried-534420-unsplash.jpg',
                'https://cdn.dnaindia.com/sites/default/files/styles/full/public/2016/11/29/524004-quadrotor-board-electric-circuit-wiki-commons.jpg',)
    bg = random.choices(bg_images)
    proj = Project.objects.get(id=project_id)
   
    try:
        image_object = project_image.objects.filter(project=proj)
    except Exception as e:
        pass
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user = request.user)
        return render(request, 'memslab/project.html', {'employee_logggedin': emp, \
            'project': proj, 'images':image_object, 'employees':Employee.objects.all(),'background':bg[0], 'coordinator':get_coordinator})
    else:
        return render(request, 'memslab/project.html', {'project': proj, 'employee_logggedin':None,\
             'employees':Employee.objects.all(),'background':bg[0], 'images':image_object, 'coordinator':get_coordinator})

def About(request):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None
 
    return render(request, 'memslab/About.html', {'employee_logggedin':emp, 'coordinator':get_coordinator, })

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
        {'form': form, 'employees': Employee.objects.all(), 'projects': Project.objects.all(), 'coordinator':get_coordinator})

def login(request):
    login1 = LoginForm()  
    return render(request, "memslab/login.html", {'form':login1, 'coordinator':get_coordinator})


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

    return render(request, "memslab/category.html", {'employee_logggedin':emp, 'topics':topics, 'employee':employee, 'empdet':categ, 'change_pic': form, 'main_topic':top, 'coordinator':get_coordinator})

@login_required
def main_form(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    form = inlineformset_factory(User, Employee, fields=(
    'id_no',
    'researcher',
    'coordinator',
    'designation',
    'department',
    'short_description',
    'Chamber_Consultation_Hours',
    'experience_in_years',
    'phone',))

    form1 = modelformset_factory(Employee_details_topic, fields=('topic',),extra=1)
    if request.method == 'POST':
        formset = form(request.POST, instance=emp.user)
        if formset.is_valid():
            formset.save()
        formset1 = form1(request.POST)
        if formset1.is_valid():
            instances = formset1.save(commit=False)
            for instance in instances:
                instance.save()
        return redirect ('/memslab/profile', emp_id=emp_id)

    formset = form(instance=emp.user)
    formset1 = form1()
    return render(request, "memslab/forms.html", {'form':formset, 'form1':formset1, 'employee':emp, 'coordinator':get_coordinator})
@login_required
def category_form(request, emp_id):
    emp = Employee.objects.get(id=emp_id)    
    form = inlineformset_factory(User, Employeedetails, fields=('topic', 'entry', ))
    if request.method == 'POST':
        formset = form(request.POST, instance=emp.user)
        if formset.is_valid():
            formset.save()
            return redirect ('/memslab/profile', emp_id=emp_id)
    formset = form(instance=emp.user)
    return render(request, "memslab/forms.html", {'form':formset, 'employee':emp, 'coordinator':get_coordinator})
@login_required
def add_projects(request):
    if  request.user.is_authenticated:
        emp = Employee.objects.get(user=request.user)
    else:
        emp = None

    form = modelformset_factory(Project, fields=('specializaiton','name','description','short_description','project_pic','status','Person1','Person2','Person3','Person4','specializaiton','specializaiton','Person5','budget','sponsoring_agency','proj_file',), extra=2)
    if request.method == 'POST':
        formset = form(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
                return redirect ('/memslab/', emp_id=emp.id)
    formset = form()
    return render(request, "memslab/forms.html", {'form':formset, 'employee':emp, 'coordinator':get_coordinator})
