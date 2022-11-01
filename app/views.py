
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from .models import Student 
import re 
from django.db.models import Q

class HomeView(View):
    def get(self,request):
        queryset=Student.objects.all().order_by("-id")
        context={
            "obj_list":queryset
        }
        return render(request,"app/index.html",context)

    def post(self,request):
        names=request.POST.getlist("names")
        departments=request.POST.getlist("departments")
        years=request.POST.getlist("years")
        dates=request.POST.getlist("dates")
        
        count=Student.objects.count()
        m_id="AB-01"
        if count:
            count=Student.objects.all().last().m_id
            count=re.findall("\d{1,10}",count)
            count=int("".join(count))
            if count<9:
                m_id="AB-0"+str(int(count)+1)
            else:
                m_id="AB-"+str(int(count)+1)

        if names and departments:
            for i in range(len(names)):
                Student.objects.create(
                    name=names[i],
                    dept=departments[i],
                    m_id=m_id,
                    admission_date=dates[i],
                    admission_year=years[i]
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
            json_data.append({
                "name":data.name,
                'dept':data.dept,
                'pk':data.pk,
                'year':data.admission_year,
                'date':data.admission_date
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




class SearchView(View):
    def get(self,request):
        qry=request.GET.get("qry")
      
        if qry:
            objs=Student.objects.filter(Q(name__icontains=qry) | Q(dept__iexact=qry)) 
        else:
            objs=Student.objects.all().order_by("-id")
        json_data=[] 
        for data in objs:
            json_data.append({
                "name":data.name,
                'dept':data.dept,
                'pk':data.pk,
                'year':data.admission_year,
                'date':data.admission_date,
                "pk":data.pk,
                "id":data.id,
                "m_id":data.m_id,
            })
        
        return JsonResponse({"message":"success","data":json_data})