from django.db import models

# Create your models here.


class SMS(models.Model):
    body = models.CharField(max_length=200,blank=False,null=False)
    output = models.CharField(max_length=10,blank=False,null=False,default="ABC")

    def __str__(self):
        return self.output
