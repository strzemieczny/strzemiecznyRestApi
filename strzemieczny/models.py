from djongo import models

# Create your models here.
class myProjects(models.Model):
    name=models.CharField(max_length=15)
    url=models.CharField(max_length=30, unique=True)
    description=models.CharField(max_length=100)
    inDev=models.BooleanField()
    image=models.ImageField(upload_to='strzemieczny/myProjects/')