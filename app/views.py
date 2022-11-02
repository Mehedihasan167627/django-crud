
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages

from app.utils import make_user_id

from .forms import StudentForm
from .models import Student 



class HomeView(View):
    def get(self,request):
        queryset=Student.objects.all().order_by("-id")
        form=StudentForm()
        context={
            "obj_list":queryset,
            'form':form
        }

        return render(request,"app/index.html",context)

    def post(self,request):
        names=request.POST.getlist("name")
        departments=request.POST.getlist("dept")
        years=request.POST.getlist("admission_year")
        dates=request.POST.getlist("admission_date")
        user_types=request.POST.getlist("user_type")
        employee_roles=request.POST.getlist("employee_role")
        
        std_queryset=Student.objects.all()
        m_id=make_user_id(std_queryset)
        
        if names and departments:
            for i in range(len(names)):
                Student.objects.create(
                    name=names[i],
                    dept=departments[i],
                    m_id=m_id,
                    admission_date=dates[i],
                    admission_year=years[i],
                    user_type=user_types[i],
                    employee_role=employee_roles[i] 
                    )
            name=",".join(names)
            messages.success(request,f"{name} created successfully!!!")
        return redirect("/")


class DeleteStudent(View):
    def post(self,request):
        id=request.POST.get("id")
        try:
            obj=Student.objects.get(id=id) 
            obj.delete()

        except:
            return "Invalid Pk"
        return JsonResponse({"message":"success"})

class UpdateView(View):
    def get(self,request):
        id=request.GET.get("id")
        objs=Student.objects.filter(m_id=id) 
        json_data=[] 
        for data in objs:
            if data.employee_role=="empty":
                emp_role=""
            else:
                emp_role=data.employee_role
            json_data.append({
                "name":data.name,
                'dept':data.dept,
                'pk':data.pk,
                'year':data.admission_year,
                'date':data.admission_date,
                 'user_type':data.user_type,
                 'employee_role':emp_role,
               
            })
        
        return JsonResponse({"message":"success","data":json_data})
    def post(self,request):
        names=request.POST.getlist("names")
        departments=request.POST.getlist("departments")
        years=request.POST.getlist("years")
        dates=request.POST.getlist("dates")

        pk=request.POST.getlist("pk")
   
        if names and departments and pk:
            for i in range(len(names)):
                std=Student.objects.get(pk=pk[i])
                std.name=names[i]
                std.dept=departments[i]
                std.admission_date=dates[i]
                std.admission_year=years[i]
                std.save()
            name=",".join(names)
            messages.success(request,f"{name} updated successfully!!!")
        return redirect("/")


