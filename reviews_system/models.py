from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.first_name + self.author.last_name}"
    
