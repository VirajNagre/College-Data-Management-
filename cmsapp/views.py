from django.shortcuts import render,redirect
from .models import StuModel,DeptModel
from .forms import StuForm,DeptForm


# Create your views here.


def home(request):
	deptData = DeptModel.objects.all()
	studentData = StuModel.objects.all()
	return render(request,"stu.html",{"data":studentData })

def dept(request):
	data = DeptModel.objects.all()
	return render(request,"dept.html",{"data":data})

def adddept(request):
	if request.method=="POST":
		data = DeptForm(request.POST)
		if data.is_valid():
			data.save()
			msg="Dept Added"
			fm = DeptForm()
			return render(request,"adddept.html",{"fm":fm,"msg":msg})
		else:
			msg="Error"
			return render(request,"adddept.html",{"fm":data,"msg":msg})
	else:		
		fm = DeptForm()
		return render(request,"adddept.html",{"fm":fm})

def remdept(request,id):
	d = DeptModel.objects.get(did=id)
	d.delete()
	return redirect("dept")

def stu(request):
	data = StuModel.objects.all()
	return render(request,"stu.html",{"data":data})

def addstu(request):
	if request.method=="POST":
		data=StuForm(request.POST)
		if data.is_valid():
			data.save()
			msg="student added"
			sf = StuForm()
			return render(request,"addstu.html",{"sf":sf,"msg":msg})
		else:
			msg="student added"
			return render(request,"addstu.html",{"sf":data,"msg":msg})
	else:
		sf = StuForm()
		return render(request,"addstu.html",{"sf":sf})

def remstu(request,id):
	s = StuModel.objects.get(rno=id)
	s.delete()
	return redirect("stu")




