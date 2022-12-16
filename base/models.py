from django.db import models

# Create your models here.

class Advocate(models.Model):
    username=models.CharField(max_length=200)
    bio =models.TextField(max_length=250 , null=True ,blank=True)#null is for the user to save the details withoit any bio
    #blank does the same thing as the null but it is just for Django
    def __str__(self):
        return self.username
        #We actually see the name instead of the objects name 