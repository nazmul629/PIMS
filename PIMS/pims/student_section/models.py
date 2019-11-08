from django.db import models
from institute_profile.models import Department,Semester,Shift

class Admission(models.Model):
    name  = models.CharField(max_length=100)
    photo = models.ImageField()
    roll_no = models.IntegerField()
    reg_no = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete = models.CASCADE)
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE)
    fathers_name =  models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    address  =  models.TextField()
    
    
    class Meta:
            unique_together = ('roll_no', 'reg_no',)
    
    def __str__(self):
        return self.name 
    