from django.db import models

# Create your models here.

class Annual(models.Model):
    annual = models.CharField(max_length=4)
    
    def __str__(self):
        return f"ปีการศึกษา {self.annual}"

class Palace(models.Model):
    
    annual = models.ForeignKey(Annual, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='palaces', blank=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    nick_name = models.CharField(max_length=128)
    position = models.CharField(max_length=64)
    
    def __str__(self):
        
        return f"{self.first_name} {self.last_name}"
        
    
class Event(models.Model):
    
    EVENT_TYPE = (
        ('กิจกรรม','กิจกรรม'),
        ('ค่าย','ค่าย'),
    )

    annual = models.ForeignKey(Annual, on_delete=models.CASCADE)
    event_img = models.ImageField(upload_to='events', blank=True)
    event_name = models.CharField(max_length=255)
    event_detail = models.TextField(default="-")
    event_type = models.CharField(max_length=64, choices=EVENT_TYPE)
    event_date_from = models.DateField()
    event_date_to = models.DateField()
    
    event_location = models.CharField(max_length=256, default="-")
    event_longitude = models.CharField(max_length=255, default="-")
    
    
    def __str__(self):
        return f"{self.event_name} / {self.annual.annual}"
    
    
class Event_image(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events')
    
    def __str__(self):
        
        return f"{self.event} {self.event.annual.annual}"
    
class Event_url(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    url_name = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    
    def __str__(self):
        
        return f"{self.event} {self.event.annual.annual}"

    
    