from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    

    def __str__(self):
        return self.name
    
class Icecreame(models.Model):
    name = models.CharField(max_length=122)
    desc = models.TextField()
    Img = models.ImageField(upload_to='images/')
    price = models.FloatField()
    
    
    

    def __str__(self):
        return self.name
    

