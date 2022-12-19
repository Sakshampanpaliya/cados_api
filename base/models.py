from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=250)
    bio=models.TextField(max_length=350,null=True,blank=True)

    def __str__(self):
        return self.name    

#Model for the Advocates
class Advocate(models.Model):
    company=models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True)
    username=models.CharField(max_length=200)
    bio =models.TextField(max_length=250 , null=True ,blank=True)#null is for the user to save the details withoit any bio
    #blank does the same thing as the null but it is just for Django
    def __str__(self):
        return self.username
        #We actually see the name instead of the objects name 

#Model for the Companies

    

#Now we have to run migrations to add them to the data base