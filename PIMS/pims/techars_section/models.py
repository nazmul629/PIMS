from django.db import models
from institute_profile.models import Department,Semester,Shift,Subjects

class Techar_rank(models.Model):
    rank = models.CharField(max_length=50) 
    def __str__(self):
        return self.rank 
class Techar_Admission(models.Model):
    name  = models.CharField(max_length=100)
    photo = models.ImageField()
    rank = models.ForeignKey(Techar_rank,on_delete=models.CASCADE) 
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    Subject  = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=70,blank=True)
    address  = models.TextField()
    
    def __str__(self):
        return self.name 
    