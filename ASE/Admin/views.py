from django.shortcuts import render
from django.http import HttpResponse
from Teacher.models import Teachers
from Student.models import Students
from django.core.mail import EmailMessage
from .forms import Register_student,Register_teacher
# Create your views here.

def admin_home(request):
	return render(request,'Admin/Admin_View_home.html')

def admin_view_profile(request):
	return render(request,'Admin/Admin_View_View_Profiles.html')

# def admin_add_teacher(request):
# 	return	render(request,'Admin/Admin_View_Add_Teacher.html')

def admin_add_teacher(request):
    form=Register_teacher()
    if request.method == 'POST':
        form=Register_teacher(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['re_password']:
                return render(request,'Admin/Admin_View_Add_Teacher.html',{'form':form,'errp':'password not matched'})
            if Teachers.objects.filter(T_id=form.cleaned_data['T_id'].lower()).count()==1:
                return render(request,'Admin/Admin_View_Add_Teacher.html',{'form':form,'erru':'User ID already'})
            t=Teachers(slug=form.cleaned_data['T_id'],T_id=form.cleaned_data['T_id'],T_name=form.cleaned_data['T_name'],T_email=form.cleaned_data['T_email'],T_password=form.cleaned_data['password'])
            t.save()
            return render(request,'Admin/Teacher_created.html')
        else:
            return render(request,'Admin/Admin_View_Add_Teacher.html',{'form':form})
    return render(request,'Admin/Admin_View_Add_Teacher.html',{'form':form})



# def admin_add_student(request):
#
# 	return render(request,'Admin/Admin_View_Add_Student.html')
#

def admin_add_student(request):
    form=Register_student()
    if request.method == 'POST':
        form=Register_student(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['re_password']:
                return render(request,'Admin/Admin_View_Add_Student.html',{'form':form,'errp':'password not matched'})
            if Students.objects.filter(S_id=form.cleaned_data['S_id'].lower()).count()==1:
                return render(request,'Admin/Admin_View_Add_Student.html',{'form':form,'erru':'User ID already'})
            t=Students(slug=form.cleaned_data['S_id'],S_id=form.cleaned_data['S_id'],S_name=form.cleaned_data['S_name'],S_email=form.cleaned_data['S_email'],S_password=form.cleaned_data['password'])
            t.save()
            return render(request,'Admin/Teacher_created.html')
        else:
            return render(request,'Admin/Admin_View_Add_Student.html',{'form':form})
    return render(request,'Admin/Admin_View_Add_Student.html',{'form':form})






def teacher_list(request):
	all_teachers = Teachers.objects.all()
	return render(request,'Admin/teacher_list.html',{"all_teachers":all_teachers})
	# return HttpResponse("dfjkhfjk")


def student_list(request):
	all_students = Students.objects.all()
	return render(request,'Admin/student_list.html',{"all_students":all_students	})
	# return HttpResponse("dfjkhfjk")

def make_email(request,slug):
	if Teachers.objects.filter(slug=slug).count() == 1:
		requested = Teachers.objects.get(slug=slug)
		url = "Admin/Admin_email_teacher.html"
	else:
		requested = Students.objects.get(slug=slug)
		url = "Admin/Admin_email_student.html"
	return render(request,url,{"a_request":requested})


def send_email(request):
	email = request.POST['email']
	subject = request.POST['subject']
	body = request.POST['body']
	email = EmailMessage(subject,body,to=[email])
	email.send()
	return render(request,"Admin/Admin_confirm.html")
