from django.db import models

class Category(models.Model):
   name = models.CharField(max_length=20)

   

   def __str__(self):
       return self.name

class Electric(models.Model):
   name = models.CharField(max_length=20)
   price=models.DecimalField( max_digits=5, decimal_places=2)
   category=models.ForeignKey("Category",on_delete=models.CASCADE)
   
   def __str__(self):
       return self.name