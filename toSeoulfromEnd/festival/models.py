from django.db import models

# Create your models here.
class festival_M(models.Model):
    title = models.CharField(max_length = 20,null = True, blank = True)
    pub_date = models.DateField(null = True, blank = True)
    locate = models.CharField(max_length = 30,null = True, blank = True)
    period = models.DateField(null = True, blank = True)
    body = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to = 'festival/',null = True, blank = True)
    likes = models.IntegerField(null = True, blank = True)
    # wirter = 
    is_school = models.BooleanField(null = True, blank = True)
    link = models.URLField(max_length = 200, null = True, blank = True)

    
