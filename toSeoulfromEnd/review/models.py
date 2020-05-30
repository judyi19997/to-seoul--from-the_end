from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    fest_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

    def summary(self):
        return self.body[:100]