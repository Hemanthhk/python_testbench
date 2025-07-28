from django.db import models

# Create your models here

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):# This is used to return a string representation of the objects
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) #If the referenced Topic is deleted,The Webpage instance will also be deleted due to the CASCADE option
    name = models.CharField(max_length=264,unique=True) #Allows only unique values for webpage
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE) #If the referenced Webpage is deleted,The AccessRecord instance will also be deleted due to the CASCADE option
    date = models.DateField() #A data field that stores the date of access.

    def __str__(self):
        """ returns the date attribute of the object as a string. 
            This is likely used for display or logging purposes, allowing the date to be easily printed or displayed when an AccessRecord object is referenced.
        """
        return str(self.date)

