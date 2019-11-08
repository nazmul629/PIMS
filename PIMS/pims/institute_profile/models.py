from django.db import models

class Acadamy(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    class Meta:
        unique_together = ('name', 'code',)
    
    def __str__(self):
        return self.name 

class Semester(models.Model):
    spelling = models.CharField(max_length=100)
    number = models.IntegerField()

    class Meta:
        unique_together = ('spelling', 'number',)
    
    def __str__(self):
        return self.spelling 

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'code',)
    
    def __str__(self):
        return self.name 

class Class_Rooms (models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.IntegerField()

    class Meta:
        unique_together = ('code',)
    
    def __str__(self):
        return self.name 