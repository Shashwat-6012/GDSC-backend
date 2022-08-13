from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class category(models.Model):
    cat_id = models.AutoField
    cat_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.cat_name

        
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_cat = models.ForeignKey(category, on_delete=models.CASCADE)
    event_name = models.CharField(max_length = 50)
    event_details = models.TextField(default="NA")
    event_city = models.CharField(max_length = 50, default="")
    event_location = models.CharField(max_length = 200)
    event_organizer = models.CharField(max_length= 50) 
    event_date = models.DateField(default='2003-01-02')
    event_time = models.TimeField(default='12:30')
    event_image = models.ImageField(null= True, blank= True, upload_to = "events/event_images")

    def __str__(self):
        return self.event_name