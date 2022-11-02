from django.db import models

from app.utils import make_year_list


class Student(models.Model):
    name=models.CharField(max_length=255)
    dept=models.CharField(max_length=255)
    str_id=models.CharField(max_length=25)
    admission_date=models.DateField()
    admission_year=models.CharField(max_length=14,choices=make_year_list())
    user_type=models.CharField(max_length=25,choices=(
        ("Student","Student"),
        ("Employee","Employee"),
     
        ),default="Student") 

    employee_role=models.CharField(max_length=25,choices=(
        ("empty","-----------"),
        ("Web Development","Web Development"),
        ("App Development","App Development"),
     
        ),default="empty") 


    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name 





