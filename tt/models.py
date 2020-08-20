from django.db import models

# Create your models here.
class sublin(models.Model):
    class_name = models.CharField(max_length=40)
    class_co = models.CharField(max_length=10)
    link = models.CharField(max_length = 50)

    def __str__(self):
        return self.class_name

class monday(models.Model):
    class_co = models.CharField(max_length = 30)
    period = models.CharField(max_length = 1)
    link = models.ForeignKey(sublin, on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return  self.class_co


class tuesday(models.Model):
    class_co = models.CharField(max_length = 30)
    period = models.CharField(max_length = 1)
    link = models.ForeignKey(sublin, on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return  self.class_co


class wednesday(models.Model):
    class_co = models.CharField(max_length = 30)
    period = models.CharField(max_length = 1)
    link = models.ForeignKey(sublin, on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return  self.class_co


class thursday(models.Model):
    class_co = models.CharField(max_length = 30)
    period = models.CharField(max_length = 1)
    link = models.ForeignKey(sublin, on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return  self.class_co


class friday(models.Model):
    class_co = models.CharField(max_length = 30)
    period = models.CharField(max_length = 1)
    link = models.ForeignKey(sublin, on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return  self.class_co


class saturday(models.Model):
    class_co = models.CharField(max_length = 30)
    period = models.CharField(max_length = 1)
    link = models.ForeignKey(sublin, on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return  self.class_co


