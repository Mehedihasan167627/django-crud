from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=255)
    dept=models.CharField(max_length=255)
    m_id=models.CharField(max_length=14)
    admission_date=models.DateField()
    admission_year=models.CharField(max_length=4)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name 



